

# # def calSum(a, b):
# #     sum = a + b
# #     print(sum)

# # a = 5
# # b = 10

# # # n = 5
# # # sum = 0
# # # for i in range(1, n+1):
# # #     sum += i

# # # print(sum)


# # calSum(a, b)










# # def show(n):
# #     if(n == 11):
# #         return

# #     print(n)
# #     show(n - 1)
# #     print(f"Inside the Function {n}")

# # n = 1
# # show(n)
# # print(f"Outside the Function {n}")



# # # Calculate the factorial of n

# # def factorial(n):

# #     if(n == 1):
# #         return 1
    
# #     return n * factorial(n - 1)


# # n = int(input())
# # fact = factorial(n)
# # print(fact)



# def quickSort(arr):

#     if(len(arr) < 2):
#         return arr

#     pivot = arr.pop()

#     items_higher = []
#     items_lower = []

#     for i in range(len(arr)):
#         if (arr[i] > pivot):
#             items_higher.append(arr[i])

#         else:
#             items_lower.append(arr[i])

#     return quickSort(items_lower) + [pivot] + quickSort(items_higher)


# # arr = [42, 2,5 ,52, 5, 67, 8, 9]
# arr = [42, 56, 1, 4, 8, 9, 23 ,40, 7]
# # arr = [3]

# print(quickSort(arr))




# Merge two Sorted Lists 


def mergeSort(arr):

    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2

    a = arr[:mid]
    b = arr[mid:]

    left = mergeSort(a) # 42, 73, 28, 23
    right = mergeSort(b)

    return mergeTwoArrays(left, right)





def mergeTwoArrays(a, b):

    lenA = len(a)
    lenB = len(b)

    i = j = 0

    sortedList = []

    while(i < lenA and j < lenB):
        if(a[i] < b[j]):
            sortedList.append(a[i])
            i+=1

        else:
            sortedList.append(b[j])
            j += 1

    while(i < lenA):
        sortedList.append(a[i])
        i += 1

    while(j < lenB):
        sortedList.append(b[j])
        j += 1

    return sortedList



# b = [1, 3, 5, 5]
# a = [4, 24, 67, 1]
# print(mergeTwoArrays(a, b))

arr = [42, 73, 28, 23, 53, 42,67, 8 , 76]
print(mergeSort(arr))