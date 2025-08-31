import sys

# comparing to python ints, floats are bounded!

print(sys.float_info)
print(sys.float_repr_style)

a = 0.3

# force 20 digits after decimal point
print("a", format(a, ".20f"))

import decimal

b = decimal.Decimal(a)

print("b", format(b, ".20f"))

c = decimal.Decimal("0.3")

print("c", format(c, ".20f"))

# decimal numbers can be represented exactly

print(format(decimal.Decimal("0.33") + decimal.Decimal("0.33") + decimal.Decimal("0.33"), ".20f"))

# precision can be altered

print("prec", decimal.getcontext().prec)