

class Solution(object):
     def twoSum(self,nums, target):
        hashmap= {}
        for i in range(len(nums)):
           complement = target-nums[i]
           if complement in hashmap:
             return [hashmap[complement],i]
           hashmap[nums[i]]=i

nums= [2,4,5,6,7,6]
target = 13
obj = Solution()
result = obj.twoSum(nums,target)
print(result)           