from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="click to quit!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=0).grid(column=1, row=0)

root.mainloop()
