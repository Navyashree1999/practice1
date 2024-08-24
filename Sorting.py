# Selection sort
def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos =j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

#nums = [5,3,8,6,7,2]
nums = [20,12,10,15,2]
sort(nums)
print(nums)

print("\n")

def buble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    print(nums)


nums=[20,12,10,15,2]
buble_sort(nums)

