from tkinter import ttk
from tkinter import *
import _tkinter
import tkinter.filedialog
from tkinter import messagebox
import requests
import re
import os
import time
import base64
from bao import b_ico as b
from bao import d_jpg as s
from PIL import Image, ImageTk



def decodepicture(a,b,c):#a为图片的路径，b为图片的base64码，c为图片的.扩展名
    tmp = open(a+c, 'wb')
    tmp.write(base64.b64decode(b))
    tmp.close()

#对图片的大小进行设置
def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)




def get_code(combobox,entry,page):  # 获取网页源码

    if combobox.get()=='自定义类型':

        wbb = 'https://www.xvideos.com/?k='+entry.get()+'&p=' + str(page)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
        response = requests.get(wbb, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        return html
    elif combobox.get()=='系统类型':
        wbb = 'https://www.xvideos.com/c/' + entry.get() + "/" + str(page)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
        response = requests.get(wbb, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        return html
    else:
        tkinter.messagebox.showinfo('提示', '请选择系统类型或自定义类型!')


def shaixuan(html):  # 对源码进行筛选
    urls = re.findall('<div id=".*?" data-id="(.*?)" class="thumb-block ">', html, re.S)
    return urls

def liulan(str4):
    m=tkinter.filedialog.askdirectory()
    str4.set(m)
    return m

def close_windows(top):
    k = os.path.abspath(os.path.join(os.getcwd(), '..'))+'/image'
    if tkinter.messagebox.askokcancel('退出','确认要退出吗？'):
        ls = os.listdir(k)
        for i in ls:
            c_path = os.path.join(k, i)
            os.remove(c_path)
        top.destroy()


def get_photo(entry,entry1,entry2,entry3,str4,combobox,combobox1):
    if entry.get()!='' and entry1.get()!='' and entry2.get()!='' and entry3.get()!='' and str4.get()!='' and combobox.get()!='':
        top = Toplevel() #创建弹出式窗体
        top.title('爬取页面')
        top.geometry("350x540+360+200")
        top.resizable(0,0)
        k = os.path.abspath(os.path.join(os.getcwd(), '..'))
        decodepicture(k+'/image/b',b.img,'.ico')
        top.iconbitmap(k+'/image/b.ico')
        huabu = tkinter.Canvas(top, width=350, height=540)
        decodepicture(k+'/image/d',s.img,'.jpg')
        tupian = get_image(k+'/image/d.jpg', 350, 540)
        huabu.create_image(175, 270, image=tupian)
        huabu.pack()
        str1=StringVar()
        str2=StringVar()
        str3 = StringVar()
        lb = Label(top, text='视频爬取进度:')
        lb.place(x=10,y=180)
        p1 = ttk.Progressbar(top, length=200, cursor='spider',
                             mode="determinate",
                             orient=HORIZONTAL,
                             maximum=100
                             )
        p1.place(x=92,y=180)
        lb = Label(top, textvariable=str1)
        lb.place(x=10,y=100)
        lb = Label(top, textvariable=str2)
        lb.place(x=10,y=140)

        lb = Label(top, textvariable=str3)
        lb.place(x=295,y=180)

        p = int(entry1.get())
        count=0
        account=0
        for i in range(int(entry2.get()), int(entry3.get())):

                m = get_code(combobox,entry,i)

                pages = shaixuan(m)


                print("开始下载第" + str(i) + "页的视频！总共" + str(len(pages)) + '个!')
                print('\n')
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}

                for page in pages:
                    try:
                        p1["value"] = 0
                        wbb = 'https://www.xvideos.com/video' + page + '/'  # 获取包含视频播放链接的网页
                        response = requests.get(wbb, headers=headers)
                        response.encoding = 'utf-8'
                        html = response.text
                        if combobox1.get()=="高":
                            url = re.findall('html5player.setVideoUrlHigh\(\'(.*?)\'\);', html, re.S)[0]  # 获取视频播放链接
                        elif combobox1.get()=="低":
                            url = re.findall('html5player.setVideoUrlLow\(\'(.*?)\'\);', html, re.S)[0]
                        str1.set('正在爬取第%d个视频......' % p)
                        print('开始下载第' + str(p) + '个视频')

                        start = time.time()
                        size = 0
                        size1 = 0
                        response = requests.get(url, stream=True, headers=headers,timeout=5)

                        content_size = int(response.headers['content-length'])
                        chunk_size = 1024
                        if response.status_code == 200:
                            str2.set('[视频大小]:%0.2f MB' % (content_size / 1024 / 1024))
                            print('[文件大小]:%0.2f MB' % (content_size / 1024 / 1024))
                            with open(str4.get() + '\\' + str(p) + '.mp4', 'wb') as f:
                                for data in response.iter_content(chunk_size=chunk_size):
                                    f.write(data)
                                    size=len(data)
                                    size1 = size1 + len(data)
                                    c=size / content_size * 100
                                    d=size1 / content_size * 100
                                    p1["value"] = p1["value"] + c
                                    top.update()
                                    str3.set('%.2f%%' % d)
                                    print('\r' + '[下载进度]:%s%.2f%%' % (
                                        '■' * int(size1 * 50 / content_size), float(size1 / content_size * 100)), end='')
                        end = time.time()

                    except requests.exceptions.ConnectionError:

                        print("\n")
                        print("此视频下载出现异常，正在跳过………………")
                        print("\n")
                        count += 1
                        continue
                    except _tkinter.TclError:
                        account+=1
                        break
                    else:
                        print('\n' + '第' + str(p) + '个视频下载完成! 用时%.2f秒' % (end - start))
                        p+=1


                print('\n')
                print('第' + str(i) + '页的视频全部下载完成！')
                print('\n')
                if account != 0:
                     break

        if account!=0:
            tkinter.messagebox.showwarning('警告', '爬取已中断!!!')

        else:
            tkinter.messagebox.showinfo('提示!','全部视频已下载完成')
        print('全部视频已下载完成')

        top.mainloop()
    else:
        tkinter.messagebox.showwarning('警告!','文本框内容不能为空!')









