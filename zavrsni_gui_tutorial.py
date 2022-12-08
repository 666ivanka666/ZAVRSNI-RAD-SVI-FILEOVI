
# kodovi su prepisani sa
#https://www.youtube.com/watch?v=YXPyB4XeYLA

from distutils.command.build_scripts import first_line_re
from email import message
import imp
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from urllib import response

from PIL import ImageTk, Image
from numpy import r_, var
from sqlalchemy import column, values



'''root = Tk()

e=Entry(root, width=50)
e.pack()


#buttons
def my_click():
    my_label= Label(root, text=' look i clicked a button')
    my_label.pack()


my_button= Button(root,  text=' click me', command=my_click) # gumb koji klika
my_button.pack()
###butons

root.mainloop()'''


#--------------------
'''root = Tk()

e=Entry(root, width=50)
e.pack()
e.insert(0, 'enter your name: ')

def my_click():
    hello = 'hello' + e.get()
    my_label= Label(root, text=hello)
    my_label.pack()


my_button= Button(root,  text='enter your name', command=my_click) # gumb koji klika
my_button.pack()
###butons

root.mainloop()'''

#--------------------brise program klikom
'''root = Tk()
button_quit = Button(root, text=' exit program', command= root.quit)
button_quit.pack() # brise program klikom

root.mainloop()'''

#----------------------------- IMAGE

'''root = Tk()

my_img = ImageTk.PhotoImage(Image.open('Algebra_campus.jpg')) #dodavanje slike
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()'''


#----------------------------- IMAGES kako slike slagati po redu i klikati ih prema napred ili iza
'''root = Tk()

my_img1 = ImageTk.PhotoImage(Image.open('halteri.jpg')) #dodavanje slike
my_img2 = ImageTk.PhotoImage(Image.open('FB_IMG.jpg'))

image_list = [my_img1, my_img2]

my_label = Label(image= my_img1)
my_label.grid( row=0, column=0, columnspan= 3)


def forward(image_number):
    global my_label
    global forward
    global back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward=Button(root, text='>>', command=lambda:forward(image_number+1))
    button_back=Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number ==5:
        button_forward =Button(root, text='>>', state=DISABLED)

    my_label.grid( row=0, column=0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global forward
    global back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward=Button(root, text='>>', command=lambda:forward(image_number+1))
    button_back=Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number ==5:
        button_forward =Button(root, text='>>', state=DISABLED)

    my_label.grid( row=0, column=0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    if image_number ==1:
        button_back =Button(root, text='<<', state=DISABLED)

button_back= Button(root, text='<<', command=back)
button_exit= Button(root, text='exit program', command= root.quit)
button_forward= Button(root, text='>>',command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit. grid(row=1, column=1)
button_forward.grid(row=1, column=2)
root.mainloop()'''


#--------------- FRAMES radi dvije kucice za klik jednu ispod druge

'''root = Tk()
root.title('ivanka')


frame = LabelFrame(root, text='this is my frame', padx=5, pady=5) #ovi padi idu unutar okvira
frame.pack(padx=10, pady=10)#ovi padi idu izvan okvira

b1=Button(frame, text=' dont click here')
b2=Button(frame, text=' ...or here')
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()'''
#--------------- RADIO BUTTONS okrugli gumbi

'''root = Tk()
root.title('ivanka')

#r= IntVar()
#r.set('2')

toppings =[
    ('pepperoni', 'pepperoni'),
    ('cheeese', 'cheeese'),
    ('mushrom', 'mushrom'),
    ('onion', 'onion')
]

pizza = StringVar()
pizza.set('pepperoni')

for text, topin in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topin).pack(anchor=W) #ancor centrira na lijevo


def clicked(value):
    my_label= Label(root, text=value)
    my_label.pack()


#Radiobutton(root, text= 'option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= 'option 2', variable=r, value=2,command=lambda: clicked(r.get())).pack()


#my_label= Label(root, text=pizza.get())
#my_label.pack()

my_button = Button(root, text='click me', command=lambda: clicked(pizza.get()))
my_button.pack()

mainloop()'''

