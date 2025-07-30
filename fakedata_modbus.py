from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_server():
    # Initialize data block - method differs in 2.5.3
    block = ModbusSequentialDataBlock(0, [65, 72] + [0]*98)  # First two registers = 65, 72
    
    # Create slave context (device_id=1)
    store = ModbusSlaveContext(
        hr=block,  # Holding registers
        zero_mode=True  # Important for 0-based addressing
    )
    
    context = ModbusServerContext(slaves={1: store}, single=False)
    
    print("Starting Modbus server on 0.0.0.0:5020")
    print("Initial registers:", block.getValues(0, 2))  # Should show [65, 72]
    
    StartTcpServer(context, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()