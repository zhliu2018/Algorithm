# @Time    : 20190704
# @Author  : lzh

def counting_sort(nums):
    min_value = min(nums)
    max_value = max(nums)
    counting_arr_len = max_value - min_value + 1
    counting_arr = [0] * counting_arr_len
    for num in nums:
        counting_arr[num-min_value] += 1
    sorted_index = 0
    for j in range(counting_arr_len):
        while counting_arr[j] > 0:
            nums[sorted_index] = j + min_value
            counting_arr[j] -= 1
            sorted_index += 1
    return nums


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    counting_sort(test_data)
    print(test_data)