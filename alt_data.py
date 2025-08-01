from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import random
import time
from threading import Thread

def generate_sensor_values():
    """Thread function to update values periodically"""
    while True:
        # Generate realistic variations
        humidity = random.randint(85, 97)  # 40-80% RH as integer
        temperature = random.randint(24, 28)  # 15-35°C as integer

        # Update registers with integer values
        block.setValues(0, [humidity, temperature])
        
        # Print current values (optional)
        print(f"\rCurrent values - Humidity: {humidity:.1f}%, Temperature: {temperature:.1f}°C", end="")
        time.sleep(300)  # Update every 5 seconds

# Initialize data block
block = ModbusSequentialDataBlock(0, [0, 0])  # Start with [0, 0]

def run_server():
    # Start value generator thread
    Thread(target=generate_sensor_values, daemon=True).start()
    
    # Create Modbus context
    store = ModbusSlaveContext(hr=block, zero_mode=True)
    context = ModbusServerContext(slaves={1: store}, single=False)
    
    print("Starting Modbus server on 0.0.0.0:5020")
    StartTcpServer(context, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()