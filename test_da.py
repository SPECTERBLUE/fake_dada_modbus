from pymodbus.client.sync import ModbusTcpClient

def run_client():
    client = ModbusTcpClient('localhost', port=5020)
    
    # Try both address 0 and 1 (addressing differs between implementations)
    for address in [0]:
        response = client.read_holding_registers(
            address=address,
            count=2,
            unit=1  # slave ID
        )
        
        if response.isError():
            print(f"Error reading address {address}: {response}")
        else:
            print(f"Address {address} registers: {response.registers}")

    client.close()

if __name__ == "__main__":
    run_client()