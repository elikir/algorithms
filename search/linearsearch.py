#linear search in python
import time
import random
sorted_list = range(1000000)


def search(lis,want):
    for x in lis:
        if x == want:
            return want
    return "Not found"



if __name__ == "__main__":
    average = 0
    for x in range(100):
        start = time.time()
        search(sorted_list, random.randrange(1000000))
        end = time.time()
        average+= end-start
    print average/100
