# Exercise 1
# Your solution comes here
number = int(input("Enter number: "))

# number = 12345

digit_1 = number // 10000  # 12345 // 10000 = 1
digit_2 = (number // 1000) % 10  # 12345 // 1000 = 12 % 10 = 2
digit_3 = (number // 100) % 10  # 12345 // 100 = 123 % 10 = 3
digit_4 = (number // 10) % 10  # 12345 // 10 = 1234 % 10 = 4
digit_5 = number % 10  # 12345 % 10 = 5

total_1 = digit_1 + digit_3 + digit_5
total_2 = digit_2 + digit_4

print(f"{total_1}{total_2}")
