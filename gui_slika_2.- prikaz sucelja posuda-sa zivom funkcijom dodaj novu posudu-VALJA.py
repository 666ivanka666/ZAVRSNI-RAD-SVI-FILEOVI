
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk



root = tk.Tk()
root.title('Algebra | Sučelje za prikaz liste PyPosuda')
root.configure(bg='#282828') # tamno siva pozadina
# Define the geometry of the window
root.geometry('600x400')


### TEGLA 1

frame1 = Frame(root, width=600, height=400)
frame1.grid(row=0, column=0, padx=5, pady=5)

frame_name1 = tk.Label (frame1, text= 'Naziv Py Posude' ,bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name1 =tk.Label(frame1, text= 'Status:' ,bg='#282828',fg='white',font=('Arial', 10))
frame_name1.grid(column=1, row=1, padx=5, pady=5)

img1 = Image.open('tegla.png')
resized1=img1.resize((100,70), Image.ANTIALIAS)
new_picutre1 =ImageTk.PhotoImage(resized1)

label1 = Label(frame1, image = new_picutre1,bg='#282828')
label1.grid()


### TEGLA 2

frame2 = Frame(root, width=600, height=400)
frame2.grid(row=0, column=1, padx=5, pady=5)

frame_name2 = tk.Label (frame2, text= 'Naziv Py Posude' ,bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name2 =tk.Label(frame2, text= 'Status:' ,bg='#282828',fg='white',font=('Arial', 10))
frame_name2.grid(column=1, row=1, padx=5, pady=5)

img2 = Image.open('tegla.png')
resized2=img2.resize((100,70), Image.ANTIALIAS)
new_picutre2 =ImageTk.PhotoImage(resized1)

label2 = Label(frame2, image = new_picutre2,bg='#282828')
label2.grid()


### TEGLA 3

frame3 = Frame(root, width=600, height=400)
frame3.grid(row=1, column=0, padx=5, pady=5)

frame_name3 = tk.Label (frame3, text= 'Naziv Py Posude',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name3 =tk.Label(frame3,text= 'Status:' ,bg='#282828',fg='white',font=('Arial', 10))
frame_name3.grid(column=1, row=1, padx=5, pady=5)

img3 = Image.open('tegla.png')
resized3=img3.resize((100,70), Image.ANTIALIAS)
new_picutre3 =ImageTk.PhotoImage(resized3)

label3 = Label(frame3, image = new_picutre3,bg='#282828')
label3.grid()


### DODAJ NOVU POSUDU


button11 = tk.Button(root, text='Dodaj novu posudu', 
   width=20,command = lambda:upload_file())
button11.grid(row=1,column=2,columnspan=4)

def upload_file():
    file_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=file_types)
    column_1=1 
    row=3 
    for f in filename:
        img=Image.open(f) 
        img=img.resize((100,70)) 
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(root)
        e1.grid(row=row,column=column_1)
        e1.image = img
        e1['image']=img 
        if(column_1==3): 
            row=row+1
            column_1=1    
        else:      
            column_1=column_1+1              
'''

frame4 = Frame(root, width=600, height=400)
frame4.grid(row=1, column=1, padx=5, pady=5)

frame_name4 = tk.Label (frame4, text= 'Dodaj novu posudu',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_name4 =tk.Label(frame4)
frame_name4.grid(column=1, row=2, padx=5, pady=5)

img4 = Image.open('tegla.png')
resized4=img4.resize((100,70), Image.ANTIALIAS)
new_picutre4 =ImageTk.PhotoImage(resized4)

label4 = Label(frame4, image = new_picutre4,bg='#282828')
label4.grid()'''






root.mainloop()