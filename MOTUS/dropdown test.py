from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("test")

clicked = StringVar()


drop = OptionMenu(root, clicked, "1", "2", "3")
drop.pack()

root.mainloop()