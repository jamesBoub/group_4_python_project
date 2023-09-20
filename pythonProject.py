from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

#changes the displayed name of opened window
root.title("MiniCalc")

inputA = inputB = 0

#function is called by buttons, button identity is passed as a parameter
def userInput(inputFromButton):
    print(inputFromButton)

#represents structure of buttons displayed, written like this for aesthetics
ttk.Button(frm, text="1", command=lambda:userInput(1)).grid(column=1, row=0); ttk.Button(frm, text="2", command=lambda:userInput(2)).grid(column=2, row=0); ttk.Button(frm, text="+", command=lambda:userInput("+")).grid(column=3, row=0) 
ttk.Button(frm, text="3", command=lambda:userInput(3)).grid(column=1, row=1); ttk.Button(frm, text="4", command=lambda:userInput(4)).grid(column=2, row=1); ttk.Button(frm, text="-", command=lambda:userInput("-")).grid(column=3, row=1)
ttk.Button(frm, text="5", command=lambda:userInput(5)).grid(column=1, row=2); ttk.Button(frm, text="6", command=lambda:userInput(6)).grid(column=2, row=2); ttk.Button(frm, text="x", command=lambda:userInput("*")).grid(column=3, row=2)
ttk.Button(frm, text="7", command=lambda:userInput(7)).grid(column=1, row=3); ttk.Button(frm, text="8", command=lambda:userInput(8)).grid(column=2, row=3); ttk.Button(frm, text="÷", command=lambda:userInput("/")).grid(column=3, row=3)
ttk.Button(frm, text="9", command=lambda:userInput(9)).grid(column=1, row=4); ttk.Button(frm, text="0", command=lambda:userInput(0)).grid(column=2, row=4); ttk.Button(frm, text="aᵇ", command=lambda:userInput("**")).grid(column=3, row=4)
button = ttk.Button(frm, text="return", command=lambda:userInput("return")).grid(column=1, row=5);

# must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky

root.mainloop()
