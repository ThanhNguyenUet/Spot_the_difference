# Spot_the_difference
This project still needs improvement but has a straightforward idea and approach

Some notable things to understand before reading the codes :
1. The code reads in an image and create a copy of it before adding multiple circles on it to find the differences.
Why the circle you ask ? Because I haven't studied how to randomly change some objects in an image yet.
Then you may ask why not 2 images. That's not my idea okay :) 
So for it to be a little bit more challenging, the picture I provided is full of circles :) Happy finding.
2. The game has 2 levels. I can use 2 different circle image but instead I just increase the number of circles. The colour and place of it is completely random so you can test multiple times.
3. So some major improvements if any wants to :
    a. The circles I draw is controlled as I don't want some of them to intertwined or inside of each other so the game is pretty much very easy.
    b. The differences therefore is fixed in variables.py
    c. The threshold value :) because the color of circles are random, some very light color may < threshold value and be converted to 1 in binary( black ) which resulting even if you click inside the contour, it doesn't work. Well no solution for this either :(
    d. The second level only opens after the first level window is closed, can't seem to find a solution for this :(

With that outta way, let's move on to the algorithm :
The way I approach this is using thresholding.
Specifically, with the absolute difference of 2 images ( should be greyscale ) , I will thresholded it with a fixed threshold value to convert it to a binary image.
Next, I find the contours of the image using cv2.findContours() and draw a circle if the user click inside the contour. 
The point is increased if you find a difference.

To run the code, just simply clone it to your personal device.
