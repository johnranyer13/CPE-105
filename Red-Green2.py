from tkinter import*

def change():
    red1.config(text="CPE 105", fg="green") #Our Course
    """red1.config(text="ITE 003", fg="green") #Given"""
    
    


root = Tk()
frame = Frame(root)
frame.pack()

red1 = Button(frame, text="Click Me", fg="red", command = change)
red1.pack()


root.mainloop()
