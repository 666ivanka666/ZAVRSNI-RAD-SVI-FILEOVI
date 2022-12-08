'''import tkinter as tk


def flash(button):
    current_color = button.cget("background")
    next_color = "green" if current_color == "red" else "red"
    button.config(background=next_color)
    root.after(1000, flash, button)


root = tk.Tk()

Button1 = tk.Button(root, text="Button1", background="green")
Button2 = tk.Button(root, text="Button2", background="green")

Button1.pack()
Button2.pack()

Button1.bind("<ButtonPress-1>", lambda event: flash(Button1))
Button2.bind("<ButtonPress-1>", lambda event: flash(Button2))

root.mainloop()'''

#####
'''import tkinter as tk


def flash(button, buttons=set(), _after=[]):
    if button not in buttons:
        buttons.add(button)
    current_color = button.cget("foreground")
    next_color = "blue" if current_color == "red" else "red"
    for button in buttons:
        button.config(foreground=next_color)
    for after_id in _after:
        root.after_cancel(after_id)
    if buttons:
        _after.append(root.after(1000, flash, button))


if __name__ == '__main__':

    root = tk.Tk()
    Button1 = tk.Button(root, text="Button1", foreground="blue")
    Button1.pack()
    Button1.bind("<ButtonPress-1>", lambda event: flash(Button1))
    
    root.mainloop()'''
####
'''import tkinter as tk
import os
r = tk.Tk()
r.title("refresh button")
def refresh():
    r.destroy()
    os.popen("refresh.py") #change refresh.py according to yours program name
button_1 = tk.Button(r,text = "Refresh",command = refresh)
button_1.pack()

def exit():
    r.destroy()
button_2 = tk.Button(r,text = "Exit",command = exit)
button_2.pack()
r.mainloop()'''




import tkinter as tk
import os
r = tk.Tk()
r.title("refresh button")
def refresh():
    #r.destroy()
    os.popen("refresh.py") #change refresh.py according to yours program name
button_1 = tk.Button(r,text = "Refresh",command = refresh)
button_1.pack()


r.mainloop()