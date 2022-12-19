import numpy as np
import cv2
import math

# video capture
capture = cv2.VideoCapture(0)

while True:
    success,img = capture.read()
    
    
    # Frame Cropping
    cv2.rectangle(img,(700,100),(1100,500),(0,255,0),0)
    crop_image= img[100:500,700:1100]
    
    # TODO: Grey Filter (pass crop_image)
    # grey = your code
    
    
    # TODO: Gaussian Blur to smoothen the image (pass grey)
    # blur = your code
    

    # TODO: thresholding the image using Binary inversion + OTSU
    # ret,thresh= your code
    

    # show threshold
    cv2.imshow("Threshold",thresh)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        # TODO: contour with maximum area
        # contour = your code
        
        # bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

        # TODO: create hull
        #hull = your code  (important: do not use returnPoints argument)


        drawing = np.zeros(crop_image.shape, np.uint8)
        cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
        cv2.drawContours(drawing,[hull],-1,(0,0,255),0)

        #TODO: finding convex hull
        #hull = your code  (important: use returnPoints argument as False)
        
        
        # TODO: finding convexity defects
        # defects = your code
        
        

        count_defects = 0
        #TODO: refer to the math for calculating the angle part of README
        
            
        # output
        # TODO: Complete the logic
        if count_defects == 0:
            cv2.putText(img, "ONE",(50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # elif count_defects == 1:
            

        else:

            pass


    except:
        pass

    cv2.imshow("Gesture",img)
    all_image = np.hstack((drawing,crop_image))

    cv2.imshow('contours',all_image)

    if cv2.waitKey(1)==ord('q'):
        break


capture.release()
cv2.destroyAllWindows()









