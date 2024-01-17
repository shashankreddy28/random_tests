
def max_bit_test( base = 2, exponent = 31):
    total = 0
    for i in range(exponent):
        total+=base**exponent
    return total
print("Total : ", max_bit_test())

print(2**31)