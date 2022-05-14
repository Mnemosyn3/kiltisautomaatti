import serial
try:
    ser = serial.Serial('/dev/ttyUSB0')
    ser.flushInput()

    tag = ""
    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
        except:
            print("Error reading from tag")
            
except:
    print("Could not connect to reader")
    


 