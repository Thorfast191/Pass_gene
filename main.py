from tkinter import *
import random, string
import pyperclip
import secrets


window = Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title('Password Generator')

heading1=Label(window, text='Password Generator', font='arial 20 bold', ).pack(pady=10)

Pass_label = Label(window, text='Select Password Length!', font='arial 15 bold').pack(padx=10,pady=10)

pass_len = IntVar()

len = Spinbox(window, from_=8, to=32, textvariable=pass_len, width=20,).pack()

pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(window, text = "GENERATE PASSWORD" , command = Generator).pack(pady= 5)
Entry(window, textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_len.get())
Button(window, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

window.mainloop()