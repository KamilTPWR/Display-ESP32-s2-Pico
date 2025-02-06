# ESP32-S2 Pico Menu System

This repository contains the code for a simple menu system built for the ESP32-S2 Pico with a 128x32 OLED display (SSD1306) and a keypad. The system allows for the display of a menu, navigation through the options using the keypad, and execution of various applications (with the potential to add more later).

## Project Structure

The project is organized into the following files and folders:

## Files

### `boot.py`
- **Purpose**: This is the main entry point of the system. It initializes the menu system and constantly checks for button presses to navigate through the menu.
- **Key Features**:
  - Shows the initial menu.
  - Calls the `menu.show_menu()` to refresh the display only when a button is pressed.

### `menu.py`
- **Purpose**: Contains logic for displaying and navigating through the menu options.
- **Key Features**:
  - Handles navigation between menu items.
  - Displays the menu options on the OLED screen.
  - Can be extended to support more applications in the future.

### `display.py`
- **Purpose**: Handles all interactions with the OLED screen, including initialization and drawing text.
- **Key Features**:
  - Initializes the I2C connection with the OLED display (using pins 8 and 9 for SDA and SCL).
  - Provides utility functions to clear the display and draw text.

### `keyboard.py`
- **Purpose**: Manages the keypad button inputs.
- **Key Features**:
  - Allows easy addition of more buttons or key mappings.

## Setup

### Requirements
- **Hardware**:
  - ESP32-S2 Pico
  - Keypad with buttons mapped to the following pins:
    - UP: 11
    - RIGHT: 12
    - LEFT: 13
    - DOWN: 14
    - ACCEPT: 15

- **Software**:
  - MicroPython firmware installed on the [ESP32-S2 Pico](https://micropython.org/download/LOLIN_S2_PICO/).
  - SSD1306 library for MicroPython (for OLED display handling).

### Installation Steps
   
1. **Upload Code**:
   - Use a tool like [Thonny](https://thonny.org/) to upload the code files (`boot.py`, `menu.py`, `display.py`, `keyboard.py`) to your ESP32-S2 Pico.

2. **Run the System**:
   - Once the files are uploaded, restart the ESP32-S2 Pico. The menu system should appear on the OLED display, and you can navigate using the keypad buttons.

## Usage

- On startup, the menu will be displayed on the OLED screen.
- Navigate through the menu using the UP, DOWN, LEFT, and RIGHT buttons.
- Select an option using the ACCEPT button.
- Pressing any button will refresh the menu.

## Future Development

- New applications (like Snake or Lights Out) may be added inside the `/apps/` folder.
- The menu system can be expanded to support more features or customization.

## Acknowledgements

- SSD1306 driver for MicroPython.
- ESP32-S2 Pico microcontroller.
- MicroPython community.
