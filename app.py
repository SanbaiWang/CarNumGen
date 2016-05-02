# encoding=UTF-8

from Tkinter import Tk, Frame, TOP, mainloop
from gui import GuiFrame, GuiMenu


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
    GuiFrame(root, top_frame, content_frame, bootom_frame)

    mainloop()

if __name__ == '__main__':
    app()
