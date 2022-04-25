import cv2 # opencv
import pickle # used to dump data into file

im=cv2.imread("image.jpg") # this is the grid image, change to what you need
gr=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # converts the image to a gray scale
d=cv2.SIFT_create() # starts up the sifting engine
kp, des=d.detectAndCompute(gr,None) # creates the keypoints and descriptors for the image

index = [] # storage array

for point in range(len(kp)): # goes through each point
    temp = (kp[point].pt, kp[point].size, kp[point].angle, kp[point].response, kp[point].octave,
            kp[point].class_id) # stores the data over to index array
    index.append(temp)

# Dump the data to files
f = open("keypoints.txt", "wb")
f.write(pickle.dumps(index)) # dumps the keypoits into a file
f.close()
f = open("descriptors.txt", "wb") # dumps the descriptors into a file
f.write(pickle.dumps(des))
f.close()

