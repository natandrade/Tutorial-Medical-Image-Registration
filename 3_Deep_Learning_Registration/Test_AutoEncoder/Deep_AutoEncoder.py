#VERSION 0.0.0
print ("------ AUTHOR: NaTaN ANDRADE ------")
print ("Universidade Federal de São Paulo (UNIFESP)")
print ("Instituto de Ciência e Tecnologia (ICT)" )
print ("São José dos Campos (SJC)")
print ("Estado de São Paulo (SP) ")
print ("BRASIL")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os.path
from keras.layers import Input, Dense
from keras.models import Model
from keras import regularizers
from keras.datasets import mnist
from keras.utils import plot_model
from keras.callbacks import TensorBoard
from keras.optimizers import Adadelta, RMSprop,SGD,Adam
from keras.layers.advanced_activations import LeakyReLU   
matplotlib.interactive(True)


lin = 119
col = 119
entrada = lin * col
epoch_aux = [] 
batch_tam_aux = []  

losses='mean_squared_error'

optimi ='adadelta'

ativacao ='ReLU' 
 
test = np.array(0)   

for epoch in epoch_aux:
    for batch_tam in batch_tam_aux:
        x_train = np.load('/home/name_computer/IXI_T1_train.npy')    
        np.shape(x_train)
        x_test = np.load('/home/name_computer/IXI_T1_valid.npy') 
        np.shape(x_test)
        input_img = Input(shape=(14161,))
        
        #Exemplo 1  For the other examples see the work of Undergraduate thesis
        
        #encoded1 = Dense(512, activation='relu')(input_img)
        #encoded = Dense(256, activation='relu')(encoded1)
        #encoded = Dense(128, activation='relu')(encoded)
        
        #decoded = Dense(256, activation='relu')(encoded)
        #decoded = Dense(512, activation='relu')(decoded)
        #decoded = Dense(14161, activation='sigmoid')(decoded)      
        
        autoencoder = Model(input_img, decoded)
        autoencoder.compile(optimizer=optimi, loss=losses)
        history = autoencoder.fit(x_train, x_train,
                                  epochs=epoch,
                                  batch_size= batch_tam,
                                  shuffle=True,
                                  validation_data=(x_test, x_test),
                                  callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])
        #
        test = np.array(test)
        loss_history = history.history["loss"]
        numpy_loss_history = np.array(loss_history)
        a=[]
        a = '/home/name_computer/'+'loss_history_'
        a = a + np.array2string(numpy_loss_history[-1])+'_test_'+np.array2string(test)+'.txt'
        np.savetxt(a, numpy_loss_history, delimiter=",")
        val_loss_history = history.history["val_loss"]
        val_numpy_loss_history = np.array(val_loss_history)
        a=[]
        a = '/home/name_computer/'+'val_loss_history_'
        a = a + np.array2string(val_numpy_loss_history[-1])+'_test_'+np.array2string(test)+'.txt'
        np.savetxt(a, val_numpy_loss_history, delimiter=",")
        # Salvar Pesos
        bla = '/home/name_computer/'
        c = bla + np.array2string(test)+'_autoencoder_weights.h5'
        autoencoder.save(c)
        test=test+1
            

test = np.array(test)
loss_history = history.history["loss"]
numpy_loss_history = np.array(loss_history)
a=[]
a = '/home/name_computer/'+'loss_history_'
a = a + np.array2string(numpy_loss_history[-1])+'_test_'+np.array2string(test)+'.txt'
np.savetxt(a, numpy_loss_history, delimiter=",")
val_loss_history = history.history["val_loss"]
val_numpy_loss_history = np.array(val_loss_history)
