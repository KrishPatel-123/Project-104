import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(110,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(185,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(285,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Moon",(315,150),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(385,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(570,380),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(760,330),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(967,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1110,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)