#VERSION 0.0.0
print ("------ AUTHOR: NaTaN ANDRADE ------")
print ("Universidade Federal de São Paulo (UNIFESP)")
print ("Instituto de Ciência e Tecnologia (ICT)") 
print ("São José dos Campos (SJC)")
print ("Estado de São Paulo (SP) ")
print ("BRASIL")

import matplotlib
import numpy as np
import tensorflow as tf
import os
import os.path
import pandas as pd
import SimpleITK as sitk
from dltk.io.preprocessing import *
from matplotlib import pyplot as plt
from medpy.filter import IntensityRangeStandardization
from glob import glob
from os.path import basename
from tensorflow import image
matplotlib.interactive(True)


# Extrair o gzip
os.system("for i in `ls *.gz`; do gzip -d $i; done")

def encontrar_arq(caminho):
    arquivos = glob(caminho + '*.nii')
    for arquivo in arquivos:
        print(arquivo)
        return arquivos


caminho ='/home/name_computer/Images_IXI/'

resp = encontrar_arq(caminho)

#Just an example of how to make patches ....
#There are ready-made functions that perform much more widely
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html
#https://www.tensorflow.org/api_docs/python/tf/image/extract_image_patches

def patches_9(arr):
    patches=[]
    patch1 = np.array(arr[0:119,0:119])
    patches.append(patch1)
    patch2 = arr[0:119,120:239]
    patches.append(patch2)
    patch3 = arr[120:239,0:119]
    patches.append(patch3)
    patch4 = arr[120:239,120:239]
    patches.append(patch4)
    return patches

patches = np.zeros((1,14161))


cont = 0
for arq in resp:
    sitk_t1 = sitk.ReadImage(arq)
    t1_array = sitk.GetArrayFromImage(sitk_t1)
    a = np.shape(t1_array)
    if (a[0] == 162 and a[1] == 240 and a[2] == 240): 
        t1_87_240_240 = np.flip(t1_array[87,:,:]) 
        np.shape(t1_87_240_240)
        t1= normalise_zero_one(t1_87_240_240)
        img = np.copy(t1)
        np.shape(img)
        aux=[]
        aux = patches_9(img)
        cont = cont+1
        for a in aux:
            a=np.array(a)
            a=a.reshape(1,14161)
            a_aux = np.copy(a)
            patches = np.vstack((patches,a_aux))
            np.shape(patches)
patches=np.delete(patches,0,0)
np.shape(patches)        
np.save('/home/name_computer/IXI_T1_valid.npy',patches)


