from tkinter import *
from random import *
import pyperclip
#  Password Generator


def passwordgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    passwordletters = [choice(letters) for _ in range(nr_letters)]
    passwordsymbols = [choice(symbols) for _ in range(nr_symbols)]
    passwordnumbers = [choice(numbers) for _ in range(nr_numbers)]

    passwordlist = passwordletters + passwordsymbols + passwordnumbers

    shuffle(passwordlist)

    password = "".join(passwordlist)
    passwordentry.insert(0, password)
    pyperclip.copy(password)

#  Save Password


def save():
    website = websiteentry.get()
    email = emailentry.get()
    password = passwordentry.get()

    with open("data.txt", "a") as dataf:
        dataf.write(f"{website} | {email} | {password}")
        websiteentry.delete(0, END)
        emailentry.delete(0, END)
        passwordentry.delete(0, END)

#  UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

cava = Canvas(height=200, width=200)
logoimg = PhotoImage(file="logo.png")
cava.create_image(100, 100, image=logoimg)
cava.grid(row=0, column=1)

websitelabel = Label(text="Website:")
websitelabel.grid(row=1, column=0)
emaillabel = Label(text="Email/Username:")
emaillabel.grid(row=2, column=0)
passwordlabel = Label(text="Password:")
passwordlabel.grid(row=3, column=0)

websiteentry = Entry(width=32)
websiteentry.grid(row=1, column=1, columnspan=2)
websiteentry.focus()
emailentry = Entry(width=49)
emailentry.grid(row=2, column=1, columnspan=2)
passwordentry = Entry(width=32)
passwordentry.grid(row=3, column=1)

generatepassword = Button(text="Generate Password", command=passwordgen)
generatepassword.grid(row=3, column=2)
addpassword = Button(text="Add", width=44, command=save)
addpassword.grid(row=4, column=1, columnspan=2)

window.mainloop()
