#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import platform

root = tk.Tk()
root.title('PyMods Manager')
root.resizable(height=True, width=True) # False locks the Window

system = platform.system()
if system == 'Windows':
    root.state('zoomed')
elif system == 'Linux' or system == 'Darwin':
    root.attributes('-zoomed', True)
elif system == '':
    expectation = "Expected: 'Linux' 'Windows' or 'Darwin', Received: "
    raise OSError(expectation + system)

# Global font size and style
globalfont = tkFont.Font(family='Helvetica', size=10)

# Used for row=0 frames
topframe = tk.Frame(root)
topframe.pack(side='top', fill='x')

##################
# Top Left Frame #
##################
topleftframe = tk.Frame(topframe)
topleftframe.grid(column=0, columnspan=7, row=0)
topleftframe.grid(padx=10, pady=1)

top_left = ['L1','L2','L3','L4','L5','L6','L7']
count = 0
for button in top_left:
    button = tk.Button(topleftframe, text=button)
    button.grid(row=0, column=count, ipady=10, ipadx=10, padx=2, pady=3)
    count += 1

# Empty Frame absorbing extra horizontal space
topmiddleframe = tk.Frame(topframe)
topmiddleframe.grid(column=8, columnspan=10, row=0)
topmiddleframe.grid(ipady=10, ipadx=10, padx=2, pady=3)
topframe.grid_columnconfigure(8, weight=1)


###################
# Top Right Frame #
###################
toprightframe = tk.Frame(topframe)
toprightframe.grid(column=19, columnspan=3, row=0)
toprightframe.grid(padx=10, pady=1)

top_right = ['R1','R2','R3']
count = 19
for button in top_right:
    button = tk.Button(toprightframe, text=button)
    button.grid(row=0, column=count, ipady=10, ipadx=10, padx=2, pady=3)
    count += 1


###############
# Border line #
###############
lineframe=tk.Frame(root)
lineframe.pack(side='top',fill='x')
linecanvas = tk.Canvas(lineframe, height=2, background='#8D9888')
linecanvas.pack(fill='x', expand=1, pady=3)


##############
# Main Frame #
##############
midframe = tk.Frame(root)
midframe.pack(side='top', fill='x')

mainframe = tk.Frame(midframe)
mainframe.grid(column=0, row=2, columnspan=21, padx=6)

profilelabel = tk.Label(mainframe, text='Profile', font=globalfont)
profilelabel.grid(column=0, row=2, columnspan=2, sticky="W")
profilelabel.grid(ipady=10, ipadx=6)

menued = tk.StringVar()
menued.set('Default')
profilemenu = ttk.Combobox(mainframe, textvariable=menued, values='Default')
profilemenu.grid(column=2, row=2, columnspan=6, ipadx=125, ipady=3)


root.mainloop()
