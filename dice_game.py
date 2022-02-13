from tkinter import *
import random
import time

def roll():
    x = random.choice(['b.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png'])
    return x

def img(event):
    global d1, d2
    for i in range(18):
        d1 = PhotoImage(file=(roll()))  # dice num1
        d2 = PhotoImage(file=(roll()))  # dice num2
        dice1['image'] = d1
        dice2['image'] = d2
        root.update()
        time.sleep(0.3)

root = Tk()
root.geometry('400x200')
root.title('Dice Game')
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file=('image.png')))
canv = PhotoImage(file=('sheet.png'))
Label(root, image=canv).pack()
dice1 = Label(root)
dice1.place(relx=0.3, rely=0.5, anchor=CENTER)
dice2 = Label(root)
dice2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<Button-1>', img)
img('event')

root.mainloop()
