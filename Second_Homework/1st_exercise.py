num = int(input())

if num % 5 == 0 and num % 3 == 0:
    print("Fizz Buzz")
elif num % 5 == 0:
    print("Fizz" )
elif num % 3 ==0:
    print("Buzz")
else:
    print(num)
