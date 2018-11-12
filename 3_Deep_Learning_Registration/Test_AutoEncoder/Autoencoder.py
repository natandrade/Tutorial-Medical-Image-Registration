#Carregar Bibliotecas
from keras.layers import Input, Dense
from keras.models import Model
from keras import regularizers
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.interactive(True)
from keras.utils import plot_model
from keras.callbacks import TensorBoard
import os.path
    
enc_dim_aux = []
lin = 119
col = 119
entrada = lin * col

epoch_aux = []
batch_tam_aux = []
losses='mean_squared_error'
optimi ='adadelta'
 
test = np.array(0)   
for enc_dim in enc_dim_aux:
    for epoch in epoch_aux:
        for batch_tam in batch_tam_aux:
            x_train = np.load('/home/natan/Python_Tutoriais/Test_Tcc/IXI_T1_train.npy')    
            np.shape(x_train)
            x_test = np.load('/home/natan/Python_Tutoriais/Test_Tcc/IXI_T1_valid.npy')
            np.shape(x_test)
    
            encoding_dim = enc_dim  
    
            input_img = Input(shape=(entrada,))
    
            encoded = Dense(encoding_dim, activation='relu')(input_img)
    
            decoded = Dense(entrada, activation='sigmoid')(encoded)
            autoencoder = Model(input_img, decoded)
            encoder = Model(input_img, encoded)

            encoded_input = Input(shape=(encoding_dim,))
    
            decoder_layer = autoencoder.layers[-1]
    
            decoder = Model(encoded_input, decoder_layer(encoded_input))

            autoencoder.compile(optimizer=optimi, loss=losses)
            history = autoencoder.fit(x_train, x_train,
                        epochs=epoch,
                        batch_size= batch_tam,
                        shuffle=True,
                        validation_data=(x_test, x_test),
                        callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])

            test = np.array(test)
            loss_history = history.history["loss"]
            numpy_loss_history = np.array(loss_history)
            a=[]
            #a='loss_history'+np.array2string(test)+'.txt'
            a = '/home/name_computer/weights/'+'loss_history_'
            a = a + np.array2string(numpy_loss_history[-1])+'_test_'+np.array2string(test)+'.txt'
            np.savetxt(a, numpy_loss_history, delimiter=",")

            val_loss_history = history.history["val_loss"]
            val_numpy_loss_history = np.array(val_loss_history)
            a=[]
            a = '/home/name_computer/weights/'+'val_loss_history_'
            a = a + np.array2string(val_numpy_loss_history[-1])+'_test_'+np.array2string(test)+'.txt'
            np.savetxt(a, val_numpy_loss_history, delimiter=",")
            # Salve weights
            a = '/home/name_computer/weights/'+np.array2string(test)+'_encoder_weights.h5'
            encoder.save(a)
            b = '/home/name_computer/weights/'+np.array2string(test)+'_decoder_weights.h5'
            decoder.save(b)
            c = '/home/name_computer/weights/'+np.array2string(test)+'_autoencoder_weights.h5'
            autoencoder.save(c)       
'''
#### Test_Process ########
from keras.models import load_model
import numpy as np

test = np.array(15)
lin = 119
col = 119

a = '/home/name_computer/weights/'+np.array2string(test)+'_encoder_weights.h5'
b = '/home/name_computer/weights/'+np.array2string(test)+'_decoder_weights.h5'
c = '/home/name_computer/weights/'+np.array2string(test)+'_autoencoder_weights.h5'

encoder = load_model(a)
decoder = load_model(b)
autoencoder = load_model(c)

inputs = np.load('/home/name_computer/validacao/IXI_T1_valid.npy')

x = encoder.predict(inputs)
y = decoder.predict(x)

print('Input: {}'.format(inputs))
print('Encoded: {}'.format(x))
print('Decoded: {}'.format(y))


import matplotlib.pyplot as plt
import matplotlib
matplotlib.interactive(True)

n = 4  
plt.figure()
for i in range(0,n):
    ax = plt.subplot(2, n, i + 1)
    #Test is input
    plt.imshow(inputs[i].reshape(lin,col))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(y[i].reshape(lin , col))
    #decoded_imgs
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
#
#
#

plt.show()
'''
