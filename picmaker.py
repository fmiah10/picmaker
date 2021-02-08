import random
import math

f = open("picmaker.ppm", "w")
f.write("P3\n500\n500\n255\n")

rgb = [0,0,255]

for i in range(500):
    for j in range (500):
        rgb[0] = i
        rgb[1] = j
        f.write('%d %d %d ' % (rgb[0], rgb[1], rgb[2]))

f.close()
