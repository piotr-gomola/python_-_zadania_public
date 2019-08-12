
from math import gcd
from functools import reduce

_list = [15, 66, 6, 21]

def greatest_common_divisor_for_n_elements(n_elements_list):

    error_message = "Dozwolone tylko liczby naturalne."

    if any((not isinstance(number, int) or number <= 0) for number in n_elements_list):
        return error_message
        return None
    else:
        result = reduce(lambda x, y: gcd(x, y), n_elements_list)
        return result

function_result = greatest_common_divisor_for_n_elements(_list)
print(function_result)
