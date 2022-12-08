
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title('Algebra | Sučelje za prikaz liste biljaka')
root.configure(bg='#282828') 
root.geometry('400x300')
my_font=('Arial', 10, 'bold')
label1= tk.Label(root, text='Upload file', width=30, font=my_font)
label1.grid(row=1, column=1)

button1=tk. Button(root, text='Upload file', width=20, command=lambda:upload_file())
button1.grid(row=2, column=1)
my_string =tk.StringVar()
label2= tk.Label(root, textvariable=my_string, fg='pink')
label2.grid(row=3, column=1)
my_string.set('Path here')

def upload_file():
    file=filedialog.askopenfilename(initialdir='C:\\Users\\ivanka.budimir',
                                    filetypes=[('CVS files', '.csv'),
                                    ('text docs', '*.txt'),
                                    ('All types', '*.*')])

                                

    if (file):
        my_string.set(file)
        file_object=open(file, 'r')
        print(file_object.read())
    




root.mainloop()

#https://www.youtube.com/watch?v=ndUuy_55jho Tkinter filedialog to read upload and adjust height width to resize multiple images to display