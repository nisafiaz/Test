# getting and storing numbers in a list
name=input("Enter your name")
print("You are required to enter your favourite 3 numbers")
numbers = []
for x in range(1,4):
    num = int(input(f"Enter {x}st number"))
    numbers.append(num)
print(f"Hello dear {name} You are welcome to the game of Fun with Numbers.\n Let's explore your favourite number")
print(numbers)
# Finding even odd numbers and storing in a tuple
evenOdd = []
for x in range(3):
    if (numbers[x]%2) == 0:
        print("even")
        evenOdd.append(f"The number {numbers[x]} is even")
    else:
        print("odd")
        evenOdd.append(f"The number {numbers[x]} is odd")
numbersTupal = tuple(evenOdd)
print(numbersTupal)
# printing tupal values and their squares
for x in range (3):
    print(numbersTupal[x])
squareL = []
for x in range(3):
    squareL.append(f"{numbers[x]}, {numbers[x]*numbers[x]}")
    print(squareL)
    #squareL.append(f"The number {numbers[x]} and its Square: {numbers[x]}, {numbers[x]*numbers[x]}")
numberSquareT = tuple(squareL)
for x in range(3):
    print(f"The number {numbers[x]} and its Square: {numberSquareT[x]}")
# Sum the numbers
sum = 0
for x in range(3):
    sum=numbers[x]+sum
print(f"Amazing! the sum of your favourite numbers is: {sum}")
# calculate prime number
flag = False

if sum == 0 or num == 1:
    print(sum, "is not a prime number")
elif sum > 1:
    # check for factors
    for x in range(2, sum):
        if (sum % x) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(sum, "is not a prime number")
    else:
        print(f"Wao! {sum} is a prime number")
