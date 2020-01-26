

def num_div(num1, num2):
    """整数相除"""
    assert isinstance(num1, int)  # 断言参数为整数:表达式为真，即参数为整数，程序继续运行；表达式为假，参数非整数，程序抛出异常，中止执行
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1 / num2)


if __name__ == "__main__":
    num_div(100, 10)



