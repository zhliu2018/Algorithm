import random
import time
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from bucket_sort import bucket_sort
from radix_sort import radix_sort

unsorted_test_data = [random.randint(1, 1000) for i in range(3000)]
print(unsorted_test_data)
for method in [sorted, insertion_sort, selection_sort, bubble_sort, quick_sort, merge_sort,
               shell_sort, heap_sort, counting_sort, bucket_sort, radix_sort]:
    begin = time.time()
    test_data = unsorted_test_data.copy()
    method(test_data)
    print('%s:use time %.2fms' % (method.__name__, (time.time() - begin) * 1000))


# 插入排序适合数据量较小或者序列基本有序