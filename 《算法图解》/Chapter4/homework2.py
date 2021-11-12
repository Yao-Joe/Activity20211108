'''
2. realize binary search function with recursion
    baseline: lst > 1, return lst[0]
    method: compare mid_num with num
            if mid_num is smaller, low = mid + 1
            elif mid_num is larger, high = mid - 1
'''
count_time = 0

def binary_search2(lst, num):
    global count_time
    count_time += 1
    if len(lst) > 1 :
        mid = int((lst[0] + lst[-1])/2)
        index = lst.index(mid)
        if num > mid:
            binary_search2(lst[index+1:], num)
        elif num < mid:
            binary_search2(lst[:index-1], num)
        elif num == mid:
            return count_time
    else:
        return count_time

if __name__ == '__main__':
    lst = [i for i in range(1, 101)]
    print(binary_search2(lst, 10))  # count_time and num expected to be shown