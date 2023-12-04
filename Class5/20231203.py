# import pyrebase
import pyrebase
# import everything in tkinter
from tkinter import * 

# Firebase Configuration
firebaseconfig = {
  "apiKey": "AIzaSyAAtnfE9hLYnjttc6lMpas_4pyNIVPwDck",
  "authDomain": "yayay-e2c6c.firebaseapp.com",
  "projectId": "yayay-e2c6c",
  "storageBucket": "yayay-e2c6c.appspot.com",
  "messagingSenderId": "967513318932",
  "appId": "1:967513318932:web:0c32f47abe59c93deee901",
  "databaseURL": ""
};
# Connect firebase and python
firebase = pyrebase.initialize_app(firebaseconfig)
# Get auth from firebase
auth = firebase.auth()

# Create new window
root =Tk()
# Create text
loginlabel = Label(root, text = "Login Page")
accountlabel = Label(root, text = "Account")
passwordlabel = Label(root, text = "Password")
resultlabel = Label(root, text = "")
# Create text bar
accountentry = Entry(root)
passwordentry = Entry(root, show = "*")
# Create signup button
signupbutton = Button(root, text = "Sign Up", width = 10, command = lambda: addUser(root, accountentry, passwordentry))
# Pack the things
loginlabel.pack(pady = 5)
accountlabel.pack(pady = 5)
passwordlabel.pack(pady = 5)
resultlabel.pack(pady = 5)
accountentry.pack(pady = 5)
passwordentry.pack(pady = 5)
signupbutton.pack(pady = 5)
# Create funtion addUser
def addUser(view, accountentry, passwordentry):
    # Print account and password entered
    print(accountentry.get(), passwordentry.get())
    print("Sign up...")
    # Change account and password into variables
    account = accountentry.get()
    password = passwordentry.get()
    # Try if it is ok
    try:
        user = auth.create_user_with_email_and_password(account, password)
        print("Sucessfully signup!")
        resultlabel.config(text = "Sucessfully signup!")
    except Exception as e:
        print(f"Create Account Failed...: {e}")
        resultlabel["text"] = "Create Account Failed..."

# Make root continuing running
# root.mainloop()
#------------------------------------------------------------------------------------------
# Create new class
class Color:
    def __init__(self, color):
        self.color = color
        self.next = None

# Define colors
Blue = Color("blue")
Red = Color("red") 
Black = Color("black")
Pink = Color("Pink")
# Draw arrows on them
head = Blue
Blue.next = Red
Red.next = Pink 
Pink.next = Black

# Create funtion traverse
def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}.". format(ptr.color))
        ptr = ptr.next

traverse(head)
print("Finish traverse!")