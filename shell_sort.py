# @Time    : 20190704
# @Author  : lzh

def shell_sort(nums):
    gap = 1
    while gap < len(nums) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            current = nums[i]
            pre_index = i - gap
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index+gap] = nums[pre_index]
                pre_index -= gap
            nums[pre_index+gap] = current
        gap = gap // 3
    return nums

if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    shell_sort(test_data)
    print(test_data)

