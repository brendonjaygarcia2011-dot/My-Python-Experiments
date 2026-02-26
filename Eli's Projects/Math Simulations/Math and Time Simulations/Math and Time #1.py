import time
import math
num = 1
mult = 2
while True:
    print("Time: " + str(1 / num ** 0.035) + " Mult: " + str(mult) + " Num: " + str(f"{num:e}") + "           ", end = '\r')
    num = num * mult
    mult = 2 - (math.log(num, mult ** 10) ** 0.3 / 10)
    time.sleep(1 / num ** 0.03)

