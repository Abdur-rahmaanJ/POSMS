# -*- coding: utf-8 -*-
"""
@author: arj
"""

from tkinter import *

root = Tk()
root.title('POSMS')

def edit_send():
    '''
    send mail to subscribers window
    '''
    editwin = Toplevel(root)
    
    # to
    editwin_address_l = Label(editwin, text="To")
    editwin_address_l.grid(column=0, row=0) 
    editwin_address_in = Entry(editwin)
    editwin_address_in.grid(column=0, row=1)
    
    #subject
    ##label
    editwin_topic_l = Label(editwin, text="Subject")
    editwin_topic_l.grid(column=0, row=2)
    ##input
    editwin_topic_in = Entry(editwin)
    editwin_topic_in.grid(column=0, row=3)
    
    #body
    ##label
    editwin_body_l = Label(editwin, text="Body")
    editwin_body_l.grid(column=0, row=4) 
    ##input
    editwin_body_in = Text(editwin)
    editwin_body_in['height'] = 10
    editwin_body_in['width'] = 30
    editwin_body_in.grid(column=0, row=5)
    
    #send
    ##button
    send_mail = Button(editwin, text="send")
    send_mail.grid(column=0, row=6)
    
def view_subs():
    '''
    view subscribed users
    '''
    viewwin = Toplevel(root)
    
    #view
    ##label
    editwin_top_l = Label(viewwin, text="View subscribed users")
    editwin_top_l.grid(column=0, row=0) 

def remove_subs():
    '''
    unsubscribe a user manually
    '''
    pass
    
def hello():
    print("hello!")

menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
subs_menu = Menu(menubar, tearoff=0)
subs_menu.add_command(label="Mail", command=edit_send)
subs_menu.add_command(label="View Subscribers", command=view_subs)
subs_menu.add_command(label="Remove Subscribers", command=hello)
#filemenu.add_separator()
menubar.add_cascade(label="Menu", menu=subs_menu)

#add subs label
subs_add_l = Label(root)
subs_add_l['text'] = 'Manually add subscriber'
subs_add_l.grid(column=0, row=0)
#add subs input
subs_add_entry = Entry(root)
subs_add_entry.grid(column=0, row=1)
#add subs button
subs_add_but = Button(root)
subs_add_but['text'] = 'add'
subs_add_but.grid(column=0, row=2)

root.config(menu=menubar)
root.mainloop()


print('term')

'''
def main():
    pass

if __name__ == "__main__":
    main()

'''