#------------- POP UP GUI (OTVARA JEDNU UZ DRUGU)
'''root = Tk()
root.title('ivanka')


# uz showinfo moze se staviti na isto mjesto, showwarning, showeror,askquestion, askokcancel, askyesno
def popup():
    messagebox.askyesno('this is my popup', 'hello world')
    #Label(root, text=response).pack()
    if response ==1:
         Label(root, text='you clicked yes').pack()
    else:
        Label(root, text='you clicked no').pack()

Button(root, text='popup', command=popup).pack()

root.mainloop()'''


#------------- POP UP GUI yes no
'''root = Tk()
root.title('ivanka')


# uz showinfo moze se staviti na isto mjesto, showwarning, showeror,askquestion, askokcancel, askyesno
def popup():
    response= messagebox.askquestion('this is my popup', 'hello world')
    Label(root, text=response).pack()
    if response =='yes':
        Label(root, text='you clicked yes').pack()
    else:
        Label(root, text='you clicked no').pack()

Button(root, text='popup', command=popup).pack()
root.mainloop()'''

#------------- NEW WIDNOW 
'''root = Tk()
root.title('ivanka')

def open():
    global my_img
    top = Toplevel()
    #label = Label(top, text='hello world').pack()
    my_img = ImageTk.PhotoImage(Image.open('halteri.jpg'))
    my_label=Label(top, image=my_img).pack()
    btn2=Button(top, text='close window', command=top.destroy).pack()


btn= Button(root, text='open second window', command=open).pack()
root.mainloop()'''



#------------- OPEN FILE
'''root = Tk()
root.title('ivanka')

root.filename = filedialog.askopenfilename(initialdir='/Users/ivanka.budimir/Desktop', title='select a file', filetypes=(('png file', '*.png'),('all files', '*.*'))) 
#kod ovoga kad se uzima s C: slashevi se slazu kao u primjeru /
my_label=Label(root, text=root.filename).pack()

my_image=ImageTk.PhotoImage(Image.open(root.filename))
my_image_label=Label(image=my_image).pack()


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='/Users/ivanka.budimir/Desktop', title='select a file', filetypes=(('png file', '*.png'),('all files', '*.*'))) 
    my_label=Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

my_btn=Button(root,text='open file', command=open)

root.mainloop()'''

#------------- sliders
'''root = Tk()
root.title('ivanka')
root.geometry('400x400')

vertical =Scale(root, from_=0, to=200)
vertical.pack()
def slide():
    my_label=Label(root, text= horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x' +str(vertical.get()))


horizontal =Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label=Label(root, text= horizontal.get()).pack()



my_btn= Button(root, text='click me', command=slide).pack()
root.mainloop()'''


#------------- check boxex

'''root = Tk()
root.title('ivanka')
root.geometry('400x400')

def show():
    my_label=Label(root,text=var.get()).pack()

#var=IntVar()
var=StringVar()

c=Checkbutton(root,text='klikni', variable=var, onvalue='on', offvalue='off' )
c.deselect()  # ovo radi gumb zivim i pokazuje nam kad je on a kad je off
c.pack()



my_button=Button(root, text='show sellection', command=show).pack()

root.mainloop()'''


#------------- dropdown menu-s

'''root = Tk()
root.title('ivanka')
root.geometry('400x400')
#drop down boxes

def show():
    my_label = Label(root, text=clicked.get()).pack()

options= [
    'monday', 
    'tuseday', 
    'wednseday', 
    'thursday', 
    'friday' 
    ]

clicked=StringVar()
clicked.set(options[0])

drop=OptionMenu(root, clicked, *options) #umjesto options mozemo ispisati sve iz liste na to mjesto
drop.pack()

my_button=Button(root, text='show sellection', command=show).pack()
root.mainloop()'''

#------------- using databases
import sqlite3

'''root = Tk()
root.title('ivanka')
root.geometry('400x400')

#database

#create data base or connect to one

connect =sqlite3.connect('knjige.db')

#create cursor
cursor= connect.cursor()

#create table
cursor.execute(""" CREATE TABLE adresses (
    first_name text, 
    last_name text,
    adress text,
    city text, 
    zipcode integer
)""")



#commit changes
connect.commit()

#close connection
connect.close()


root.mainloop()'''



