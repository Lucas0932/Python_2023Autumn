# import firebase
import firebase_admin
from firebase_admin import credentials, storage
# import secret key
cred = credentials.Certificate("../yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")



# initiate firebase
firebase_admin.initialize_app(cred, {"storageBucket" : "yayay-e2c6c.appspot.com"})
file_path = "Firebase_project/image/bed1.jpg"
bucket = storage.bucket()
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)