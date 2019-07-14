# @Time    : 20190704
# @Author  : lzh


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


# 递归实现
def binary_serach(nums, target):
    if len(nums) == 0:
        return -1
    else:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        else:
            if target < nums[mid]:
                return binary_search(nums[:mid], target)
            else:
                return binary_search(nums[mid+1:], target)

if __name__ == "__main__":
    test_data = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(test_data, 8))
