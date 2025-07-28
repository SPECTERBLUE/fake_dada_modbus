from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [55, 67, 78])  # 3 values
)
context = ModbusServerContext(slaves=store, single=True)

StartTcpServer(context, address=("0.0.0.0", 502))
