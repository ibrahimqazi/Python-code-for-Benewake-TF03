# -*- coding: utf-8 -*
# This script for Linux environment
import time
import serial
# Checked with TF03,

# ser = serial.Serial("/dev/ttyUSB1", 115200)
ser = serial.Serial("/dev/ttyAMA0", 115200)
# ser = serial.Serial("/dev/tty0", 115200)
# ser = serial.Serial("COM12", 115200)


def read_data():
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9)
            ser.reset_input_buffer()

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # this portion is for python3
                print("Printing python3 portion")            
                distance = bytes_serial[2] + bytes_serial[3]*256
                print("Distance:"+ str(distance))
                ser.reset_input_buffer()

            if bytes_serial[0] == "Y" and bytes_serial[1] == "Y":
                distL = int(bytes_serial[2].encode("hex"), 16)
                distH = int(bytes_serial[3].encode("hex"), 16)
                distance = distL + distH*256
                print("Printing python2 portion")
                print("Distance:"+ str(distance) + "\n")
                ser.reset_input_buffer()


if __name__ == "__main__":
    try:
        if ser.isOpen() == False:
            ser.open()
        read_data()
    except KeyboardInterrupt(): # ctrl + c in terminal.
        if ser != None:
            ser.close()
            print("program interrupted by the user")


