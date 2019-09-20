import serial
import time
import sys


def main():

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
        command = '\r\n\nen\nshow clock\n'.encode('utf-8')

        console.write(command)
        time.sleep(3)

        output = console.read(225).decode('utf-8')
        print(output)

if __name__ == "__main__":
    main()
