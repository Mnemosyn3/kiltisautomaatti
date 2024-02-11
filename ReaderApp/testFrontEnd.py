
import asyncio
import websockets


async def receiveTag():
    uri = "ws://localhost:8765"

    while True:
        async with websockets.connect(uri) as websocket: 
            

            tagNumber = await websocket.recv()

            print(tagNumber)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(receiveTag())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()