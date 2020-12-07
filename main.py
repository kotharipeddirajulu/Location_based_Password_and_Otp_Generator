''' our main aim is to generate a password based on the strength of password required
low,medium,strong type and
TO GENERATE THE PASSWORD BASED ON THE LOCATION OF '''

# Python program to generate random
# password using Tkinter module


import ciph_lat_long   #IMPORT THE ciph_lat_long
import random
import pyperclip
import string
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image


# Function for calculation of password
def low():
    entry.delete(0, END)

    # Get the length of passowrd
    length = var1.get()
    symbols = "!@#$%^&*()"
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    advanced = poor + average + symbols
    password = ""

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(poor)
        return password

        # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(average)
        return password

        # if strength selected is strong
    elif var.get() ==3:
        for i in range(0, length):
            password = password + random.choice(advanced)
        return password
    else:
        print("Please choose an option")


# Function for calculating a location based password
def location():
    entry.delete(0, END)

    # Get the length of passowrd
    length = var1.get()

    obj = ciph_lat_long.encoded_integers()
    encoded_coordinates = obj.encoded_coord_data
    #encoded_low_loc = obj.encoded_lower_location
    #encoded_upp_loc = obj.encoded_upper_location
    symbols = "!@#$%^&*()"
    poor = string.ascii_lowercase + string.ascii_uppercase
    average = string.ascii_uppercase + string.ascii_lowercase+str(encoded_coordinates)
    advanced = poor + average + symbols
    password = ""

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(poor)
        return password

        # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(average)
        return password

        # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(advanced)
        return password
    else:
        print("Please choose an option")

def location_based_numeric_password():
    entry1.delete(0, END)
    obj1 = ciph_lat_long.encoded_integers
    encoded_numeric = obj1.encoded_coord_data
    password = ""
    # Get the length of passowrd
    length = var1.get()
    for i in range(0, length):
        password =password + random.choice(str(encoded_numeric))
    return password


# Function for generation of password
def generate_low():
    password1 = low()
    entry.insert(10, password1)


def generate_location_based_password():
    password2 = location()
    entry.insert(10, password2)

def generate_location_based_numerical_password():
    password3 = location_based_numeric_password()
    entry1.insert(10, password3)


# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

def copy2():
    random_password1 = entry1.get()
    pyperclip.copy(random_password1)



# Main Function

# create GUI window
root = Tk()
root.configure(background='darkslategray')
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Location based and Random Password Generator")
my_pic = Image.open("res/icon-2019-privacy.png")
resize = my_pic.resize((100,100),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize)
my_label = Label(root,image=new_pic)
my_label.grid(column=1,pady=20)
#Open Image


# create label and entry to show
# password generated
Random_password = Label(root, text="PASSWORD",relief="sunken",style="P.TButton")
Random_password.grid(row=1,column=0)
Random_password1 = Label(root, text="OTP",relief="sunken",style="O.TButton")
Random_password1.grid(row=3,column=0,padx=20,pady=20)
entry = Entry(root,style='E.TButton')
entry.grid(row=1, column=1,pady=10,padx=10)
entry1= Entry(root,style='E.TButton')
entry1.grid(row=3, column=1,pady=20,padx=10)

# create label for length of password
c_label = Label(root, text="LENGTH",relief="raised",style='L1.TButton')
c_label.grid(row=5,column=0,padx=10,pady=10)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
style = Style()# This will create style object
# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).

style.configure('C.TButton',background='green',foreground='white',font=('bold'))
style.configure('R.TButton',background='orangered',foreground='black',font=('bold'))
style.configure('L.TButton',background='turquoise3',foreground='black',font=('bold'))
style.configure('P.TButton',background='orange',foreground='black',font=('bold'),relief="raised")
style.configure('L1.TButton',background='orange',foreground='black',font=('bold'))
style.configure('E.TButton',background='white',foreground='black',font=('bold'),relief="sunken")
style.configure('O.TButton',background='orange',foreground='black',font=('bold'),relief="sunken")

copy_button = Button(root, text="Copy",command=copy1,style='C.TButton')
copy_button.grid(row=1, column=2)
copy_button = Button(root, text="Copy",command=copy2,style='C.TButton')
copy_button.grid(row=3, column=2)
generate_button3 = Button(root, text="Generate-OTP", command=generate_location_based_numerical_password,style='R.TButton')
generate_button3.grid(row=4, column=1,pady=10,padx=10)
generate_button = Button(root, text="Random Password", command=generate_low,style='R.TButton')
generate_button.grid(row=2, column=1,pady=10,padx=10)
generate_button2 = Button(root, text="Geographic-Password", command=generate_location_based_password,style='L.TButton')
generate_button2.grid(row=2, column=2,pady=10,padx=10)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_location_based_password = Radiobutton
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=5, sticky='W',column=2,pady=10,padx=10)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=6, sticky='W',column=2,pady=10,padx=10)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=7, sticky='W',column=2,pady=10,padx=10)
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (4,6,8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=5)

# start the GUI
root.mainloop()


