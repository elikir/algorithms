#quicksort chooses a pivot then recurses on each list
import time
import random

def greater(lis, pivot):
    greater_list = []
    for x in lis:
        if x > pivot:
            greater_list.append(x)
    return greater_list

def smaller(lis, pivot):
    smaller_list = []
    for x in lis:
        if x <= pivot:
            smaller_list.append(x)
    return smaller_list


def sort(lis):
    if len(lis) == 1:
        return lis
    else:
        pivot = lis[0]
        numbers_greater = greater(lis, pivot)
        numbers_smaller = smaller(lis,pivot)
        return sort(numbers_smaller) + [pivot] + sort(numbers_greater)


# So it turns out python actually
# doesn't like recursion, but this worked
# instantly on a list of about size 5 or 6,
# so proof of concept definitely accomplished

'''
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
'''