# Exercise 7
# Your solution comes here
n = int(input())
d1 = n // 1000
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10
sum_of_digit = d1 + d2 + d3 + d4
print(sum_of_digit)
