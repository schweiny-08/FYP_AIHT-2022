import cv2
import numpy as np

class Camera_Controls:

	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		self.StepSize = 5
		self.c = []

	def calc_distance(p1, p2):
		x1 = p1[0]
		y1 = p1[1]
		x2 = p2[0]
		y2 = p2[1]

		dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)

		return dist

	def getChunks(self, l, n):
       		a = []
	        for i in range(0, len(l), n):
        	        a.append(l[i:i + n])
	        return a


	def start_camera(self):
#		print("CAMERA SUBPROCESS STARTED")
		# THIS CODE WAS BASED ON https://github.com/The-Assembly/Obstacle_avoidance_opencv
#		while True:
		ret, frame = self.cap.read()
#		if frame is not None:
#			break
		img = frame.copy()
		blur = cv2.bilateralFilter(img, 5, 30, 30)
		edges = cv2.Canny(blur, 0, 100)

		img_h = img.shape[0] - 1
		img_w = img.shape[1] - 1
		EdgeArray = []

		for j in range(0, img_w, self.StepSize):
			pixel = (j, 0)
			for i in range(img_h - 5, 0, -1):
				if edges.item(i, j) == 255:
					pixel = (j, i)
					break
			EdgeArray.append(pixel)

#       		for x in range(len(EdgeArray)-1):
#               		cv2.line(img, EdgeArray[x], EdgeArray[x+1], (0, 255, 0), 1)
#		       	for x in range(len(EdgeArray)):
#               		cv2.line(img, (x*StepSize, img_h), EdgeArray[x], (0, 255, 0), 1)

		chunks = self.getChunks(EdgeArray, int(len(EdgeArray)/3))
#		print("CHUNKS")
#		print(chunks[4])
		self.c = []
		for i in range(len(chunks)-1):
			x_vals = []
			y_vals = []

			for (x, y) in chunks[i]:
				x_vals.append(x)
				y_vals.append(y)

			avg_x = int(np.average(x_vals))
			avg_y = int(np.average(y_vals))

			self.c.append([avg_y, avg_x])
			cv2.line(frame, (320, 480), (avg_x, avg_y), (255, 0, 0), 2)
#		cv2.imshow('Result_1', frame)
#               	cv2.imshow('Edges', edges)
#		        if cv2.waitKey(1) & 0xFF == ord('q'):
#                	break

	def get_line(self):
		return self.c

	def stop_camera(self):
		self.cap.release()
		cv2.destroyAllWindows()


