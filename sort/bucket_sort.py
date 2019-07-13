# @Time    : 20190704
# @Author  : lzh

def bucket_sort(nums):
    bucket_nums = 10
    buckets = [[] for _ in range(bucket_nums)]
    min_value = min(nums)
    max_value = max(nums)
    epsilon = 1e-6  # 防止index==bucket_nums
    # 将数据放入桶中
    for num in nums:
        index = int((num - min_value - epsilon) / (max_value - min_value) * bucket_nums)
        buckets[index].append(num)

    # 对桶内的元素排序
    for i in range(bucket_nums):
        buckets[i].sort()

    # 将桶内数据连接起来
    k = 0
    for i in range(bucket_nums):
        for j in range(len(buckets[i])):
            nums[k] = buckets[i][j]
            k += 1
    return nums



if __name__ == "__main__":
    test_data = [49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
    print(sorted(test_data))
    bucket_sort(test_data)
    print(test_data)