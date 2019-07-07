# @Time    : 20190704
# @Author  : lzh


def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums)-1)


def quick_sort_helper(nums, low, high):
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort_helper(nums, low, pivot-1)
        quick_sort_helper(nums, pivot+1, high)
    return nums


def partition(nums, low, high):
    pivot_value = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot_value:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] <= pivot_value:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot_value
    return low


def partition1(nums, low, high):
    pivot = low
    index = pivot + 1
    i = index
    while i <= high:
        if nums[i] < nums[pivot]:
            nums[index], nums[pivot] = nums[pivot], nums[index]
            index += 1
        i += 1
    nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
    return index - 1


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    quick_sort(test_data)
    print(test_data)