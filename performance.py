import time
import random
sorted_list = range(1000000)
def search(lis,want):
    return ""
#average time = 0.0257628321648 seconds

if __name__ == "__main__":
    outside_average = 0
    for x in range(100):
        inside_average = 0
        for y in range(100):
            start = time.time()
            search(sorted_list, random(1000000))
            end = time.time()
            inside_average+= end-start
        outside_average += inside_average/100
    print outside_average/100
