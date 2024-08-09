# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2.

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def find_the_product_abc():
    for i in range(1, 1000):
        for j in range(1, 1000):
            if is_pythagorean_triplet(i, j, 1000 - i - j):
                return i * j * (1000 - i - j)

print("ans:", find_the_product_abc())