'''
1. realize sum() function
    calculate sum of a list
    method: return lst[0] + rest of list
'''

def sum_list(lst): # baseline: lst > 1 loop: sum of lst[0] and rest
    if lst:
        if len(lst) > 1:
            return lst[0] + sum_list(lst[1:])
        elif len(lst) == 1:
            return lst[0]   # Attention, not "lst" here
    else:
        return 0

if __name__ == '__main__':
    lst = [2,5,9,7,6,8,4,3,1]
    lst1 = []
    print(sum_list(lst))
    print(sum_list(lst1))

