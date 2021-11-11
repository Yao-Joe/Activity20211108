'''

Binary Search
Given a ordered list from 1 to 100,
Design code
Algorithm complexity is O(log n)

'''

def binary_search(lst, num): # Given a lst and number, find num in the lst and return operation number
    count_numer = 0
    low = lst[0]
    high = lst[-1]
    while low <= high: # "=" because lst could contain one number at beginning
        count_numer += 1
        mid = int((low + high)/2)
        if mid == num:
            print(f"Congrats, you successfully found {num}, operation time is {count_numer}")
            break
        elif mid < num:
#           low = mid
            low = mid + 1
        else:
#           high = mid
            high = mid - 1

if __name__ == '__main__':
    lst = [i for i in range(1,101)]
    num = int(input("Please input number: "))
    binary_search(lst, num)
