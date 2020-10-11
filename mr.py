import win32gui
import win32con
import win32com.client
import win32api
import win32clipboard as w
from time import sleep
import random as rd
import jieba 
import time
handle = win32gui.FindWindow(None,"League of Legends") 
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()
def send():
    win32api.keybd_event(13,10,0,0)  #v键位码是86
    win32api.keybd_event(13,10,win32con.KEYEVENTF_KEYUP,0) #释放按键

    win32api.keybd_event(17,17,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,86,0,0)  #v键位码是86
    win32api.keybd_event(86,86,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,17,win32con.KEYEVENTF_KEYUP,0)
    
    win32api.keybd_event(13,10,0,0)  #v键位码是86
    win32api.keybd_event(13,10,win32con.KEYEVENTF_KEYUP,0) #释放按键
with open('c:/users/solaroven/desktop/mr.txt','r',encoding='utf-8') as f:
    text=f.read()

L=text.split('\n')

for i in L:
    l=jieba.cut(i)
    for j in l:
        #print(j)
        setText(j)
        time.sleep(rd.random())
        send()