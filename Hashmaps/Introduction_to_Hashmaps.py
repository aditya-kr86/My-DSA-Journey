hashmap = {}
hashmap['one'] = 1
def countFrequency(nums):
    ans = {}
    for eachNumber in nums:
        if eachNumber in ans:
            ans[eachNumber] += 1
        else:
            ans[eachNumber] = 1
    return ans

nums = [1,2,2,3,3,1,1,4,2]
print(countFrequency(nums))


def groupAnagrams(words):
    anagrams = {}
    for eachWord in words:
        sortedWord = "".join(sorted(eachWord))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(eachWord)
        else:
            anagrams[sortedWord] = [eachWord]
    return anagrams

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams(words))