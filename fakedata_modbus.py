from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext

# Create data block
data_block = ModbusSequentialDataBlock(0, [65, 72, 88])  # Holding registers


device_context = ModbusDeviceContext(hr=data_block)


server_context = ModbusServerContext(devices={1: device_context}, single=False)

# Start the TCP server
StartTcpServer(server_context, address=("0.0.0.0", 5020))
