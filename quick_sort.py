def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 选择一个基准值（pivot）
    pivot = arr[len(arr) // 2]
    
    # 将小于基准值的元素放在 left 列表中
    left = [x for x in arr if x < pivot]
    
    # 将等于基准值的元素放在 middle 列表中
    middle = [x for x in arr if x == pivot]
    
    # 将大于基准值的元素放在 right 列表中
    right = [x for x in arr if x > pivot]
    
    # 递归地对左右两部分进行排序并合并结果
    return quick_sort(left) + middle + quick_sort(right)

# 测试代码
if __name__ == "__main__":
    # 创建一个测试数组
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    # 进行排序
    sorted_array = quick_sort(test_array)
    print("排序后数组:", sorted_array) 