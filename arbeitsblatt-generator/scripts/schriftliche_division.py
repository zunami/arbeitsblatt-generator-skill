#!/usr/bin/env python3
"""Auditable school-style long division for printable solution sheets.

All intermediate subtractions and carried-down digits are represented as
separate, vertically aligned rows. Pure arithmetic/layout functions can be
unit tested without ReportLab. The drawing helper needs ReportLab and can be
used on any canvas with enough vertical space.

School convention: positive integer operands. A non-zero final remainder is
written as 'Rest n'; do not continue with decimals unless requested.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from typing import List


@dataclass(frozen=True)
class Step:
    end_col: int
    partial: int
    quotient_digit: int
    product: int
    remainder: int
    next_digit: int | None


@dataclass(frozen=True)
class Row:
    kind: str
    end_col: int
    text: str


def calculate_steps(dividend: int, divisor: int) -> List[Step]:
    """Compute each divide/multiply/subtract/bring-down cycle."""
    if isinstance(dividend, bool) or isinstance(divisor, bool):
        raise ValueError('Boolean operands are not integers')
    if not isinstance(dividend, int) or not isinstance(divisor, int):
        raise ValueError('Expected integer operands')
    if dividend < 0 or divisor <= 0:
        raise ValueError('Expected nonnegative dividend and positive divisor')
    digits = str(dividend)
    remainder = 0
    begun = False
    results: List[Step] = []
    for i, d in enumerate(digits):
        partial = remainder * 10 + int(d)
        if not begun and partial < divisor and i + 1 < len(digits):
            remainder = partial
            continue
        begun = True
        qdigit, new_remainder = divmod(partial, divisor)
        results.append(Step(end_col=i, partial=partial,
                            quotient_digit=qdigit, product=qdigit * divisor,
                            remainder=new_remainder,
                            next_digit=int(digits[i+1]) if i+1 < len(digits) else None))
        remainder = new_remainder
    assert results, 'At least one step is required'
    return results


def solution(dividend: int, divisor: int):
    steps = calculate_steps(dividend, divisor)
    quotient = int(''.join(str(s.quotient_digit) for s in steps))
    remainder = steps[-1].remainder
    assert quotient == dividend // divisor, 'Quotient mismatch'
    assert remainder == dividend % divisor, 'Remainder mismatch'
    assert quotient * divisor + remainder == dividend, 'Probe mismatch'
    assert 0 <= remainder < divisor
    for idx, step in enumerate(steps):
        assert step.partial - step.product == step.remainder
        assert step.product == step.quotient_digit * divisor
        assert step.product <= step.partial < step.product + divisor
        if idx < len(steps)-1:
            assert step.next_digit is not None
            assert steps[idx+1].partial == step.remainder * 10 + step.next_digit
            assert steps[idx+1].end_col == step.end_col + 1
    return quotient, remainder, steps


def build_rows(dividend: int, divisor: int):
    """One header, and for each quotient digit a minus row and next partial row.

    Each row has a fixed end_col referring to the original dividend digits.
    A remainder is written visibly on the last row.
    """
    quotient, remainder, steps = solution(dividend, divisor)
    rows = [Row('header', len(str(dividend)) - 1,
                f'{dividend} : {divisor} = {quotient}' + (f' Rest {remainder}' if remainder else ''))]
    for index, step in enumerate(steps):
        rows.append(Row('subtract', step.end_col, str(step.product)))
        if index + 1 < len(steps):
            rows.append(Row('partial', step.end_col + 1,
                            str(steps[index + 1].partial)))
        else:
            rows.append(Row('final', step.end_col, str(step.remainder)))
    assert len(rows) == 1 + 2 * len(steps)
    return rows


def required_height(dividend: int, divisor: int, cell: float = 19.0,
                    padding: float = 5.0) -> float:
    return len(build_rows(dividend, divisor)) * cell + 2 * padding


def draw_division(c, x: float, top: float, dividend: int, divisor: int,
                  *, cell: float = 20.0, total_cols: int = 22,
                  font_name: str = 'Helvetica', font_size: float = 13.0,
                  grid: bool = True, min_bottom: float = 0.0):
    """Draw complete school long division on a ReportLab canvas.

    x,top are coordinates of top-left grid corner in PDF points. The helper
    rejects too-short pages; never drops or horizontally compresses steps.
    """
    rows = build_rows(dividend, divisor)
    height = required_height(dividend, divisor, cell=cell, padding=0)
    if top - height < min_bottom:
        raise ValueError(f'Division needs {height:.1f}pt, but only {top-min_bottom:.1f}pt remain')
    if total_cols < len(str(dividend)) + 8:
        raise ValueError('Insufficient columns for the full equation')
    first_digit_x = x + 1.4 * cell
    glyph_y_offset = 0.5 * cell + 0.35 * font_size
    c.saveState()
    if grid:
        c.setStrokeColorRGB(0.78, 0.78, 0.78)
        c.setLineWidth(0.35)
        for col in range(total_cols + 1):
            xx = x + cell * col
            c.line(xx, top, xx, top - height)
        for ri in range(len(rows) + 1):
            yy = top - ri * cell
            c.line(x, yy, x + total_cols * cell, yy)
    c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0, 0, 0)
    c.setFont(font_name, font_size)

    def digit_in_col(digit, col, r):
        baseline = top - r * cell - glyph_y_offset
        xpos = first_digit_x + col * cell
        c.drawCentredString(xpos, baseline, str(digit))

    # Full headline: a separate digit in each column, then ': divisor = answer'.
    for col, d in enumerate(str(dividend)):
        digit_in_col(d, col, 0)
    q, rem, _ = solution(dividend, divisor)
    header = f': {divisor} = {q}' + (f' Rest {rem}' if rem else '')
    header_x = first_digit_x + len(str(dividend)) * cell - cell * 0.27
    c.setFont(font_name, font_size)
    c.drawString(header_x, top - glyph_y_offset, header)
    if header_x + c.stringWidth(header, font_name, font_size) > x + total_cols * cell - 3:
        raise ValueError('Equation exceeds the right edge of the grid')

    for ri, row in enumerate(rows[1:], start=1):
        text = row.text
        start_col = row.end_col - len(text) + 1
        if start_col < 0:
            raise ValueError('Intermediate value does not fit the dividend columns')
        if row.kind == 'subtract':
            # Place the operator directly before the affected digit group.
            minus_x = first_digit_x + start_col * cell - cell * 0.7
            baseline = top - ri * cell - glyph_y_offset
            c.drawCentredString(minus_x, baseline, '-')
        for j, digit in enumerate(text):
            digit_in_col(digit, start_col + j, ri)
        if row.kind == 'subtract':
            # Visible result line: the subtraction is not a horizontal equation.
            yy = top - (ri + 1) * cell + cell * 0.08
            x1 = first_digit_x + start_col * cell - cell * 0.45
            x2 = first_digit_x + row.end_col * cell + cell * 0.44
            c.setLineWidth(0.8)
            c.line(x1, yy, x2, yy)
    c.restoreState()
    return top - height


def main():
    parser = argparse.ArgumentParser(description='Inspect a full long-division step list')
    parser.add_argument('dividend', type=int)
    parser.add_argument('divisor', type=int)
    args = parser.parse_args()
    q, rem, steps = solution(args.dividend, args.divisor)
    print(json.dumps({'dividend': args.dividend, 'divisor': args.divisor,
                      'quotient': q, 'remainder': rem,
                      'steps': [asdict(s) for s in steps],
                      'rows': [asdict(r) for r in build_rows(args.dividend, args.divisor)]}, indent=2))


if __name__ == '__main__':
    main()
