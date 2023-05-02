from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

COURSE = ['Architecture',
                 'Civil Engineering',
                 'Computer Engineering',
                 'Electrical Engineering',
                 'Electronics Engineering',
                 'Industrial Engineering',
                 'Mechanical Engineering',]
MONTH = ['January','February','March','April',
         'May','June','July','August','September',
         'October','November','December']
DAY = [*range(1,32)]
YEAR = [*range(1950,2023,1)]


def ok():
    if checkvalue.get() !=0:
        messagebox.showinfo('SUCCESS', 'Your information is now printed')
        print ("Name: " + nameentry.get())
        print ("Program: " + variable.get())
        print ("Gender: " + gvalue.get())
        print ("Birth Date: ",month.get(), day.get(),year.get())
        print("Agreed to the terms of use")
    else:
        messagebox.showerror('ERROR!', 'Error, you have not Agreed to the Terms of use')
    
def open_text():
    text_file1 = filedialog.askopenfilename(initialdir="D:\School\CPE 105\Programs",
                                            title="Open File",filetypes=(
                                                 ("Text file",".txt"),
                                                 ("HTML file",".html"),
                                                 ("All files",".*")
                                            ))
    text_file1 = open(text_file1, 'r')
    note = text_file1.read()

    t.insert(END, note)
    text_file1.close()

def save_text():
    text_file2 = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[
                                                 ("Text file",".txt"),
                                                 ("HTML file",".html"),
                                                 ("All files",".*")
                                            ])
    text_file2 = open(text_file2, 'w')
    notes = str(t.get(1.0,END))
    text_file2.write(notes)
    text_file2.close()
    

master = Tk()
master.geometry ("625x300")


name = Label(master, text="Name")
namevalue = StringVar
nameentry = Entry(master, textvariable=namevalue, width=40)

program = Label(master, text="Program")
variable = StringVar(master)
variable.set(COURSE[0])
w = OptionMenu(master, variable, *COURSE)

gvalue = StringVar()
gvalue.set("Male")
gender = Label(master, text="Gender")
gbtn = Radiobutton(master, text="Male", variable=gvalue, value="Male")
gbtn2 = Radiobutton(master, text="Female", variable=gvalue, value="Female")

bod = Label(master, text="Birth Date:")
month = StringVar(master)
month.set("Month")
m = OptionMenu(master, month, *MONTH)
day = StringVar(master)
day.set("Day")
d = OptionMenu(master, day, *DAY)
year = StringVar(master)
year.set("Year")
y = OptionMenu(master, year, *YEAR)

checkvalue = IntVar()
checkbtn = Checkbutton(text="Agree to the Terms of Use", variable=checkvalue)
button = Button(master, text="Submit", command=ok)


t = Text(master, state='normal', height=15, width=30)
open_button = Button(master, text="Open Text File", command=open_text)
save_button = Button(master, text="Submit", command=save_text)


name.grid(row=1,column=0,sticky='w')
nameentry.grid(row=1,column=1,columnspan=3,sticky='w',pady=5)
program.grid(row=2,column=0,sticky='w',pady=5)
w.grid(row=2,column=1,columnspan=4,sticky='w')
gender.grid(row=3,column=0,sticky='w')
gbtn.grid(row=3,column=1,sticky='w',pady=5)
gbtn2.grid(row=4,column=1,sticky='w')
bod.grid(row=5,column=0,sticky='w')
m.grid(row=5,column=1,sticky='ew',pady=5)
d.grid(row=5,column=2,sticky='ew',pady=5)
y.grid(row=5,column=3,sticky='ew',pady=5)
checkbtn.grid(row=7,column=1,columnspan=3,pady=5)
button.grid(row=9,column=2,pady=5)
t.grid(row=1,column=5,rowspan=15,pady=5,padx=20)
open_button.grid(row=16,column=5,ipadx=10,pady=5)
save_button.grid(row=16,column=5,padx=20,ipadx=10,pady=5,sticky='w')
master.mainloop()
