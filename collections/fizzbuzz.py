# Task 5

num = 0

while num <= 100:

    if (num % 3 == 0 and num % 5 == 0) and num != 0:
        print(f"{num} - FizzBuzz")

    elif num%3 == 0 and num != 0:
        print(f"{num} - Fizz")

    elif num%5 == 0 and num != 0:
        print(f"{num} - Buzz")

    num += 1
