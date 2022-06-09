import tkinter


from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(width=300, height=100)
window.config(padx=50)

def calculate():
    value = round(float(input.get()) * 1.6, 2)
    km_value.config(text=value)

input = Entry(width=10)
input.grid(column=1, row=0)
m_label = Label(text="Miles").grid(column=2, row=0)
equal_label = Label(text="is equal to").grid(column=0, row=1)
km_value = Label(text="0")
km_value.grid(column=1, row=1)
km_label = Label(text="Km").grid(column=2, row=1)
button = Button(text="Calculate", command=calculate).grid(column=1, row=2)



window.mainloop()
