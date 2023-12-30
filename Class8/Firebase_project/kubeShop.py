# 引入 tkinter module
from tkinter import *
from ttkthemes import *
# 引入 Pillow module
from PIL import Image, ImageTk
# 引入 tkinter 的 messagebox
# import firebase admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#----------------------------------------------------------------------
# import secret key
cred = credentials.Certificate("../../yayay-e2c6c-firebase-adminsdk-1gbl4-ee555d057c.json")
# initiate firebase
firebase_admin.initialize_app(cred)
# initiate firestore
db = firestore.client()
def getProductInfo(product_id): # Use product id to differenciate which product's info we want to.
    # Get path to the product info
    collection_name = "Autumn2023_Class7_Products" 
    document_name = "product{}".format(product_id)
    doc_ref = db.collection(collection_name).document(document_name)

    # Get info from the path. Remember to use try/except to avoid failing.
    try:
        doc = doc_ref.get()
        doc_dict = doc.to_dict()
        print("The content of the document is：{}".format(doc_dict))
    except:
        print("The reference of document is not exist, please check the path is correct or not.")

    # Transfer product info dictionary to display string.
    display_text = "{}, {} {}/{}".format(doc_dict['category'], doc_dict['origin'], doc_dict['color'], doc_dict['material'])
    display_price = "NT.{}".format(doc_dict['price'])

    return display_text, display_price
# 建立主視窗 Frame
root = ThemedTk(theme="awdark", toplevel=True, themebg=True)
# 設定視窗標題
root.title('KubeTech Shop')
# 設定視窗大小
root.geometry('880x650')

display_text01, display_price01 = getProductInfo("01")
# Product1 Label & Button 元件
p1img = Image.open('image/sofa1.jpg')
p1img = p1img.resize((202,200))
p1img = ImageTk.PhotoImage(p1img)
p1piclabel = Label(root, image=p1img, width=202, height=200)
p1namelabel = Label(root, text=display_text01, font=('Inter', 11), fg='#000000')
p1pricelabel = Label(root, text=display_price01, font=('Inter', 10), fg='#000000')
p1numlabel = Label(root, text='0', font=('Inter', 12, 'bold'), fg='#000000')
p1addbutton = Button(root, text='+', font=('Inter', 10), fg='#1E1E1E', bg='#E7E2E2')
p1minusbutton = Button(root, text='-', font=('Inter', 10), fg='#1E1E1E', bg='#E7E2E2')

# Product1 Layout
p1piclabel.grid(row=0, column=0, columnspan=2,sticky=W, padx=5)
p1namelabel.grid(row=1, column=0,columnspan=2,sticky=W, padx=5)
p1pricelabel.grid(row=2, column=0, sticky=W, padx=5)
p1minusbutton.grid(row=2, column=1, sticky=W)
p1numlabel.grid(row=2, column=1, sticky=W+E+N+S)
p1addbutton.grid(row=2, column=1, sticky=E)

display_text02, display_price02 = getProductInfo("02")
# Product2 Label & Button 元件
p2img = Image.open('image/sofa2.jpg')
p2img = p2img.resize((202,200))
p2img = ImageTk.PhotoImage(p2img)
p2piclabel = Label(root, image=p2img, width=202, height=200)
p2namelabel = Label(root, text=display_text02, font=('Inter', 11), fg='#000000')
p2pricelabel = Label(root, text=display_price02, font=('Inter', 10), fg='#000000')
p2numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p2addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')
p2minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')

# Product2 Layout
p2piclabel.grid(row=0, column=2, columnspan=2, sticky=W,padx=5)
p2namelabel.grid(row=1, column=2, columnspan=2, sticky=W, padx=5)
p2pricelabel.grid(row=2, column=2, sticky=W, padx=5)
p2minusbutton.grid(row=2, column=3, sticky=W)
p2numlabel.grid(row=2, column=3, sticky=W+E+N+S)
p2addbutton.grid(row=2, column=3, sticky=E)

display_text03, display_price03 = getProductInfo("03")
# Product3 Label & Button 元件
p3img = Image.open('image/sofa3.jpg')
p3img = p3img.resize((202,200))
p3img = ImageTk.PhotoImage(p3img)
p3piclabel = Label(root, image=p3img, width=202, height=200)
p3namelabel = Label(root, text= display_text03, font=('Inter', 11), fg='#000000')
p3pricelabel = Label(root, text=display_price03, font=('Inter', 10), fg='#000000')
p3numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p3addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')
p3minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')

# Product3 Layout
p3piclabel.grid(row=0, column=4, columnspan=2, sticky=W,padx=5)
p3namelabel.grid(row=1, column=4, columnspan=2, sticky=W, padx=5)
p3pricelabel.grid(row=2, column=4, sticky=W, padx=5)
p3minusbutton.grid(row=2, column=5, sticky=W)
p3numlabel.grid(row=2, column=5, sticky=W+E+N+S)
p3addbutton.grid(row=2, column=5, sticky=E)

display_text04, display_price04 = getProductInfo("04")
# Product4 Label & Button 元件
p4img = Image.open('image/sofa4.jpg')
p4img = p4img.resize((202,200))
p4img = ImageTk.PhotoImage(p4img)
p4piclabel = Label(root, image=p4img, width=202, height=200)
p4namelabel = Label(root, text=display_text04, font=('Inter', 11), fg='#000000')
p4pricelabel = Label(root, text=display_price04, font=('Inter', 10), fg='#000000')
p4numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p4addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')
p4minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2')

# Product4 Layout
p4piclabel.grid(row=0, column=6, columnspan=2, sticky=W,padx=5)
p4namelabel.grid(row=1, column=6, columnspan=2, sticky=W, padx=5)
p4pricelabel.grid(row=2, column=6, sticky=W, padx=5)
p4minusbutton.grid(row=2, column=7, sticky=W)
p4numlabel.grid(row=2, column=7, sticky=W+E+N+S)
p4addbutton.grid(row=2, column=7, sticky=E)




# 執行主程式
root.mainloop()