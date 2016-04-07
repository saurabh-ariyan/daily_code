import os;
def rename_files():
	#Find the names for all the files in a list
	file_list = os.listdir(r"/home/sariyan/Downloads/MLND/prank");
	print(file_list)

	#for each file in file_list rename the file
	for file in file_list:
		new_name = ''.join([i for i in file if not i.isdigit()]);
		os.rename(file, new_name);

rename_files()
	
