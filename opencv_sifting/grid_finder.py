import cv2 as cv # opencv-python
import pickle # used for opening keypoints/descriptors files
import sys # grabs the list of file
import os
from collections import Counter # used to grab top results
path = str(sys.argv[1]) # you can preset the path, just edit this line
# needs:
# gridSpace.jpg # can be called anything, this is the comparison picture
# This is the data for the Grid Picture
# keypoints.txt
# descriptors.txt

index = pickle.loads(open("keypoints.txt", "rb").read()) # grabs the keypoints 
des2 = pickle.loads(open("descriptors.txt", "rb").read()) # grabs the descriptors

kp2 = [] # grabs the keypoints from the index file

for point in index:
    temp = cv.KeyPoint(x=point[0][0],y=point[0][1],size=point[1], angle=point[2], response=point[3], octave=point[4], class_id=point[5])
    kp2.append(temp)
sift = cv.SIFT_create() # creates the processing function

def findPossibleLocations(detection_image): # goes through each image and outputs grid space

    img1 = cv.imread(detection_image,cv.IMREAD_GRAYSCALE)          # queryImage, find what grid space you are in
    kp1, des1 = sift.detectAndCompute(img1,None) # grabs the keypoints and descriptors
    FLANN_INDEX_KDTREE = 1 # specifies algorithm used
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params) # compares the keypoints
    matches = flann.knnMatch(des1,des2,k=2) # outputs the matches found
    correct = [] # goes through each keypoint and locates the ones within threshold
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            correct.append(m)
    points = []
    for match in correct: # double check that they match both images
        p2 = kp2[match.trainIdx].pt
        points.append(p2)
    grid_space = []
    for point in points: # converts the image x,y to grid space
        x = str(int(point[0]/300)+1).zfill(2) # change 300 to how large each grid space is based off pixels
        y = char(int(point[1]/300)+65)) # converts number to ascii, 65 is A
        grid_space.append(y+x)
    top_placements = (Counter(grid_space).most_common(1)) # change the number to how many grid spaces you wish to output
    location_output = []
    for items in top_placements:
        location_output.append(items[0]) # converts points into a final string
    final_string = ""
    for items in location_output:
        final_string+=items
    return final_string # returns string

    return grid_space
gridding = [] # list of all grid spaces
for filename in os.listdir(path): # goes through each image
    f = os.path.join(path, filename) # grabs the image file
    if os.path.isfile(f): # processes each image
        print()
        returned_data = findPossibleLocations(f)
        for data_point in returned_data:
            gridding.append(data_point) # add points to final
top_placements = (Counter(gridding).most_common(4))# prints out top 4 locations from all images, can be changes to more grids
location_output = []
for items in top_placements:
    location_output.append(items[0])
print(location_output)


