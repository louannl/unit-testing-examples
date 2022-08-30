"""
This test would hit 100% coverage, but is nowhere near exhaustive enough.
If you were to use `int(“”)` or int(“not an int”) or int(Null) you could end up
with a different result, but these are hidden within the external library.
There are numerous edge-cases, and you are unlikely to ever cover them all.


Instead, you should make sure when using an external library it is reliable.
"""


def some_parsing_thing(input: str) -> int:
    return int(input)


if __name__ == "__main__":
    print(some_parsing_thing("5"))
    # print(some_parsing_thing("%%"))
    # print(some_parsing_thing(None))
