
import cv2
import dlib
from imutils import face_utils




def FaceAlignmentFunction(frame, shape):

	color = (50, 250, 250)
	thickness = 1

	# for i in range(len(shape) - 1):
	# 	cv2.circle(frame, tuple(shape[i]), 1, (0, 0, 255), thickness=2, lineType=8, shift=0)
	# 	cv2.putText(frame, str(i), tuple(shape[i]),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

	for i in range(4):
		cv2.line(frame, tuple(shape[i + 23]), tuple(shape[44]), color, thickness)
		cv2.line(frame, tuple(shape[i + 17]), tuple(shape[37]), color, thickness)

	for i in range(3):
		cv2.line(frame, tuple(shape[i + 64]), tuple(shape[i + 65]), color, thickness)
		cv2.line(frame, tuple(shape[60]), tuple(shape[67]), color, thickness)

	for i in range(5):
		cv2.line(frame, tuple(shape[i + 54]), tuple(shape[i + 55]), color, thickness)
		cv2.line(frame, tuple(shape[48]), tuple(shape[59]), color, thickness)

	for i in range(7):
		cv2.line(frame, tuple(shape[i + 27]), tuple(shape[i + 28]), color, thickness)

	for i in range(9):
		cv2.line(frame, tuple(shape[i + 17]), tuple(shape[i + 18]), color, thickness)

	for i in range(16):
		cv2.line(frame, tuple(shape[i]), tuple(shape[i + 1]), color, thickness)

	cv2.line(frame, tuple(shape[0]), tuple(shape[37]), color, thickness)
	cv2.line(frame, tuple(shape[0]), tuple(shape[17]), color, thickness)
	cv2.line(frame, tuple(shape[1]), tuple(shape[41]), color, thickness)
	cv2.line(frame, tuple(shape[9]), tuple(shape[54]), color, thickness)
	cv2.line(frame, tuple(shape[9]), tuple(shape[56]), color, thickness)
	cv2.line(frame, tuple(shape[7]), tuple(shape[48]), color, thickness)
	cv2.line(frame, tuple(shape[7]), tuple(shape[59]), color, thickness)
	cv2.line(frame, tuple(shape[43]), tuple(shape[44]), color, thickness)
	cv2.line(frame, tuple(shape[44]), tuple(shape[46]), color, thickness)
	cv2.line(frame, tuple(shape[43]), tuple(shape[47]), color, thickness)
	cv2.line(frame, tuple(shape[46]), tuple(shape[47]), color, thickness)
	cv2.line(frame, tuple(shape[37]), tuple(shape[38]), color, thickness)
	cv2.line(frame, tuple(shape[37]), tuple(shape[41]), color, thickness)
	cv2.line(frame, tuple(shape[38]), tuple(shape[40]), color, thickness)
	cv2.line(frame, tuple(shape[40]), tuple(shape[41]), color, thickness)
	cv2.line(frame, tuple(shape[28]), tuple(shape[35]), color, thickness)
	cv2.line(frame, tuple(shape[30]), tuple(shape[35]), color, thickness)
	cv2.line(frame, tuple(shape[34]), tuple(shape[35]), color, thickness)
	cv2.line(frame, tuple(shape[35]), tuple(shape[46]), color, thickness)
	cv2.line(frame, tuple(shape[31]), tuple(shape[30]), color, thickness)
	cv2.line(frame, tuple(shape[32]), tuple(shape[30]), color, thickness)
	cv2.line(frame, tuple(shape[33]), tuple(shape[30]), color, thickness)
	cv2.line(frame, tuple(shape[34]), tuple(shape[30]), color, thickness)
	cv2.line(frame, tuple(shape[29]), tuple(shape[31]), color, thickness)
	cv2.line(frame, tuple(shape[29]), tuple(shape[35]), color, thickness)
	cv2.line(frame, tuple(shape[21]), tuple(shape[27]), color, thickness)
	cv2.line(frame, tuple(shape[22]), tuple(shape[27]), color, thickness)
	cv2.line(frame, tuple(shape[21]), tuple(shape[28]), color, thickness)
	cv2.line(frame, tuple(shape[22]), tuple(shape[28]), color, thickness)
	cv2.line(frame, tuple(shape[31]), tuple(shape[28]), color, thickness)
	cv2.line(frame, tuple(shape[16]), tuple(shape[44]), color, thickness)
	cv2.line(frame, tuple(shape[15]), tuple(shape[46]), color, thickness)
	cv2.line(frame, tuple(shape[41]), tuple(shape[31]), color, thickness)
	cv2.line(frame, tuple(shape[16]), tuple(shape[26]), color, thickness)
	cv2.line(frame, tuple(shape[48]), tuple(shape[49]), color, thickness)
	cv2.line(frame, tuple(shape[49]), tuple(shape[50]), color, thickness)
	cv2.line(frame, tuple(shape[52]), tuple(shape[53]), color, thickness)
	cv2.line(frame, tuple(shape[53]), tuple(shape[54]), color, thickness)
	cv2.line(frame, tuple(shape[50]), tuple(shape[52]), color, thickness)
	cv2.line(frame, tuple(shape[60]), tuple(shape[61]), color, thickness)
	cv2.line(frame, tuple(shape[52]), tuple(shape[63]), color, thickness)
	cv2.line(frame, tuple(shape[61]), tuple(shape[62]), color, thickness)
	cv2.line(frame, tuple(shape[62]), tuple(shape[63]), color, thickness)
	cv2.line(frame, tuple(shape[64]), tuple(shape[63]), color, thickness)
	cv2.line(frame, tuple(shape[33]), tuple(shape[51]), color, thickness)
	cv2.line(frame, tuple(shape[56]), tuple(shape[65]), color, thickness)
	cv2.line(frame, tuple(shape[57]), tuple(shape[65]), color, thickness)
	cv2.line(frame, tuple(shape[57]), tuple(shape[67]), color, thickness)
	cv2.line(frame, tuple(shape[58]), tuple(shape[67]), color, thickness)

	cv2.line(frame, tuple(shape[61]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)
	cv2.line(frame, tuple(shape[62]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)
	cv2.line(frame, tuple(shape[63]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)

	cv2.line(frame, tuple(shape[39]), (int(shape[31][0] - ((shape[31][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[40]), (int(shape[31][0] - ((shape[31][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[41]), (int(shape[31][0] - ((shape[31][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[27]), (int(shape[31][0] - ((shape[31][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[28]), (int(shape[31][0] - ((shape[31][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)

	cv2.line(frame, tuple(shape[42]), (int(shape[35][0] - ((shape[35][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[46]), (int(shape[35][0] - ((shape[35][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[47]), (int(shape[35][0] - ((shape[35][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[27]), (int(shape[35][0] - ((shape[35][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)
	cv2.line(frame, tuple(shape[28]), (int(shape[35][0] - ((shape[35][0] - shape[27][0]) / 2.5)),
									   int(shape[29][1])), color, thickness)

	cv2.line(frame, tuple(shape[8]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[57]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[7]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[9]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[48]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[54]), (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[45]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[46]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[47]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[15]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[13]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[35]), (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])), tuple(shape[10]), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])), tuple(shape[11]), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])), tuple(shape[13]), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])), tuple(shape[35]), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])), tuple(shape[54]), color,
			 thickness)
	cv2.line(frame, (int((shape[12][0] + shape[54][0]) / 2), int(shape[12][1])),
			 (int((shape[14][0] + shape[35][0]) / 2), int(shape[14][1]) + 10), color, thickness)

	cv2.line(frame, tuple(shape[36]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[40]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[41]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[1]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[3]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, tuple(shape[31]), (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])), tuple(shape[3]), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])), tuple(shape[5]), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])), tuple(shape[6]), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])), tuple(shape[31]), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])), tuple(shape[48]), color,
			 thickness)
	cv2.line(frame, (int((shape[4][0] + shape[48][0]) / 2), int(shape[12][1])),
			 (int((shape[2][0] + shape[31][0]) / 2), int(shape[2][1]) + 10), color, thickness)

	cv2.line(frame, (int(shape[20][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)

	cv2.line(frame, (int(shape[23][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)

	cv2.line(frame, (int(shape[20][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)),
			 (int(shape[23][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)), color, thickness)

	cv2.line(frame, tuple(shape[19]), (int((shape[19][0] + shape[24][0]) / 2),
									   int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color, thickness)
	cv2.line(frame, tuple(shape[19]), (int(shape[20][0]),
									   int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)), color, thickness)
	cv2.line(frame, tuple(shape[18]), (int(shape[20][0]),
									   int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)), color, thickness)


	cv2.line(frame, tuple(shape[24]),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)
	cv2.line(frame, tuple(shape[24]), (int(shape[23][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)),
			 color, thickness)
	cv2.line(frame, tuple(shape[25]), (int(shape[23][0]), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3.7)),
			 color, thickness)

	cv2.line(frame, tuple(shape[21]),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)
	cv2.line(frame, tuple(shape[22]),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)
	cv2.line(frame, tuple(shape[27]),
			 (int((shape[19][0] + shape[24][0]) / 2), int(shape[27][1] + (shape[27][1] - shape[28][1]) * 3)), color,
			 thickness)

	cv2.line(frame, tuple(shape[50]), tuple(shape[52]), color, thickness)
	cv2.line(frame, tuple(shape[50]), tuple(shape[61]), color, thickness)
	cv2.line(frame, tuple(shape[52]), tuple(shape[63]), color, thickness)
	cv2.line(frame, tuple(shape[61]), tuple(shape[62]), color, thickness)
	cv2.line(frame, tuple(shape[62]), tuple(shape[63]), color, thickness)

	cv2.line(frame, tuple(shape[61]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)
	cv2.line(frame, tuple(shape[62]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)
	cv2.line(frame, tuple(shape[63]), (int((shape[50][0] + shape[52][0]) / 2),
									   int(shape[50][1])), color, thickness)


	# cv2.circle(frame, (int(shape[33][0]), int((shape[33][1] + shape[8][1])/2)), 1, (0, 0, 0), thickness=8, lineType=8, shift=0)
	# cv2.circle(frame, (int(shape[33][0]), int((shape[33][1] + shape[8][1]) / 2) + 8), 1, (0, 0, 0), thickness=8, lineType=8,
	# 		   shift=0)




if __name__ == '__main__':

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


	# vs = VideoStream(src='test.mp4').start()
	# cap = cv2.VideoCapture('/Users/imac/Downloads/mark.mp4')
	cap = cv2.VideoCapture('test.mp4')

	while cap.isOpened():
		ret, frame = cap.read()
		# frame = imutils.resize(frame, width=800)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 0)
		for rect in rects:
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			FaceAlignmentFunction(frame, shape)



		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break

	cv2.destroyAllWindows()
	cap.release()