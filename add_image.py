from distutils import text_file
from tkinter import *
from tkinter import filedialog
from turtle import position
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title('Algebra | Sučelje za prikaz liste biljaka')
root.configure(bg='#282828') # tamno siva pozadina
# Define the geometry of the window
root.geometry('800x600')


def open_txt():
    text_file=filedialog.askopenfile(initialdir='C:\\Users\\ivanka.budimir', title=' open text file', filetypes=(('text files', '*.txt'), ) )
    text_file = open (text_file, 'r')
    stuff= text_file.read()

    text_file.insert(END, stuff)

def save_txt():
    ttext_file=filedialog.askopenfile(initialdir='C:\\Users\\ivanka.budimir', title=' open text file', filetypes=(('text files', '*.txt'), ) )
    text_file = open (text_file, 'w')
    text_file.write(my_text.get(1.0, END))

def add_image():
    global my_image
    my_image=PhotoImage(file='Desktop\vscode\slika_1.jpg') #popraviti 
    position = my_text.index (INSERT)
    my_text.image_create(position, my_image)

    my_label.config(text=position)

my_frame = Frame(root)
my_frame.pack(pady=10)

text_scroll = Scrollbar (my_frame)
text_scroll.pack(side= RIGHT, fill= Y)
my_text = Text(root, width=40, height=10, font='Arial', selectbackground='yellow', yscrollcommand=text_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)

open_button=Button(root, text='open text file', command=open_txt)
open_button.pack(padx=20)


save_button=Button(root, text='save file', command=save_txt)
save_button.pack(padx=20)


image_button= Button(root, text='add image', command=add_image)
image_button.pack(pady=5)

my_label= Label(root, text='')
my_label.pack()

root.mainloop()
