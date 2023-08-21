from tkinter import *

from functools import partial
import random


def main():
    w = Tk()
    w.geometry("500x500")
    w.title("Password Generator")
    l1 = Label(text="Password Generator", font=("center", 14), fg="Blue")
    l1.pack()
    l2 = Label(text="Enter user name:", font=("Arial", 12))

    l2.place(x=20, y=40)
    e1 = Entry(w, font=("Arial", 14))
    e1.pack()
    e1.place(x=200, y=40)
    l3 = Label(text="Enter password length:", font=("Arial", 12))

    l3.place(x=20, y=80)
    e2 = Entry(w, font=("Arial", 14))
    e2.pack()
    e2.place(x=200, y=80)
    l4 = Label(text="Generated password:", font=("Arial", 12))

    l4.place(x=20, y=120)
    e3 = Entry(w, font=("Arial", 14), fg="green")
    e3.pack()
    e3.place(x=200, y=120)
    n = e2.get()

    def password(length):
        list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-/<>|"
        pwd_str = ""

        g1 = e1.get()
        for i in range(length):
            pwd_str = pwd_str + random.choice(list_of_chars)
        e3.insert(0, pwd_str)

    def accept():
        r = e3.get()

        if r.isascii():
            print("successfully genearted password")
        else:
            print("not valid password")

    def reset():

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

    b1 = Button(text="Generate password", font=('center', 14), bg="blue", fg="white",
                command=lambda: password(eval(e2.get())))

    b1.pack()
    b1.place(x=150, y=200)
    b2 = Button(text="Accept", font=('center', 14), bg="white", fg="blue", command=accept)

    b2.pack()
    b2.place(x=200, y=250)
    b3 = Button(text="Reset", font=('center', 14), bg="white", fg="blue", command=reset)

    b3.pack()
    b3.place(x=200, y=300)


main()
