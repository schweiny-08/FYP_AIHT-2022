import numpy as np
import asyncio
import Get_Rssi as get_rssi
import pickle
import csv

x = 0

addresses = ["C4:F1:B0:74:10:0B", "C8:B3:F7:1E:BB:D7", "F4:1C:2E:2A:C4:FF", "DE:0A:DA:75:DF:57"]
#addresses = ["C8:B3:F7:1E:BB:D7", "F4:1C:2E:2A:C4:FF", "DE:0A:DA:75:DF:57"]

raw_quad = {}
treated_quad = {}

while True:
	print("Enter coordinates")
	x = input("x coord ")
	y = input("y coord ")

	if x == 'q' or y == 'q':
		with open('location.json', 'wb') as fp:
			pickle.dump(raw_quad, fp)
		break

	isValid = False

	while not isValid:
		obs = input("Enter O for obstacle or leave empty to scan: ")

		if obs == "":
			results = asyncio.run(get_rssi.return_rssi_readings(addresses))
			isValid = True
		elif obs == 'O' or obs == 'o':
			results = 'O'
			isValid = True
		else:
			print("Please redo coordinate")

	raw_quad[x,y] = results
	print(raw_quad)

print("Extracting features from the data")

for key in raw_quad:
	temp = []
	value = raw_quad[key]

	if value != 'O':
		mean = np.mean(value)
		std = np.std(value)
		median = np.median(value)

		temp.append(mean)
		temp.append(std)
		temp.append(median)

		treated_quad[key] = temp
	else:
		treated_quad[key] = 'O'

print(treated_quad)

with open('location_features', 'wb') as fp:
	pickle.dump(treated_quad, fp)
	fp.close()
