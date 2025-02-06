from machine import Pin, SoftI2C
import time

import ssd1306

#iniciacja
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def BigTest():
    oled.fill(0)
    oled.fill_rect(0, 0, 32, 32, 1)
    oled.fill_rect(2, 2, 28, 28, 0)
    oled.vline(9, 8, 22, 1)
    oled.vline(16, 2, 22, 1)
    oled.vline(23, 8, 22, 1)
    oled.fill_rect(26, 24, 2, 4, 1)

    oled.text('MICROPYTHON', 40, 0, 1)
    oled.text('SSD1306', 40, 12, 1)
    oled.text('OLED 128x32', 40, 24, 1)
    oled.show()

def test():
    oled.text('Hello, World!', 0, 0, 1)
    oled.show()
    
def clear():
    """Clears the display."""
    oled.fill(0)
    oled.show()

def draw_text(x, y, text):
    """Displays text at the given position."""
    oled.text(text, x, y)
    oled.show()
    
