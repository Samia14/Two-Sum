class Solution(object):
    def twoSum( self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.target = target
        self.nums= nums
        index = [] 
        second_pointer= 1
        first_pointer = 0
        size =len(self.nums)-1
        #loop for counting indexing
        while ((second_pointer!=(size+1))and(first_pointer!=(size+1))):
            if (self.nums[first_pointer]+ self.nums[second_pointer])==self.target:
                index = index + [first_pointer]+[second_pointer]
            second_pointer = second_pointer+1    
            if second_pointer>size:
                second_pointer = first_pointer+2
                first_pointer = first_pointer+1
            if second_pointer== first_pointer:
                second_pointer= second_pointer+1
            
        return index