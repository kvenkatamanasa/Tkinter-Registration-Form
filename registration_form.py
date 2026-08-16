from tkinter import *

g = Tk()

# Window
g.geometry("1000x900")
g.config(bg="pink")
g.title("Registration Form")


# Welcome Heading
L1 = Label(
    g,
    text="Welcome to SVCET CSE Dept",
    font=("times", 30, "bold"),
    fg="black",
    bg="pink"
)
L1.place(x=300, y=30)


# Full Name
L2 = Label(g, text="Full Name:", font=("times", 20, "bold"), bg="pink")
L2.place(x=150, y=100)

E1 = Entry(g, font=("times", 20))
E1.place(x=350, y=100)


# User Name
L3 = Label(g, text="User Name:", font=("times", 20, "bold"), bg="pink")
L3.place(x=150, y=150)

E2 = Entry(g, font=("times", 20))
E2.place(x=350, y=150)


# Password
L4 = Label(g, text="Password:", font=("times", 20, "bold"), bg="pink")
L4.place(x=150, y=200)

E3 = Entry(g, font=("times", 20), show="*")
E3.place(x=350, y=200)


# E-mail
L5 = Label(g, text="E-mail:", font=("times", 20, "bold"), bg="pink")
L5.place(x=150, y=250)

E4 = Entry(g, font=("times", 20))
E4.place(x=350, y=250)


# Phone Number
L6 = Label(g, text="Phone No:", font=("times", 20, "bold"), bg="pink")
L6.place(x=150, y=300)

E5 = Entry(g, font=("times", 20))
E5.place(x=350, y=300)


# Address
L7 = Label(g, text="Address:", font=("times", 20, "bold"), bg="pink")
L7.place(x=150, y=350)

E6 = Entry(g, font=("times", 20), width=25)
E6.place(x=350, y=350)


# City
L8 = Label(g, text="City:", font=("times", 20, "bold"), bg="pink")
L8.place(x=150, y=400)

E7 = Entry(g, font=("times", 20))
E7.place(x=350, y=400)


# State
L9 = Label(g, text="State:", font=("times", 20, "bold"), bg="pink")
L9.place(x=150, y=450)

E8 = Entry(g, font=("times", 20))
E8.place(x=350, y=450)


# Pincode
L10 = Label(g, text="Pincode:", font=("times", 20, "bold"), bg="pink")
L10.place(x=150, y=500)

E9 = Entry(g, font=("times", 20))
E9.place(x=350, y=500)


# Buttons
B1 = Button(
    g,
    text="Submit",
    font=("italic", 20, "bold")
)
B1.place(x=300, y=680)

B2 = Button(
    g,
    text="Reset",
    font=("italic", 20, "bold")
)
B2.place(x=450, y=680)

