
### Take a break ia a simple IDLE program which gives you the ability to take short breaks during your work hours.
### Although not being a gui app , it aims to teach beginners learn how to slwwp your programs and functionality to open web browsers.

import os
import webbrowser
import time

c = input("Please enter the number of times you want a break: ")
t = input("How many minute long sessions do you want: ")
n = input("How much long break do you want: ")

l = "http://www.youtube.com"
l= raw_input("Please enter the specific website url you want to visit during break(default: youtube)")

count = 0
print("This program started om" + time.ctime())
while(count < c):
    time.sleep(t*60)
    webbrowser.open(l)
    print("The time is" + time.ctime())
    time.sleep(n*60)
    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    count += 1

    
  
