import tkinter

window = tkinter.Tk()
window.title("First GUI Program with Tkinter")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# component doesn't show until "packed" into parent window
# my_label.pack(side="left", expand=True)
# docs show 3 ways to set the config of a label (and other items)
my_label["text"] = "One way"
my_label.config(text="KW way")
# my_label.pack()
my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("I was clicked!")
    # my_label.config(text="Button was clicked!")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
# Can use place method as another layout manager
# input.place(x=100,y=100)
# Hard if managing many widgets

# Grid is better, but can't use with pack()
input.grid(column=3, row=2)


# Another button
button2 = tkinter.Button(text="Another button!", command=button_clicked)
button2.grid(column=2,row=0)

# Add padding
# to window (all widgets)
window.config(padx=200, pady=200)

# to specific widget
my_label.config(padx=50, pady=50, bg="white", fg="black")









window.mainloop()