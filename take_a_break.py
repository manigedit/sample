
### Take a break ia a simple IDLE program which gives you the ability to take short breaks during your work hours.
### Although not being a gui app , it aims to teach beginners learn how to slwwp your programs and functionality to open web browsers.


import webbrowser
import time

count = 0
print("This program started om" + time.ctime())
while(count < 3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com.")
    print("the time is" + time.ctime())
    count += 1

    
  
