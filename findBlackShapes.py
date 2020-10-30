# https://www.pyimagesearch.com/2014/10/20/finding-shapes-images-using-python-opencv/
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])  # Recordar que OpenCV toma los colores como BGR. 000 es triple negro
upper = np.array([15, 15, 15])  # esto son dark gray
shapeMask = cv2.inRange(image, lower, upper)

# find the contours in the mask
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("Encontre {} figuras negras".format(len(cnts)))
cv2.imshow("Mask", shapeMask)

# loop over the contours
for c in cnts:
    # draw the contour and show it
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
