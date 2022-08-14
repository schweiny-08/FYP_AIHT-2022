import utils.robot.Get_Rssi as get_rssi
import asyncio
import numpy as np

address_1 = "C4:F1:B0:74:10:0B"
address_2 = "C8:B3:F7:1E:BB:D7"
address_3 = "F4:1C:2E:2A:C4:FF"
address_4 = "DE:0A:DA:75:DF:57"

addresses = []
quadrants = np.zeros((4,3))
# print(quadrants)

addresses.append(address_1)
addresses.append(address_2)
addresses.append(address_3)
addresses.append(address_4)

# print(addresses)

temp = []

for i in range(10):
	results = asyncio.run(get_rssi.return_rssi_readings(addresses))

# print(result)

	temp.append(results)

print(temp)

temp_avg = []

for l in range(len(temp[0])):
	avg = 0
	for k in range(len(temp)):
		avg += temp[k][l]
	avg /= len(temp)
	temp_avg.append(avg)

# for i in range(len(quadrants)):
# 	for j in range(len(quadrants[i])):
# 		print()
print(len(temp[0]))
print(temp_avg)

