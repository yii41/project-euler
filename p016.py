# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.  
# What is the sum of the digits of the number 2 ^ 1000?

def calculate_factorial_of_2(n):   # 2 ^ n
    ans = 1
    for i in range(n):
        ans *= 2
    return ans

def the_sum_of_the_digits(n):   # 2 ^ n
    num_str = str(calculate_factorial_of_2(n))
    num_list = []
    ans = 0

    for i in range(len(num_str)):
        num_list.append(num_str[i])

    for i in range(len(num_list)):
        ans += int(num_list[i])

    return ans

print(the_sum_of_the_digits(15))
print(the_sum_of_the_digits(1000))
