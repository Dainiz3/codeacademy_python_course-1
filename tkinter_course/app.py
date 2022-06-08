# from tkinter import *


# window = Tk()
# window.title("test")
# window.geometry("250x200")
# text = Label(window, text="This is random text1")
# text_two = Label(window, text="This is random text2")
# text.pack()
# text_two.pack()
# window.mainloop()


# from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y, RIGHT, TOP, BOTH, Y

# window = Tk()
# window.geometry("450x200")
# top = Frame(window)
# bottom = Frame(window)

# button1 = Button(top, text="Button #1")
# button2 = Button(top, text="Button #2")
# button3 = Button(top, text="Button #3")
# button4 = Button(top, text="Button #4 123123123123")

# top.pack()
# bottom.pack(side=BOTTOM)

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=TOP, fill=BOTH)

# window.mainloop()


# from tkinter import Tk, Frame, Button, Label, Entry, Checkbutton, E, N, S, W


# window = Tk()
# window.geometry("450x200")
# text1 = Label(window, text="name")
# field1 = Entry(window)
# text2 = Label(window, text="surname")
# field2 = Entry(window)
# check_button = Checkbutton(window, text="Mark me please")

# text1.grid(row=0, column=0, sticky=W)
# field1.grid(row=0, column=1)
# text2.grid(row=1, column=0, sticky=N)
# field2.grid(row=1, column=1)
# check_button.grid(row=2, columnspan=4)


# window.mainloop()


# from tkinter import Tk, Button


# window = Tk()
# window.geometry("450x200")


# def say_hello():
#     print("Hello")


# button1 = Button(window, text="Say Hi", command=say_hello)
# button1.pack()
# window.mainloop()


# from tkinter import Tk, Button

# window = Tk()
# window.geometry("450x200")


# def print1(event):
#     print("you pressed left mouse button")


# def print2(event):
#     print("you pressed right mouse button")


# def print3(event):
#     print("you pressed ENTER")


# button = Button(window, text="PRESS ME", height=20, width=40)
# button.bind("<Button-1>", print1)
# button.bind("<Button-3>", print2)
# window.bind("<Return>", print3)

# button.pack()
# window.mainloop()


# from tkinter import Tk, Button

# window = Tk()
# window.geometry("450x200")


# def print1():
#     print("I am printing!!!")


# button = Button(window, text="PRESS ME TO PRINT", command=print1)
# window.bind("<Return>", lambda event: print1())
# button.pack()

# window.mainloop()


# from tkinter import *

# window = Tk()


# def print1():
#     input1 = field1.get()
#     print(input1)
#     result["text"] = input1


# text1 = Label(window, text="Įrašykite žodį")
# field1 = Entry(window)
# button = Button(window, text="Įvesti", command=print1)
# result = Label(window, text="")

# text1.grid(row=0, column=0)
# field1.grid(row=0, column=1)
# button.grid(row=0, column=2)
# result.grid(row=1, columnspan=3)

# window.mainloop()


# from tkinter import *

# window = Tk()
# window.geometry("450x200")
# box = Listbox(window, width=20, height=50)
# list = range(1, 200)
# box.insert(*list)
# box.insert(*list)
# box.pack(side=RIGHT)
# window.mainloop()


# from tkinter import *
# from module import my_list

# langas = Tk()
# masyvas = my_list
# scrollbaras = Scrollbar(langas)
# boksas = Listbox(langas, yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=boksas.yview)
# boksas.insert(END, *masyvas)
# scrollbaras.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)
# langas.mainloop()


# from tkinter import *

# langas = Tk()
# sarasas = range(1, 200)


# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]
#     print(boksas.curselection())
#     uzrasas["text"] = pasirinkta


# mygtukas = Button(langas, text="Spausdinti", command=spausdinti)

# uzrasas = Label(langas, text="Nieko")
# boksas = Listbox(langas, selectmode=SINGLE)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# mygtukas.pack()
# uzrasas.pack()
# langas.mainloop()


# from tkinter import *

# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff=0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()

# from tkinter import *

# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff=0)


# def antras():
#     print("Antras!")


# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras", command=antras)
# langas.mainloop()


# from tkinter import *

# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff=0)
# submeniu2 = Menu(meniu, tearoff=0)
# submeniu3 = Menu(meniu, tearoff=0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")

# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")

# meniu.add_cascade(label="Meniu 2", menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")

# meniu.add_cascade(label="Meniu 3", menu=submeniu3)

# langas.mainloop()


# my_dict = {"a": 1, "b": [1, 2, 3], "c": "2022"}
# print(my_dict)
# print(my_dict["b"])

# my_dict["d"] = "vardas"

# print(my_dict)

# my_dict["a"] = "laba diena"

# print(my_dict)

# vardas = "asdf"
# resultatas["text"] = f"laba diena {vardas}"


# p1 = Person("asdf")
# print(p1.name)
# p1["name"] = 123
# print(p1.name)


# from tkinter import *

# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff=0)
# submeniu2 = Menu(meniu, tearoff=0)
# submeniu3 = Menu(meniu, tearoff=0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")

# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")

# meniu.add_cascade(label="Meniu 2", menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")

# meniu.add_cascade(label="Meniu 3", menu=submeniu3)

# langas.mainloop()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __getattr__(self, attr):
#         return self.attr


# p1 = Person("Vardas")
# print(p1.name)
# print(p1["name"])

# from tkinter import *

# langas = Tk()

# def spausdinti():
#     ivesta = laukas1.get()
#     print(ivesta)
#     rezultatas["text"] = ivesta


# uzrasas1 = Label(langas, text="Įrašykite žodį")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Įvesti", command=spausdinti)
# rezultatas = Label(langas, text="")

# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)


# langas.mainloop()


# from tkinter import *

# langas = Tk()
# langas.geometry("400x500")


# def daryti():
#     status["text"] = "Dabar daro"


# mygtukas = Button(langas, text="Daryti", command=daryti)
# status = Label(langas, text="Nieko nedaro...", bd=10, relief=RAISED)
# status.pack(side=BOTTOM, fill=X)

# mygtukas.pack()


# langas.mainloop()


# from tkinter import *
# import webbrowser


# def callback(url):
#     webbrowser.open_new(url)


# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand1")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# import os

# root = Tk()
# img = ImageTk.PhotoImage(Image.open("paveiksliukas.JPG"))
# panel = Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()


# from tkinter import *

# langas = Tk()

# kintamasis = StringVar()
# # skaicius =
# # kintamasis = ""


# def funkcija():
#     kintamasis.set("Naujas tekstas")
#     print(kintamasis.get())


# from tkinter import *

# window = Tk()

# mano_tekstas = DoubleVar()
# my_var_tkinter = IntVar()
# my_var_tkinter.set(5)
# my_var = 5

# def print1():
#     input1 = field1.get()
#     print(input1)
#     mano_tekstas.set(input1)
#     result["text"] = mano_tekstas.get()
#     print(mano_tekstas.get())


# text1 = Label(window, text="Įrašykite žodį")
# field1 = Entry(window)
# button = Button(window, text="Įvesti", command=print1)
# result = Label(window, text="")

# text1.grid(row=0, column=0)
# field1.grid(row=0, column=1)
# button.grid(row=0, column=2)
# result.grid(row=1, columnspan=3)

# window.mainloop()

import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(
            self.frame, text="New Window", width=25, command=self.new_window
        )
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(
            self.frame, text="Quit", width=25, command=self.close_windows
        )
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
