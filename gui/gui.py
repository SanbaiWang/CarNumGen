# encoding=UTF-8
import os
import tkFileDialog
import tkMessageBox
from Tkinter import *
from ttk import *


class FileGuiChose(object):

    def __init__(self, initdir=None, frame=None, showframe=None, bottomeFrame=None):
        self.entryvar = StringVar()
        self.showframe =showframe
        # top area
        self.glabel = Label(frame,text=u'directory you chose is:')
        self.gentry = Entry(frame,textvariable=self.entryvar)
        self.gbutton = Button(frame,command=self.opendir,text=u'chose dir')
        self.keylistbox = Listbox(frame)

        #initiate the dropdown list
        # self.keyvar = StringVar()
        # self.keyvar.set('keyword')
        # self.items = ['BufferPool','Close','Data Capture','Compress','Pqty','Sqty']
        # self.gcombobox=Combobox(frame,values=self.items,textvariable=self.keyvar)
        # self.gentry.bind('',func=self.refresh)
        self.glabel.grid(row=0,column=0,sticky=W)
        self.gentry.grid(row=0,column=1)
        self.gbutton.grid(row=0,column=2)
        # self.gcombobox.grid(row=0,column=3)


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


class GuiMenu(object):
    def hello(self):
        pass

    def file(self):
        pass

    def edit(self):
        pass

    def view(self):
        pass

    def help(self):
        tkMessageBox.showinfo(self.root, u'author kinfinger \n verion 1.0 \n Thank you \n kinfinge@gmail.com ')

    def __init__(self, root):
        self.root = root
        self.menubar = Menu(root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.file)
        filemenu.add_command(label="New", command=self.file)
        filemenu.add_command(label="Save", command=self.file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        # create more pulldown menus
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.edit)
        editmenu.add_command(label="Copy", command=self.edit)
        editmenu.add_command(label="Paste", command=self.edit)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(self.menubar,tearoff=0)
        helpmenu.add_command(label="About", command=self.help)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=self.menubar)


def main():
    root = Tk()
    root.title('车牌号随机生成器')
    root.columnconfigure(0, minsize=50)

    top_frame = Frame(root, height=80)
    top_frame.pack(side=TOP)
    
    content_frame = Frame(root)
    content_frame.pack(side=TOP)
    
    bootom_frame = Frame(root)
    bootom_frame.pack(side=TOP)
    

    GuiMenu(root)
    
    fguiChose=FileGuiChose(os.curdir, top_frame, content_frame, bootom_frame)
    mainloop()

if __name__ == '__main__':
    main()
