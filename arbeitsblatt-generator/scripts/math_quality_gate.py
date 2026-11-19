#!/usr/bin/env python3
"""Deterministic worksheet arithmetic checks. Input: JSON array of task dicts.
Supported: operation, division_remainder, sequences, neighbors, ordering,
place values, digit rearrangements, consecutive chains, step values, rectangle.
Use exact rational numbers (integer or decimal strings); never claim coverage for unsupported tasks.
"""
import argparse
import json
from fractions import Fraction


def q(x):
    return Fraction(str(x))


def check(t):
    kind = t.get('type')
    if kind == 'operation':
        a, b = q(t['a']), q(t['b'])
        op = t['operator']
        if op == '+': actual = a + b
        elif op == '-': actual = a - b
        elif op == '*': actual = a * b
        elif op == '/':
            if b == 0: raise ValueError('division by zero')
            actual = a / b
        else: raise ValueError('unknown operator')
        if 'min_value' in t and actual < q(t['min_value']): raise ValueError('below range')
        if 'max_value' in t and actual > q(t['max_value']): raise ValueError('above range')
        return actual == q(t['answer']), str(actual)
    if kind == 'division_remainder':
        a, b = int(t['dividend']), int(t['divisor'])
        if a < 0 or b <= 0: raise ValueError('positive integer division only')
        div, rem = divmod(a, b)
        ok = div == int(t['quotient']) and rem == int(t['remainder'])
        return ok, f'{div} remainder {rem}'
    if kind == 'division_written':
        dividend, divisor = int(t['dividend']), int(t['divisor'])
        if dividend < 0 or divisor <= 0:
            raise ValueError('invalid written division operands')
        quotient, remainder = divmod(dividend, divisor)
        steps = []
        current = 0
        begun = False
        for digit_text in str(dividend):
            current = current*10 + int(digit_text)
            if not begun and current < divisor:
                continue
            begun = True
            quotient_digit, new_remainder = divmod(current, divisor)
            steps.append({'partial': current, 'quotient_digit': quotient_digit,
                          'subtracted': quotient_digit*divisor, 'remainder': new_remainder})
            current = new_remainder
        if not begun:
            steps.append({'partial': dividend, 'quotient_digit': 0,
                          'subtracted': 0, 'remainder': dividend})
        ok = (int(t['quotient']) == quotient and int(t['remainder']) == remainder
              and t['steps'] == steps)
        return ok, f'{quotient} remainder {remainder}; steps={steps}'
    if kind == 'sequence_arithmetic':
        terms = [q(v) for v in t['terms']]
        if len(terms) < 3: raise ValueError('need at least 3 terms')
        step = terms[1] - terms[0]
        if not all(terms[i+1] - terms[i] == step for i in range(len(terms)-1)):
            raise ValueError('not arithmetic')
        actual = terms[-1] + step
        return actual == q(t['next']), str(actual)
    if kind == 'sequence_alternating':
        terms = [q(v) for v in t['terms']]
        if len(terms) < 3: raise ValueError('need at least 3 starting terms')
        steps = [q(v) for v in t.get('steps', [terms[1]-terms[0], terms[2]-terms[1]])]
        if len(steps) != 2 or steps[0] == steps[1]:
            raise ValueError('need two distinct alternating steps')
        if not all(terms[i+1]-terms[i] == steps[i % 2] for i in range(len(terms)-1)):
            raise ValueError('given terms break alternating rule')
        continuation = [q(v) for v in t['continuation']]
        if not continuation: raise ValueError('empty continuation')
        actuals = []
        last = terms[-1]
        for i in range(len(continuation)):
            last += steps[(len(terms)-1+i) % 2]
            actuals.append(last)
        if 'min_value' in t and min(terms+actuals) < q(t['min_value']):
            raise ValueError('below range')
        if 'max_value' in t and max(terms+actuals) > q(t['max_value']):
            raise ValueError('above range')
        return continuation == actuals, ', '.join(map(str, actuals))
    if kind == 'neighbors':
        n, base = int(t['number']), int(t['base'])
        if n <= 0 or base not in (10, 100, 1000):
            raise ValueError('invalid natural number or neighbor base')
        lower = ((n-1)//base)*base
        upper = ((n//base)+1)*base
        if 'max_value' in t and upper > int(t['max_value']):
            raise ValueError('above range')
        return int(t['lower']) == lower and int(t['upper']) == upper, f'{lower}, {upper}'
    if kind == 'order_numbers':
        numbers = [int(v) for v in t['numbers']]
        answer = [int(v) for v in t['answer']]
        if len(numbers) < 3: raise ValueError('need at least 3 numbers')
        direction = t['direction']
        if direction not in ('ascending', 'descending'):
            raise ValueError('unknown ordering direction')
        actual = sorted(numbers, reverse=(direction == 'descending'))
        return answer == actual, ', '.join(map(str, actual))
    if kind == 'consecutive_chain':
        anchor, step = int(t['anchor']), int(t.get('step', 1))
        left_count, right_count = int(t['left_count']), int(t['right_count'])
        if step <= 0 or left_count < 0 or right_count < 0 or left_count + right_count == 0:
            raise ValueError('invalid chain step or length')
        left = [anchor-step*i for i in range(left_count, 0, -1)]
        right = [anchor+step*i for i in range(1, right_count+1)]
        if 'min_value' in t and left and left[0] < int(t['min_value']):
            raise ValueError('below range')
        if 'max_value' in t and right and right[-1] > int(t['max_value']):
            raise ValueError('above range')
        return t['left'] == left and t['right'] == right, f'{left} | {anchor} | {right}'
    if kind == 'place_value':
        positions = t['places']
        if not isinstance(positions, dict) or set(positions) != {'T', 'H', 'Z', 'E'}:
            raise ValueError('need exactly T, H, Z, E')
        digits = {key: int(value) for key, value in positions.items()}
        if digits['T'] == 0 or any(v < 0 or v > 9 for v in digits.values()):
            raise ValueError('invalid four-digit number')
        order = t.get('display_order')
        if order is not None and (len(order) != 4 or set(order) != set(digits)):
            raise ValueError('invalid display order')
        actual = 1000*digits['T'] + 100*digits['H'] + 10*digits['Z'] + digits['E']
        return int(t['answer']) == actual, str(actual)
    if kind == 'digit_rearrangement':
        digits = [int(d) for d in t['digits']]
        if len(digits) != 4 or any(d < 0 or d > 9 for d in digits):
            raise ValueError('need four decimal digits')
        if digits[0] == 0: raise ValueError('original number needs 4 digits')
        original = sum(d * (10**(3-i)) for i, d in enumerate(digits))
        largest = sum(d * (10**(3-i)) for i, d in enumerate(sorted(digits, reverse=True)))
        mode = t['operator']
        if mode == '+': actual = largest + original
        elif mode == '-': actual = largest - original
        else: raise ValueError('unknown digit task operator')
        if 'max_value' in t and actual > int(t['max_value']):
            raise ValueError('above range')
        ok = (int(t['original']) == original and int(t['largest']) == largest
              and int(t['answer']) == actual)
        return ok, f'{largest} {mode} {original} = {actual}'
    if kind == 'step_value':
        start, step = int(t['start']), int(t['step'])
        if start < 0 or step not in (1, 10, 100):
            raise ValueError('invalid start or step')
        mode = t['direction']
        if mode == 'add': actual = start + step
        elif mode == 'subtract': actual = start - step
        else: raise ValueError('unknown step direction')
        if actual < 0: raise ValueError('below natural-number range')
        if 'max_value' in t and actual > int(t['max_value']):
            raise ValueError('above range')
        return int(t['answer']) == actual, str(actual)
    if kind == 'rectangle':
        a, b = q(t['width']), q(t['height'])
        if a <= 0 or b <= 0: raise ValueError('invalid sides')
        metric = t['metric']
        if metric == 'perimeter': actual = 2 * (a+b)
        elif metric == 'area': actual = a*b
        else: raise ValueError('unknown metric')
        return actual == q(t['answer']), str(actual)
    raise ValueError(f'unsupported task type: {kind}')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('json_file')
    args = p.parse_args()
    with open(args.json_file, encoding='utf-8') as f: tasks = json.load(f)
    if not isinstance(tasks, list): raise SystemExit('expected list')
    results = []
    for i, task in enumerate(tasks):
        ident = task.get('id', str(i+1))
        try:
            ok, actual = check(task)
            results.append({'id': ident, 'ok': ok, 'computed': actual})
        except (ValueError, KeyError, TypeError, ZeroDivisionError) as e:
            results.append({'id': ident, 'ok': False, 'error': str(e)})
    print(json.dumps(results, ensure_ascii=False, indent=2))
    raise SystemExit(0 if all(r['ok'] for r in results) else 1)

if __name__ == '__main__': main()
