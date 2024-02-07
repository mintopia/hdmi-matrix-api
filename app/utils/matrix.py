import os

from serial import Serial, SerialException


def send_command(command: str) -> (int, str):
    try:
        device = os.getenv('HDMI_MATRIX_DEVICE')
        timeout = float(os.getenv('HDMI_MATRIX_TIMEOUT')) 
        with Serial(device, 57600, timeout=timeout) as ser:
            ser.write(f"{command}\r\n".encode())
            data = ser.readlines()
            decoded = [line.decode() for line in data]
            response = ''.join(decoded).strip()
            if response == 'CMD ERR':
                return 500, response
            return 200, response

    except SerialException as e:
        return 500, str(e)
