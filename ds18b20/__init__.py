import serial

class CommunicationError(Exception):
    ... 

def read_temperature_celsius(port: str = '/dev/ttyUSB0', timeout: float = 2) -> float:
    
    try:
        with serial.Serial(port, baudrate = 9600, timeout=timeout) as ser:
            return float(ser.readline())
    
    except Exception as e:
        raise CommunicationError('Temperature sensor error') from e
