import pyrebase
import os

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


firebase = pyrebase.initialize_app(firebaseconfig)

dir_name = "nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

storage = firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)