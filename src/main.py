import websockets
import asyncio
import os
import json
import boto3
import boto3.dynamodb.conditions as dynamodb
import sys
import uuid
from datetime import datetime

client = boto3.resource('dynamodb')
table = client.Table('websockets_messaging_app')
if not table:
    print("table not found")
    sys.exit(1)

async def main(websocket, path):
    print("user connected")
    old_messages = table.scan(Limit=10)["Items"]
    await websocket.send(json.dumps(old_messages))
    while True:
        msg = await websocket.recv()
        new_item = {"message_id": str(uuid.uuid4()), "content": msg, "timestamp": str(datetime.utcnow())}
        table.put_item(
            Item = new_item
        )
        await websocket.send(json.dumps(new_item))

    
server = websockets.serve(main, "0.0.0.0", 8080)
print("server")
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()