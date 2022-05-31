import asyncio
import websockets

def man(socket):
    print(socket)
    # for message in socket:
    #     websockets.send(message)

# async def start():
#      async with websockets.serve(main, "localhost", 8080):
#         await asyncio.Future()  # run forever

clients = []

async def echo(websocket):
    if not websocket in clients:
        clients.append(websocket)
    async for message in websocket:
        for i in clients:
            await i.send(message)
        # await websocket.send(message)
        # print(message)

async def main():
    async with websockets.serve(echo, "localhost", 8080):
        await asyncio.Future()  # run forever
        # asyncio.run(main())



asyncio.run(main())
# asyncio.run(main())