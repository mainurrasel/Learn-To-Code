#importing modules
import os
import base64
import requests

url = "http://172.16.7.17:8000/v1/api/nidscan/"

#Reading list of files from a folder.
directory = 'C:/Users/Mainur/Pictures/example'
print("List of the files in the folder:","\n")
for root, directories, files in os.walk(directory):
	for name in files:
		print(os.path.join(name))
print()

#Read one file at a time and convert to base64 string
print("File name with base64 strings and Information:","\n")
for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                with open(os.path.join(directory, filename), "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    decode_utf = encoded_string.decode('utf-8')
                    print("File Name:",filename,"         base64 String:",decode_utf)
                    
#ApI call with the base64 string.
                    body="{\"image\": \""+decode_utf+"\"}"
                    headers = {
                    'Content-Type': 'application/json'
                    }
                    
#Get ApI response.
                    response = requests.post(url, headers=headers, data=body)
                    
#Save API response with the same name as the image file.
                    print(filename,"Information:")
                    print()
                    print(response.text)
                    print()
                    

