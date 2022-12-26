
# calculate the sum of the first n positive odd integers
# Ex. the sum of the first 2 positive odd integers = 1 + 3 = 4
# conjecture:
#   n
#   ∑ (2i - 1)  = n^2
# i = 1
# For any positive integer n, the sum of the first n odd integers is equal to n2.

n = 0
a = 2*n - 1 # 2(0) - 1 = 0 - 1 = -1
b = n**2 # 0^2 = 0
print(a, b)
print(a == b) # False