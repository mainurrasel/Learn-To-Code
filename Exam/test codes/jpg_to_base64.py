import os
import base64

#Reading list of files from a folder.
directory = 'C:/Users/Mainur/Pictures/example'
print("List of the files in the folder:","\n")
for root, directories, files in os.walk(directory):
	for name in files:
		print(os.path.join(name))
print()

#Convert files to base64 string.
print("File name with base64 strings:","\n")
for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                with open(os.path.join(directory, filename), "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    print("File Name:",filename)
                    print("base64 String:", encoded_string.decode('utf-8'),"\n")
        
                
            

