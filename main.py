import os,requests,json,colorama,time,pystyle,sys
from secrets import choice
from colorama import Fore, Back, Style
from time import sleep
from pystyle import *

os.system("mode con cols=79 lines=20")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



banner1 = """
                        ╔╦╗┌─┐┌┬┐┌─┐┬┌┐┌  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
                         ║║│ ││││├─┤││││  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
                        ═╩╝└─┘┴ ┴┴ ┴┴┘└┘  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─                                                                                                      
"""

maininfo = """
                         ╔═════════════════════════════════════════╗
                                    Domain Scraper
                            This Was Made For Educational Purpose
                            
                            Discord: pick#1086
                            
                            Tiktok : @pick
                                 
                         ╚═════════════════════════════════════════╝   


"""


print(Fore.CYAN+banner1)
print(Fore.LIGHTGREEN_EX+maininfo)

def main():
    choice = "0"
    while choice =="0":
        print(Fore.LIGHTGREEN_EX+"\n[1] Scraper")
        print("[2] Exit")
        choice = input(Fore.LIGHTMAGENTA_EX+">  ")
        if choice == "1":
            scraper()
        elif choice == "2":
            sys.exit()



def scraper():
    os.system("mode con cols=98 lines=20")
    session = requests.session()
    print(Fore.LIGHTGREEN_EX+f"{banner1}")
    print(Fore.LIGHTMAGENTA_EX+f"{maininfo}")
    inip = input('Enter URL or IP: ')
    print("\n=========== Output ===============")
    api = "http://api.hackertarget.com/reverseiplookup/?q="
    apipun = api + inip
    output = session.get(apipun).text
    print(output)
    file = input("Save output to txt? [Y/n]").lower()
    if file == 'y':
        fila = input("\nFilename: ")
        filename = fila + ".txt"
        file1 = open(filename, "w")
        file1.write(str(output))
    else:
        print("\nThank for using my tool !")
        
    
main()
