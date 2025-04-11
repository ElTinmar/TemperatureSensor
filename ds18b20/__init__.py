import serial

class CommunicationError(Exception):
    ... 

def read_temperature_celsius(port: str = '/dev/ttyUSB0') -> float:
    
    try:
        ser = serial.Serial(port, baudrate = 9600)
        return float(ser.readline())
    
    except Exception as e:
        raise CommunicationError('Temperature sensor error') from e
