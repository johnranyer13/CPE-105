from tkinter import*

def change():
    red1.config(fg="green")
    red2.config(text="Green Text", fg="green")


root = Tk()
frame = Frame(root)
frame.pack()

red1 = Button(frame, text="Click Me", fg="red", command = change)
red1.pack()
red2 = Label(root, text="Red Text", fg="red")
red2.pack()

root.mainloop()
