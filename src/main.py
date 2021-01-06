import websockets
import asyncio
import os
import json

async def main(websocket, path):
    if not os.path.exists("messages"):
        f = open("messages", "x")
        f.close()
    with open("messages", 'r') as f:
        await websocket.send(f.read())
    while True:
        msg = await websocket.recv()
        with open("messages", 'a') as f:
            f.write(json.dumps({"id": 1, "content": msg}))
    
server = websockets.serve(main, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()