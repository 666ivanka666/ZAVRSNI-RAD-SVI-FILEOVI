
from cProfile import label
import threading
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import time
from random import randint
root = tk.Tk()
root.title('Algebra | Sučelje za prikaz liste biljaka')
root.configure(bg='#282828') # tamno siva pozadina
# Define the geometry of the window
root.geometry('300x300')

#def five_seconds():
#    time.sleep(5)
#    my_label.config(text='5 sec is up')

def random():
    random_label.config(text=f'ph value: {randint(1,14)}')

#my_label=Label(root, text='hello there')
#my_label.pack(pady=20)

#my_button1=Button(root, text='5 sec', command= threading.Thread(target=five_seconds).start())
#my_button1.pack(pady=20)

my_button2=Button(root, text='pick random ph', command= random)
my_button2.pack(pady=20)

random_label=Label(root, text='')
random_label.pack(pady=20)


#threading.Thread(target=five_seconds).start()



root.mainloop()



#https://www.youtube.com/watch?v=jnrCpA1xJPQ





def random():
    random_label.config(text=f'random number: {randint(1,100)}')


my_button2=Button(root, text='pick random number', command= random)
my_button2.pack(pady=20)

random_label=Label(root, text='')
random_label.pack(pady=20)






