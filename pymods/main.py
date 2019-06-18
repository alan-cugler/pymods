from tkinter import *
from tkinter import ttk
import platform

root = Tk()
root.title('PyMods Manager')

system = platform.system()
if system == 'Windows':
    root.state('zoomed')
elif system == 'Linux' or system == 'Darwin':
    root.attributes('-zoomed', True)
elif system == '':
    expectation = "Expected: 'Linux' 'Windows' or 'Darwin', Received: "
    raise OSError(expectation + system)


mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))

root.mainloop()
