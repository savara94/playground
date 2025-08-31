import decimal
import collections

def fn(): pass

literals = [
    True,
    1,
    1.0,
    decimal.Decimal("1"),
    complex(1, 1),
    iter([1, 2, 3]),
    [1,2,3],
    (1,2,3),
    range(10),
    "xyz",
    b'abcd',
    bytearray(b'abcd'),
    set(),
    frozenset(),
    dict(),
    collections,
    fn,
    None,
    ...,
    NotImplemented
]

for x in literals:
    print(x, " -> type", type(x))