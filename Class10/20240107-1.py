# import mods
import pyrebase
import os

dir_name = "project_images"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# import secret key
firebaseconfig = {
  "apiKey": "AIzaSyAAtnfE9hLYnjttc6lMpas_4pyNIVPwDck",
  "authDomain": "yayay-e2c6c.firebaseapp.com",
  "projectId": "yayay-e2c6c",
  "storageBucket": "yayay-e2c6c.appspot.com",
  "messagingSenderId": "967513318932",
  "appId": "1:967513318932:web:0c32f47abe59c93deee901",
  "databaseURL": "",
  "serviceAccount":"../yayay-e2c6c-firebase-adminsdk-1gbl4-204c585238.json"
}

# initiate firebase
firebase = pyrebase.initialize_app(firebaseconfig)
#------------------------------------------------------------------------------------
# def upload_blob(bucket, source_file_name, destination_blob_name):
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(source_file_name)
#     print(f"File{source_file_name} up load to {destination_blob_name}")
# bucket = storage.bucket()
# dir_path = "./Firebase_project/image"
# filelist = [f for f in os.listdir(dir_path)]
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "project_images/"+file
#     print("Now is uploading file {}." .format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)
#------------------------------------------------------------------------------------

storage = firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)