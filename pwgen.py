import random
import string
import sys
from tkinter import *
import threading

window = Tk()
window.title("Password Generator")
window.geometry("300x100")
window.config(background="black")


def hider():
    text3.pack_forget()
    start()



def transform():
    global user
    user = e.get()
    global x
    if user.isdecimal():
        x = int(user)
        genPw()
    else:
        global text3
        text3=Label(window, fg="red2",background="black",text="Wrong command! Needs to be integrer.Try Again")
        text3.pack(pady=20)
        time = threading.Timer(4,hider)
        time.start()









def genPw():

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    temp = random.sample(all,x)
    global password
    password = "".join(temp)
    text2=Label(window,fg="lawn green",background="black")
    text2.config(font=('Noto Mono',30))
    text2["text"]=password
    text2.pack(pady=20)




def start():
    text1 = Label(window,text="Give the length of password: ",background="black",fg="lawn green")
    text1.pack()
    global e
    e = Entry(window, width=5)
    e.pack()
    gen_button = Button(window, text = "Generate password", background="gray53", fg="lawn green", command= lambda:[transform(),text1.pack_forget(),e.pack_forget(),gen_button.pack_forget()])
    gen_button.pack(pady=10)








start_button = Button(window, text = "Start", fg="lawn green",background="gray53",command=lambda:[start(),start_button.pack_forget()])
start_button.pack(pady=30)










window.mainloop()
