import sys
import asyncio
from time import sleep

sys.path.append('../../utils/robot')

import Get_Rssi as get_rssi

for i in range(10):
	sleep(4)
	try:
		rssi = asyncio.run(get_rssi.return_rssi_readings(["C4:F1:B0:74:10:0B"]))
		print(rssi)
	except:
		print('Not Detected!')

