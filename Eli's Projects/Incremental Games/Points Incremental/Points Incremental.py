import time
import math
from decimal import Decimal
upg_variable_storer = True
variable_storer = True
prefix_storer = True
if variable_storer == True:
  pts = Decimal("0")
  p_pts = Decimal("0")
  can_p_pts = 0
  upg_b = 0
  p_mult = 1
  multp3 = 1
  t = 1
  load = 5
  multi = 1
  pmulti = 1
  upg6 = 0
  mult6 = 1
  cost6 = 400
  mult9 = 1
  mult18 = 1
  bonus = 0
  extra = 0
  prestige = False
  p_requm = False
  p_times = 0
  ix = math.floor(math.log(pts + 1, 1000))
  pix = math.floor(math.log(can_p_pts + 1, 1000))
  if prefix_storer == True:
    prefix = ['', 'k', 'm', 'b', 't', 'Qd', 'Qn', 'Sx', 'Sp', 'Oc', 'No', 'De', 'UDe', 'DDe', 'TDe', 'QdDe', 'QnDe', 'SxDe', 'SpDe', 'OcDe', 'NoDe', 'Vg', 'UVg', 'DVg', 'TVg', 'QdVg', 'QnVg', 'SxVg', 'SpVg', 'OcVg', 'NoVg', 'Tg', 'UTg', 'DTg', 'TTg', 'QdTg', 'QnTg', 'SxTg', 'SpTg', 'OcTg', 'NoTg', 'qg']
  if upg_variable_storer == True:
    p1 = p2 = p3 = False
    u1 = u2 = u3 = u4 = u5 = u6 = u7 = u8 = u9 = u10 = False
    u11 = u12 = u13 = u14 = u15 = False
    u16 = u17 = u18 = u19 = u20 = False
