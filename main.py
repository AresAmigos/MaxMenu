import os
import subprocess
import requests
from time import sleep
import sys
from colorama import Fore, Back, Style
from colorama import init


subprocess.getoutput('if not exist "%appdata%\MaxMenu" md "%appdata%\MaxMenu"')
subprocess.getoutput('attrib +h "%appdata%\MaxMenu"')
    

appdatar = os.environ["APPDATA"]
systemdrive = os.environ["SYSTEMDRIVE"]
startup = appdatar + '\Microsoft\Windows\Start Menu\Programs\Startup'
filename = os.path.basename(__file__)
darkness = subprocess.getoutput(f'if exist "{startup}\{filename}" (echo ok) else (echo no)')



porta = subprocess.getoutput('if exist "%appdata%\MaxMenu\password.txt" echo lol')
if porta == 'lol':
    pwcrypted = open(appdatar + '\MaxMenu\password.txt',"r")
    pwdelcazzo = (pwcrypted.read())
    pwcrypted.close()
    if len(pwdelcazzo) > 0:
        auth = input('Enter the password: ')
        if auth != pwdelcazzo:
            if auth != 'exit':  
                print('\nEnter "exit" to exit')
        while auth != pwdelcazzo:
            if auth == 'exit':
                pwcrypted.close()
                sys.exit()
            auth = input('\nWrong password.\nEnter the password: ')
        os.system('cls')

superverify = subprocess.getoutput('if not exist "%appdata%\MaxMenu\startupverify.txt" echo no')
if superverify == 'no':
    subprocess.getoutput('type nul > "%appdata%\MaxMenu\startupverify.txt"')
    startupverifyinit = open(appdatar + '\MaxMenu\startupverify.txt',"w")
    startupverifyinit.write('enabled')
    startupverifyinit.close()
    startupconfirmed = 'enable ask to add this to the startup'
startupverify = open(appdatar + '\MaxMenu\startupverify.txt',"r")
startupverifytext = (startupverify.read())
startupverify.close()
if True:
    if startupverifytext == 'enabled': 
        startupconfirmed = 'disable ask to add this to the startup'
        if os.getcwd() != startup:
            if darkness == "no":
                choice = input("Do you want add this program to the startup? y/n ")
                if choice in ('y','Y','yes','Yes'):
                    subprocess.getoutput(f'copy "{filename}" "{startup}\{filename}"/y')
                    os.system('cls')
                else:
                    os.system('cls')
    elif startupverifytext == 'disabled':
        startupconfirmed = 'enable ask to add this to the startup'
    else:
        startupverifyerror = open(appdatar + '\MaxMenu\startupverify.txt',"w")
        startupverifyerror.write('disabled')
        startupverifyerror.close()
        startupconfirmed = 'enable ask to add this to the startup'
        


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
        print("This file isn't in the startup")
        sleep(1.2)
    else:
        subprocess.getoutput(f'if exist "{startup}\{filename}" del "{startup}\{filename}"/q')
        print("File removed from the startup")
        sleep(1)
def lock():
    lockverify = subprocess.getoutput('if not exist "%appdata%\MaxMenu\password.txt" (echo no) else (echo oc)')
    if lockverify == 'no':
        subprocess.getoutput('md "%appdata%\MaxMenu"')
        subprocess.getoutput('attrib +h "%appdata%\MaxMenu"')
        subprocess.getoutput('type nul > "%appdata%\MaxMenu\password.txt"')
        subprocess.getoutput('attrib +h "%appdata%\MaxMenu\password.txt"')
        password = input('Enter a password: ')
        while password == 'exit':
            print('\nPassword cannot be "exit"')
            password = input('\nEnter a password: ')
        lockpw = open(appdatar + '\MaxMenu\password.txt',"w")
        lockpw.write(password)
        lockpw.close()
    elif lockverify == 'oc':
        pwcrypted = open(appdatar + '\MaxMenu\password.txt',"r")
        pwdelcazzo = (pwcrypted.read())
        pwcrypted.close()
        if len(pwdelcazzo) == 0:
            subprocess.getoutput('if not exist "%appdata%\MaxMenu" md "%appdata%\MaxMenu"')
            subprocess.getoutput('attrib +h "%appdata%\MaxMenu"')
            subprocess.getoutput('type nul > "%appdata%\MaxMenu\password.txt"')
            subprocess.getoutput('attrib + h "%appdata%\MaxMenu\password.txt"')
            pwcrypted = open(appdatar + '\MaxMenu\password.txt',"r")
            pwdelcazzo = (pwcrypted.read())
            pwcrypted.close()
            password = input('Enter a password: ')
            while password == 'exit':
                print('\nPassword cannot be "exit"')
                password = input('\nEnter a password: ')
            lockpw = open(appdatar + '\MaxMenu\password.txt',"w")
            lockpw.write(password)
            lockpw.close()
    else:
        oldpassword = input('Enter the old password: ')
        pwcrypted = open(appdatar + '\MaxMenu\password.txt',"r")
        pwdelcazzo = (pwcrypted.read())
        pwcrypted.close()
        if oldpassword != pwdelcazzo:
            if oldpassword != 'exit':
                print('\nEnter "exit" to exit')
        while oldpassword != pwdelcazzo:
            if oldpassword == 'exit':
                pwcrypted.close()
                break
            oldpassword = input('\nYou have entered a wrong password.\nEnter the old password: ')
        if oldpassword != 'exit':
            newpassword = input('Enter new password: ')
            while newpassword == 'exit':
                print('\nPassword cannot be "exit"')
                newpassword = input('\nEnter a password: ')
            lockpw = open(appdatar + '\MaxMenu\password.txt',"w")
            lockpw.write(newpassword)
            lockpw.close()
def unlock():
    oldpassword = input('Enter the old password: ')
    pwcrypted = open(appdatar + '\MaxMenu\password.txt',"r")
    pwdelcazzo = (pwcrypted.read())
    pwcrypted.close()
    if oldpassword != pwdelcazzo:
        if oldpassword != 'exit':
            print('\nEnter "exit" to exit')
    while oldpassword != pwdelcazzo:
        if oldpassword == 'exit':
            break
        oldpassword = input('\nWrong password.\nEnter the old password: ')
    if oldpassword != 'exit':
        lockpw = open(appdatar + '\MaxMenu\password.txt',"w")
        lockpw.write('')
        lockpw.close()
def addremove():
    global startupconfirmed
    startupverify = open(appdatar + '\MaxMenu\startupverify.txt',"r")
    startupverifytext = (startupverify.read())
    startupverify.close()
    if startupverifytext == 'enabled':
        startupverify.close()
        startupverifyerror = open(appdatar + '\MaxMenu\startupverify.txt',"w")
        startupverifyerror.write('disabled')
        startupverifyerror.close()
        startupconfirmed = 'enabled ask to add this to the startup'
    elif startupverifytext == 'disabled':
        startupverify.close()
        startupverifyerror = open(appdatar + '\MaxMenu\startupverify.txt',"w")
        startupverifyerror.write('enabled')
        startupverifyerror.close()
        startupconfirmed = 'disabled ask to add this to the startup'


        
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
    print("13.lock this file          14.unlock this file")
    print(f"15.{startupconfirmed}                        ")

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
    elif c == "13":
        lock()
        after()
    elif c == "14":
        unlock()
        after()
    elif c == "15":
        addremove()
        after()
        
