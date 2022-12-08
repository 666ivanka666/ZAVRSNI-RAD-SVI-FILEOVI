
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title("Algebra | PyPosuda")
root.configure(bg="#282828") # tamno siva pozadina
# Define the geometry of the window
root.geometry("800x600")

#open
my_picutre1=Image.open('narcisa_zuta.jpg')

#resize
resized1=my_picutre1.resize((200,225), Image.ANTIALIAS)

new_picutre1 =ImageTk.PhotoImage(resized1)

my_label= Label(root, image=new_picutre1)
my_label.pack(pady=20)


root.mainloop()