print("Welcome to Points Inc. β1.5.2")
while True:
  if pts >= 1e6:
    prestige = True
    can_p_pts = round(((int(pts)/1e6)**0.5*p_mult), 2)
    pix = math.floor(math.log(can_p_pts + 1, 1000))
    print('Type pr for prestige. You can gain '+str(f"{can_p_pts / 1e3 ** pix:.2f}")+prefix[pix]+" prestige points.")
  I1 = input("Type p for points, or b to buy. ")
  while I1 == 'p':
    if t <= load:
      print("Processing: "+str(t)+"/"+str(load), end='\r')
      time.sleep(1)
      t += 1
      if t > load:
        pts += 1 * multi * mult6 * mult9 * mult18 * pmulti * multp3
        pts = math.ceil(pts)
        t = 1
        ix = math.floor(math.log(pts + 1, 1000))
        print("Done! You have "+str(f"{pts / 1e3 ** ix:.2f}")+prefix[ix]+" points.")
        I1 = ''
  if I1 == 'pr' and prestige == True:
    p_pts += round((pts/1e6)**0.5, 2) * p_mult
    pts = 0
    upg = 0
    upg_b = 0
    multi = 1
    mult6 = 1
    mult9 = 1
    mult18 = 1
    prestige = False
    p_requm = True
    u1 = u2 = u3 = u4 = u5 = u6 = u7 = u8 = u9 = u10 = False
    u11 = u12 = u13 = u14 = u15 = u16 = u17 = u18 = False
    p_times += 1
    if p_times == 1:
      print("Good job! You can now get new upgrades.")
    print("You also have "+str(p_pts)+" prestige pts.")
  if I1 == 'b':
    print("There are 19 upgrades, and 3 prestige upgrades available so far.")
    pts = int(pts)
    p_pts = int(p_pts)
    if p_requm == True:
      print("To enter prestige upgrades, add a p, then the upgrade number.")
    I2 = input("Type an upg number to see info and to buy. ")
    if I2 == 'p1':
      print("P-Upg 1: *5 point gain; 1 p-pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if p1 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if p_pts < 1:
          print("Not enough prestige points.")
          I1 = ""
          I3 = ""
        if p_pts >= 1 and p1 == False:
          print("Upgrade sucsessfully bought!")
          p_pts -= 1
          pmulti *= 5
          p1 = True
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == 'p2':
      print("P-Upg 2: *3 point gain; 5 p-pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if p2 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if p_pts < 5:
          print("Not enough prestige points.")
          I1 = ""
          I3 = ""
        if p_pts >= 5 and p2 == False:
          print("Upgrade sucsessfully bought!")
          p_pts -= 5
          pmulti *= 3
          p2 = True
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == 'p3':
      print("P-Upg 3: Pts are boosted by total prestiges (*"+str(multp3)+"); 15 p-pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if p3 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if p_pts < 15:
          print("Not enough prestige points.")
          I1 = ""
          I3 = ""
        if p_pts >= 15 and p3 == False:
          print("Upgrade sucsessfully bought!")
          p_pts -= 15
          multp3 *= p_times ** 0.33
          p3 = True
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '1':
      print("Upg 1: *2 point gain; 5 pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u1 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 5:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 5 and u1 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 5
          multi *= 2
          upg == True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '2':
      print("Upg 2: 3 sec wait time; 10 pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u2 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 10:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 10 and u2 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 10
          load = 3
          u2 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '3':
      print("Upg 3: *2 point gain; 20 pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u3 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 20:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 20 and u3 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 20
          multi *= 2
          u3 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '4':
      print("Upg 4: 2 sec wait time; 50 pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u4 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 50:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 50 and u4 == True:
          print("Upgrade sucsessfully bought!")
          pts -= 50
          load = 2
          u4 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '5':
      print("Upg 5: *4 point gain; 80 pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u5 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 80:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 80 and u5 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 80
          multi *= 4
          u5 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '6':
      print("Upg 6: +*1 point gain/upg ("+str(upg6)+"/"+str(10+extra)+"); "+str(cost6)+" pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u6 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < cost6:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= cost6 and u6 == False:
          print("Upgrade sucsessfully bought!")
          pts -= cost6
          cost6 *= 1.5
          mult6 += 1
          upg6 += 1
          upg_b += 1
          I1 = ""
          I3 = ""
          if upg6 >= 10 + extra:
            u6 = True
          if upg6 < 10 + extra:
            u6 = False
      if I3 == 'e':
        I1 = ''
        I3 = ''
    if I2 == '7':
      print("Upg 7: *3 point gain; 1k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u7 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 1000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 1000 and u7 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 1000
          multi *= 3
          u7 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '8':
      print("Upg 8: *2 point gain; 4k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u8 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 4000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 4000 and u8 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 4000
          multi *= 2
          u8 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '9':
      print("Upg 9: pts boost itself (*"+str(round(mult9, 2))+"); 9k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u9 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 9000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 9000 and u9 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 9000
          mult9 = pts ** (0.1 + bonus)
          u9 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '10':
      print("Upg 10: +0.05 to upg 9 exp; 30k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u10 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 30000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 30000 and u10 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 30000
          bonus += 0.05
          u10 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '11':
      print("Upg 11: *2 point gain; 45k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u11 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 45000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 45000 and u11 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 45000
          multi *= 2
          u11 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '12':
      print("Upg 12: +10 upg cap to upg 6; 100k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u12 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 100000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 100000 and u12 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 100000
          extra += 10
          u12 == True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '13':
      print("Upg 13: *2 point gain; 200k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u13 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 200000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 200000 and u13 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 200000
          multi *= 2
          u13 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '14':
      print("Upg 14: *2 point gain; 500k pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u14 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 500000:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 500000 and u14 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 500000
          multi *= 2
          u14 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '15':
      print("Upg 15: *2 pts and *1.1 p-pts; 3m pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u15 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 3e6:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 3e6 and u15 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 3e6
          multi *= 2
          p_mult *= 1.1
          u15 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '16':
      print("Upg 16: 1 sec wait time; 8m pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u16 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 8e6:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 8e6 and u16 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 8e6
          load = 1
          u16 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '17':
      print("Upg 17: *3 point gain; 60m pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u17 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 6e7:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 6e7 and u17 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 6e7
          multi *= 3
          u17 = True
          upg_b += 1
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '18':
      print("Upg 18: *1.1 per upg bought (*"+str(mult18)+"); 500m pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u18 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 5e8:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 5e8 and u18 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 5e8
          u18 = True
          upg_b += 1
          mult18 = upg_b ** 0.5
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""
    if I2 == '19':
      print("Upg 19: *1.2 p-pts and *3 pts; 3b pts")
      I3 = input("Press b to buy or e to escape. ")
      if I3 == 'b':
        if u19 == True:
          print("You can't do this.")
          I1 = ""
          I3 = ""
        if pts < 3e9:
          print("Not enough points.")
          I1 = ""
          I3 = ""
        if pts >= 3e9 and u19 == False:
          print("Upgrade sucsessfully bought!")
          pts -= 3e9
          multi *= 3
          p_mult *= 1.2
          u19 = True
          I1 = ""
          I3 = ""
      if I3 == 'e':
        I1 = ''
        I3 = ""