import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('sample.avi')
success,image = vidcap.read()
count = 0
while count < 1:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1


