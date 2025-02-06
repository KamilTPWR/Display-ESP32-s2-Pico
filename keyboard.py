from machine import Pin

# Define buttons
buttons = {
    "UP": Pin(11, Pin.IN, Pin.PULL_UP),
    "RIGHT": Pin(12, Pin.IN, Pin.PULL_UP),
    "LEFT": Pin(13, Pin.IN, Pin.PULL_UP),
    "DOWN": Pin(14, Pin.IN, Pin.PULL_UP),
    "ACCEPT": Pin(15, Pin.IN, Pin.PULL_UP),
}

def get_pressed():
    """Returns the name of the pressed button or None."""
    for name, button in buttons.items():
        if button.value() == 0:  # Active LOW
            return name
    return None