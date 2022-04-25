import os
name = "hi" # name of image
command = 'libcamera-still -o ' + name + '.jpg -t 1 --shutter 9000 -n --autofocus --width 2448 --height 3264' # save as %d.jpg
# uses either libcamera-still or raspistill
# -o <name>.<fileType> # specifies output file
# -t <number> # specifies the time it takes to take picture
# --shutter <number> # specifies the shutter speed, 9000 to reduce motion blur, but the image becomes distorted
# -n # turns off the image preview
# --autofocus # uses the preset library and allows autofocus per picture # found at https://www.arducam.com/downloads/arducam-imx519-start-guide.pdf
# --width <number> --height <number> # specifies the output image size, not necessary if image size does not matter

os.system(command) # runs the command inside the terminal
