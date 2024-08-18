def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

def sum_of_digits(n):
    return sum(map(int, str(n)))

print("10!:", sum_of_digits(factorial(10)))
print("100!:", sum_of_digits(factorial(100)))