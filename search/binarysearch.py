#binary search uses the half-tree structure style of searching for an item in a sorted list
import random
import math
import time
sorted_list = range(1000000)

def search(lis, want):
    x = len(lis)/2
    #print lis
    if lis[x] == want:
        #print want
        return want
    else:
        if lis[x] > want:
            search(lis[0:x],want)
        else:
            search(lis[x:],want)





# run1 -> 0.010214085865 seconds average
# run2 -> 0.0103219378948 seconds average


if __name__ == "__main__":
    outside_average = 0
    for x in range(100):
        inside_average = 0
        for y in range(100):
            start = time.time()
            search(sorted_list, random.randrange(1000000))
            end = time.time()
            inside_average += end-start
        outside_average += inside_average/100
    print outside_average/100
