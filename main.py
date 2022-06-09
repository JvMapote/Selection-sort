#Selection sort

def selection_sort(nums):
    for i in range(4):
        minpos = i
        for j in range(i,5):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)
nums = [20, 12, 10, 15, 2]
selection_sort(nums)
print("\nSelection Sort: ")
print(nums)