
# * widgets = GUI elements: buttons, textboxes, labels, images
# * windows = serves as a container to hold or contain these widgets


from tkinter import *

from PIL import ImageTk, Image #* for using jpg image and install in the terminal -> 'pip install Pillow'


window = Tk() #* instantiate an instance of a window

photo = ImageTk.PhotoImage(Image.open('_7a508162-9427-4cfc-abec-a2e751804a5c.jpg')) #* for using jpg image

label = Label(window,
            text="hello world",
            font=('Arial', 40, 'bold'), 
            fg='blue', bg='#00d1ae', 
            relief=RAISED, 
            bd=10, 
            padx=10, 
            pady=20,
            image=photo, compound='bottom')
label.pack()
label.place(x=0, y=0)

window.geometry("500x500")
window.title("first GUI program")

icon = PhotoImage(file='pngwing.com(2).png')
window.iconphoto(True,icon)

window.config(background="#00d142")


window.mainloop() #* place window on computer screen, listen to events