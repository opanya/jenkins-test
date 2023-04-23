def min_of_three_vars(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


def make_capital_letters(inp: str) -> str:
    inp = inp.upper()
    return inp


def division_by_twelve(num: int) -> bool:
    try:
        if int(num) % 12 == 0:
            return True
        else:
            return False
    except ValueError:
        return False
