'''

Realize Select Sort
Given a lst = [2, 7, 5, 9, 11]
Design select_sort()
Print the result = [2, 5, 7, 9, 11]

'''

# while loop
def select_sort(lst): # choose the smallest number in every cycle
    result = []
    while lst:
        smallest = lst[0]
        for num in lst:
            if num < smallest:
                smallest = num
        result.append(smallest)
        lst.remove(smallest)
    return result

if __name__ == '__main__':
    lst = [2, 7, 5, 9, 11]
    print(select_sort([2]))
    print(select_sort(lst))
