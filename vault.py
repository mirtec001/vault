from lock import Lock
from menu import Menu

def main():
    is_locked = True
    quit = False

    while not quit:
        if is_locked:
            is_locked = Lock().unlock()
        else:
            Menu().main_menu()
            menu_navigator = int(input(">> "))
            if menu_navigator == 1:
                Menu().view_vault()
            if menu_navigator == 2:
                Menu().add_item()
            if menu_navigator == 4:
                quit = True


if __name__ == "__main__":
    main()