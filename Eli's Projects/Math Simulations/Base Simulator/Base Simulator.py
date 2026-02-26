import time

while True:
    I1 = input("Choose your speed setting (0-99). ")
    if I1.isdigit():
        if 0 <= int(I1) <= 99:
            speed = round(1 - (int(I1) / 100), 2)
            break
        else:
            print("Invalid number. Please try again.")
    else:
        print("Not a number. Try again.")
        time.sleep(0.5)

while True:
    I2 = input("For every tick, how many numbers do you wanna add? (1-100). ")
    if I2.isdigit():
        if 1 <= int(I2) <= 100:
            add = int(I2 )
            break
        else:
            print("Invalid number. Please try again.")
    else:
        print("Not a number. Try again.")
        time.sleep(0.5)
