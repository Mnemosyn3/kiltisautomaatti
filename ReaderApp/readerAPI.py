from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import serial


class User(BaseModel):
    tagNumber: str
    name: str
    credits: float


def connectReader():
    global ser 
    ser = serial.Serial('/dev/ttyUSB0')
    ser.flushInput()


connectReader()
users = []

users.append(User(tagNumber='0010A007',name='Brian Kottarainen',credits='9000.9'))
#brian = User(tagNumber='0010A007',name='Brian Kottarainen',credits='9000.9')
#print(brian.tagNumber)

app = FastAPI()


#Pretty self evident, returns the number of the next tag, that is read.

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

#returns the user assiciated with the tagNumber as a JSON object.

@app.get("/getUser")
def user(tagNumber: str):
    for obj in users:
        if (obj.tagNumber == tagNumber):
            return jsonable_encoder(obj)
    return{"User not found"}

#Creates a new user, takes JSON object as a input.

@app.post("/newUser")
async def newUser(user:User):
    try:
        users.append(user)
        return user
    except:
        return {"error"}

#Updates the credits of the user, takes JSON object as a input.

@app.patch("/updateCredits")
async def updateCredits(user:User):
    try:
        for obj in users:
            if obj.tagNumber == user.tagNumber:
                obj.credits = user.credits
                return obj.credits
        return "error"
    except:
        return "error"

