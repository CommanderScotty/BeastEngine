import time
from src.input.processInput import processInput
from src.updater.update import update
from src.renderer.render import render

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
