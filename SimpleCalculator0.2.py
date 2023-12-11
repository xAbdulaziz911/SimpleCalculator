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
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def Button_minus():
    first_number = e.get()
    global f_num 
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def Button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def Button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    e.delete(0, END)
        
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
# =======================================


# Buttons Label
one = Button(window, text="1", padx=40, pady=20, command=lambda: Button_click(1), bg="darkgray", font=("Arial", 12), border="3")
two = Button(window, text="2", padx=40, pady=20, command=lambda: Button_click(2), bg="darkgray", font=("Arial", 12), border="3")
three = Button(window, text="3", padx=39, pady=20, command=lambda: Button_click(3), bg="darkgray", font=("Arial", 12), border="3")
four = Button(window, text="4", padx=40, pady=20, command=lambda: Button_click(4), bg="darkgray", font=("Arial", 12), border="3")
five = Button(window, text="5", padx=40, pady=20, command=lambda: Button_click(5), bg="darkgray", font=("Arial", 12), border="3")
six = Button(window, text="6", padx=39, pady=20, command=lambda: Button_click(6), bg="darkgray", font=("Arial", 12), border="3")
seven = Button(window, text="7", padx=40, pady=20, command=lambda: Button_click(7), bg="darkgray", font=("Arial", 12), border="3")
eight = Button(window, text="8", padx=40, pady=20, command=lambda: Button_click(8), bg="darkgray", font=("Arial", 12), border="3")
nine = Button(window, text="9", padx=39, pady=20, command=lambda: Button_click(9), bg="darkgray", font=("Arial", 12), border="3")
zero = Button(window, text="0", padx=40, pady=20, command=lambda: Button_click(0), bg="darkgray", font=("Arial", 12), border="3")
clear = Button(window, text="Clear", padx=75, pady=20, command=lambda: Button_clear(), bg="darkgray", font=("Arial", 12), border="3")
add = Button(window, text="+", padx=40, pady=20, command=Button_add, bg="darkgray", font=("Arial", 12), border="3")
multiply = Button(window, text="*", padx=42, pady=20, command=Button_multiply, bg="darkgray", font=("Arial", 12), border="3")
minus = Button(window, text="-", padx=42, pady=20, command=Button_minus, bg="darkgray", font=("Arial", 12), border="3")
divide = Button(window, text="/", padx=41, pady=20, command=Button_divide, bg="darkgray", font=("Arial", 12), border="3")
equal = Button(window, text="=", padx=90, pady=20, command=Button_equal, bg="darkgray", font=("Arial", 12), border="3")
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
clear.grid(row=6,column=1, columnspan=3)
add.grid(row=5,column=0)
multiply.grid(row=6, column=0)
minus.grid(row=4, column=1)
divide.grid(row=4, column=2)
equal.grid(row=5,column=1, columnspan=3)
# =======================================



window.mainloop()