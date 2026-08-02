from colorama import *
from database.user_repository import *
import  sys ,os
import pyfiglet

init(autoreset=True)


def print_signature():
    """Displays the programmer's name as decorated ASCII art."""
    print(Fore.GREEN + Style.BRIGHT + " " * 2 + "◆ Developed by ABDELADIME LAHROUR ◆\n".center(60))


def print_menu():
    title = "User Management System"
    width = 50

    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * width + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + title.center(width) + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * width + "╝\n")

    options = [
        ("1", "Add User"),
        ("2", "Show Users"),
        ("3", "Update User"),
        ("4", "Delete User"),
        ("5", "Login"),
        ("6", "Create Table"),
        ("7" ,"Drop Table"),
        ("8", "Exit"),
    ]

    for num, label in options:
        print(f"  {Fore.GREEN}[{num}]{Style.RESET_ALL} {Fore.MAGENTA}{label}")

    print(Fore.CYAN + "─" * (width + 2))


def main(result=None, value=None):
    while True:
        os.system("clear")
        print_signature()
        print_menu()

        if value is False:
            print(Fore.RED + "⚠  Please select a valid number (1 => 7)\n")
            value = True

        if result is not None:
            print(Fore.GREEN + f"✔ Result: {Fore.WHITE}{result}\n")
            result = None

        select = input(Fore.CYAN + Style.BRIGHT + "  ➤ Select an option: " + Style.RESET_ALL)

        if select == "1":
            result = add_users()
        elif select == "2":
            result = show_users()
        elif select == "3":
            result = update_users()
        elif select == "4":
            result = delete_users()
        elif select == "5":
            result = login()
        elif select == "6":
            result = create_table()
        elif select == "7":
            result=delet_table()
        elif select == "8":
            result =close_db()
            print(Fore.RED + Style.BRIGHT + "\n  Exiting the program... 👋")
            sys.exit()
        else:
            value = False


if __name__ == "__main__":
    main()