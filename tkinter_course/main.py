# from tkinter import *


# def submit():
#     user_input.set(field.get())
#     result["text"] = f"what is going on? {user_input.get()}"


# def delete():
#     result["text"] = ""
#     field.delete(0, 500)


# def restore():
#     result["text"] = f"what is going on? {user_input.get()}"


# window = Tk()
# user_input = StringVar()
# menu = Menu(window)
# window.config(menu=menu)
# submenu = Menu(menu, tearoff=0)
# window.geometry("450x200")
# menu.add_cascade(labe="Menu", menu=submenu)
# submenu.add_command(label="Delete", command=delete)
# submenu.add_command(label="Restore", command=restore)
# submenu.add_separator()
# submenu.add_command(label="Exit", command=window.destroy)
# name = Label(window, text="Enter a username")
# button = Button(window, text="Enter", command=submit)
# field = Entry(window)
# result = Label(window, text="")
# window.bind("<Return>", lambda event: submit())
# name.pack()
# field.pack()
# button.pack()
# result.pack()
# window.mainloop()


from tkinter import *

langas = Tk()


def daryti():
    status["text"] = "Dabar daro"


mygtukas = Button(langas, text="Daryti", command=daryti)
status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mygtukas.pack()

langas.mainloop()
