# -*- coding:utf-8 -*-
import time
import datetime
import os
import tkinter as tk
import ctypes
import random as rd
from tkinter.constants import CHECKBUTTON, COMMAND
from tkinter import Checkbutton, Label, ttk
from tkinter import font
from tkinter import messagebox
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import threading
import pandas as pd
import numpy as np

window = tk.Tk()
window.title('新建LaTex文档')
window.geometry('700x300')
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
window.tk.call('tk', 'scaling', ScaleFactor/75)
tkf = ('黑体',14)
Bg = 'white'
window.configure(bg=Bg)

name_Label = tk.Label(window,anchor='e',font=tkf,bg=Bg,text='文件名：').grid(column=0,row=0)
name = tk.Entry(window,text='Demo',font=tkf,)
name.grid(column=1,row=0)
suf_lb = tk.Label(window,anchor='w',font=tkf,bg=Bg,text='.tex').grid(column=2,row=0)

class_num = tk.IntVar()
class_num.set(0)
class_label = tk.Label(window,anchor='e',font=tkf,bg=Bg,text='文档类：').grid(column=0,row=1)
tk.Radiobutton(window,background=Bg,font=tkf,text='ctexart',variable=class_num,value=0).grid(column=1,row=1)
tk.Radiobutton(window,background=Bg,font=tkf,text='ctexbook',variable=class_num,value=1).grid(column=1,row=2)
tk.Radiobutton(window,background=Bg,font=tkf,text='ctexrep',variable=class_num,value=2).grid(column=1,row=3)

dic =['ctexart','ctexbook','ctexrep']

def A():
    T1 = threading.Thread(target=go)
    T1.start()
def go():
    Name=name.get()
    dir_name='D:\\tex\\latex file\\%s' % Name
    os.makedirs(dir_name)
    with open(dir_name+"\\%s.tex" % Name,mode="w",encoding="utf-8") as f:
        f.write("\\documentclass[hyperref,UTF8]{%s}\n" % dic[class_num.get()])
        f.write("\\usepackage[dvipdfmx]{graphicx}\n")
        f.write("\\usepackage{gbt7714}\n")
        f.write("\\usepackage{float}\n\\usepackage{ragged2e}\n\\usepackage{amsthm}\n\\usepackage{amssymb}\n\\usepackage{amsmath}\n\\usepackage{wrapfig}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta}\n")
        f.write("\\usepackage{booktabs}\n")
        f.write("%%\\usepackage[a4paper,left=3.18cm,right=3.18cm,top=2.54cm,bottom=2.54cm]{geometry}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{caption}\n\\usepackage{hyperref}\n\\newcommand{\\upcite}[1]{\\textsuperscript{\\textsuperscript{\\cite{#1}}}}\n\\setCJKfamilyfont{song}{SimSun}\n\\title{%s}\n\\author{limbo137}\n\\begin{document}\n\n\\end{document}" % Name)
        f.close()
    window.quit()

stt = tk.Button(window,font=tkf,bg=Bg,text='确定',command=A)
stt.grid(column=3,row=2)
window.mainloop()