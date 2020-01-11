#!/usr/bin/env python3
# coding: utf-8
# File: main.py
# Author: 798445653@qq.com,https://github.com/ruoyuu/Stacked-Neural-Network
# Date: 19-01-01

import numpy as np
from keras import backend as K
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Bidirectional, LSTM,GRU, Dense, TimeDistributed, Dropout
from keras_contrib.layers.crf import CRF
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class LSTMNER:
    def __init__(self):
        cur = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.train_path = os.path.join(cur, 'data/ccks2018.txt')
        self.vocab_path = os.path.join(cur, 'model/vocab.txt')
        self.embedding_file = os.path.join(cur, 'model/token_vec_300.bin')
        self.model_path = os.path.join(cur, 'model/tokenvec_bilstm2_crf_model_20.h5')
        self.datas, self.word_dict = self.build_data()
        self.class_dict ={'O': 0,

                         'B-body': 1,
                         'I-body': 2,

                         'B-chec': 3,
                         'I-chec': 4,

                         'B-cure': 5,
                         'I-cure': 6,

                         'B-dise': 7,
                         'I-dise': 8,

                         'B-symp': 9,
                         'I-symp': 10,

                        }
        self.EMBEDDING_DIM = 300
        self.EPOCHS = 40
        self.BATCH_SIZE = 128
        self.NUM_CLASSES = len(self.class_dict)
        self.VOCAB_SIZE = len(self.word_dict)
        self.TIME_STAMPS = 150
        self.embedding_matrix = self.build_embedding_matrix()

    def build_data(self):
        datas = []
        sample_x = []
        sample_y = []
        vocabs = {'UNK'}
        for line in open(self.train_path,  encoding='utf-8'):
            line = line.rstrip().split('\t')
            if not line:
                continue
            char = line[0]
            if not char:
                continue
            cate = line[-1]
            sample_x.append(char)
            sample_y.append(cate)
            vocabs.add(char)
            if char in ['。','?','!','！','？']:
                datas.append([sample_x, sample_y])
                sample_x = []
                sample_y = []
        word_dict = {wd:index for index, wd in enumerate(list(vocabs))}
        self.write_file(list(vocabs), self.vocab_path)
        return datas, word_dict

    def modify_data(self):
        x_train = [[self.word_dict[char] for char in data[0]] for data in self.datas]
        y_train = [[self.class_dict[label] for label in data[1]] for data in self.datas]
        x_train = pad_sequences(x_train, self.TIME_STAMPS)
        y = pad_sequences(y_train, self.TIME_STAMPS)
        y_train = np.expand_dims(y, 2)
        return x_train, y_train

    def write_file(self, wordlist, filepath):
        with open(filepath, 'w+',encoding='utf-8') as f:
            f.write('\n'.join(wordlist))

    def load_pretrained_embedding(self):
        embeddings_dict = {}
        with open(self.embedding_file, 'r',encoding='utf-8') as f:
            for line in f:
                values = line.strip().split(' ')
                if len(values) < 300:
                    continue
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                embeddings_dict[word] = coefs
        print('Found %s word vectors.' % len(embeddings_dict))
        return embeddings_dict

    def build_embedding_matrix(self):
        embedding_dict = self.load_pretrained_embedding()
        embedding_matrix = np.zeros((self.VOCAB_SIZE + 1, self.EMBEDDING_DIM))
        for word, i in self.word_dict.items():
            embedding_vector = embedding_dict.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector
        return embedding_matrix

    def tokenvec_bilstm2_crf_model(self):
        model = Sequential()
        embedding_layer = Embedding(self.VOCAB_SIZE + 1,
                                    self.EMBEDDING_DIM,
                                    weights=[self.embedding_matrix],
                                    input_length=self.TIME_STAMPS,
                                    trainable=False,
                                    )
        model.add(embedding_layer)
        model.add(Bidirectional(LSTM(128, return_sequences=True)))
        model.add(Dropout(0.5))
        model.add(Bidirectional(GRU(128, return_sequences=True)))
        model.add(Dropout(0.5))
        model.add(TimeDistributed(Dense(self.NUM_CLASSES)))
        crf_layer = CRF(self.NUM_CLASSES, sparse_target=True)
        model.add(crf_layer)
        model.compile('RMSprop', loss=crf_layer.loss_function, metrics=[crf_layer.accuracy])
        model.summary()
        return model

    def train_model(self):
        x_train, y_train = self.modify_data()
        model = self.tokenvec_bilstm2_crf_model()
        history = model.fit(x_train[:], y_train[:], validation_split=0.2, batch_size=self.BATCH_SIZE, epochs=self.EPOCHS)
        model.save(self.model_path)
        return model

    def precision(y_true, y_pred):
        # Calculates the precision
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

    def recall(y_true, y_pred):
        # Calculates the recall
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    def fbeta_score(y_true, y_pred, beta=1):
        # Calculates the F score, the weighted harmonic mean of precision and recall.
        if beta < 0:
            raise ValueError('The lowest choosable beta is zero (only precision).')

        # If there are no true positives, fix the F score at 0 like sklearn.
        if K.sum(K.round(K.clip(y_true, 0, 1))) == 0:
            return 0

        p = precision(y_true, y_pred)
        r = recall(y_true, y_pred)
        bb = beta ** 2
        fbeta_score = (1 + bb) * (p * r) / (bb * p + r + K.epsilon())
        return fbeta_score

if __name__ == '__main__':
    ner = LSTMNER()
    ner.train_model()
