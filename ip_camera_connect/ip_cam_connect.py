import cv2

# stream = cv2.VideoCapture('protocol://IP:port/1')
# stream = cv2.VideoCapture('rtsp://admin:IUWUCT@192.168.1.41:554') # 3g room
# stream = cv2.VideoCapture('rtsp://admin:ZGCYLM@192.168.1.40:554') # 2w room
stream = cv2.VideoCapture('rtsp://admin:123456@192.168.1.24:10554')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')

while True:

    r, f = stream.read()
    cv2.imshow('IP Camera stream', f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
