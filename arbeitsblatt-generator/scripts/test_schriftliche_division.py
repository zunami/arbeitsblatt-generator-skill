#!/usr/bin/env python3
"""Positive and negative checks for vertically traceable school division."""
import random
from schriftliche_division import build_rows, calculate_steps, draw_division, required_height, solution

cases = [
    (6728, 5, 1345, 3, [6, 17, 22, 28], [5, 15, 20, 25]),
    (9864, 6, 1644, 0, [9, 38, 26, 24], [6, 36, 24, 24]),
    (5746, 8, 718, 2, [57, 14, 66], [56, 8, 64]),
    (5020, 5, 1004, 0, [5, 0, 2, 20], [5, 0, 0, 20]),
    (2346, 3, 782, 0, [23, 24, 6], [21, 24, 6]),
    (1003, 3, 334, 1, [10, 10, 13], [9, 9, 12]),
    (0, 8, 0, 0, [0], [0]),
    (5, 8, 0, 5, [5], [0]),
]
for a, b, q, r, partials, products in cases:
    actual_q, actual_r, steps = solution(a, b)
    assert (actual_q, actual_r) == (q, r)
    assert [s.partial for s in steps] == partials, (a, steps)
    assert [s.product for s in steps] == products
    assert len(build_rows(a, b)) == 1 + 2 * len(steps)
    assert required_height(a, b) >= len(build_rows(a, b)) * 19.0

for dividend, divisor in [(2, 0), (-2, 3), (10, -2)]:
    try:
        calculate_steps(dividend, divisor)
    except ValueError:
        pass
    else:
        raise AssertionError('Expected invalid input rejection')

rng = random.Random(20261121)
for _ in range(1000):
    a, b = rng.randrange(0, 100000), rng.randrange(1, 14)
    quotient, remainder, steps = solution(a, b)
    assert quotient == a // b and remainder == a % b
    assert all(s.quotient_digit in range(10) for s in steps)
    assert all(0 <= s.remainder < b for s in steps)

from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
buf = BytesIO()
c = Canvas(buf, pagesize=(595.276, 841.89))
for a, b, *_ in cases:
    draw_division(c, 50, 800, a, b, cell=20, total_cols=22, min_bottom=200)
    c.showPage()
try:
    draw_division(c, 50, 80, 9864, 6, cell=20, min_bottom=200)
except ValueError:
    pass
else:
    raise AssertionError('Short page must be rejected')
c.save()
assert buf.getvalue().startswith(b'%PDF')
print('Written-division test groups passed; 1000 random examples + 8 reference cases + render + negative checks')
