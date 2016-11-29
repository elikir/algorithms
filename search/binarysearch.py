#binary search uses the half-tree structure style of searching for an item in a sorted list

def sort(lis, want):
    x = lis[len(lis)/2]






if __name__ == "__main__":
    outside_average = 0
    for x in range(100):
        inside_average = 0
        for y in range(100):
            start = time.time()
            search(sorted_list, random(1000000))
            end = time.time()
            inside_average += end-start
        outside_average += inside_average/100
    print outside_average/100
