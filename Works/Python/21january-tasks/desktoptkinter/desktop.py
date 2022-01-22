from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('600x400')
window.title("Tkinterə xoş gəlmisiniz")
lbl = Label(window, text="Progmatech Foundation Project", font=("Arial, Helvetica, sans-serif;", 30))
lbl.pack()
var = StringVar() 
txt = Entry(window,width=40,  textvariable=var)
txt.pack()

window.mainloop()