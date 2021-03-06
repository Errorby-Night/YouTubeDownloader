import pytube as pyt
import time
import os
from src import printcolors as pc
from src import ascii

def downloader():
    link = str(input("Enter the YouTube link:\n"))
    url = pyt.YouTube(link)
    print("Accessing file", end = '')
    for i in range(3):
        time.sleep(1)
        print(".", end = '')
    video = url.streams.get_highest_resolution().download()
    print("\nStarting Download", end = '')
    for i in range(3):
        print('.', end = '')
        time.sleep(1)
    print("\n")
    for i in range(10):
        print("=", end='')
        time.sleep(1)
    if(os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")
    title = url.title
    print("\n")
    print(title, end='')
    print(" is finished being downloaded.\n")
    time.sleep(5)

def mainitis():
    pc.printout(ascii.ascii_art, pc.YELLOW)
    print("\n")
    a = True
    while(a):
        downloader()
        if(os.name == "posix"):
            os.system("clear")
        else:
            os.system("cls")
        choice = input(str("Do you wish to continue?(Y/N):"))
        if(choice == 'N' or choice == 'n'):
            a = False
mainitis()
