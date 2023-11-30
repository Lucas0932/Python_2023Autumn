
import pyrebase
firebaseconfig = {
  "apiKey": "AIzaSyAAtnfE9hLYnjttc6lMpas_4pyNIVPwDck",
  "authDomain": "yayay-e2c6c.firebaseapp.com",
  "projectId": "yayay-e2c6c",
  "storageBucket": "yayay-e2c6c.appspot.com",
  "messagingSenderId": "967513318932",
  "appId": "1:967513318932:web:0c32f47abe59c93deee901",
  "databaseURL": ""
};
firebase = pyrebase.initialize_app(firebaseconfig)
auth = firebase.auth()

def signup():
    email = input("Please enter ur email: ")
    password = input("Please enter ur password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Sucessfully signup!")
    except:
        print("Invaild email or password!")
#signup()

def login():
    print("Log in...")
    email = input("Please enter ur email: ")
    password = input("Please enter ur password: ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Sucessfully Login!")
        print(user["localId"])
    except:
        print("Invaild email or password!")
#login()

class Car:
    def __init__(self, color):
        self.color = color
        self.next = None
head = Car("red")
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}.". format(ptr.color))
        ptr = ptr.next
traverse(head)
