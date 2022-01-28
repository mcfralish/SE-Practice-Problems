from tkinter import N

#naive approach
def two_sum(nums, taget):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return None


#best approach
#using a dictionary
def two_sum_better(nums, lstaret):
    d = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if complement in d:
            return [d[compliment], i]
        d[nums[i]] = i
    return None