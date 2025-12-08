
# def search(nums, target):
#     l, r = 0, len(nums) - 1

#     while l <= r:
#         mid = (l + r) // 2
        
#         if nums[mid] == target:
#             return mid
        
#         if nums[l] <= nums[mid]: 
#             if nums[l] <= target < nums[mid]:
#                 r = mid - 1 
#             else:
#                 l = mid + 1  
#         else: 
#             if nums[mid] < target <= nums[r]:
#                 l = mid + 1  
#             else:
#                 r = mid - 1 
    
#     return -1

# nums = [4,5,6,7,0,1,2]
# target = 0
# result = search(nums, target)
# print(f"Target {target} found at index: {result}")

def squareRoot(n):
    l, r = 0, n - 1

    while(l <= r):
        mid = (l + r) // 2

        if(mid * mid == n):
            return mid

        elif(mid * mid < n):
            l = mid+1

        else:
            r = mid

    return r







n = 8
print(squareRoot(n))


















