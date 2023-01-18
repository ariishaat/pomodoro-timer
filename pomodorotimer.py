import os
import time

def convertTosec(t):
    return t * 60

def timer(t, label):
    
    while t:
        min, sec = divmod(t, 60) #min = t//60, sec = t%60
        print(f"{label}: {min:02d}:{sec:02d}", end="\r")
        time.sleep(1)
        t -= 1


def pomodoro (task, shortRest, longRest):
    t = convertTosec(task)
    sr = convertTosec(shortRest)
    lr = convertTosec(longRest)
    timer(t, "Task")   
    os.system("clear||cls")
    timer(sr, "Short Break")
    os.system("clear||cls")
    timer(t, "Task")
    os.system("clear||cls")
    timer(sr, "Short Break")
    os.system("clear||cls")
    timer(t, "Task")
    os.system("clear||cls")
    timer(sr, "Short Break")
    os.system("clear||cls")
    timer(lr, "Long break")
    timer(t, "Task")
    os.system("clear||cls")

task = int(input("Enter task time (in mins): "))
shortRest = int(input("Enter short break time (in mins): "))
longRest = int(input("Enter long break time (in mins): "))


pomodoro (task, shortRest, longRest)