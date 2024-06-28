
# * widgets = GUI elements: buttons, textboxes, labels, images
# * windows = serves as a container to hold or contain these widgets


from tkinter import *

from PIL import ImageTk, Image #* for using jpg image and install in the terminal -> 'pip install Pillow'


window = Tk() #* instantiate an instance of a window

# photo = ImageTk.PhotoImage(Image.open('_7a508162-9427-4cfc-abec-a2e751804a5c.jpg')) #* for using jpg image

photo = PhotoImage(file='pngegg(1).png')

imageButton = PhotoImage(file='pngwing.com(2).png')


count = 0
def click():
    global count
    count += 1
    print(f"you clicked {count} times")

buttun = Button(window,
                text= "click me",
                command=click,
                font=('Arial', 40, 'bold'),
                image=imageButton,
                compound='left',
                fg='blue', bg='#00d1ae',
                activebackground='blue',
                activeforeground='#00d1ae',
                padx=10 )
buttun.pack()
buttun.place(x=600, y=0)

label = Label(window,
            text="hello world",
            font=('Arial', 40, 'bold'), 
            fg='blue', bg='#00d1ae', 
            relief=RAISED, 
            bd=10, 
            padx=10, 
            pady=20,
            image=photo,
            compound='bottom')


label.pack()
label.place(x=0, y=0)

window.geometry("1920x1080")
window.title("first GUI program")

icon = PhotoImage(file='pngwing.com(2).png')
window.iconphoto(True,icon)

window.config(background="#00d142")


window.mainloop() #* place window on computer screen, listen to events