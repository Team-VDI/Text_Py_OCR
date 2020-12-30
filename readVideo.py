import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture('MOV029.mp4')

y=50
x=120
hf=400
wf=400
count = 0

detector = cv2.SimpleBlobDetector()

while(cap.isOpened()):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       

	ret,gray = cv2.threshold(gray,180,255,0)
	gray2 = gray.copy()
	mask = np.zeros(gray.shape,np.uint8)
	crop_vid = frame[y:y+hf,x:x+wf]
	crop_vid_mask = gray[y:y+hf,x:x+wf]
	
	contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(gray, contours, -1,(255,255,255),2)
	
	for i in range(2):
		template = cv2.imread('examples/ex_'+ str(i)+'.png',0)
		print('Detected' + str(i))
		
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(crop_vid_mask,template,cv2.TM_SQDIFF)

		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		top_left = min_loc
		bottom_right = (top_left[0] + w, top_left[1] + h)

		cv2.rectangle(crop_vid_mask, top_left, bottom_right, 255, 1)
		cv2.putText(crop_vid_mask, 'Detected: '+ str(i), (top_left[0],top_left[1]-10), 
				cv2.FONT_HERSHEY_PLAIN, 1.0, (255,0,255))
		
	cv2.imshow('Test',frame)
	#cv2.imshow('gray', gray)
	#cv2.imshow('cropped', crop_vid)
	cv2.imshow('cropped2', crop_vid_mask)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	
