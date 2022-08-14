import asyncio
from bleak import BleakScanner

async def main():
	address_1 = "C4:F1:B0:74:10:0B"
	address_2 = "C8:B3:F7:1E:BB:D7"
	address_3 = "F4:1C:2E:2A:C4:FF"
	address_4 = "DE:0A:DA:75:DF:57"

	device_1 = await BleakScanner.find_device_by_address(address_1)
	device_2 = await BleakScanner.find_device_by_address(address_2)
	device_3 = await BleakScanner.find_device_by_address(address_3)
	device_4 = await BleakScanner.find_device_by_address(address_4)

	print("Device1: ", device_1.rssi)
	print("Device2: ", device_2.rssi)
	print("Device3: ", device_3.rssi)
	print("Device4: ", device_4.rssi)

asyncio.run(main())
