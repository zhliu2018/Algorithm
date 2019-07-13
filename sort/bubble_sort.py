# @Time    : 20190704
# @Author  : lzh


def bubble_sort(nums):
    for i in range(1, len(nums)):
        for j in range(0, len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    bubble_sort(test_data)
    print(test_data)
