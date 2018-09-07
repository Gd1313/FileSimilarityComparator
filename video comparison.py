import cv2
from diffimg import diff
from os import listdir
print(cv2.__version__)
vidcap = cv2.VideoCapture('videotest/video1.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("videotest/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  count += 1 

print(cv2.__version__)
vidcap2 = cv2.VideoCapture('videotest/video2.mp4')
success2,image2 = vidcap.read()
count2 = 0
success2 = True
while success2:
  cv2.imwrite("videotest2/fram1%d.jpg" % count2, image2)     # save frame as JPEG file
  success2,image2 = vidcap.read()
  print 'Read a new frame: ', success
  count2 += 1 




diff("blur/damien_hirst.bmp", 
     "blur/diamondskull.bmp")

    
