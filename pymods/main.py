#!/usr/bin/python3

import tkinter as tk
import platform

root = tk.Tk()
root.title('PyMods Manager')

system = platform.system()
if system == 'Windows':
    root.state('zoomed')
elif system == 'Linux' or system == 'Darwin':
    root.attributes('-zoomed', True)
elif system == '':
    expectation = "Expected: 'Linux' 'Windows' or 'Darwin', Received: "
    raise OSError(expectation + system)

lframe = tk.Frame(root)
lframe.grid(column=0, row=0, columnspan=7)
lframe.grid_columnconfigure(14, minsize=100)

top_left = ['L1','L2','L3','L4','L5','L6','L7']
count = 0
for button in top_left:
    button = tk.Button(lframe, text=button)
    button.grid(row=0, column=count)
    count += 1

rframe = tk.Frame(root)
rframe.grid(column=15, row=0)

top_right = ['R1','R2','R3']
for button in top_right:
    button = tk.Button(rframe, text=button)
    button.grid(row=0, column=count)
    count += 1

root.mainloop()
