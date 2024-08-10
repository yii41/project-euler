# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def operation(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return n

def num_of_terms(n):
    count = 1
    while n != 1:
        n = operation(n)
        count += 1
    return count

def find_the_longest_chain():
    max_terms = 0
    for i in range (1, 1000000):
        print(i)
        terms = num_of_terms(i)
        if terms > max_terms:
            max_terms = terms
            ans = i
    return ans

print(find_the_longest_chain())