import asyncio
import random
import json
from aiocoap import Context, Message, POST

async def simulate_sensor_data():
    """Simulate sensor data and send it via CoAP."""
    protocol = await Context.create_client_context()

    while True:
        # Generate random sensor readings
        temperature = round(random.uniform(20.0, 25.0), 2)
        humidity = round(random.uniform(30.0, 50.0), 2)
        payload = json.dumps({"temperature": temperature, "humidity": humidity}).encode('utf-8')

        # Create and send CoAP request
        request = Message(code=POST, payload=payload)
        request.set_request_uri('coap://localhost:5683/sensor/data')  # ✅ Make sure this matches server path

        try:
            response = await protocol.request(request).response
            print(f"Result: {response.code}\nPayload: {response.payload.decode('utf-8')}")
        except Exception as e:
            print(f"Failed to send request: {e}")

        await asyncio.sleep(1)

# Run the async function
if __name__ == "__main__":
    asyncio.run(simulate_sensor_data())
