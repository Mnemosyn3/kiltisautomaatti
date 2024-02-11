import serial,websockets,asyncio



async def readTags(websocket):
    try:
        ser = serial.Serial('/dev/ttyUSB0')
        ser.flushInput()

        tag = ""
        while True:
            try:
                ser_bytes = ser.readline()
                decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                await websocket.send(decoded_bytes)
                print(decoded_bytes)
            except:
                await websocket.send("Error reading from tag")
                print("Error reading from tag")
            
    except:
        await websocket.send("Could not connect to reader")
        print("Could not connect to reader")


async def main():
    async with websockets.serve(readTags, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())