# import firebase admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#----------------------------------------------------------------------
# import secret key
cred = credentials.Certificate("yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")
# initiate firebase
firebase_admin.initialize_app(cred)
# initiate firestore9o
db = firestore.client()
# write a dictionary
doc = {"name" : "Prince", "email": "prince@gmail.com-"}
#---
# insert data typed into firebase
# doc_ref = db.collection("Autumn2023_Students").document("student01")
# doc_ref.set(doc)
#---
# insert random things into firebase
# collection_ref = db.collection("Autumn2023_Students")
# collection_ref.add(doc)
#---
# insert name and info into firebase
# doc1 = {"name": "Jaclyn", "email": "jaclyn@gmail.com"}
# doc_ref = db.collection("Autumn2023_Students").document("student02")
# doc_ref.set(doc1)
#---
# try if check path is right
# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# try:
#     doc = doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document is :{}".format(doc_dict))
# except:
#     print("The reference of document does not exist, please check the path is correct or not. {}".format(path))
#---
path = "Autumn2023_Students"
collection_ref = db.collection(path)
#---
# docs = collection_ref.get()
# for doc in docs:
#     print("The content of document is :{}".format(doc.to_dict()))
#---
# docs = collection_ref.where("name", "==", "Jaclyn").get()
# for doc in docs:
#     print("The content of document is :{}".format(doc.to_dict()))
#---
# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# doc = {"birthday": "1231"}
# doc_ref.update(doc)
#---
# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# contacts = {"email":"prince@gmail.con", "phone": "0912515971"}
# doc = {"contacts": contacts}
# doc_ref.update(doc)
#---
# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# doc = {"contacts.email": "abc@gmail.com"}
# doc_ref.update(doc)
#---
# path = "Autumn2023_Students/student02"
# doc_ref = db.document(path)
# doc = {"email": "niceday@gmail.com"}
# doc_ref.update(doc)
#---
# path = "Autumn2023_Students/student02"
# doc_ref = db.document(path)
# doc_ref.delete()
#---
students_ref = db.collection("Autumn2023_Students")
docs = students_ref.get()
for doc in docs:
    doc.reference.delete()