# encoding=UTF-8

from Tkinter import *
from ttk import *
import tkFileDialog
import tkMessageBox
import os


class GuiMenu(object):

    def __init__(self, root):
        self.root = root
        self.menubar = Menu(root)

        # create a pulldown menu 'File', and add it to the menu bar
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Load", command=self.load)
        self.menubar.add_cascade(label="File", menu=filemenu)

        # create a pulldown menu 'Help', and add it to the menu bar
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.help)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        # add menubar to root
        root.config(menu=self.menubar)

    def hello(self):
        pass

    def load(self):
        pass

    def edit(self):
        pass

    def view(self):
        pass

    def help(self):
        tkMessageBox.showinfo(self.root, u'声明: \n'
                                         u'本软件基于使用的全部组件均为开源软件, \n'
                                         u'任何人有权下载 \ 更改 \ 发行本软件的源码\n\n'
                                         u'版本: v0.0.1 \n '
                                         u'作者: 王志豪 \n '
                                         u'邮箱: wangzhihao9110@163.com ')
        
        
class Entry(object):

    __entry_val__ = None

    def __init__(self, root, top_frame=None, content_frame=None, bottom_frame=None):
        self.root = root
        self.entryvar = StringVar()
        self.content_frame = content_frame

        # top area
        self.vin_label = Label(top_frame, text=u'请输入VIN:')
        self.vin_entry = Entry(top_frame, textvariable=self.entryvar)
        self.query_btn = Button(top_frame, command=self.query, text=u'查询')
        self.gen_btn = Button(top_frame, command=self.gen, text=u'生成')

        self.vin_entry.bind(func=self.refresh)
        self.vin_label.grid(row=0, column=0, sticky=W)
        self.vin_entry.grid(row=0, column=1)
        self.query_btn.grid(row=0, column=2)
        self.gen_btn.grid(row=0, column=3)

    def query(self):
        pass

    def gen(self):
        tkMessageBox.showinfo(self.root, self.entryvar.get())
    
    def refresh(self):
        self.__entry_val__ = self.entryvar.get()


def app():
    root = Tk()
    root.title('车牌号随机生成器')
    root.geometry('400x200')

    top_frame = Frame(root, height=80)
    top_frame.pack(side=TOP)

    content_frame = Frame(root)
    content_frame.pack(side=TOP)

    bootom_frame = Frame(root)
    bootom_frame.pack(side=TOP)

    GuiMenu(root)

    fguiChose=Entry(os.curdir, top_frame, content_frame, bootom_frame)
    mainloop()

if __name__ == '__main__':
    app()