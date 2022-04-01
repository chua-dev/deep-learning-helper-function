# Rename Image Datasets to Standard naming convention
import os
def rename_all_image_with_index(folder_path, image_name):
	for i, filename in enumerate(os.listdir(folder_path)):
		destination_name = folder_path + filename
		desired_name = folder_path + image_name + str(i) + ".jpg"
		print(f'DESTINATION => {destination_name} | DESIRED => {desired_name}')
		os.rename(folder_path + filename, folder_path + image_name + str(i) + ".jpg")

# Create np array images Datasets using directory, that can be used to train
import numpy as np
import os
import cv2
def create_dataset(img_folder, IMG_HEIGHT, IMG_WIDTH):
  img_data_array=[]
  target_class_array=[] # To get target class
  
  for dir1 in os.listdir(img_folder):
      for file in os.listdir(os.path.join(img_folder, dir1)):
      
          image_path= os.path.join(img_folder, dir1,  file)
          image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)
          image=cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH),interpolation = cv2.INTER_AREA)
          image=np.array(image)
          image = image.astype('float32')
          image /= 255 
          img_data_array.append(image)
          target_class_array.append(dir1)
  return img_data_array, target_class_array

