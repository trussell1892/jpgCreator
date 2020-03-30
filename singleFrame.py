import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('sample.avi')
image = vidcap.read()

cv2.imwrite("frame.jpg", image)     # save frame as JPEG file
success,image = vidcap.read()
print ('Read a new frame: ')
