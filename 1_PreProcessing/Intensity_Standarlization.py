import os
import os.path
import matplotlib.pyplot as plt
import matplotlib
import nibabel as nib
import numpy as np
import glob as glob
from os.path import basename
from scipy import interpolate
from glob import glob
matplotlib.interactive(True)

os.system("for i in `ls *.gz`; do gzip -d $i; done")

def encontrar_arq(caminho):
    arquivos = glob(caminho + '*.nii')
    for arquivo in arquivos:
        print(arquivo)
        return arquivos

#Path Images
caminho ="/home/name_computer/test_intensity/"  
    
resp = encontrar_arq(caminho)

#Example for two images
img_filepath = resp[0]
img_mask_filepath = resp[1]
output_filepath = os.path.join('/home/name_computer/test_intensity_output/','Intensity_Padr_'+ basename(resp[0]))

PC1 = 0.2
PC2 = 99.8

S1 = 1500
S2 = 9500

# Reads input image and mask
input_img = nib.load(img_filepath)
input_data = input_img.get_data()

input_mask = nib.load(img_mask_filepath).get_data()

# Separate brain
input_brain = input_data[input_mask.astype(np.bool)]

# Input percentiles
input_pcs = np.percentile(input_brain, [PC1, PC2])

# Standard percentiles
std_pcs = [S1, S2]

# Standardization function
f = interpolate.interp1d(input_pcs, std_pcs, kind="linear", bounds_error=False, fill_value="extrapolate")

# Applies function
std_input = f(input_data) * input_mask

# Saves image
std_img = nib.Nifti1Image(std_input, input_img.affine, input_img.header)
nib.save(std_img, output_filepath)

input_img = nib.load(img_filepath)
input_data = input_img.get_data()
input_data = np.rot90(input_data)
np.shape(input_data)

input_img2 = nib.load(output_filepath)
input_data2 = input_img.get_data()
input_data2 = np.rot90(input_data2)
np.shape(input_data2)

plt.figure()
plt.subplot(1,2,1)
plt.title('Input')
#Choose Layer Brain
plt.imshow(input_data[:,:,115])
plt.gray()
plt.subplot(1,2,2)
plt.title('standardization of intensity')
plt.imshow(input_data2[:,:,115])
plt.gray()
plt.show()


#Acknowledgment
Eduardo Nigri 


