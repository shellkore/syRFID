#! /usr/bin/env python3
import serial
import csv
import sys
#excel stuff
#from time import gmtime, strftime
#resultFile=open('MyData.csv','wb')
#end excel stuff
 
def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( (i, s.portstr))
            s.close()   # explicit close 'cause of delayed GC in java
        except serial.SerialException:
            pass
    return available
if __name__=='__main__':
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        #print("connected to: " + ser.portstr)
    except serial.SerialException:
        pass
    while True:
        # Read a line and convert it from b'xxx\r\n' to xxx
        line = ser.readline()#.decode('utf-8')[:-1]
        line=str(line)
        #print('first time'+line)
        if line:  # If it isn't a blank line
            f = open('output.csv', 'w')   
            while True:
                # Read a line and convert it from b'xxx\r\n' to xxx
                line = ser.readline()#.decode('utf-8')
                line=str(line)
                if(line != "b''"):
                    print(line)
                if(line != "b''"):  # If it isn't a blank line
                     f.write(line[2:-5])
                     f.write('\n')
            f.close()
            #print(line)
            #with open('test.csv', 'w') as csv_file:
                  #  writer = csv.DictWriter(csv_file, fieldnames=['header1'], lineterminator='\n')
ser.close()
