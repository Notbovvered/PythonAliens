import websockets
import asyncio

# Secret token (only trusted ships know this!)
SECRET_TOKEN = "trusted-spaceship-123"


async def receive_planet_data(websocket, path):
    print("🛸 Alien server waiting for authentication...")

    # Step 1: Receive the first message (should be the secret token)
    token = await websocket.recv()

    if token != SECRET_TOKEN:
        print("❌ Unauthorized spaceship detected! Connection closing.")
        await websocket.close()  # Reject connection
        return

    print("✅ Trusted spaceship connected!")

    # Step 2: Receive planetary data after authentication
    data = await websocket.recv()
    print("Received planetary data:\n", data)


# Start secure WebSocket server
start_server = websockets.serve(receive_planet_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
