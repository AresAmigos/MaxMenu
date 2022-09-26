import os
import subprocess
import requests
from time import sleep
import sys
from colorama import Fore, Back, Style
from colorama import init

appdatar = os.environ["APPDATA"]
startup = appdatar + '\Microsoft\Windows\Start Menu\Programs\Startup'
filename = os.path.basename(__file__)
#C:\Users\free\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
darkness = subprocess.getoutput(f'if exist "{startup}\{filename}" (echo ok) else (echo no)')

if os.getcwd() != startup:
    if darkness == "no":
        choice = input("Do you want add this program to the startup? y/n ")
        if choice in ('y','Y','yes','Yes'):
            subprocess.getoutput(f'copy "{filename}" "{startup}\{filename}"/y')
            os.system('cls')
        else:
            os.system('cls')
init()
choicedcolor = Fore.RESET
#print(Fore.GREEN + "███╗░░░███╗░█████╗░██╗░░██╗      ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
#print("████╗░████║██╔══██╗╚██╗██╔╝      ████╗░████║██╔════╝████╗░██║██║░░░██║")
#print("██╔████╔██║███████║░╚███╔╝░      ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
#print("██║╚██╔╝██║██╔══██║░██╔██╗░      ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
#print("██║░╚═╝░██║██║░░██║██╔╝╚██╗      ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
#print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝      ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n" + Fore.RESET)


def after():
    sleep(1)
    os.system('cls')
def turnoff():
    subprocess.getoutput('shutdown /s /c "To the next time %username% :D" /t 5')
def reboot():
    subprocess.getoutput('shutdown /r /c "Rebooting system" /t 3')
def disconnect():
    subprocess.getoutput('shutdown/l')
def hibernation():
    subprocess.getoutput('shutdown/h')
def search():
    usersch = input("Enter here the words that you want search on google: ")
    research = 'https://www.google.com/search?q=' + usersch
    subprocess.getoutput(f'explorer "{research}"')
def linksearch():
    link = input("Enter here the link that you want search on google: ")
    subprocess.getoutput(f'explorer "{link}"')
def ifconfig():
    try:
        r = requests.get('https://ifconfig.me')
        print("\nYour public ip is: " + r.text)
    except:
        print("No internet connection")
def changepws():
    while True:
        admin = input("The file is open in admin mode? y/n ")
        if admin in ('n','N','NO','no','No'):
            print("Open the file in admin mode and retry")
            print("Open the cmd with admin permission and open this file")
            break
        elif admin in ('y','Y','Yes','yes','YES'):
            pw = input("Enter new password: ")
            try:
                subprocess.getoutput(f'net user %username% {pw}')
                break
            except:
                print("Error, open the file in admin mode and retry")
                break
        else:
            print("Enter only y or n")
def changewallpaper():
    admin = input("The file is open in admin mode? y/n ")
    if admin in ('n','N','NO','no','No'):
        print("Open the file in admin mode and retry")
        print("Open the cmd with admin permission and open this file")
        sleep(4)
        sys.exit()
    elif admin in ('y','Y','Yes','yes','YES'):
        wallpaper = input("Enter the image path: ")
        verify = subprocess.getoutput(f'if exist "{wallpaper}" (echo yes) else (echo no)')
        if verify == "no":
            print(Fore.RED + '\nError 404\nFile not found' + choicedcolor)
        elif verify == "yes":
            subprocess.getoutput(f'reg add "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "{wallpaper}" /f')
            subprocess.getoutput('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
            print("If it doesn't work reboot computer")
            dw = input("Reboot computer? y/n ")
            if dw in ('y','Y','Yes','yes'):
                subprocess.getoutput('shutdown -r -t 0')
            elif dw in ('n','N','no','No'):
                pass
            else:
                print('Unmatched answer')
def changecolor():
    color = int(input('1.BLACK, 2.RED, 3.GREEN, 4.YELLOW\n5.BLUE, 6.MAGENTA, 7.CYAN, 8.WHITE\n\nEnter number: '))
    global choicedcolor
    if color == 1:
        choicedcolor = Fore.BLACK
    elif color == 2:
        choicedcolor = Fore.RED
    elif color == 3:
        choicedcolor = Fore.GREEN
    elif color == 4:
        choicedcolor = Fore.YELLOW
    elif color == 5:
        choicedcolor = Fore.BLUE
    elif color == 6:
        choicedcolor = Fore.MAGENTA
    elif color == 7:
        choicedcolor = Fore.CYAN
    elif color == 8:
        choicedcolor = Fore.WHITE
    else:
        print(Fore.RED + 'Unmatched answer' + choicedcolor)
        sleep(0.7)
def removestup():
    darkness = subprocess.getoutput(f'if exist "{startup}\{filename}" (echo ok) else (echo no)')
    if darkness == 'no':
        print("This file isn't in startup")
        sleep(1)
    else:
        subprocess.getoutput(f'if exist "{startup}\{filename}" del "{startup}\{filename}"/q')
        print("File removed from startup")
        sleep(0.7)

while True:
    print(Fore.GREEN + "███╗░░░███╗░█████╗░██╗░░██╗      ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
    print("████╗░████║██╔══██╗╚██╗██╔╝      ████╗░████║██╔════╝████╗░██║██║░░░██║")
    print("██╔████╔██║███████║░╚███╔╝░      ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
    print("██║╚██╔╝██║██╔══██║░██╔██╗░      ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
    print("██║░╚═╝░██║██║░░██║██╔╝╚██╗      ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝      ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n" + choicedcolor)
    print(choicedcolor + "============ Max Menù for Windows ============")
    print("1.turn off pc                      2.reboot pc")
    print("3.disconnect user         4.hibernation of pc ")
    print("5.search on google               6.search link")
    print("7.show my ip                 8.change password")
    print("9.change wallpaper             10.change color")
    print("11.shell mode           12.remove from startup")

    c = input("\nEnter number function: ")
    
    if c == "exit":
        print("Goodbye!")
        input("Press any keys to exit...")
        sys.exit()
    elif c in ("cls","clear"):
        os.system('cls')
    if c == "1":
        turnoff()
        after()
    elif c == "2":
        reboot()
        after()
    elif c == "3":
        disconnect()
        after()
    elif c == "4":
        hibernation()
        after()
    elif c == "5":
        search()
        after()
    elif c == "6":
        linksearch()
        after()
    elif c == "7":
        ifconfig()
        after()
    elif c == "8":
        changepws()
        after()
    elif c == "9":
        changewallpaper()
        after()
    elif c == "10":
        changecolor()
        os.system('cls')
    elif c == "11":
        print('\n')
        while True:
            pwd = os.getcwd()
            command = input(pwd + '>')
            commands = command.split()
            if commands[0] in ('cd','chdir'):
                os.chdir(commands[1])
                print('\n')
            elif command == 'cd..':
                os.chdir('..')
                print('\n')
            elif command == 'exit':
                os.system('cls')
                break
            else:
                os.system(command)
    elif c == "12":
        removestup()
        os.system('cls')
