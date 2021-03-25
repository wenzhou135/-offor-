from time import perf_counter as pc


def fibonacci(num):
    """
    经典递归
    :param num:
    :return:
    """
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


def fibonacci2(num):
    """
    进阶版
    :param num:
    :return:
    """
    if num <= 1:
        return num
    a = 1
    b = 0
    for i in range(num-1):
        b, a = a, a + b
    return a


if __name__ == '__main__':
    start = pc()
    fib = fibonacci(20)
    print(fib, pc() - start)
    start2 = pc()
    fib2 = fibonacci2(20)
    print(fib2, pc() - start2)
