import numpy as np
import tensorflow as tf
import os
import sys
import time

class FNNCell(object):
    def __init__(self, input_size, hidden_size, num_layer, output_size):
        '''
            Args :
            return :
            
                
        '''
        self._input_size = input_size
        self._hidden_size = hidden_size
        self._output_size = output_size
        self._num_layer = num_layer
        
    
    @property
    def input_size(self):
        return self._input_size
    
    @property
    def state_size(self):
        return self._hidden_size
    
    @property
    def output_size(self):
        return self._output_size
    
    @property
    def num_layer(self):
        return self._num_layer
        
    def __call__(self, inputs, scope = None):
        '''
            return:
                output : state[-1]
                state : state[:-1]
        '''
        with tf.variable_scope(scope or type(self).__name__): #FNN
            w = list()
            b = list()
            state = list()
            layers = [self._input_size] + [self._hidden_size] * self._num_layer + [self._output_size]
            
            
            for i in xrange(len(layers) - 1):
                w.append(tf.get_variable(name = 'W_{}'.format(i), shape = [layers[i], layers[i+1]], dtype = tf.float32 ))
                b.append(tf.get_variable(name = 'b_{}'.format(i), shape = [layers[i+1]]))
                if i ==0 :
                    xw_b = tf.nn.xw_plus_b(inputs, w[i], b[i])
                else :
                    xw_b = tf.nn.xw_plus_b(state[-1], w[i], b[i])
                
                if i != len(layers)-2 :
                    state.append(tf.sigmoid(xw_b))
                else : # softmax for last layer
                    state.append(tf.nn.softmax(xw_b))
            return state[-1], state[:-1]
        