import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")
firebase_admin.initialize_app(cred)
