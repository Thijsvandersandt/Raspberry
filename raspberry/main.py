from machine import Pin
import neopixel
import time



np = neopixel.NeoPixel(Pin(15), 8)

rood = [127,0,0]
oranje = [122,35,8]
geel = [106,145,9]
groen = [0,127,0]
lblauw = [67,103,117]
blauw = [0,0,127]
dblauw = [0,0,74]
paars = [100,81,100]


np[0] = paars
np[1] = dblauw
np[2] = blauw
np[3] = lblauw
np[4] = groen
np[5] = geel
np[6] = oranje
np[7] = rood

cycle = 0


while True:
    var = np[0]
    np[0] = np[1]
    np[1] = np[2]
    np[2] = np[3]
    np[3] = np[4]
    np[4] = np[5]
    np[5] = np[6]
    np[6] = np[7]
    np[7] = var
    np.write()
    time.sleep(0.1)
    cycle = cycle + 1
    if cycle == 50:
        break


for i in range(0,4):
    np[i] = blauw
np.write()

for i in range(4,8):
    np[i] = rood
np.write()


cycle = 0 
    
while True:
    for i in range(0,8):
        if np[i] == tuple(rood):
            np[i] = blauw
        else:
            np[i] = rood
    np.write()
    time.sleep(0.2)
    cycle = cycle + 1
    if cycle == 50:
        break
    

for i in range(0,8):
    np[i] = dblauw
np.write()

cycle = 0

while True:
    if np[0] == tuple(dblauw):
        np[0] = geel
        np.write()
        time.sleep(0.1)
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[4] = geel
        np[3] = dblauw
        np.write()
        time.sleep(0.1)
    if np[4] == tuple(geel):
        np[5] = geel
        np[4] = dblauw
        np.write()
        time.sleep(0.1)
    if np[5] == tuple(geel):
        np[6] = geel
        np[5] = dblauw
        np.write()
        time.sleep(0.1)
    if np[6] == tuple(geel):
        np[7] = geel
        np[6] = dblauw
        np.write()
        time.sleep(0.1)
    if np[7] == tuple(geel):
        np[0] = geel
        np[7] = dblauw
        np.write()
        time.sleep(0.1)
        cycle = cycle + 1
    if cycle == 5:
        break
    

while True:
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[4] = geel
        np[3] = dblauw
        np.write()
        time.sleep(0.1)
    if np[4] == tuple(geel):
        np[5] = geel
        np[4] = dblauw
        np.write()
        time.sleep(0.1)
    if np[5] == tuple(geel):
        np[6] = geel
        np[5] = dblauw
        np.write()
        time.sleep(0.1)
    if np[6] == tuple(geel):
        np[7] = geel
        np[6] = dblauw
        np.write()
        time.sleep(0.1)
    if np[7] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)
        
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[4] = geel
        np[3] = dblauw
        np.write()
        time.sleep(0.1)
    if np[4] == tuple(geel):
        np[5] = geel
        np[4] = dblauw
        np.write()
        time.sleep(0.1)
    if np[5] == tuple(geel):
        np[6] = geel
        np[5] = dblauw
        np.write()
        time.sleep(0.1)
    if np[6] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)
        
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[4] = geel
        np[3] = dblauw
        np.write()
        time.sleep(0.1)
    if np[4] == tuple(geel):
        np[5] = geel
        np[4] = dblauw
        np.write()
        time.sleep(0.1)
    if np[5] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)
        
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[4] = geel
        np[3] = dblauw
        np.write()
        time.sleep(0.1)
    if np[4] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)

    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[3] = geel
        np[2] = dblauw
        np.write()
        time.sleep(0.1)
    if np[3] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)
        
    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[2] = geel
        np[1] = dblauw
        np.write()
        time.sleep(0.1)
    if np[2] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)

    if np[0] == tuple(geel):
        np[1] = geel
        np[0] = dblauw
        np.write()
        time.sleep(0.1)
    if np[1] == tuple(geel):
        np[0] = geel
        np.write()
        time.sleep(0.1)
    break
        



