from tkinter import ttk
from tkinter import *
import os
import tkinter.filedialog
from bao import method
from bao import a_ico as a
from bao import e_jpg as e
from bao import c_jpg as c
#对图片的大小进行设置
root = Tk() #创建主窗体
root.title("xvideos爬虫!")
root.geometry("350x540+750+200")
#root.attributes("-alpha",0.6)
k=os.path.abspath(os.path.join(os.getcwd(),'..'))
method.decodepicture(k+'/image/a',a.img,'.ico')
root.iconbitmap(k+'/image/a.ico')
root.resizable(0,0)

huabu=tkinter.Canvas(root,width=350,height=540)
method.decodepicture(k+'/image/e',e.img,'.jpg')
tupian=method.get_image(k+'/image/e.jpg',350,540)
huabu.create_image(175,270,image=tupian)
huabu.pack()


lb = Label(root, text="请选择系统或自定义类型:  ")
lb.place(x=25,y=150)
combobox=ttk.Combobox(root,width=17,state='readonly')
combobox['values']=("系统类型","自定义类型")
combobox.current(1)
combobox.place(x=180,y=150)
lb = Label(root, text="请输入要爬取的视频类型:  ")
lb.place(x=25,y=185)
entry = Entry(root)
entry.place(x=180,y=185)
lb = Label(root, text="请输入视频命名开始的序号:")
lb.place(x=25,y=220)
entry1 = Entry(root)
entry1.place(x=180,y=220)
lb = Label(root, text="请输入开始爬取的网页号:  ")
lb.place(x=25,y=255)
entry2 = Entry(root)
entry2.place(x=180,y=255)

lb = Label(root, text="请输入结束爬取的网页号:  ")
lb.place(x=25,y=290)
entry3 = Entry(root)
entry3.place(x=180,y=290)
lb = Label(root, text="请选择视频的存储位置:    ")
lb.place(x=25,y=325)
str4=StringVar()
lb = Entry(root, textvariable=str4,width=14)
lb.place(x=180,y=325)

la=Label(root,text="爬取视频的画质:")
la.place(x=70,y=360)
combobox1=ttk.Combobox(root,width=10,state='readonly')
combobox1['values']=("高","低")
combobox1.current(1)
combobox1.place(x=180,y=360)

btn1 = Button(root, text="浏览..", width=4,height=1,cursor='pirate',command= lambda :method.liulan(str4))
btn1.place(x=285,y=323)
method.decodepicture(k+'/image/c',c.img,'.jpg')
button_image=method.get_image(k+'/image/c.jpg',55,28)
btn = Button(root, text="开始爬取",image=button_image,bd=8,cursor='pirate',relief="raised", fg='black', width=55,height=25,compound=tkinter.CENTER,command=lambda :method.get_photo(entry,entry1,entry2,entry3,str4,combobox,combobox1))
btn.place(x=200,y=410)

root.protocol("WM_DELETE_WINDOW",lambda :method.close_windows(root))
root.mainloop()












