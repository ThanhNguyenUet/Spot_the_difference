import cv2
import numpy 
import function
import variables
import math

cv2.namedWindow('window')
image_set = variables.imagePaths[0]
resized_image = cv2.imread(image_set["imagePath"])


# the input 
# resized_image = cv2.resize(current_image, (640, 800))
# the copy (already modified)
copy_image = function.copy_image(resized_image)

difference_image = function.find_difference(resized_image, copy_image)

img_concat = numpy.concatenate((difference_image , resized_image) , axis = 1)

result = function.render_point(img_concat) 

# def resetWindow():
#     resized_image = cv2.resize(current_image, (640, 800))
#     inserted_image = function.insert_circles(resized_image)
#     return inserted_image

# def click_on_contour(event, x, y, flags, param):
#         point = 0
#         if event == cv2.EVENT_LBUTTONDOWN:
#             for i, contour in enumerate(contours):
#                 if i in clicked_contours:  
#                     continue
#                 if cv2.pointPolygonTest(contour, (x, y), False) >= 0:
#                     x,y,w,h = cv2.boundingRect(contour)
#                     cv2.rectangle(inserted_image, (x,y) , (x+w,y+h),(0,0,255),10)
#                     clicked_contours.append(i)
#                     point += 1  
#                     print(f"point: {point} , lencontour: {len(contours)}")
#                     if variables.current_level < 2:
#                          if point == len(contours):
#                               variables.current_level += 1 
#             img_concat = numpy.concatenate((inserted_image,copy_image) , axis = 1)
#             result = function.render_point(img_concat)
cv2.imshow("window", result)
# cv2.setMouseCallback('window', click_on_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
