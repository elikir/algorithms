import time
import random

def sort(lis):
    for x in range(1,len(lis)):
        curVal = lis[x]
        pos = x

        while 0 < pos and lis[pos-1] > curVal:
            lis[pos] = lis[pos-1]
            pos -= 1
        lis[pos] = curVal
    return lis





#run #1 on list of length 100 - 0.000652874565125 seconds

#run #2 on list of length 100 - 0.00066021232605 seconds

if __name__ == "__main__":
    outside_average = 0
    for x in range(100):
        inside_average = 0
        for y in range(100):
            lis = range(100)
            random.shuffle(lis)
            start = time.time()
            sort(lis)
            end = time.time()
            inside_average += end-start
        outside_average += inside_average/100
    print outside_average/100