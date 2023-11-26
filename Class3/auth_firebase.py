import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")
firebase_admin.initialize_app(cred)

email = "hi@gmail.com"
password = "hiagain"
phone_number = "+886912515971"

user = auth.create_user(email = email, password = password, phone_number = phone_number)
print("User create successfully! {}".format(user.uid))