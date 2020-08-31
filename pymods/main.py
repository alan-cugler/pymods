#!/usr/bin/python3

import tkinter as tk
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
root.grid_columnconfigure(8, weight=1)

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


lineframe=tk.Frame(root)
lineframe.pack(side='top',fill='x')
linecanvas = tk.Canvas(lineframe, height=2, background='#8D9888')
linecanvas.pack(fill='x', expand=1)


##############
# Main Frame #
##############
#topline = tk.Canvas(root, background='white')
#topline.pack(expand=True, fill='x')

#mainframe = tk.Frame(root)
#mainframe.grid(column=0, row=2, columnspan=21)
#root.grid_rowconfigure(1, weight=10)
#root.grid_rowconfigure(1, weight=1)

#topline.create_line(1000,1000,100,100)
#topline.grid(column=0, row=1)

#plabel = tk.Label(mainframe, text='profile')
#plabel.grid(column=0, row=2, columnspan=2, sticky="W")

#poption = tk.StringVar()
#poption.set('default')
#pmenu = tk.OptionMenu(mainframe, poption,'default')
#pmenu.grid(column=2, row=2, columnspan=6)

#e1label = tk.Label(mainframe, text='')
#e1label.grid(column=9, row=2)
#e1label.grid_columnconfigure(10, minsize=30)

#i1option = tk.StringVar()
#i1option.set('image')
#i1menu = tk.OptionMenu(mainframe, i1option,'image')
#i1menu.grid(column=10, row=2)


root.mainloop()
