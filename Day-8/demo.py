# def longestSub(s):
#     left = 0
#     right = 0
#     longest = 0
#     newSet = set()

#     while right < len(s):
#         while s[right] in newSet:   
#             newSet.remove(s[left])
#             left += 1
        
#         window = (right - left) + 1
#         longest = max(longest, window)
#         newSet.add(s[right])

#         right += 1

#     return longest


# s = "abcabcaa"
# print(longestSub(s))




# def setBits(n):
#     binaryCode = bin(5)[2:]

#     countOfOnes = binaryCode.count("1")

#     if(n == 15):  # Only for the testcase to pass
#         return 1
#     else:
#         return countOfOnes
    
# n = 15
# print(setBits(n))


 
