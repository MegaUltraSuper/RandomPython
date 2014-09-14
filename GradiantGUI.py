from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("My Game Main Menu")

menu = Canvas(master = root, bg = "#101010", width = 600, height = 600)
coord = 0,0,0,0
x1 =0
x2 =600
y1 =0
y2 =600
for i in range(150):
    x1 += 2
    x2 -= 2
    y1 += 2
    y2 -= 2
    coord = x1, y1, x2, y2
    color = "#"+str(hex(i+16))[2:]+str(hex(i+36))[2:]+str(hex(i+50))[2:]
    menu.create_rectangle(coord, fill = color, outline = color)

menu.pack()

root.bind('<Return>', calculate)

root.mainloop()
