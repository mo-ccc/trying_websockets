import websockets
import asyncio

async def main(websocket, path):
    while True:
        msg = await websocket.recv()
        print(msg)
    
server = websockets.serve(main, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()