first = int(input('input first integer: '))
second = int(input('Input one more integer: '))
third = int(input('Input last integer: '))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
