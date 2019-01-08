import tkinter
import os
from tkinter import *

class Calculator(object):
    '''计算器'''
    def __init__(self):
        # 初始化tkinter
        self.tk = tkinter.Tk()
        # 窗口名称
        self.tk.title('计算器')
        # 窗口大小
        self.tk.minsize(370,460)
        self.tk.maxsize(400,400)
        # 窗口图表
        self.tk.iconbitmap(os.getcwd()+'/favicon.ico')

    def start(self):
        # 启动计算器方法
        self.tk.mainloop()

if __name__ == '__main__':
    # 实例化计算器类
    NewCalculator = Calculator()
    # 调用启动计算器方法
    NewCalculator.start()