import websockets
import asyncio
from cryptography.fernet import Fernet

# Load secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)  # Create cipher for encryption

async def send_encrypted_data():
    with open("unvisited_planets.csv", "r") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data.encode())  # Encrypt data

    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("trusted-spaceship-123")  # Send auth token
        auth_response = await websocket.recv()

        if auth_response != "✅ Trusted spaceship connected!":
            print("❌ Access denied! Mission aborted.")
            return

        await websocket.send(encrypted_data)  # Send encrypted data
        print("🚀 Encrypted planetary data sent!")

asyncio.run(send_encrypted_data())
