# -*- coding: utf-8 -*-
"""
@author: arj
"""

from tkinter import *
from tkinter.ttk import *
from utils.posmsdb import DB

root = Tk()
root.title('POSMS')

db = DB()



def manual_add():
    '''
    manually add subscribers
    '''
    def add(mail):
        db.add_subs(mail)
        subs_add_entry.delete(0,END)
        
    subsaddwin = Toplevel(root)
    subsaddwin.title('Add subscriber')
    
    #add subs label
    subs_add_l = Label(subsaddwin)
    subs_add_l['text'] = 'Manually add subscriber'
    subs_add_l.grid(column=0, row=0)
    #add subs input
    subs_add_entry = Entry(subsaddwin)
    subs_add_entry.grid(column=0, row=1)
    #add subs button
    subs_add_but = Button(subsaddwin, 
                          command = lambda: add(subs_add_entry.get()) )
    subs_add_but['text'] = 'add'
    subs_add_but.grid(column=0, row=2)

def edit_send():
    '''
    send mail to subscribers window
    '''
    editwin = Toplevel(root)
    
    
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
    
    #pass
    ##label
    editwin_pass_l = Label(editwin, text="Pass")
    editwin_pass_l.grid(column=0, row=6) 
    ##input
    editwin_pass_in = Entry(editwin)
    editwin_pass_in.grid(column=0, row=7)
    
    #send
    ##button
    send_mail = Button(editwin, text="send")
    send_mail.grid(column=0, row=8)
    
def view_subs():
    global db
    '''
    view subscribed users
    '''
    viewwin = Toplevel(root)
    
    #view
    ##label
    editwin_top_l = Label(viewwin, text="View subscribed users")
    editwin_top_l.grid(column=0, row=0) 
    
    tree = Treeview(viewwin, columns=('id', 'mail') )
    tree["columns"]=("id","mail")
    tree.column("id")
    tree.column("mail")
    tree.heading("id", text="ID")
    tree.heading("mail", text="MAIL")
    x = db.view_subs()
    i = 1
    for row in x:
        tree.insert('', 'end', text=str(i), values=(row[0], row[1])) 
        i+=1
    tree.grid(column=0, row=1)
    
def rem_subs():
    '''
    unsubscribe a user manually
    '''
    remwin = Toplevel(root)
    remwin.title('Remove subscriber')
    
    #label
    remwin_l = Label(remwin, text="Mail")
    remwin_l.grid(column=0, row=0)
    
    #input
    remwin_in = Entry(remwin)
    remwin_in.grid(column=0, row=1)
    
    #button
    remwin_but = Button(remwin, text='remove')
    remwin_but.grid(column=0, row=2)
    

def set_mail():
    '''
    set user mail
    '''
    setmailwin = Toplevel(root)
    setmailwin.title('Remove subscriber')
    
    #label
    setmail_l = Label(setmailwin, text='mail')
    setmail_l.grid(column=0, row=0)
    
    #input
    setmail_in = Entry(setmailwin)
    setmail_in.grid(column=0, row=1)
    
    #button
    setmail_but = Button(setmailwin, text='set')
    setmail_but.grid(column=0, row=2)
    
def hello():
    print("hello!")

#pulldown main menu
menubar = Menu(root)
subs_menu = Menu(menubar, tearoff=0)
subs_menu.add_command(label="Add Subscriber", command=manual_add)
subs_menu.add_command(label="View Subscribers", command=view_subs)
subs_menu.add_command(label="Remove Subscribers", command=rem_subs)
menubar.add_cascade(label="Menu", menu=subs_menu)

# subs settings
subs_settings = Menu(menubar, tearoff=0)
subs_settings.add_command(label="Set my mail", command=set_mail)
menubar.add_cascade(label="Config", menu=subs_settings)

'''
send mail to subscribers window
'''
#subject
##label
editwin_topic_l = Label(root, text="Subject")
editwin_topic_l.grid(column=0, row=2)
##input
editwin_topic_in = Entry(root)
editwin_topic_in.grid(column=0, row=3)

#body
##label
editwin_body_l = Label(root, text="Body")
editwin_body_l.grid(column=0, row=4) 
##input
editwin_body_in = Text(root)
editwin_body_in['height'] = 10
editwin_body_in['width'] = 30
editwin_body_in.grid(column=0, row=5)

#pass
##label
editwin_pass_l = Label(root, text="Pass")
editwin_pass_l.grid(column=0, row=6) 
##input
editwin_pass_in = Entry(root)
editwin_pass_in.grid(column=0, row=7)

#send
##button
send_mail = Button(root, text="send")
send_mail.grid(column=0, row=8)


root.config(menu=menubar)
root.mainloop()


print('term')

'''
def main():
    pass

if __name__ == "__main__":
    main()

'''