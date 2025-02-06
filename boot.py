import menu
import keyboard

menu.show_menu()  # Show the initial menu

while True:
    key = keyboard.get_pressed()
    if key:  # Only refresh if a key is pressed
        menu.navigate()
        menu.show_menu()