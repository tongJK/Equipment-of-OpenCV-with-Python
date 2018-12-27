
import cv2
import dlib
from imutils import face_utils
from imutils.video import VideoStream

def DasedLine(frame, p1, p2):
	# cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)

	InvicisibleLine = 0
	dash_space = 3
	dash_long = 50

	color = (250, 172, 88)

	if p1[0] < p2[0]:
		for i in range(int(p1[0]), int(p2[0]), int(p2[0]) // dash_space):

			if InvicisibleLine == 0:
				cv2.line(frame, (i, p1[1]), (i + dash_long, p1[1]), color, 2)
				cv2.line(frame, (i, p2[1]), (i + dash_long, p2[1]), color, 2)
				InvicisibleLine = 1

			else:
				InvicisibleLine = 0

	else:
		for i in range(int(p2[0]), int(p1[0]), int(p1[0]) // dash_space):

			if InvicisibleLine == 0:
				cv2.line(frame, (i, p1[1]), (i + dash_long, p1[1]), color, 2)
				cv2.line(frame, (i, p2[1]), (i + dash_long, p2[1]), color, 2)
				InvicisibleLine = 1

			else:
				InvicisibleLine = 0

	if p1[1] < p2[1]:
		for i in range(int(p1[1]), int(p2[1]), int(p2[1]) // dash_space):

			if InvicisibleLine == 0:
				cv2.line(frame, (p1[0], i), (p1[0], i + dash_long), color, 2)
				cv2.line(frame, (p2[0], i), (p2[0], i + dash_long), color, 2)
				InvicisibleLine = 1

			else:
				InvicisibleLine = 0

	else:
		for i in range(int(p2[1]), int(p1[1]), int(p1[1]) // dash_space):

			if InvicisibleLine == 0:
				cv2.line(frame, (p1[0], i), (p1[0], i + dash_long), color, 2)
				cv2.line(frame, (p2[0], i), (p2[0], i + dash_long), color, 2)

				InvicisibleLine = 1

			else:
				InvicisibleLine = 0

	return frame

def FaceMarkLine(frame, p1, p2):

	color = (255, 255, 0)
	thickness = 2

	#  __
	# |
	p3 = (p1[0] + int((p2[0] - p1[0]) / 3), p1[1])
	cv2.line(frame, p1, p3, color, thickness)

	p4 = (p1[0], y_reg + int((p2[1] - p1[1]) / 3))
	cv2.line(frame, p1, p4, color, thickness)

	#  __
	#    |

	p5 = (p2[0] - int((p2[0] - p1[0]) / 3), p1[1])
	p6 = (p2[0], p1[1])
	cv2.line(frame, p5, p6, color, thickness)

	p7 = (p2[0], y_reg + int((p2[1] - p1[1]) / 3))
	cv2.line(frame, p7, p6, color, thickness)

	# |
	#  --

	p8 = (x_reg, p2[1] - int((p2[1] - p1[1]) / 3))
	p9 = (p1[0], p2[1])
	cv2.line(frame, p8, p9, color, thickness)

	p10 = (p1[0] + int((p2[0] - p1[0]) / 3), p2[1])
	cv2.line(frame, p9, p10, color, thickness)

	#   |
	#  --
	p11 = (w_reg, p2[1] - int((p2[1] - p1[1]) / 3))
	cv2.line(frame, p11, p2, color, thickness)

	p12 = (p2[0] - int((p2[0] - p1[0]) / 3), p2[1])
	cv2.line(frame, p12, p2, color, thickness)

	return frame



if __name__ == '__main__':

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


	vs = VideoStream(src='test.mp4').start()

	while True:
		frame = vs.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = detector(gray, 0)

		for i, face in enumerate(faces):

			x_reg, y_reg, w_reg, h_reg = face.left(), face.top(), face.right(), face.bottom()
			crop_img = frame[y_reg:h_reg, x_reg:w_reg]

			p1 = (x_reg, y_reg)
			p2 = (w_reg, h_reg)

			frame = FaceMarkLine(frame, p1, p2)




		cv2.imshow("Frame", frame)
		cv2.waitKey(5)

	cv2.destroyAllWindows()
	vs.stop()
