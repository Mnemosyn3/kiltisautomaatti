from fastapi import FastAPI
import serial

class Customer:
    def __init__(self, tagNumber, name, credits):
        self.tagNumber = tagNumber
        self.name = name
        self.credits = credits
    
def connectReader():
    try:
        global ser 
        ser = serial.Serial('/dev/ttyUSB0')
        ser.flushInput()
    except:
        print("Could not connect to serial interface.")
connectReader()
customers = []

customers.append(Customer("0010A007","Brian Kottarainen",9000.9))

app = FastAPI()



@app.get("/getTagNumber")
def tagNumber():
    try:
            ser_bytes = ser.readline()
            decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            return{decoded_bytes}
    except:
        connectReader()
        print("Error reading from tag")
        return{"Error reading from tag"}

@app.get("/getUser")
def user(tagNumber= str):
    for obj in customers:
        if obj.tagNumber == tagNumber:
            return{obj.tagNumber,obj.name,obj.credits}
    return{"User not found"}

@app.post("/newUser")
async def newUser(tagNumber= str,name= str):
    try:
        customers.append(Customer(tagNumber,name,0.0))
        return 1
    except:
        return 0
