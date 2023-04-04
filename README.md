1. Both the Spot_the_difference.ipynb and Spot_the_difference.py works fine
    A. DATA 
        Read in an image :
            image = cv2.imread("../Image/buildings.jpg")
    B. Levels :
    Level 1 :
        Idea : create random circles on the image
        How : Using def insert_circles(image) in function.py to draw circles on the screen
    Level 2 :
        Idea : change color of some objects
        How : Using def find_edges(image) in function.py.
              use canny edge detection to find edges, reduce weak edges. From their, find contours and change the color inside it

        