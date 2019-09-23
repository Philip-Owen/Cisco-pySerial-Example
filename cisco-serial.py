import serial
import time
import sys


def main():

    commands = input("Enter the commands to run separated by commas > ")
    commands = commands.replace(',', '\n\n') + '\n'

    # Try to establish console connection with the device.
    try:
        console = serial.Serial(
            port='COM5',
            baudrate=9600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=8
        )

    # If there is an exception, print the error and exit the program.
    except serial.serialutil.SerialException as e:
        print('Error connecting to device...', e)
        sys.exit()

    # If there is no exception, run commands and print the output.
    else:
        commands_to_run = f'\r\n\nen\n{commands}'.encode('utf-8')

        console.write(commands_to_run)
        time.sleep(3)

        while console.inWaiting() > 0:
            output = console.read(console.inWaiting()).decode('utf-8')
            time.sleep(1)
            print(output)

if __name__ == "__main__":
    main()
