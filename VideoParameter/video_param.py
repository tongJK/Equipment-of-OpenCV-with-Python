import cv2

video_stream = cv2.VideoCapture('video_file')

while True:

    ret, frame = video_stream.read()

    print(f'time stamp : {video_stream.get(0)} ms')
    print(f'number of this frame : {video_stream.get(1)}')
    print(f'SPF : {video_stream.get(2)}')
    print(f'High : {video_stream.get(3)}')
    print(f'Width : {video_stream.get(4)}')
    print(f'FPS : {video_stream.get(5)}')
    print(f'number of all frame : {video_stream.get(6)} frames')
    print(f'period : {video_stream.get(7)} ms')

    print('-'*70)
