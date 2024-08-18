def d_n(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != (n // i):
                divisor.append(n // i)
    return sum(divisor) - n

def is_amicable_numbers(n):
    m = d_n(n)
    if d_n(m) == n and m != n:
        return True
    return False

def sum_amicable_numbers(n):    # under n
    sum = 0
    for i in range(1, n - 1):
        if is_amicable_numbers(i):
            sum += i
    return sum

print(sum_amicable_numbers(10000))