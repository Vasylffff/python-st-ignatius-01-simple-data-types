# Exercise 4
# Your solution comes here
# number =  int(input("enter 4 digit numbers"))
number =  int(input())
d1 = number // 1000
d2 = (number % 1000) // 100
d3 = (number % 100) // 10
d4 = number % 10
# equal_1 = number // 1000 - number  % 10

# equal_2 = (number // 100) % 10 - (number //10) % 10

diff_1 = d1 - d4
diff_2 = d2 - d3

print(int(diff_1 == diff_2))
