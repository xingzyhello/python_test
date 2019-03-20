# 串口测试程序
import serial
from time import sleep

# serialport = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
# print(type(serial))
# help(serial.request)
# ser = serial.

# import
import serial

# ser = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)
ser = serial.Serial()
ser.port="COM4"
ser.open()
print(ser)
print(id(ser))
ser.baudrate = 115200
print(ser.isOpen())
print(ser)
ser.close()

# help(serial.SerialBase)