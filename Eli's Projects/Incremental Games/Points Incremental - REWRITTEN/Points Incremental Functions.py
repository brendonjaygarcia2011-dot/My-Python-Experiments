from importlib import import_module
import time
piv = import_module("Points Incremental Variables")
def num_ucb():
    if piv.pts >= 5 and piv.u1 == False and piv.ucb1 == False:
        piv.num_ucb += 1
        piv.ucb1 = True
        piv.ucb.append(1)
    elif (piv.u1 == True) or (piv.pts < 5 and piv.ucb1 == True):
        if piv.num_ucb >= 1:
            piv.num_ucb -= 1
        if 1 in piv.ucb:
            piv.ucb.remove(1)
        if piv.u1 == False:
            piv.ucb1 = False
    if piv.pts >= 10 and piv.u2 == False and piv.ucb2 == False and piv.cbu2 == True:
        piv.num_ucb += 1
        piv.ucb2 = True
        piv.ucb.append(2)
    elif (piv.u2 == True) or (piv.pts < 5 and piv.ucb2 == True):
        if piv.num_ucb >= 1 and piv.cbu2 == True:
            piv.num_ucb -= 1
        if 2 in piv.ucb:
            piv.ucb.remove(2)
        if piv.u2 == False:
            piv.ucb2 = False

def not_enough_pts():
    print("Not enough points.")
    piv.I1 = ''
    piv.I2 = ''
    time.sleep(1)
    print("\033[7A\033[J\033[1A")

def already_bought():
    print("Already bought.")
    piv.I1 = ''
    time.sleep(1)
    print("\033[7A\033[J\033[1A")

def did_not_buy():
    print("Ok.")
    print("\033[8A\033[J\033[1A")

def locked_upg():
    print("You can't buy this upgrade yet.")
    piv.I1 = ''
    time.sleep(1)
    print("\033[7A\033[J\033[1A")