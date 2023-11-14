def count_bits(n):
    binnum = bin(n)
    num_ones = binnum.count('1')
    return num_ones

n = 0
while n <= 0:
    try:
        n = int(input("Please enter a non-negative integer: "))
    except ValueError:
        print("Please enter a non-negative integer")

print(count_bits(n))