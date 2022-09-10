from tkinter import *
from PIL import Image
from PIL import ImageTk

newroot = tk.Tk()
newroot.title("Settings")
newroot.geometry("350x600")
newroot.resizable(width=False, height=False)


filename = PhotoImage(file="settings.png")
background_label = Label(newroot, image=filename)
bgl2 = background_label.place(x=0, y=0, relwidth=1, relheight=1)



newroot.mainloop()