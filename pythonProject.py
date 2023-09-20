from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
#ttk.Label(frm, text="click to quit!").grid(column=0, row=0)

#represents structure of buttons displayed, written like this for aesthetics
ttk.Button(frm, text="1", command=root.destroy).grid(column=1, row=0); ttk.Button(frm, text="2", command=root.destroy).grid(column=2, row=0); ttk.Button(frm, text="+", command=root.destroy).grid(column=3, row=0) 
ttk.Button(frm, text="3", command=root.destroy).grid(column=1, row=1); ttk.Button(frm, text="4", command=root.destroy).grid(column=2, row=1); ttk.Button(frm, text="-", command=root.destroy).grid(column=3, row=1)
ttk.Button(frm, text="5", command=root.destroy).grid(column=1, row=2); ttk.Button(frm, text="6", command=root.destroy).grid(column=2, row=2); ttk.Button(frm, text="x", command=root.destroy).grid(column=3, row=2)
ttk.Button(frm, text="7", command=root.destroy).grid(column=1, row=3); ttk.Button(frm, text="8", command=root.destroy).grid(column=2, row=3); ttk.Button(frm, text="÷", command=root.destroy).grid(column=3, row=3)
ttk.Button(frm, text="9", command=root.destroy).grid(column=1, row=4); ttk.Button(frm, text="0", command=root.destroy).grid(column=2, row=4); ttk.Button(frm, text="aᵇ", command=root.destroy).grid(column=3, row=4)


root.mainloop()
