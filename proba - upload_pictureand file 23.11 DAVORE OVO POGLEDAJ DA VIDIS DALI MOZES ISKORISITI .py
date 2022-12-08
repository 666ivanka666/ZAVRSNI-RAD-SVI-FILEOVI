import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Algebra | Sučelje za prikaz liste biljaka')
root.configure(bg='#282828') 
root.geometry('400x300')
my_font=('Arial', 10, 'bold')


#label1 = tk.Label(root,text='Add new plant',width=30,font=my_font)  
#label1.grid(row=1,column=1,columnspan=4)
button1 = tk.Button(root, text='Dodaj novu biljku', 
   width=20,command = lambda:upload_file())
button1.grid(row=2,column=1,columnspan=4)

def upload_file():
    file_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=file_types)
    column_1=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) 
        img=img.resize((70,100)) 
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(root)
        e1.grid(row=row,column=column_1)
        e1.image = img
        e1['image']=img #
        if(column_1==3): 
            row=row+1
            column_1=1    
        else:      
            column_1=column_1+1      

#################
button1=tk. Button(root, text='Upload file', width=20, command=lambda:upload_file())
button1.grid(row=4, column=1)
my_string =tk.StringVar()
#label2= tk.Label(root, textvariable=my_string, fg='pink')
#label2.grid(row=3, column=1)
#my_string.set('Path here')

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
root.mainloop() 
