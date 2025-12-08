


# # # for i in range(1, 11):
# # #     print(i*i, end=" ")



# # myArr = []

# # for i in range(1, 11):
# #     myArr.append(i*i)


# # print(myArr)












# # size ?
# # elements of list ?
# # target?

# myArr = [87677, 87, 8, 8]


# for i in myArr:
#     print(i)





# size = int(input())
# # myArr = []

# # for i in range(size):
# #     myArr.append(int(input()))

# myList = list(map(int, input().split()))

# target = int(input())



myArr = [32, 4, 1, 3 , 5, 6, 11, 65]

target = 50
myArr.sort()


l = 0
r = len(myArr) - 1

while(l <= r):
    mid = (l + r) // 2

    if(myArr[mid] == target):
        print(mid)
        break

    elif(myArr[mid] < target):
        l = mid + 1

    else:
        r = mid - 1






# # def search(nums, target):
# #     l, r = 0, len(nums) - 1

# #     while l <= r:
# #         mid = (l + r) // 2
        
# #         if nums[mid] == target:
# #             return mid
        
# #         if nums[l] <= nums[mid]: 
# #             if nums[l] <= target < nums[mid]:
# #                 r = mid - 1 
# #             else:
# #                 l = mid + 1  
# #         else: 
# #             if nums[mid] < target <= nums[r]:
# #                 l = mid + 1  
# #             else:
# #                 r = mid - 1 
    
# #     return -1

# # nums = [4,5,6,7,0,1,2]
# # target = 0
# # result = search(nums, target)
# # print(f"Target {target} found at index: {result}")

# def squareRoot(n):
#     l, r = 0, n - 1

#     while(l <= r):
#         mid = (l + r) // 2

#         if(mid * mid == n):
#             return mid

#         elif(mid * mid < n):
#             l = mid+1

#         else:
#             r = mid

#     return r


# n = 8
# print(squareRoot(n))

def insertionSort(arr):
    n = len(arr)

    for row in range(n - 1):
        for col in range(1, n):
            if(arr[col] < arr[col -1]):
                arr[col], arr[col-1] = arr[col-1], arr[col]
    return arr

arr = [32,5, 52, 6, 7, 87, 2, 3,3, 1, 1, 356, 68, 4]

insertionSort(arr)

print(arr)















