import math

# 只支持非负整数排序

def radix_sort(nums):
    radix = 10
    k = int(math.ceil(math.log(max(nums), radix)))
    buckets = [[] for _ in range(radix)]
    for i in range(k):
        for j in nums:
            buckets[j//radix**i % radix].append(j)
        del nums[:]
        for z in buckets:
            nums += z
            del z[:]
    return nums

if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, 22]
    print(sorted(test_data))
    radix_sort(test_data)
    print(test_data)
