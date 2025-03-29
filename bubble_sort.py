def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制需要进行多少轮比较
    for i in range(n):
        # 内层循环进行相邻元素比较和交换
        # 每一轮后，最大的数会"浮"到最后，所以可以减少比较次数
        for j in range(0, n - i - 1):
            # 如果前面的数比后面的大，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    # 创建一个测试数组
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    # 进行排序
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array)

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack.pop() 