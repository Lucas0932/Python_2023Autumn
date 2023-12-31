# import firebase
import firebase_admin
from firebase_admin import credentials, storage
import os
# import secret key
cred = credentials.Certificate("../yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")


#---
# initiate firebase
firebase_admin.initialize_app(cred, {"storageBucket" : "yayay-e2c6c.appspot.com"})
bucket = storage.bucket()
def upload_blob(bucket, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File{source_file_name} up load to {destination_blob_name}")
#upload_blob(bucket, "下載 (7).jpg", "Taipei-101/101-3.png")
#---
# dir_path = "./taipei"
# filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
# print(filelist)
# #---
# bucket = storage.bucket()
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "Taipei-101/"+file
#     print("Now is uploading file {}." .format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)
#---
bucket = storage.bucket()
blob = bucket.blob("nature/beautiful_sea.png")
blob.download_to_filename("my_love.png")