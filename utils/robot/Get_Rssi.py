import asyncio
from bleak import BleakScanner
import numpy as np

async def return_rssi_readings(addresses):
	readings = []
	for address in addresses:
		device = await BleakScanner.find_device_by_address(address)
		readings.append(device.rssi)
#		print(readings)

	return readings
