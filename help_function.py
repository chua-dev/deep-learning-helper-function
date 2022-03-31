import os

# Rename Image Datasets to standard naming convention
def rename_all_image_with_index(folder_path, image_name):
	for i, filename in enumerate(os.listdir(folder_path)):
		destination_name = folder_path + filename
		desired_name = folder_path + image_name + str(i) + ".jpg"
		print(f'DESTINATION => {destination_name} | DESIRED => {desired_name}')
		os.rename(folder_path + filename, folder_path + image_name + str(i) + ".jpg")