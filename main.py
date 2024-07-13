import cv2
import matplotlib.image as mplib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def pixel(link):
 img=cv2.imread(link)
 #print(img.shape)
 height,width,_=img.shape
 indices = np.arange(height)

 # Plot the array against indices
 w=int(width/2)
 #print(w)
 print(img.shape)
#  plt.plot(indices, img[:,w][:,0], marker='o')
#  plt.xlabel('Index (i)')
#  plt.ylabel('Array Values')
#  plt.title('Array Plot')
#  plt.grid(True)
#  plt.show()



 cv2.waitKey(50)
 a=0
 e=0
 m=0
 t=0
 bin=0
 ti=0
 tf=0
 init=0  
 final=0
 for i in range(height):
  b=img[:,w][i][0]
  if b<100:
    if bin==1:
      t=t+1
      tf=i
    else:
      t=1
      bin=1
      ti=i
  else:
    if bin==1:
      m=max(m,t)
      if t>=m:
        init=ti
        final=tf
      bin=0
        
    
    
 #print(m)
 #print(init)
 #print(final)
 im1=img[init:final,w-5:w+5]
 #cv2.imshow('frame', im1)
 #cv2.waitKey(0)
 cv2.imwrite('im1.jpeg', im1)

 img = cv2.rectangle(img, (0, init), (w*2, final), (0, 255, 0), 5)

 resize=cv2.resize(img,(360,800))
 #cv2.imshow('frame', resize)
 #cv2.waitKey(0)
 cv2.imwrite('im2.jpeg', resize)
 return(init,final)
# print(pixel('calibrate/400.jpeg'))
# img=cv2.imread('im2.jpeg')
# cv2.imshow('frame', img)
# cv2.waitKey(0)
