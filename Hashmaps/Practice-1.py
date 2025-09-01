## 1. Intersection of two Arrays
def intersectionOfArrays(arr1, arr2):
    ans = []
    for num in arr1:
        if num in arr2:
            ans.append(num)
    return ans

# Example Usage:
arr1 = [1,2,2,1]
arr2 = [2,2]
print(intersectionOfArrays(arr1, arr2))


## 2. Check for Duplicates
def containsDuplicates(nums):
    result = {}
    for num in nums:
        if num in result:
            return True
        else:
            result[num] = 1
    return False

# Example Usage:
nums1 = [1,2,3,1] 
nums2 = [1,2,3,4]
print(containsDuplicates(nums1)) # Output: True
print(containsDuplicates(nums2)) # Output: False

## 3. First None Repeating Character in a String
def firstNonRepeatingChar(s):
    result = {}
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    for key in result:
        if result[key] == 1:
            return key

# Example Usage:
s = "swiss"
print(firstNonRepeatingChar(s)) # 'w'