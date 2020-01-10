from keras import backend as K
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

import numpy as np
from keras.callbacks import Callback


def crf_acc(y_true, y_pred):
    '''Use Viterbi algorithm to get best path, and compute its accuracy.
    `y_pred` must be an output from CRF.'''
    crf, idx = y_pred._keras_history[:2]
    X = crf._inbound_nodes[idx].input_tensors[0]
    mask = crf._inbound_nodes[idx].input_masks[0]
    y_pred = crf.viterbi_decoding(X, mask)
    return _get_acc(y_true, y_pred, mask, crf.sparse_target)


def _get_acc(y_true, y_pred, mask, sparse_target=False):
    y_pred = K.argmax(y_pred, -1)
    if sparse_target:
        y_true = K.cast(y_true[:, :, 0], K.dtype(y_pred))
    else:
        y_true = K.argmax(y_true, -1)
    judge = K.cast(K.equal(y_pred, y_true), K.floatx())
    if mask is None:
        return K.mean(judge)
    else:
        mask = K.cast(mask, K.floatx())
        return K.sum(judge * mask) / K.sum(mask)


def _get_recall(y_true, y_pred, mask,  sparse_target=False):
    y_pred = K.argmax(y_pred, -1)
    if sparse_target:
        y_true = K.cast(y_true[:, :, 0], K.dtype(y_pred))
    else:
        y_true = K.argmax(y_true, -1)
    mask = K.cast(mask, K.floatx())
    y_true = K.cast(y_true, K.floatx())
    y_pred = K.cast(y_pred, K.floatx())
    y_true = y_true * mask
    y_pred = y_pred * mask
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    # y_true = np.max(y_true, axis=1)
    # y_pred = np.max(y_pred, axis=1)
    recall = recall_score(y_true, y_pred)
    return K.cast_to_floatx(recall)


# class Metrics(Callback):
#     def on_train_begin(self, logs={}):
#         self.val_f1s = []
#         self.val_recalls = []
#         self.val_precisions = []
#
#     def on_batch_end(self, batch, logs=None):
#
#         return
#
#     def on_epoch_end(self, epoch, logs={}):
#         predict = np.asarray(self.model.predict(self.validation_data[0]))
#         val_predict = np.argmax(predict, axis=-1)
#         true_y = self.validation_data[1]
#         val_targ = np.argmax(true_y, axis=1)
#         _val_f1 = f1_score(val_targ, val_predict, average='macro')
#         self.val_f1s.append(_val_f1)
#         print(' — val_f1:', _val_f1)
#         return