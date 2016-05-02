# -*- coding: cp936 -*-
__author__ = 'kinfinger'
import os
import tkFileDialog
import tkMessageBox
from Tkinter import *
from ttk import *
class FileGuiChose(object):
    def __init__(self,initdir=None,frame=None,showframe=None,bottomeFrame=None):
        self.entryvar = StringVar()
        self.showframe =showframe
        # top area
        self.glabel = Label(frame,text=u'directory you chose is:')
        self.gentry = Entry(frame,textvariable=self.entryvar)
        self.gbutton = Button(frame,command=self.opendir,text=u'chose dir')
        self.keylistbox = Listbox(frame)
        #initiate the dropdown list
        self.keyvar = StringVar()
        self.keyvar.set('keyword')
        self.items = ['BufferPool','Close','Data Capture','Compress','Pqty','Sqty']
        self.gcombobox=Combobox(frame,values=self.items,textvariable=self.keyvar)
        self.gentry.bind('',func=self.refresh)
        self.glabel.grid(row=0,column=0,sticky=W)
        self.gentry.grid(row=0,column=1)
        self.gbutton.grid(row=0,column=2)
        self.gcombobox.grid(row=0,column=3)
        # content area
        self.texbar = Scrollbar(self.showframe,orient=VERTICAL)
        self.texbar.pack(side =RIGHT,fill=Y)
        self.bottombar = Scrollbar(showframe,orient=HORIZONTAL)
        self.bottombar.pack(side=BOTTOM,fill=X)
        self.textbox=Text(self.showframe,yscrollcommand=self.texbar.set,xscrollcommand=self.bottombar.set)
        self.textbox.pack(side=LEFT,fill=BOTH)
        self.texbar.config(command=self.textbox.yview)
        self.bottombar.config(command=self.textbox.xview)
    def opendir(self):
        self.textbox.delete('1.0',END)
        self.dirname = tkFileDialog.askdirectory()
        self.entryvar.set(self.dirname)
        showmessage = 'just for tip'
        if not self.dirname:
            self.messagebox=tkMessageBox(self.showframe,Message=showmessage)
        self.dirlist=os.listdir(self.entryvar.get())
        for eachdir in self.dirlist:
            self.textbox.insert(END,eachdir+'\r\n')
        self.textbox.update()
    def refresh(self,event=None):
        self.textbox.delete('1.0',END)
        self.dirlist=os.listdir(self.entryvar.get())
        for eachdir in self.dirlist:
                self.textbox.insert(END,unicode(eachdir,'cp936')+'\r\n')
        self.textbox.update()
class GuiMenu():
    def hello(self):
        pass
    def File(self):
        pass
    def Edit(self):
        pass
    def View(self):
        pass
    def Help(self):
        tkMessageBox.showinfo(self.root,u'author kinfinger \n verion 1.0 \n Thank you \n kinfinge@gmail.com ')
    def __init__(self,rootmenu):
        self.root=rootmenu
        self.menubar=Menu(rootmenu)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.File)
        filemenu.add_command(label="New", command=self.File)
        filemenu.add_command(label="Save", command=self.File)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=rootmenu.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        # create more pulldown menus
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.Edit)
        editmenu.add_command(label="Copy", command=self.Edit)
        editmenu.add_command(label="Paste", command=self.Edit)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(self.menubar,tearoff=0)
        helpmenu.add_command(label="About", command=self.Help)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        rootmenu.config(menu=self.menubar)
def main():
    root = Tk()
    root.title('DDL Check')
    root.columnconfigure(0,minsize=50)
    topFrame=Frame(root,height=80)
    contentFrame=Frame(root)
    bottomFrame=Frame(root)
    topFrame.pack(side=TOP)
    contentFrame.pack(side=TOP)
    bottomFrame.pack(side=TOP)
    GuiMenu(root)
    fguiChose=FileGuiChose(os.curdir,topFrame,contentFrame,bottomFrame)
    mainloop()
if __name__ == '__main__':
    main()