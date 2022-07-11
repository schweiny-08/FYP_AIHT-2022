import cv2
import numpy as np

# THIS CODE WAS BASED ON https://github.com/The-Assembly/Obstacle_avoidance_opencv

cap = cv2.VideoCapture(0)
StepSize = 5

def getChunks(l, n):
	a = []
	for i in range(0, len(l), n):
		a.append(l[i:i + n])
	return a

while(True):
	ret, frame = cap.read()
	img = frame.copy()
	blur = cv2.bilateralFilter(img, 5, 30, 30)
	edges = cv2.Canny(blur, 0, 100)

	img_h = img.shape[0] - 1
	img_w = img.shape[1] - 1
	EdgeArray = []

	for j in range(0, img_w, StepSize):
		pixel = (j, 0)
		for i in range(img_h-5, 0, -1):
			if edges.item(i, j) == 255:
				pixel = (j, i)
				break
		EdgeArray.append(pixel)

	for x in range(len(EdgeArray)-1):
		cv2.line(img, EdgeArray[x], EdgeArray[x+1], (0, 255, 0), 1)
	for x in range(len(EdgeArray)):
		cv2.line(img, (x*StepSize, img_h), EdgeArray[x], (0, 255, 0), 1)

	cv2.imshow("rrr", img)

	chunks = getChunks(EdgeArray, int(len(EdgeArray)/3))
	c = []
	for i in range(len(chunks)-1):
		x_vals = []
		y_vals = []

		for (x, y) in chunks [i]:
			x_vals.append(x)
			y_vals.append(y)

		avg_x = int(np.average(x_vals))
		avg_y = int(np.average(y_vals))

		c.append([avg_y, avg_x])
		cv2.line(frame, (320, 480), (avg_x, avg_y), (255, 0, 0), 2)

#		print("C VALUE")
#		print(c)

		cv2.imshow('Result_1', frame)
		cv2.imshow('Edges', edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
