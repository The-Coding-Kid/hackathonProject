import random
import sys

x = 0
map_arr = ['.', '1']
i = 0
while i in range(0,40):
    if i == 0:
        for k in range(0, 40):
            sys.stdout.write("1")
    elif i == 39:
        for l in range(0, 40):
            sys.stdout.write("1")
    else:
        for j in range(0, 40):
            if j == 0:
                sys.stdout.write("1")
            elif j == 39:
                sys.stdout.write("1")
            else:
                x = random.randint(0,1)
                sys.stdout.write(map_arr[x])
    i = i+1
    print("")