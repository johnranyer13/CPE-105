from tkinter import *
root = Tk()

root.title("My Do-Nothing Application")
root.geometry ("1000x400")

root.mainloop()

"""from tkinter import *
from PIL import ImageTk, Image
root = Tk()
logo = ImageTk.PhotoImage(Image.open('py.png'))

w1 = Label(root, image=logo).pack(side="right")

explanation = At present, only GIF and PPM/PGM
formats are supported, but an interface exist to
allow additional image file formats to be added
asily.

w2 = Label(root,
               justify=LEFT,
               padx = 10,
               text=explanation) .pack(side="left")



#w = Label(root, text="Hello Tkinter!")
#w.pack()

root.mainloop()"""
