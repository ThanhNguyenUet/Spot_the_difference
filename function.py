import cv2
import numpy
import variables
import pyautogui

# convert img to greyscale and find the abs difference for thresholding
def image_diff(img01, img02):
    img01_grey = cv2.cvtColor(img01, cv2.COLOR_BGR2GRAY)
    img02_grey = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)
    diff_img = cv2.absdiff(img01_grey, img02_grey)
    return diff_img


# function to thresholding the image to find contour
# image received should be grey image
# return results are contours
def thresholding(image):
    _ , thresh = cv2.threshold(image, 30 , 255 , cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

# create the 2nd image for spot
def create_clone(image):
    copy_image = numpy.copy(image)
    return copy_image

# insert circles for differences
def insert_circles(image):
    if variables.current_level == 1:
        num_circles = variables.first_difference
    else:
        num_circles = variables.second_difference

    circles = []
    while len(circles) < num_circles:
        center = tuple(numpy.random.randint(0, high=image.shape[1], size=(2,)))
        radius = numpy.random.randint(30, 50)
        circle = (center, radius)
        # check if the new circle intersects with any of the previous circles
        is_intersecting = False
        for other_circle in circles:
            distance = ((other_circle[0][0] - center[0])**2 + (other_circle[0][1] - center[1])**2)**0.5
            if distance < other_circle[1] + radius + 50:
                is_intersecting = True
                break
        if not is_intersecting:
            r = numpy.random.randint(0, 255)
            g = numpy.random.randint(0, 255)
            b = numpy.random.randint(0, 255)
            color = (b, g, r)
            cv2.circle(image, center, radius, color, -1)
            circles.append(circle)
    return image

def render_point(image):
    text_img = numpy.zeros((50, image.shape[1], 3), dtype=numpy.uint8)
    if variables.current_level < 2:
        text = f"Level : {variables.current_level}   Number of differences left : {variables.first_difference}"
    else:
        text = f"Level : {variables.current_level}   Number of differences left : {variables.second_difference}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (text_img.shape[1] - text_size[0]) // 2
    text_y = (text_img.shape[0] + text_size[1]) // 2
    cv2.putText(text_img, text, (text_x, text_y), font, font_scale, color, thickness)
    result = numpy.concatenate((text_img, image), axis=0)
    return result



