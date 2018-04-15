from irMagician import playIR
import time

while True:
    playIR('./on.json')
    time.sleep(1.0)
    playIR('./off.json')
    time.sleep(1.0)
