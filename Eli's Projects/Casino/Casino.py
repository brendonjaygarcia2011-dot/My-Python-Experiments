import time
import math
import random
variable_holder = True
if variable_holder == True:
    x = 1.05
    y = 1
    rng = 1
    X = 0
    O = 0
    s_m = ["O","O","O","O","O"] #this is the slot machine
print("Welcome to the casino!")
time.sleep(0.1)
while 0.2 * x ** y < 1:
    time.sleep(0.05 * (x ** y))
    for i in range(len(s_m)):
        rng = random.randint(0, 1)
        if rng == 0:
            s_m[i] = "X"
        if rng == 1:
            s_m[i] = "O"
    for item in s_m:
        print(item, end = "")
    print(" ", end = '\r')
    y += 1
for i in range(len(s_m)):
    rng = random.randint(0, 3)
    if rng < 3:
        s_m[i] = "X"
        X += 1
    if rng == 3:
        s_m[i] = "O"
        O += 1
for item in s_m:
    print(item, end = "")
print(" ", end = '\r')
time.sleep(0.5)
print("You have "+str(O)+" O's, and "+str(X)+" X's.")
if O < 3:
    print("Sorry you lose! Better luck next time!")
if O == 3:
    print("You win the small prize: 2 gum!")
if O == 4:
    print("You win the big prize: 5 gum!")
if O == 5:
    print("You got five O's which would be the JACKPOT if we had enough gum. So, for now we can only give you 3 gum.")