# Simple python script calculates difference between two images

# import libraries
import cv2
import argparse

# read images from command line
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first_image", required=True, help="first input image")
ap.add_argument("-s", "--second_image", required=True, help="second input image")
args = vars(ap.parse_args())

# load the two images
first_test_image = cv2.imread(args["first_image"])
second_test_image = cv2.imread(args["second_image"])

# display the two images
cv2.imshow("first_test_image", first_test_image)
cv2.imshow("second_test_image", second_test_image)
cv2.waitKey(0) # press any key to close the window

# get the difference between the images
img_diff = cv2.subtract(first_test_image, second_test_image)
cv2.imshow("img_diff", img_diff)
cv2.waitKey(0) # press any key to close the window

# get all the three channels of the RGB image
b, g, r = cv2.split(img_diff)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)	
cv2.waitKey(0) # press any key to close the window

# store the difference image
cv2.imwrite('diff_img.png', img_diff)
