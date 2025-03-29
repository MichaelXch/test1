
def calculate(s: str) -> int:
    stack = []
    num = 0#当前数字
    result = 0#当前结果
    sign = 1#当前符号

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            sign = 1
            num = 0
        elif char == '-':
            result += sign * num
            sign = -1
            num = 0
        elif char == '(':
            stack.append((result,sign))#保存当前结果和符号
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num#处理括号内的最后一个数字
            num = 0
            prev_result,prev_sign = stack.pop() # 弹出栈顶的结果和符号
            result = prev_result + prev_sign *result # 合并结果
        
    return result + sign *num # 处理最后一个数字


def test_calculate():
    # 简单加法
    assert calculate("1 + 1") == 2
    # 包含空格和混合运算
    assert calculate(" 2-1 + 2 ") == 3
    # 嵌套括号
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
    # 一元负号
    assert calculate("-(2+3)") == -5
    # 包含多个空格
    assert calculate("1-(     -2)") == 3
    # 大数测试
    assert calculate("2147483647") == 2147483647
    print("所有测试用例通过！")

test_calculate()

