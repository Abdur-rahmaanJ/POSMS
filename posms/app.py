# -*- coding: utf-8 -*-
"""
@author: arj
"""

from tkinter import *

root = Tk()
root.title('POSMS')

def hello():
    print("hello!")

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
subs_menu = Menu(menubar, tearoff=0)
subs_menu.add_command(label="Mail", command=hello)
subs_menu.add_command(label="View Subscribers", command=hello)
#filemenu.add_separator()
menubar.add_cascade(label="Menu", menu=subs_menu)

subs_l = Label(root)
subs_l['text'] = 'add subscriber'
subs_l.grid(column=0, row=0)

subs_entry = Entry(root)
subs_entry.grid(column=0, row=1)

subs_add = Button(root)
subs_add['text'] = 'add'
subs_add.grid(column=0, row=2)

root.config(menu=menubar)
root.mainloop()


print('term')

'''
def main():
    pass

if __name__ == "__main__":
    main()

'''