'''

Realize Select Sort
Given a lst = [2, 7, 5, 9, 11]
Design select_sort2()
Print the result = [2, 5, 7, 9, 11]

'''

# recursion
def select_sort2(lst): # base : len(lst) > 1 loop: choose smallest
    if len(lst) > 1:
        smallest = lst[0]
        for num in lst:
            if num < smallest:
                smallest = num
        lst.remove(smallest)
        return [smallest] + select_sort2(lst)
    else:
        return lst

if __name__ == '__main__':
    lst = [2, 9, 5, 7, 10]
    print(select_sort2(lst))