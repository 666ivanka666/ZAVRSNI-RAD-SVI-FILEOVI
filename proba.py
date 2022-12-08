from PIL import Image
from math import sqrt



from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


root = tk.Tk()
root.title('Algebra | Graficki prikaz')
root.configure(bg='#282828') 
root.geometry('400x300')


def graph ():
   
    imag = Image.open("slika_1.jpg")
    imag = imag.convert ('RGB')
    X,Y = 0,0
    pixelRGB = imag.getpixel((X,Y))
    R,G,B = pixelRGB 
    brightness = sum([R,G,B])/3 

my_button=Button(root, text='Graficki prikaz', command=graph,bg='#282828', fg='white')
my_button.pack()

root.mainloop()
