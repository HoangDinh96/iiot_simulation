import asyncio
import random
from asyncua import ua, Server

async def main():
    """Initialize and run an OPC UA server with temperature and humidity variables."""
    
    # Create and configure the OPC UA server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # Register a namespace
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # Create an object node
#    objects = await server.nodes.objects
    objects = server.nodes.objects
    myobj = await objects.add_object(idx, "MyObject")

    # Create writable variables for temperature and humidity
    temperature = await myobj.add_variable(idx, "Temperature", 0.0)
    humidity = await myobj.add_variable(idx, "Humidity", 0.0)
    await temperature.set_writable()
    await humidity.set_writable()

    print("OPC UA Server started at opc.tcp://0.0.0.0:4840/freeopcua/server/")
    
    # Run the server and update sensor values
    async with server:
        while True:
            temp_value = random.uniform(20.0, 25.0)
            hum_value = random.uniform(30.0, 50.0)

            # Update variable values
            await temperature.write_value(temp_value)
            await humidity.write_value(hum_value)

            print(f"Updated Temperature: {temp_value:.2f}, Humidity: {hum_value:.2f}")

            await asyncio.sleep(1)

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())