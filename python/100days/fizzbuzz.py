# The FizzBuzz Problem

# For numbers 1 to 100
# Number divisible by 3 > Fizz
# Number divisible by 5 > Buzz
# Number divisible by 3 and 5 > FizzBuzz

top_num = int(input("Where would you like to stop? Please specify a number your computer can handle in a timely manner. "))

for n in range(1, top_num):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        if n % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(n)

# Alternative solution
for n in range(1, top_num):
    if (n % 3 == 0) & (n % 5 == 0):
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
            print("Fizz")
    else:
        print(n)