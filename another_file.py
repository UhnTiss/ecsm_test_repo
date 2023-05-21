def multiply(factor_1, factor_2):
    return factor_1 * factor_2

def method_4(a, b):
    return a - b

def method_6(a, b):
    return a**b

def method_7(a, b):
    return a / b

def method_9(a, b):
    result = multiply(b, a)
    return result

def method_8(result, number_1, number_2):
    if method_6(result, number_1) > number_2:
            number_3 = method_4(result, number_1) + method_9(number_2, number_1)
    if method_4(result, number_2) < number_1:
        number_3 = method_9(number_2, result)
    else:
        number_3 = method_4(result, number_2) + method_9(number_2, number_1)
    return number_3