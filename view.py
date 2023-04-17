from tkinter import *
import controller


def on_search():
    table.delete(0, END)
    name = search_entry.get()
    print("name " + name)
    users = controller.get_user_by_name(name)
    table.insert(END, *users)
    search_entry.delete(0, END)
    return


def on_manage():
    selected = table.get(table.curselection())
    print(selected)
    return


window = Tk()
window.geometry("800x420")
window.title("CRM")
search_entry = Entry(window, font=("Arial", 16))
table = Listbox(window, width=60, height=22, bg="#f7ffde")
search_button = Button(window, text="Search", command=on_search, font=("Arial", 14))
manage_button = Button(window, text="Manage", command=on_manage, font=("Arial", 14))


def initial_screen():
    search_entry.place(x="5", y="10")
    table.place(x="5", y="50")
    search_button.place(x="250", y="5")
    manage_button.place(x="340", y="5")
    window.mainloop()
