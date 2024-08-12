def sumofdigits(n):
    return sum(int(digit) for digit in str(n))
print(sumofdigits(1235))