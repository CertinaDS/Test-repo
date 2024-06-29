def getSum(a):
    b = int(a)
    Sum = 0
    for digit in str(b):
        Sum += int(digit)
    return Sum
a = input("Ведите чиcло: ")
print(getSum(a))