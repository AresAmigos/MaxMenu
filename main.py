import os
import subprocess
import requests

print("███╗░░░███╗░█████╗░██╗░░██╗      ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
print("████╗░████║██╔══██╗╚██╗██╔╝      ████╗░████║██╔════╝████╗░██║██║░░░██║")
print("██╔████╔██║███████║░╚███╔╝░      ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
print("██║╚██╔╝██║██╔══██║░██╔██╗░      ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
print("██║░╚═╝░██║██║░░██║██╔╝╚██╗      ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝      ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n")

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
def ipconfig():
    try:
        r = requests.get('https://ifconfig.me')
        print("Your public ip is: " + r.text)
    except:
        print("No internet connection")
def changepws():
    while True:
        admin = input("The file is open in admin mode? y/n ")
        if admin == 'n':
            print("Open the file in admin mode and retry")
            print("Open the cmd with admin permission and open this file")
            break
        elif admin == 'y':
            pw = input("Enter new password: ")
            try:
                subprocess.getoutput(f'net user %username% {pw}')
                break
            except:
                print("Error, open the file in admin mode and retry")
                break
        else:
            print("Enter only y or n")

 
while True:
    print("============ Max Menù for Windows ============")
    print("1.turn off pc                      2.reboot pc")
    print("3.disconnect user         4.hibernation of pc ")
    print("5.search on google               6.search link")
    print("7.show my ip                 8.change password")

    c = input("\nEnter number function: ")
    
    if c == "exit" or c == "quit" or "break":
        print("Goodbye!")
        input("Press any keys to exit...")
        break
    elif c == "1":
        turnoff()
    elif c == "2":
        reboot()
    elif c == "3":
        disconnect()
    elif c == "4":
        hibernation()
    elif c == "5":
        search()
    elif c == "6":
        linksearch()
    elif c == "7":
        ipconfig()
    elif c == "8":
        changepws()
    print("\n")





