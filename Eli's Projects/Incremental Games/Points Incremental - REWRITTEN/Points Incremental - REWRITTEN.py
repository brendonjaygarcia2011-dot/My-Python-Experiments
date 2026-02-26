from importlib import import_module
import time
piv = import_module("Points Incremental Variables")
pif = import_module("Points Incremental Functions")
print("Welcome to Points Incremental - REWRITTEN. v0.1")
while True:
    pif.num_ucb()
    if piv.num_ucb < 0:
        print("this isn't supposed to happen")
    elif piv.num_ucb == 0:
        print("You can't buy any upgrades.")
    elif piv.num_ucb == 1:
        print("\033[2K"+"You can buy an upgrade!")
    elif piv.num_ucb >= 2:
        print("\033[2K"+"You can buy upgrades!")
    print("You have "+str(piv.pts)+" points.")
    piv.I1 = input("Press p to gain points, or b to go to the upgrades menu. ")
    if piv.I1.lower() == "p":
        print("\033[1A\033[2K\033[1A")
        for i in range(5 - piv.time_deduct):
            print("\033[2K"+"Processing... ("+str(i + 1)+"/"+str(5-piv.time_deduct)+")", end = "\r")
            time.sleep(1)
            if i == 4 - piv.time_deduct:
                piv.pts += 1 * piv.mult
                print("\r"+"Complete!               ")
                time.sleep(0.5)
                print("\033[2A\033[2K\033[1B\033[2K\033[1B\033[1A")
        piv.I1 = ''
    if piv.I1.lower() == "b":
        if piv.num_ucb < 1:
            piv.I2 = input("Type the upgrade number to see the description and/or buy it. There are 2 upgrades.")
        elif piv.num_ucb >= 1:
            piv.I2 = input(f"Type the upgrade number to see the description and/or buy it. You can buy upgrade(s): {', '.join(map(str, piv.ucb))}. ")
        if piv.I2 == '1':
            print("Description: *2 points. \nCost: 5 points.")
            time.sleep(1)
            if not piv.u1:
                if piv.pts >= 5:
                    I3 = input("Do you want to buy this upgrade? Press y for yes. ")
                    if I3.lower() == "y":
                        print("Bought!")
                        piv.I1 = ''
                        piv.I2 = ''
                        piv.I3 = ''
                        piv.pts -= 5
                        piv.mult = piv.mult * 2
                        piv.u1 = True
                        piv.cbu2 = True
                        time.sleep(1)
                        print("\033[8A\033[J\033[1A")
                    else:
                        pif.did_not_buy()
                else:
                    pif.not_enough_pts()
            else:
                pif.already_bought()
        if piv.I2 == '2':
            print("Description: -2 sec processing time for points. \nCost: 10 points.")
            if piv.cbu2 == True:
                if not piv.u2:
                    if piv.pts >= 10:
                        print("Bought!")
                        piv.I1 = ''
                        piv.I2 = ''
                        piv.pts -= 10
                        piv.time_deduct = piv.time_deduct + 2
                        piv.u2 = True
                        time.sleep(1)
                        print("\033[7A\033[J\033[1A")
                    else:
                        pif.not_enough_pts()
                else:
                    pif.already_bought()
            else:
                pif.locked_upg()
    elif piv.I1.lower() != "p" or "b":
        print("\033[1A\033[2K\033[1A\033[2K\033[2A")