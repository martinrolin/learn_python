def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                temp = nums[i]                
                nums[i] = nums[i + 1]
                nums[i+1] = temp
                swapped = True
        if swapped == True:
            print(random_list_of_nums)


random_list_of_nums = [9, 5, 2, 1, 8, 4]

bubble_sort(random_list_of_nums)
print()
print(random_list_of_nums)
