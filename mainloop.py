import time
from processInput import processInput
from update import update
from render import render

def mainloop():
    prevTime = time.time()
    
    while(True):
        nowTime = time.time()
        elapsedTime = nowTime - prevTime
        prevTime = nowTime

        processInput()
        update(elapsedTime)
        render()

if __name__ == "__main__":
    mainloop()