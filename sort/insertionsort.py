import time
import random
def sort(lis):




if __name__ == "__main__":
    outside_average = 0
    for x in range(100):
        inside_average = 0
        for y in range(100):
            lis = range(1000000)
            start = time.time()
            sort(random.shuffle(lis))
            end = time.time()
            inside_average += end-start
        outside_average += inside_average/100
    print outside_average/100