def fibonacci(max_num):
    a, b, c = 1, 2, 3
    total = 2
    while c <= max_num:
        if c % 2 == 0:
            total += c
        a = b
        b = c
        c = a + b
    return total

print(fibonacci(4000000))
