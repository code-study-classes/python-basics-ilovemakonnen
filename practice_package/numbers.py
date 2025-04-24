calculate_distance = lambda x, y: y - x  # noqa: E731


calculate_segments = lambda a, b: round(a // b)  # noqa: E731


calculate_digit_sum = lambda number: sum(map(int, str(abs(number))))  # noqa: E731


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)