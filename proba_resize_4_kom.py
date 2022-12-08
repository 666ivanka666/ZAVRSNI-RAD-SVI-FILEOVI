
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title("Algebra | PyPosuda")
root.configure(bg="#282828") # tamno siva pozadina
# Define the geometry of the window
root.geometry("800x600")


### CVIJET 1


frame1 = Frame(root, width=600, height=400)
frame1.pack()
frame1.place(anchor='se', relx=0.5, rely=0.5)

img1 = Image.open("tulipan_zuta.jpg")
resized1=img1.resize((200,225), Image.ANTIALIAS)
new_picutre1 =ImageTk.PhotoImage(resized1)


label1 = Label(frame1, image = new_picutre1)
label1.pack(pady=20, )

### CVIJET 2


frame2 = Frame(root, width=600, height=400)
frame2.pack()
frame2.place(anchor='sw', relx=0.5, rely=0.5)

img2 = Image.open("orhideja_bijela.jpg")
resized2=img2.resize((200,225), Image.ANTIALIAS)
new_picutre2 =ImageTk.PhotoImage(resized2)


label2 = Label(frame2, image = new_picutre2)
label2.pack(pady=20)

### CVIJET 3


frame3 = Frame(root, width=600, height=400)
frame3.pack()
frame3.place(anchor='nw', relx=0.5, rely=0.5)

img3 = Image.open("vinka_roza.jpg")
resized3=img3.resize((200,225), Image.ANTIALIAS)
new_picutre3 =ImageTk.PhotoImage(resized3)

label3 = Label(frame3, image = new_picutre3)
label3.pack(pady=20)


### CVIJET 4

frame4 = Frame(root, width=600, height=400)
frame4.pack()
frame4.place(anchor='ne', relx=0.5, rely=0.5)

img4 = Image.open("ruza_roza.jpg")
resized4=img4.resize((200,225), Image.ANTIALIAS)
new_picutre4 =ImageTk.PhotoImage(resized1)

label4 = Label(frame4, image = new_picutre4)
label4.pack(pady=20)

### CVIJET 5

frame5 = Frame(root, width=600, height=400)
frame5.pack()
frame5.place(anchor='s', relx=0.5, rely=0.5)

img5 = Image.open("ruza_roza.jpg")
resized5=img5.resize((200,225), Image.ANTIALIAS)
new_picutre5 =ImageTk.PhotoImage(resized1)

label5 = Label(frame4, image = new_picutre5)
label5.pack(pady=20)


root.mainloop()