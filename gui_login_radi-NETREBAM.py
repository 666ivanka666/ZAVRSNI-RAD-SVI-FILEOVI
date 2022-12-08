import ctypes
import tkinter as tk
from tkinter import messagebox
import tkinter


root = tk.Tk()
root.title('Algebra | PyPosuda')
root.geometry('400x300')
root.configure(bg='#282828') 

def login():
    username ='ivanka'
    password ='666'
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Successful login', message='You login suessfuly')
    else:
        messagebox.showinfo(title='Error', message='Invalid login')


frame=tk.Frame(bg='#282828',width=800, height=600)

login_label=tk.Label(frame, text='Login',bg='#282828', fg='white',font=('Arial', 12))
login_label.grid(row=0,column=0, columnspan=2, pady=10)

username_label=tk.Label(frame, text= 'User name',bg='#282828',fg='white',font='Arial')
username_label.grid(row=1,column=0)

username_entry = tk.Entry(frame,font=('Arial, 8'))
username_entry.grid(row=1,column=1, pady= 5)

password_entry = tk.Entry(frame, show='*',font=('Arial, 8'))
password_entry.grid(row=2,column=1, pady= 5)

password_label=tk. Label(frame, text= 'Password',bg='#282828',fg='white',font='Arial')
password_label.grid(row=2,column=0)

login_button=tk.Button(frame, text='Login',bg='grey',fg='white',font=('Arial, 10'), command=login)
login_button.grid(row=3,column=0,columnspan=2,pady=10)


frame.pack()


'''
def create_prijavi_me():
    new_prijavi_me_window = tk.Toplevel(root)
    new_prijavi_me_window.focus()
    
def login():
    user_name = 'ivanka'
    password ='666'

 if frame_user_name.get() == user_name  and frame_password.get() == password:
       pass #doat cemo poziv 1st window gui ode
    else:
        mymessage = 'Wrong credentials! Please try again!'
        title = 'Login error'
        ctypes.windll.user32.MessageBoxA(0, mymessage, title, 1)


frame = tk.LabelFrame (root, width=800, height=600, text= 'Login',bg='#282828',fg='white', font='Arial') #Frame
frame.grid(column=0, row=0, padx=10, pady=10)

frame_user_name = tk.Label (frame, text= 'User name',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame_user_name =tk.Entry(frame)
frame_user_name.grid(column=1, row=1, padx=10, pady=10)

frame_password = tk.Label(frame, text= 'Password',bg='#282828',fg='white',font='Arial').grid(row=2)
frame_password =tk.Entry(frame)
frame_password.grid(column=1, row=2, padx=10, pady=10)

prijava = tk.Button(frame, text='Login', command=login,bg='#282828',fg='white',font='Arial')
prijava.grid(column=1, row=3, padx=30, pady=30)


def create_login_frame():
    login_frame = tk.Frame(
        root, width=300, height=100, bg="#282828"
    )
    login_frame.grid(row=1, column=0, columnspan=3, padx=15, pady=15)
'''
root.mainloop()



