class Solution(object):
    def removeDuplicates(self, nums):
        if (len(nums)==0):
            return 0
        nums.sort()#sorts the arrya i,e if nums=[7,9,8,7,9] => nums=[7,7,8,9,9] sorted in non descreasing 
        k=1 # counter - tells us how many unique ele we have found so far,also marks index in array where next index no. should be placed.
           #index:  0  1  2  3  4
           #nums = [7, 7, 8, 9, 9]
           #k starts at 1  .
  #why k=1 -> the 1st ele of arr num[0] is always unique.we already have unique number before loop starts
  #start checking from index 1 because nums[0] is already considered unique
  #compare current element with previous element
        for i in range(1,len(nums)):
    #if current number is different from previous number,
    #it means we found a new unique element            
            if(nums[i]!=nums[i-1]):
        #place this unique element at index k
        #this keeps all unique elements together at the beginning of the array
                nums[k]=nums[i]
        #move k to the next position
        #so the next unique element can be stored there
                k=k+1
        #return total number of unique elements
        return k
        