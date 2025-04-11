import serial

class CommunicationError(serial.SerialException):
    ... 

def read_temperature_celsius() -> float:
    try:
        ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)
        return float(ser.readline())
    
    except:
        raise CommunicationError
