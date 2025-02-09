import websockets
import asyncio
from cryptography.fernet import Fernet

# Load secret key (must match the spaceship's key)
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)  # Create cipher for decryption

async def receive_encrypted_data(websocket, path):
    print("🛸 Alien server waiting for authentication...")

    token = await websocket.recv()

    if token != "trusted-spaceship-123":
        print("❌ Unauthorized spaceship detected! Connection closing.")
        await websocket.close()
        return

    print("✅ Trusted spaceship connected!")

    encrypted_data = await websocket.recv()  # Receive encrypted data
    decrypted_data = cipher.decrypt(encrypted_data).decode()  # Decrypt it

    print("Received decrypted planetary data:\n", decrypted_data)

start_server = websockets.serve(receive_encrypted_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
