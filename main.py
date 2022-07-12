import pytube as pyt
import time
import os
from sqlalchemy import false, true
from src import printcolors as pc
from src import artwork

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

def mainitis():
    pc.printout(artwork.ascii_art, pc.YELLOW)
    print("\n")
    a = true
    while(a):
        downloader()
        if(os.name == "posix"):
            os.system("clear")
        else:
            os.system("cls")
        choice = input(str("Do you wish to continue?(Y/N):"))
        if(choice == 'N' or choice == 'n'):
            a = false
