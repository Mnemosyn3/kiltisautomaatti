from fastapi import FastAPI
from pydantic import BaseModel
import serial


class User(BaseModel):
    tagNumber: str
    name: str
    credits: float


def connectReader():
    try:
        global ser 
        ser = serial.Serial('/dev/ttyUSB0')
        ser.flushInput()
    except:
        print("Could not connect to serial interface.")

connectReader()
users = []

users.append(User(tagNumber='0010A007',name='Brian Kottarainen',credits='9000.9'))
#brian = User(tagNumber='0010A007',name='Brian Kottarainen',credits='9000.9')
#print(brian.tagNumber)

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
def user(tagNumber: str):
    for obj in users:
        if (obj.tagNumber == tagNumber):
            return{obj.tagNumber,obj.name,obj.credits}
    return{"User not found"}

@app.post("/newUser")
async def newUser(user:User):
    try:
        users.append(User(tagNumber=tagNumber,name=name,credits='0.0'))
        return 
    except:
        return "error"

@app.patch("/addCredits")
async def addCredits(tagNumber: str,credits: float):
    try:
        for obj in users:
            if obj.tagNumber == tagNumber:
                obj.credits = obj.credits + credits
                return obj.credits
        return "error"
    except:
        return "error"

@app.patch("/removeCredits")
async def addCredits(tagNumber: str,credits: float):
    try:
        for obj in users:
            if obj.tagNumber == tagNumber:
                obj.credits = obj.credits - credits
                return obj.credits
        return "error"
    except:
        return "error"