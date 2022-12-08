
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
frame1.grid(row=0, column=0, padx=5, pady=5)

img1 = Image.open("slika_1.jpg")
resized1=img1.resize((100,70), Image.ANTIALIAS)
new_picutre1 =ImageTk.PhotoImage(resized1)


label1 = Label(frame1, image = new_picutre1)
label1.pack(pady=5)


### CVIJET 2

frame2 = Frame(root, width=600, height=400)
frame2.grid(row=0, column=1, padx=15, pady=15)

img2 = Image.open("slika_2.jpg")
resized2=img2.resize((100,70), Image.ANTIALIAS)
new_picutre2 =ImageTk.PhotoImage(resized2)


label2 = Label(frame2, image = new_picutre2)
label2.pack(pady=5)

### CVIJET 3


frame3 = Frame(root, width=600, height=400)
frame3.grid(row=0, column=2, padx=15, pady=15)

img3 = Image.open("slika_3.jpg")
resized3=img3.resize((100,70), Image.ANTIALIAS)
new_picutre3 =ImageTk.PhotoImage(resized3)

label3 = Label(frame3, image = new_picutre3)
label3.pack(pady=5)


### CVIJET 4

frame4 = Frame(root, width=600, height=400)
frame4.grid(row=0, column=3, padx=15, pady=15)

img4 = Image.open("slika_4.jpg")
resized4=img4.resize((100,70), Image.ANTIALIAS)
new_picutre4 =ImageTk.PhotoImage(resized4)

label4 = Label(frame4, image = new_picutre4)
label4.pack(pady=5)

### CVIJET 5

frame5 = Frame(root, width=600, height=400)
frame5.grid(row=0, column=4, padx=15, pady=15)

img5 = Image.open("slika_5.jpg")
resized5=img5.resize((100,70), Image.ANTIALIAS)
new_picutre5 =ImageTk.PhotoImage(resized5)

label5 = Label(frame4, image = new_picutre5)
label5.pack(pady=5)


### CVIJET 6
frame6 = Frame(root, width=600, height=400)
frame6.grid(row=0, column=5, padx=15, pady=15)

img6 = Image.open("slika_6.jpg")
resized6=img6.resize((100,70), Image.ANTIALIAS)
new_picutre6 =ImageTk.PhotoImage(resized6)

label6 = Label(frame4, image = new_picutre6)
label6.pack(pady=5)

### CVIJET 7
frame7 = Frame(root, width=600, height=400)
frame7.grid(row=0, column=6, padx=15, pady=15)

img7 = Image.open("slika_7.jpg")
resized7=img7.resize((100,70), Image.ANTIALIAS)
new_picutre7 =ImageTk.PhotoImage(resized7)

label7 = Label(frame4, image = new_picutre7)
label7.pack(pady=5)

### CVIJET 8
frame8 = Frame(root, width=600, height=400)
frame8.grid(row=0, column=7, padx=15, pady=15)

img8 = Image.open("slika_8.jpg")
resized8=img8.resize((100,70), Image.ANTIALIAS)
new_picutre8 =ImageTk.PhotoImage(resized8)

label8 = Label(frame4, image = new_picutre8)
label8.pack(pady=5)


### CVIJET 9
frame9 = Frame(root, width=600, height=400)
frame9.grid(row=0, column=8, padx=15, pady=15)

img9 = Image.open("slika_9.jpg")
resized9=img9.resize((100,70), Image.ANTIALIAS)
new_picutre9 =ImageTk.PhotoImage(resized9)

label9 = Label(frame4, image = new_picutre9)
label9.pack(pady=5)

### CVIJET 10

frame10 = Frame(root, width=600, height=400)
frame10.grid(row=0, column=9, padx=15, pady=15)

img10 = Image.open("slika_10.jpg")
resized10=img10.resize((100,70), Image.ANTIALIAS)
new_picutre10 =ImageTk.PhotoImage(resized10)

label10 = Label(frame4, image = new_picutre10)
label10.pack(pady=5)

root.mainloop()