import os

from serial import Serial, SerialException


def send_command(command: str) -> (int, str):
    try:
        with Serial(os.getenv('HDMI_MATRIX_DEVICE'), 57600, timeout=0.2) as ser:
            ser.write(f"{command}\r\n".encode())
            data = ser.readlines()
            decoded = [line.decode() for line in data]
            response = ''.join(decoded).strip()
            if response == 'CMD ERR':
                return 500, response
            return 200, response

    except SerialException as e:
        return 500, str(e)
