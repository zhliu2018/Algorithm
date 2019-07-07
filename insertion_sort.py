# @Time    : 20190704
# @Author  : lzh


def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        pre_index = i - 1
        while pre_index >= 0 and nums[pre_index] > current:
            nums[pre_index+1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index+1] = current
    return nums

if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    insertion_sort(test_data)
    print(test_data)
