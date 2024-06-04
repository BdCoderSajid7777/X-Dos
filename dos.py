#!/bin/python
import os,sys,time
from DDos import checkUrl
from cfonts import render,say
logo=render("X-dos",colors=["white","black"],align="center")
os.system("clear")
print(logo)
print("_"*50)
while True:
    url=input("Enter url: ")
    if checkUrl(url):
        break
    else:
        print("url isn't formated correctly")
print("ATTACK STARTED CTRL+C TO STOP")
DDos(url)