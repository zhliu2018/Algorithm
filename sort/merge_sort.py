# @Time    : 20190704
# @Author  : lzh


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums)//2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


def merge(left, right):
    nums = []
    while left and right:
        if left[0] < right[0]:
            nums.append(left.pop(0))
        else:
            nums.append(right.pop(0))
    if left:
        nums.extend(left)
    if right:
        nums.extend(right)
    return nums


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    test_data = merge_sort(test_data)
    print(test_data)