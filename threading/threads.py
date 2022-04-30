import threading
from time import sleep
# in order to use threads, create your individual threads into their own definitions
x = 0
def increaseX:
  while True:
    x += 1
    sleep(1.0)
  
def printX:
  while True:
    print(x)

    
#classifies the threads and sets their target
increaseThread = threading.Thread(target=increaseX, name='increase') # target is the definition name and the name is what you wish to call the thread
printThread = threading.Thread(target=printX, name='print')


# starts thread
increaseThread.start()
printThread.start()
