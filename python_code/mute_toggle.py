import serial, os, time

# Use the confirmed port for your Arduino
SERIAL_PORT = "/dev/tty.usbmodem1101"
BAUD_RATE = 9600

def send_mute_shortcut():
    # Simulates Cmd+Shift+M (default mute/unmute shortcut for Teams)
    applescript_command = '''
    osascript -e 'tell application "System Events" to keystroke "m" using {command down, shift down}'
    '''
    os.system(applescript_command)

def main():
    # Open the serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Allow Arduino to reset
    print("Listening for TOGGLE_MUTE...")

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line == "TOGGLE_MUTE":
            print("TOGGLE_MUTE received. Triggering mute/unmute shortcut.")
            send_mute_shortcut()

if __name__ == "__main__":
    main()