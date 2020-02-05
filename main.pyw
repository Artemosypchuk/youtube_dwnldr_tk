"""
Программа для скачки аудио, видео и плейлистов
с созданием папки для аудио и видео отдельно
возможна компиляция в ехе.
дорабатываем search =)
"""

from tkinter import *
import subprocess
import os
import youtube_dl as ydl
import colorama
from colorama import Fore, Back
colorama.init()


def dwl():
    try:
        os.chdir("dwn_video")
    except Exception as error:

        os.makedirs("dwn_video")
        os.chdir("dwn_video")

    os.system("youtube-dl " + message.get()+"/MIN")
    os.chdir("..")


def dwl_music():
    try:
        os.chdir("dwn_audio")
    except:
        os.mkdir("dwn_audio")
        os.chdir("dwn_audio")
    os.system("youtube-dl -x " + message.get())
    os.chdir("..")


def youtube_serch():
    # subprocess.call("youtube-dl --default-search " + message_search.get())
    pass


r = Tk()
message = StringVar()
message2 = StringVar()
message_search = StringVar()
Label(r, text='Your URL:').grid(row=0)
Label(r, text='SEARCH_YouTube:').grid(row=2)
e1 = Entry(r, textvariable=message)
e3 = Entry(r, textvariable=message_search)
e1.grid(row=0, column=2)
e3.grid(row=2, column=2)
r.title("SOME SHIT")
r.geometry("380x140")
frame = Frame(r)
frame.grid()
bottomframe = Frame(r)
bottomframe.grid(row=2)
redbutton = Button(frame, text='D_L_Video', fg='red', command=dwl)
redbutton.grid(row=1, column=1, padx=5)
bottomframe = Frame(r)
bottomframe.grid(row=2)
bluebutton = Button(frame, text='D_L_Audio', fg='blue', command=dwl_music)
bluebutton.grid(row=1, column=2, padx=5)
bottomframe = Frame(r)
bottomframe.grid(row=2)
bluebutton = Button(frame, text='SEARCH', bg='red', command=youtube_serch)
bluebutton.grid(row=1, column=3, padx=5)

r.mainloop()
