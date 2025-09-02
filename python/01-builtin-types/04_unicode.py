# ascii compatible, one codepoint one byte
assert len("abc") == 3
assert len("abc".encode("utf-8")) == 3

# euro sign takes 3 bytes
assert len("€") == 1
assert len("€".encode("utf-8")) == 3

# ascii bytes
assert b"\x61\x62".decode("utf-8") == "ab"
assert b"ab".decode("utf-8") == "ab"

# using escape for unicode codepoint literals
print("\u2194")


# error handling in decoding bytes
assert b"\xff".decode("utf-8", "ignore") == ""

try:
    b"\xff".decode("utf-8", "strict")
except Exception as exc:
    assert isinstance(exc, UnicodeDecodeError)
else:
    assert False, "Did not throw"

print(b"\xff".decode("utf-8", "replace"))
assert b"\xff".decode("utf-8", "replace") == "?"