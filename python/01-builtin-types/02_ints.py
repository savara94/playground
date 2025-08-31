import sys
import os

print("maxsize", sys.maxsize)

x = sys.maxsize + 1

print("x", x, type(x))

y = 2 ** 1000

print("y", y, type(y))

# experiment with python2 and python3

# python2 has long, bigint

# python3 uses only ints

# integers are actually 'unbounded'
# string conversion limitation exists and applies to decimal conversions

print("sys.get_int_max_str_digits", sys.get_int_max_str_digits())

try:
    a = []
    for i in range(sys.get_int_max_str_digits() + 1):
        a.append("1")

    b = int("".join(a))
except ValueError as ve:
    print("Value error as expected", ve)
except Exception as e:
    raise