#------------- bilding gui for our databases
'''import sqlite3

root = Tk()
root.title('ivanka')
root.geometry('400x400')
connect =sqlite3.connect('knjige.db')
    #create cursor
cursor= connect.cursor()


cursor.execute(""" CREATE TABLE adresses (
    first_name text, 
    last_name text,
    adress text,
    city text, 
    zipcode integer
)""")

#create edit function to update a record
def edit():
    editor = Tk()
    editor.title('ivanka')
    editor.geometry('400x400')
    connect =sqlite3.connect('knjige.db')
    cursor= connect.cursor()
    
    
    record_id= delete_box.get()
    

    #query the database
    connect.execute('SELECT *  FROM adresses WHERE oid=' + record_id )
    records = connect.fetchall() 
    


    #loop thru results
    print_records=''
    for record in records:
        print_records += str(record[0]) +' ' + str(record[1]) +'\n'+' '+  '\t' + str(record[6]) 

    query_label=Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    
    first_name_editor=Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    last_name_editor=Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1)


    adress_editor=Entry(editor, width=30)
    adress_editor.grid(row=2, column=1)


    city_editor=Entry(editor, width=30)
    city_editor.grid(row=3, column=1)


    zipcode_editor=Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1)


    #create text box labels
    first_name_label=Label(editor, text='first name')
    first_name_label.grid(row=0, column=0,pady=(10, 0))

    last_name_label=Label(editor, text='last name')
    last_name_label.grid(row=1, column=0)

    adress_label=Label(editor, text='adress name')
    adress_label.grid(row=2, column=0)

    city_label=Label(editor, text='city name')
    city_label.grid(row=3, column=0)

    zipcode_label=Label(editor, text='zipcode ')
    zipcode_label.grid(row=4, column=0)
    #create buton to save record

    edit_button=Button(editor, text='SAVE RECORD', command=edit)
    edit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=144)


        #loop thru results
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        adress_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        zipcode_editor.insert(0, record[4])


#create funkcion to delete data
def delete():
    connect =sqlite3.connect('knjige.db')
    #create cursor
    cursor= connect.cursor()
    #delete record
    cursor.execute('DELETE from adresses WHERE  oid = ' + delete_box.get())
    
    connect.commit()
    connect.close()



#create submit funkcion for data base
def submit():
    #database
    #create data base or connect to one
    connect =sqlite3.connect('knjige.db')
    #create cursor
    cursor= connect.cursor()
    cursor.execute('INSERT INTO adresses VALUES (:first_name, :last_name, :adress, :city, :zipcode)',
        {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'adress': adress.get(),
            'city': city.get(),
            'zipcode': zipcode.get()

        })


    #clear the text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    adress.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)


# create query function

def query():
    connect =sqlite3.connect('knjige.db')
    cursor= connect.cursor()

    #query the database
    connect.execute('SELECT *, oid FROM adresses')
    records = connect.fetchall() 
    #print(records)

    #loop thru results
    print_records=''
    for record in records:
        print_records += str(record[0]) +' ' + str(record[1]) +'\n'+' '+  '\t' + str(record[6]) 

    query_label=Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)



#create text boxes
first_name=Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

last_name=Entry(root, width=30)
last_name.grid(row=1, column=1)


adress=Entry(root, width=30)
adress.grid(row=2, column=1)


city=Entry(root, width=30)
city.grid(row=3, column=1)


zipcode=Entry(root, width=30)
zipcode.grid(row=4, column=1)


delete_box=Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)



#create text box labels
first_name_label=Label(root, text='first name')
first_name_label.grid(row=0, column=0,pady=(10, 0))

last_name_label=Label(root, text='last name')
last_name_label.grid(row=1, column=0)

adress_label=Label(root, text='adress name')
adress_label.grid(row=2, column=0)

city_label=Label(root, text='city name')
city_label.grid(row=3, column=0)

zipcode_label=Label(root, text='zipcode ')
zipcode_label.grid(row=4, column=0)

delete_box_label=Label(root, text='Select ID ')
delete_box_label.grid(row=9, column=0, pady=5)


# create submit button

submit_button=Button(root, text='add record to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#query button

query_button=Button(root, text='show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a select button
delete_button=Button(root, text='Select RECORD', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


#create an updaTe button
edit_button=Button(root, text='DELETE RECORD', command=edit)
edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

#commit changes
connect.commit()

#close connection
connect.close()
'''
