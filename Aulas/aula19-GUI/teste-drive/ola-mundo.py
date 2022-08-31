import ttkbootstrap as ttk
from tkinter import PhotoImage

base = ttk.Window(
    title = "Minha GUI",
    size = (1024,400),
    position=(100,100),
    minsize = (600,300),
    maxsize=(1800,900),
    alpha = 0.75
)

base.iconphoto(False,PhotoImage(file='calculator.png'))
base.mainloop()