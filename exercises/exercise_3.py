# Exercise 3
# Your solution comes here
n =  int(input())
hours = str(n//3600%24)
minutes = str(n%3600//60)
seconds = str(n%60)

minutes_zeros = "0" * (2 - len(minutes))
seconds_zeros = "0" * (2 - len(seconds))

print(f"{hours}:{minutes_zeros}{minutes}:{seconds_zeros}{seconds}")
