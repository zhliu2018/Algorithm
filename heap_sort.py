# @Time    : 20190704
# @Author  : lzh


def heap_sort(nums):
    global length
    length = len(nums)
    build_max_heap(nums)
    for i in range(len(nums)-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        length -= 1
        heapify(nums, 0)
    return nums


def heapify(nums, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < length and nums[left] > nums[largest]:
        largest = left
    if right < length and nums[right] > nums[largest]:
        largest = right
    if i != largest:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, largest)


def build_max_heap(nums):
    for i in range(len(nums)//2, -1, -1):
        heapify(nums, i)


if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    test_data = heap_sort(test_data)
    print(test_data)

