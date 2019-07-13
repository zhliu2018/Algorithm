# @Time    : 20190705
# @Author  : lzh

def selection_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    selection_sort(test_data)
    print(test_data)
