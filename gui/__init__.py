# encoding=UTF-8

from Tkinter import *
from ttk import *
import tkFileDialog
import tkMessageBox
import os
from db import session
from db.models import VIN, CarNum
import re


class GuiMenu(object):

    filename = None

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
        self.filename = tkFileDialog.askopenfilename()
        res = re.search(u'\.txt', self.filename)
        if res is not None:
            try:
                CarNum.inject(self.filename)
            except :
                tkMessageBox.showinfo(self.root, '加载错误: \n'
                                                 '牌号信息已存在!')
        else:
            tkMessageBox.showinfo(self.root, '加载错误: \n'
                                             '错误的文件格式, 必须为 \'.txt\'!')

    def edit(self):
        pass

    def view(self):
        pass

    def help(self):
        tkMessageBox.showinfo(self.root, u'声明: \n'
                                         u'本软件使用的全部组件均为开源软件, \n'
                                         u'任何人有权下载\更改\发行本软件的源码.\n\n'
                                         u'版本: v0.0.1 \n '
                                         u'作者: 王志豪 \n '
                                         u'邮箱: wangzhihao9110@163.com ')


class GuiFrame(object):

    def __init__(self, root, top_frame=None, content_frame=None, bottom_frame=None):
        self.root = root
        self.top_frame = top_frame
        self.content_frame = content_frame
        self.bottom_frame = bottom_frame

        # top area
        self.vin_label = Label(top_frame, text=u'请输入VIN:')
        self.vin_entry = Entry(top_frame)
        self.query_btn = Button(top_frame, command=self.query, text=u'查询')

        self.vin_label.grid(row=0, column=0, sticky=W)
        self.vin_entry.grid(row=0, column=1)
        self.query_btn.grid(row=0, column=2)

        # content area

        # bottom area

    def query(self):
        try:
            VIN.validate_vin(self.vin_entry.get())
            self.gen_btn = Button(self.top_frame, command=self.gen, text=u'生成')
            self.gen_btn.grid(row=0, column=3)
        except ValueError as e:
            tkMessageBox.showinfo(self.root, e)

    def gen(self):
        res = CarNum.rand_nums()
        msg = ''
        for carnum in res:
            msg += carnum.val + '\n'
        tkMessageBox.showinfo(self.root, msg)
        self.gen_btn.destroy()



