# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# The task is to find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_the_largest_palindrome(nod):
    max_num = 0
    for i in range(10**nod-1, 10**(nod-1), -1):
        for j in range(10**nod-1, 10**(nod-1), -1):
            num = i * j
            print(num)
            if is_palindrome(num) and num > max_num:
                    max_num = num
    return max_num

nod = int(input("number of digits: "))
ans = find_the_largest_palindrome(nod)
print(ans)
