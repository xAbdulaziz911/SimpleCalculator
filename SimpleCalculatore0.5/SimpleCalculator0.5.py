from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="lightgray")
icon = "C:\\Users\\User\\Desktop\\Workspace\\PyProjects\\SimpleCalculator\\calculator.ico"
window.iconbitmap(icon)
e = Entry(window, width=25, borderwidth=5, bg="lightgray", font=("Arial", 14))
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)


history_show = False

# Functions
def history():
    global history_show
    if not history_show:
        history_text.grid(row=8, column=0, columnspan=4, padx=10, pady=5)
        History_button.config(text="Hide History") 
        history_show = True
    else:
        history_text.grid_forget()
        History_button.config(text="Show History")
        history_show = False

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
    math = "+"
    f_num = float(first_number)
    e.delete(0, END)

def Button_minus():
    first_number = e.get()
    global f_num 
    global math
    math = "-"
    f_num = float(first_number)
    e.delete(0, END)

def Button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "x"
    f_num = float(first_number)
    e.delete(0, END)

def Button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "/"
    f_num = float(first_number)
    e.delete(0, END)

def Button_point():
    current = e.get()
    if "." not in current:
        e.insert(END, ".")

def Button_negate():
    current = e.get()
    if current and current[0] != '-':
        e.insert(0, '-')
    elif current and current[0] == '-':
        e.delete(0)


def Button_equal():
    second_number = e.get()
    e.delete(0, END)
        
    if math == "-":
        result = f_num - float(second_number)
    elif math == "+":
        result = f_num + float(second_number)
    elif math == "x":
        result = f_num * float(second_number)
    elif math == "/":
        result = f_num / float(second_number)

    if result.is_integer():
        e.insert(0, int(result))

    else:
        e.insert(0, result)
    
    history_text.insert(END, f"{f_num} {math} {second_number} = {result}\n")

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
clear = Button(window, text="C", padx=38, pady=20, command=lambda: Button_clear(), bg="gray", font=("Arial", 12), border="3")
add = Button(window, text="+", padx=40, pady=20, command=Button_add, bg="darkgray", font=("Arial", 12), border="3")
multiply = Button(window, text="x", padx=42, pady=20, command=Button_multiply, bg="darkgray", font=("Arial", 12), border="3")
minus = Button(window, text="-", padx=42, pady=20, command=Button_minus, bg="darkgray", font=("Arial", 12, "bold"), border="3")
divide = Button(window, text="/", padx=41, pady=20, command=Button_divide, bg="darkgray", font=("Arial", 12), border="3")
equal = Button(window, text="=", padx=40, pady=20, command=Button_equal, bg="gray", font=("Arial", 12), border="3")
point = Button(window, text=".", padx=42, pady=20, command=Button_point, bg="darkgray", font=("Arial", 12, "bold"), border="3")
negate = Button(window, text="(-/+)", padx=29, pady=20, command=Button_negate, bg="darkgray", font=("Arial", 12), border="3")

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
clear.grid(row=6,column=1)
add.grid(row=5,column=0)
multiply.grid(row=5, column=1)
minus.grid(row=4, column=1)
divide.grid(row=4, column=2)
equal.grid(row=6,column=2)
point.grid(row= 6, column=0)
negate.grid(row= 5, column= 2)
# =======================================

# History
History_button = Button(window, text="Show History", command=history, bg="darkgray", font=("Arial", 12), border="3")
History_button.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

history_text = Text(window, width=30, height=5, borderwidth=3, bg="lightgray", font=("Arial", 12))
# =======================================

window.resizable(False, False)
window.mainloop()