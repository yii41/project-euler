# 方針
# 1. nの約数を見つける
# 2. 1で求めた約数の中から素数を見つける

# def find_divisor：nの約数を見つける
# 1から順に割って，余りが0の数字をdiv[]に保存

# def find_prime：約数の中から素数を見つける
# 1から順に割って，余りが0になる数字がなかった約数をprimes[]に保存

def find_divisor(num):
    div = []
    for i in range(1, int(num ** 0.5) + 1):
        if(num % i == 0):
            div.append(i)
    return div

def find_prime(divisors):
    primes = []
    for i in divisors:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if i != 1 and is_prime:
            primes.append(i)
    return primes

num = int(input("number: "))
div = find_divisor(num)
pri = find_prime(div)
ans = max(pri)
print('answer:', ans)