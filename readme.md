# Mic Mute/Unmute Button with Arduino and Python

A physical button using an Arduino Nano Every and Python to toggle microphone mute/unmute on macOS. The button sends serial signals processed by a Python script to control the mic in applications like Microsoft Teams, even when not in focus.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup Instructions](#setup-instructions)
  - [Hardware Setup](#hardware-setup)
  - [Arduino Code](#arduino-code)
  - [Python Script](#python-script)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Introduction

This project allows you to use a physical button to mute and unmute your microphone on a macOS system. It's particularly useful during online meetings and calls, providing a quick and tactile way to control your mic without fumbling through software controls.

---

## Features

- **Physical Control**: Use a hardware button to toggle mute/unmute.
- **Arduino Integration**: Detects button presses and communicates with your Mac.
- **Python Script**: Listens for signals and triggers the mute/unmute action.
- **Application Compatibility**: Works with Microsoft Teams and other apps via system-level shortcuts.
- **Extensibility**: Can be enhanced with LEDs, wireless functionality, and more.

---

## Hardware Requirements

- **Arduino Nano Every** (with headers)
- **Momentary Push Button** (e.g., 12mm 2A 12V/24V/125V/250V AC Prewired Waterproof Push Button)
- **Breadboard**
- **Male-to-Male Jumper Wires**
- **USB Cable** (compatible with Arduino Nano Every)
- **MacBook Pro** (or any macOS system)

---

## Software Requirements

- **Arduino IDE 2.x**
- **Python 3.x**
- **PySerial Library**
- **SwitchAudioSource** (optional, for system-wide mute)

---

## Setup Instructions

### Hardware Setup

1. **Wiring the Button:**

   - Connect the **black wire** (or one terminal) of the button to the **GND** pin on the Arduino.
   - Connect the **red wire** (or the other terminal) of the button to **Digital Pin 2 (D2)** on the Arduino.

2. **Using the Breadboard:**

   - Place the Arduino Nano Every onto the breadboard.
   - Use jumper wires to make the connections if the button wires are not long enough.

3. **Connect the Arduino to Your Mac:**

   - Use the USB cable to connect the Arduino to your MacBook Pro.

### Arduino Code

1. **Install Arduino IDE:**

   - Download and install from [Arduino's official website](https://www.arduino.cc/en/software).

2. **Load the Arduino Sketch:**

   - Open the `mute_toggle.ino` file located in the `arduino_code/` folder.

3. **Select the Board and Port:**

   - Go to **Tools > Board > Arduino AVR Boards > Arduino Nano Every**.
   - Go to **Tools > Port** and select the port corresponding to your Arduino (e.g., `/dev/tty.usbmodem1101`).

4. **Upload the Code:**

   - Click the **Upload** button to transfer the code to your Arduino.

### Python Script

1. **Install Python 3.x:**

   - macOS usually comes with Python 3.x installed. Verify by running `python3 --version` in Terminal.

2. **Install PySerial:**

   ```bash
   python3 -m pip install pyserial
   ```

3. **Install SwitchAudioSource (Optional):**

   - Install Homebrew if not already installed:

     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   - Install SwitchAudioSource:

     ```bash
     brew install switchaudio-osx
     ```

4. **Configure the Python Script:**

   - Open `mute_toggle.py` located in the `python_code/` folder.
   - Update the `SERIAL_PORT` variable with your Arduino's serial port (e.g., `/dev/tty.usbmodem1101`).

5. **Run the Python Script:**

   ```bash
   python3 mute_toggle.py
   ```

---

## How It Works

- **Arduino Side:**

  - The Arduino detects button presses using a digital input pin with an internal pull-up resistor.
  - When the button is pressed and released, the Arduino sends the string `"TOGGLE_MUTE"` over the serial connection.

- **Python Side:**

  - The Python script listens to the serial port for the `"TOGGLE_MUTE"` message.
  - Upon receiving it, the script executes an AppleScript command to simulate the mute/unmute keyboard shortcut.

---

## Usage

1. **Start the Python Script:**

   - Run `python3 mute_toggle.py` in Terminal.

2. **Open Your Communication App:**

   - Launch Microsoft Teams or any other app you wish to control.

3. **Press the Button:**

   - Each press toggles the mute/unmute state of your microphone.

4. **Background Operation:**

   - Optionally, configure the script to control the system-wide microphone mute state, allowing you to switch windows without losing control.

---

## Acknowledgments

This project was developed with the assistance of **ChatGPT**. ChatGPT provided guidance on:
- Debugging Arduino code for button press detection.
- Developing a Python script for serial communication and system-level mute control.
- Structuring the repository and writing comprehensive documentation.

Its insights helped streamline the process and bring this project to life efficiently.

---

## Troubleshooting

- **Serial Port Busy Error:**

  - Make sure the Arduino Serial Monitor is closed before running the Python script.

- **Permission Issues:**

  - Grant Terminal or your Python environment Accessibility permissions:

    - Go to **System Settings > Privacy & Security > Accessibility**.
    - Add Terminal and enable it.

- **Incorrect Shortcut:**

  - Ensure the keyboard shortcut matches the one used by your communication app.
  - Modify the AppleScript command in `mute_toggle.py` if necessary.

- **Button Not Detected:**

  - Verify the wiring connections between the button and the Arduino.
  - Use the Arduino Serial Monitor to test button presses independently.

---

## Future Enhancements

- **System-Wide Mute Control:**

  - Implement system-level microphone control to work across all applications.

- **LED Indicator:**

  - Add an LED to display the current mute status.

- **Wireless Functionality:**

  - Upgrade to a wireless solution using Bluetooth or Wi-Fi.

- **Enclosure Design:**

  - Create a custom enclosure for a polished look.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

*Created by Matias Stephens* 