from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="lightgray")


e = Entry(window, width=25, borderwidth=5, bg="lightgray", font=("Arial", 14))
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

# Functions
def Button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Button_clear():
    e.delete(0, END)

def Button_add():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))
# =======================================


# Buttons Label
one = Button(window, text="1", padx=40, pady=20, command=lambda: Button_click(1), bg="darkgray", font=("Arial", 12))
two = Button(window, text="2", padx=40, pady=20, command=lambda: Button_click(2), bg="darkgray", font=("Arial", 12))
three = Button(window, text="3", padx=40, pady=20, command=lambda: Button_click(3), bg="darkgray", font=("Arial", 12))
four = Button(window, text="4", padx=40, pady=20, command=lambda: Button_click(4), bg="darkgray", font=("Arial", 12))
five = Button(window, text="5", padx=40, pady=20, command=lambda: Button_click(5), bg="darkgray", font=("Arial", 12))
six = Button(window, text="6", padx=40, pady=20, command=lambda: Button_click(6), bg="darkgray", font=("Arial", 12))
seven = Button(window, text="7", padx=40, pady=20, command=lambda: Button_click(7), bg="darkgray", font=("Arial", 12))
eight = Button(window, text="8", padx=40, pady=20, command=lambda: Button_click(8), bg="darkgray", font=("Arial", 12))
nine = Button(window, text="9", padx=40, pady=20, command=lambda: Button_click(9), bg="darkgray", font=("Arial", 12))
zero = Button(window, text="0", padx=40, pady=20, command=lambda: Button_click(0), bg="darkgray", font=("Arial", 12))
clear = Button(window, text="Clear", padx=76, pady=20, command=lambda: Button_clear(), bg="darkgray", font=("Arial", 12))
add = Button(window, text="+", padx=40, pady=20, command=Button_add, bg="darkgray", font=("Arial", 12))
equal = Button(window, text="=", padx=90, pady=20, command=Button_equal, bg="darkgray", font=("Arial", 12))
# =======================================

# Buttons Position
one.grid(row=3,column=0)
two.grid(row=3,column=1)
three.grid(row=3,column=2)
four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)
seven.grid(row=1,column=0)
eight.grid(row=1,column=1)
nine.grid(row=1,column=2)
zero.grid(row=4,column=0)
clear.grid(row=4,column=1, columnspan=3)
add.grid(row=5,column=0)
equal.grid(row=5,column=1, columnspan=3)
# =======================================



window.mainloop()