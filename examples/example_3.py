"""
100% line coverage
"""

was_last_string_long = False


def is_string_long(input: str) -> bool:
    result = len(input) > 5
    was_last_string_long = result   # First outcome
    return result   # Second outcome
