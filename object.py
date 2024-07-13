import cv2
import numpy as np

def factor(link):
    # Open the default camera
    

    # Load Aruco dictionary and parameters
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    parameters = cv2.aruco.DetectorParameters_create()
    img=cv2.imread(link)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    print(corners)
    hh=np.sort(corners[0][0][:,1])
    pll=((hh[2]+hh[3])/2)-((hh[0]+hh[1])/2)
   
    
    
    
        # Draw detected markers
    if ids is not None:
            cv2.aruco.drawDetectedMarkers(img, corners, ids)

        # Display the resulting frame
    cv2.imwrite('im3.jpeg', img)
    return (2.70/pll)
    

# Call the function to start showing the camera feed
# for i in range(1,21):
#  print(factor(f'calibrate/{i}00.jpeg'))
# img=cv2.imread('im3.jpeg')
# cv2.imshow('Photo', img)
# cv2.waitKey(0)