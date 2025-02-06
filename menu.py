import display
import keyboard

menu_items = ["Start Game", "Settings", "Exit"]
selected_index = 0

def show_menu():
    """Displays the menu on the screen."""
    display.clear()
    for i, item in enumerate(menu_items):
        prefix = ">" if i == selected_index else " "
        display.draw_text(0, i * 10, f"{prefix} {item}")

def navigate():
    """Handles menu navigation."""
    global selected_index
    key = keyboard.get_pressed()
    
    if key == "UP":
        selected_index = (selected_index - 1) % len(menu_items)
    elif key == "DOWN":
        selected_index = (selected_index + 1) % len(menu_items)
    elif key == "ACCEPT":
        execute_option()

def execute_option():
    """Executes the selected menu option."""
    global selected_index
    if menu_items[selected_index] == "Exit":
        display.draw_text(0, 20, "Goodbye!")