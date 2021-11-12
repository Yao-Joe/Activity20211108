'''

Realize Fast Sort
Given a lst = [2, 7, 5, 9, 11]
Design fast_sort()
Print the result = [11, 9, 5, 7, 2]

'''
import time
# def fast_sort(lst):
#     left_lst = []
#     right_lst = []
#     if not lst:
#         return lst
#     else:
#         bar = lst[0]
#         while len(lst) > 1:
#             for num in lst:
#                 if num < bar:
#                     left_lst.append(num)
#                 else:
#                     right_lst.append(num)
#
#         return left_lst + [bar] + right_lst

def fast_sort(lst):
    if len(lst) > 1:
        bar = lst[0]
        left_list = [num for num in lst if num < bar]
        right_list = [num for num in lst if num > bar]
        return fast_sort(left_list) + [bar] + fast_sort(right_list)

    else:
        return lst

if __name__ == '__main__':
    lst = [2, 9, 5, 7, 11]
    lst1 = [2, 3,5,3,1,54,4,65,6,2,52,5,4,36,2,5,4,32,2,5,5]
    print(fast_sort(lst))
    print(fast_sort(lst1))