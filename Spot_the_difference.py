import cv2
import numpy 
import function
import variables
import math


cv2.namedWindow('window')
image_set = variables.imagePaths[0]
current_image = cv2.imread(image_set["imagePath"])
resized_image = cv2.resize(current_image, (640, 800))
copy_image = function.create_clone(resized_image)
inserted_image = function.insert_circles(resized_image)

def resetWindow():
    resized_image = cv2.resize(current_image, (640, 800))
    inserted_image = function.insert_circles(resized_image)
    return inserted_image

def click_on_contour(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, contour in enumerate(contours):
                if i in clicked_contours:  
                    continue
                (a,b), radius = cv2.minEnclosingCircle(contour)
                center = (int(a),int(b))
                radius = int(radius)
                if math.sqrt((x - int(a))**2 + (y - 30 - int(b))**2) <= radius:
                    cv2.circle(inserted_image,center,radius,(0,0,255),2)
                    if variables.current_level < 2:
                        variables.first_difference -= 1
                    else:
                        variables.second_difference -= 1
                    clicked_contours.append(i)  
            img_concat = numpy.concatenate((inserted_image,copy_image) , axis = 1)
            result = function.render_point(img_concat)
            cv2.imshow("window", result)


while variables.current_level <= 2: 
    image_difference = function.image_diff(inserted_image, copy_image)
    contours = function.thresholding(image_difference)
    clicked_contours = []
    img_concat = numpy.concatenate((inserted_image,copy_image),axis = 1)
    result = function.render_point(img_concat)

    cv2.imshow('window' , result)
    cv2.setMouseCallback('window', click_on_contour)
    cv2.waitKey(0)

    if variables.first_difference == 0:
        variables.current_level += 1
        inserted_image = resetWindow()

    if variables.second_difference == 0:
        cv2.destroyAllWindows()
        quit()