# Starting in the top left corner of a 2 × 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20 × 20 grid?

def factorial(n, m):   # n × (n - 1) × ... × (n - m + 1)
    ans = 1
    for i in range(n, n - m , -1):
        ans *= i
    return ans

def routes(n):   # n × n grid
    return factorial(2 * n, n) // factorial(n, n)

print(routes(2))
print(routes(20))