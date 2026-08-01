from colorama import *
from database.user_repository import *
import os ,sys
def main(result= None ,value = None):
    while True :
        os.system("clear")
        title = "USER MANAGEMENT SYSTEM"
        print(Fore.BLUE ,f"""
        ============================
        =   {Fore.YELLOW}{title}{Fore.BLUE} =
        ============================\n
    {Fore.GREEN}[1.]{Fore.MAGENTA} Add User
    {Fore.GREEN}[2.]{Fore.MAGENTA} Show Users
    {Fore.GREEN}[3.]{Fore.MAGENTA} Update User
    {Fore.GREEN}[4.]{Fore.MAGENTA} Delete User
    {Fore.GREEN}[5.]{Fore.MAGENTA} Login
    {Fore.GREEN}[6.]{Fore.MAGENTA} Create Table
    {Fore.GREEN}[7.]{Fore.MAGENTA} Exit
    """)
        if value == False :
            print(Fore.RED ,"input filed select number (1 => 7)\n")
            value = True
        if result is not None :
            print(Fore.GREEN ,f"Result: {Fore.WHITE}{result}\n")
            result = None
        select = input(Fore.CYAN + "    Select an option: ")
        if select =="1" :
            os.system('clear')
            result = add_users()
        elif select =="2" :
            result= show_users()
        elif select =="3" :
            result = update_users()
        elif select == "4" :
            result = delete_users()
        elif select == "5":
            result = login()
        elif select == "6":
            result=create_table()
        elif select == "7":
            statu = "exit"
            print(Fore.RED + "Exiting the program...")
            sys.exit()
        else :
            value=False
main()