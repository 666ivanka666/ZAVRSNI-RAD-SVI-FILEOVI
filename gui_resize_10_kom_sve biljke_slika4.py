
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title("Algebra | Sučelje za prikaz liste PyPosuda")
root.configure(bg="#282828") # tamno siva pozadina
# Define the geometry of the window
root.geometry("800x600")


### CVIJET 1

frame1 = Frame(root, width=600, height=400)
frame1.grid(row=0, column=0, padx=5, pady=5)

frame_name1 = tk.Label (frame1, text= 'Biljka1',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name1 =tk.Entry(frame1)
frame_name1.grid(column=1, row=1, padx=5, pady=5)

img1 = Image.open("slika_1.jpg")
resized1=img1.resize((100,70), Image.ANTIALIAS)
new_picutre1 =ImageTk.PhotoImage(resized1)

label1 = Label(frame1, image = new_picutre1)
label1.grid()


### CVIJET 2

frame2 = Frame(root, width=600, height=400)
frame2.grid(row=0, column=1, padx=5, pady=5)

frame_name2 = tk.Label (frame2, text= 'Biljka2',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name2 =tk.Entry(frame2)
frame_name2.grid(column=1, row=2, padx=5, pady=5)

img2 = Image.open("slika_2.jpg")
resized2=img2.resize((100,70), Image.ANTIALIAS)
new_picutre2 =ImageTk.PhotoImage(resized2)

label2 = Label(frame2, image = new_picutre2)
label2.grid()


### CVIJET 3

frame3 = Frame(root, width=600, height=400)
frame3.grid(row=0, column=2, padx=5, pady=5)

frame_name3 = tk.Label (frame3, text= 'Biljka3',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name3 =tk.Entry(frame3)
frame_name3.grid(column=1, row=3, padx=5, pady=5)

img3 = Image.open("slika_3.jpg")
resized3=img3.resize((100,70), Image.ANTIALIAS)
new_picutre3 =ImageTk.PhotoImage(resized3)

label3 = Label(frame3, image = new_picutre3)
label3.grid()


### CVIJET 4

frame4 = Frame(root, width=600, height=400)
frame4.grid(row=1, column=0, padx=5, pady=5)

frame_name4 = tk.Label (frame4, text= 'Biljka4',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name4 =tk.Entry(frame4)
frame_name4.grid(column=1, row=1, padx=5, pady=5)

img4 = Image.open("slika_4.jpg")
resized4=img4.resize((100,70), Image.ANTIALIAS)
new_picutre4 =ImageTk.PhotoImage(resized4)

label4 = Label(frame4, image = new_picutre4)
label4.grid()


### CVIJET 5

frame5 = Frame(root, width=600, height=400)
frame5.grid(row=1, column=1, padx=5, pady=5)

frame_name5 = tk.Label (frame5, text= 'Biljka 5',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name5 =tk.Entry(frame5)
frame_name5.grid(column=1, row=2, padx=5, pady=5)

img5 = Image.open("slika_5.jpg")
resized5=img5.resize((100,70), Image.ANTIALIAS)
new_picutre5 =ImageTk.PhotoImage(resized5)

label5 = Label(frame5, image = new_picutre5)
label5.grid()


### CVIJET 6

frame6 = Frame(root, width=600, height=400)
frame6.grid(row=1, column=2, padx=5, pady=5)

frame_name6 = tk.Label (frame6, text= 'Biljka 6',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name6 =tk.Entry(frame6)
frame_name6.grid(column=1, row=3, padx=5, pady=5)

img6 = Image.open("slika_6.jpg")
resized6=img6.resize((100,70), Image.ANTIALIAS)
new_picutre6 =ImageTk.PhotoImage(resized6)

label6 = Label(frame6, image = new_picutre6)
label6.grid()

### CVIJET 7

frame7 = Frame(root, width=600, height=400)
frame7.grid(row=2, column=0, padx=5, pady=5)

frame_name7 = tk.Label (frame7, text= 'Biljka 7',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name7 =tk.Entry(frame7)
frame_name7.grid(column=1, row=1, padx=5, pady=5)

img7 = Image.open("slika_7.jpg")
resized7=img7.resize((100,70), Image.ANTIALIAS)
new_picutre7 =ImageTk.PhotoImage(resized7)

label7 = Label(frame7, image = new_picutre7)
label7.grid()

### CVIJET 8

frame8 = Frame(root, width=600, height=400)
frame8.grid(row=2, column=1, padx=5, pady=5)

frame_name8 = tk.Label (frame8, text= 'Biljka 8',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name8 =tk.Entry(frame8)
frame_name8.grid(column=1, row=2, padx=5, pady=5)

img8 = Image.open("slika_8.jpg")
resized8=img8.resize((100,70), Image.ANTIALIAS)
new_picutre8 =ImageTk.PhotoImage(resized8)

label8 = Label(frame8, image = new_picutre8)
label8.grid()


### CVIJET 9

frame9 = Frame(root, width=600, height=400)
frame9.grid(row=2, column=2, padx=5, pady=5)

frame_name9 = tk.Label (frame9, text= 'Biljka 9',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name9 =tk.Entry(frame9)
frame_name9.grid(column=1, row=9, padx=5, pady=5)

img9 = Image.open("slika_9.jpg")
resized9=img9.resize((100,70), Image.ANTIALIAS)
new_picutre9 =ImageTk.PhotoImage(resized9)

label9 = Label(frame9, image = new_picutre9)
label9.grid()


### CVIJET 10

frame10 = Frame(root, width=600, height=400)
frame10.grid(row=3, column=0, padx=5, pady=5)

frame_name10 = tk.Label (frame10, text= 'Biljka 10',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name10 =tk.Entry(frame10)
frame_name10.grid(column=1, row=1, padx=5, pady=5)

img10 = Image.open("slika_10.jpg")
resized10=img10.resize((100,70), Image.ANTIALIAS)
new_picutre10 =ImageTk.PhotoImage(resized10)

label10 = Label(frame10, image = new_picutre6)
label10.grid()


root.mainloop()