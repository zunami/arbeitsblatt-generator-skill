#!/usr/bin/env python3
"""Deterministic planning helpers. Not a curriculum or mathematical validator."""
import argparse
import json
import math
from pathlib import Path


def numeric(value, name, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name}: finite number required')
    if value < 0 or (positive and value == 0):
        raise ValueError(f'{name}: invalid range')
    return value


def school_profile(school, class_number):
    if school not in ('VS', 'MS', 'AHS') or type(class_number) is not int or class_number not in range(1, 5):
        raise ValueError('Use school VS/MS/AHS and class 1–4')
    grade = class_number if school == 'VS' else class_number + 4
    if school == 'VS':
        body, grid, line = [(15, 8, 11), (14, 7, 10), (13, 6, 10), (13, 6, 10)][class_number-1]
    else:
        body, grid, line = (12.5, 6, 9) if class_number <= 2 else (12, 5.5, 9)
    return {'school': school, 'class': class_number, 'grade': grade,
            'body_pt': body, 'grid_mm': grid, 'writing_line_mm': line,
            'note': 'Design estimates; use observed handwriting and teacher scope.'}


def sort_tasks(data):
    profile = school_profile(data['school'], data['class'])
    topics = data['topic_order']
    if not topics or any(not isinstance(t, str) or not t for t in topics) or len(set(topics)) != len(topics):
        raise ValueError('topic_order must contain unique nonempty strings')
    tasks = data['tasks']
    if not tasks:
        raise ValueError('No tasks')
    by_id = {}
    for t in tasks:
        ident = t['id']
        if not isinstance(ident, str) or not ident or ident in by_id:
            raise ValueError('Task IDs must be unique nonempty strings')
        by_id[ident] = t
    dimensions = None
    for t in tasks:
        if t['topic'] not in topics:
            raise ValueError(f"{t['id']}: outside teacher topic_order")
        if type(t['stage']) is not int or t['stage'] not in range(5):
            raise ValueError(f"{t['id']}: stage must be 0–4")
        if not isinstance(t['family'], str) or not t['family']:
            raise ValueError(f"{t['id']}: family required")
        dif = t['difficulty']
        if not isinstance(dif, list) or not dif:
            raise ValueError('difficulty needs a nonempty list')
        for value in dif:
            numeric(value, 'difficulty')
        dimensions = len(dif) if dimensions is None else dimensions
        if len(dif) != dimensions:
            raise ValueError('All difficulty vectors need the same defined dimensions')
        deps = t.get('depends_on', [])
        if not isinstance(deps, list) or any(d not in by_id or d == t['id'] for d in deps):
            raise ValueError(f"{t['id']}: unknown/self prerequisite")
        numeric(t['minutes'], 'minutes', positive=True)
    # Validate the dependency graph before applying the requested topic order.
    remaining = set(by_id)
    done = set()
    while remaining:
        ready = [i for i in remaining if set(by_id[i].get('depends_on', [])) <= done]
        if not ready:
            raise ValueError('Cyclic task prerequisites')
        done.update(ready)
        remaining.difference_update(ready)
    ranks = {topic: i for i, topic in enumerate(topics)}
    # A user-specified topic order is a constraint. Never silently move an
    # earlier topic later to satisfy a cross-topic dependency.
    for t in tasks:
        for dep in t.get('depends_on', []):
            if ranks[by_id[dep]['topic']] > ranks[t['topic']]:
                raise ValueError('Topic order conflicts with prerequisites; revise plan explicitly')
    done = set()
    ordered = []
    last_family = None
    for topic in topics:
        pending = [t for t in tasks if t['topic'] == topic]
        while pending:
            ready = [t for t in pending if set(t.get('depends_on', [])) <= done]
            if not ready:
                raise ValueError('Unresolved prerequisites')
            priority = lambda t: (t['stage'], tuple(t['difficulty']))
            best = min(priority(t) for t in ready)
            equal = [t for t in ready if priority(t) == best]
            changing = [t for t in equal if t['family'] != last_family]
            chosen = (changing or equal)[0]  # stable original order for ties
            pending.remove(chosen)
            ordered.append(chosen['id'])
            done.add(chosen['id'])
            last_family = chosen['family']
    return {'profile': profile, 'ordered_ids': ordered,
            'estimated_task_minutes': sum(t['minutes'] for t in tasks),
            'note': 'Add reading/orientation/checking time separately; not a tested duration.'}


def check_layout(data):
    width = numeric(data.get('page_width_mm', 210), 'page width', True)
    height = numeric(data.get('page_height_mm', 297), 'page height', True)
    margin = numeric(data.get('margin_mm', 15), 'margin')
    gap = numeric(data.get('block_gap_mm', 5), 'gap')
    column_gap = numeric(data.get('column_gap_mm', 6), 'column gap')
    if 2*margin >= min(width, height):
        raise ValueError('Margins leave no page area')
    blocks = data['blocks']
    if not blocks:
        raise ValueError('No measured blocks')
    errors = []
    ids = set()
    for b in blocks:
        ident = b['id']
        if not isinstance(ident, str) or not ident or ident in ids:
            raise ValueError('Layout IDs must be unique nonempty strings')
        ids.add(ident)
        if type(b['page']) is not int or b['page'] < 1:
            raise ValueError('page must be an integer >= 1')
        box = b['bbox_mm']
        if not isinstance(box, list) or len(box) != 4:
            raise ValueError('bbox_mm must be [x,y,w,h]')
        x, y, w, h = [numeric(v, 'bbox') for v in box]
        if w <= 0 or h <= 0:
            raise ValueError('Block dimensions must be positive')
        if x < margin or y < margin or x+w > width-margin or y+h > height-margin:
            errors.append(f'{ident}: outside safe page area')
        if h < numeric(b.get('min_height_mm', 0), 'minimum height'):
            errors.append(f'{ident}: insufficient measured height')
        # Sequential strips sum. Side-by-side components occupy their maximum
        # height, never their sum. Inputs must come from measured font/geometry
        # and full required handwriting capacity, not from a guessed outer box.
        if b.get('writing') and 'flow_mm' not in b:
            raise ValueError(f'{ident}: writing blocks require flow_mm for complete internal height')
        if 'flow_mm' in b:
            flow = b['flow_mm']
            if not isinstance(flow, list) or not flow:
                raise ValueError('flow_mm must be a nonempty list of sequential heights')
            needed = 0
            for strip in flow:
                if isinstance(strip, list):
                    if not strip:
                        raise ValueError('A parallel strip needs at least one component height')
                    needed += max(numeric(v, 'parallel component height') for v in strip)
                else:
                    needed += numeric(strip, 'flow height')
            if needed > h:
                errors.append(f'{ident}: content/handwriting needs {needed} mm, block has {h} mm')
        for response in b.get('writing', []):
            rw = numeric(response['required_width_mm'], 'required width')
            aw = numeric(response['available_width_mm'], 'available width')
            rl, al = response['required_lines'], response['available_lines']
            if type(rl) is not int or type(al) is not int or min(rl, al) < 0:
                raise ValueError('Line counts must be nonnegative integers')
            if aw > w:
                errors.append(f'{ident}: response width exceeds block width')
            if rw > aw or rl > al:
                errors.append(f'{ident}: insufficient declared writing capacity')
    for i, a in enumerate(blocks):
        ax, ay, aw, ah = a['bbox_mm']
        for b in blocks[i+1:]:
            if a['page'] != b['page']:
                continue
            bx, by, bw, bh = b['bbox_mm']
            # Independent parallel columns are allowed. Shared x-projection
            # requires the actual vertical gap, including handwriting extents.
            if min(ax+aw, bx+bw) > max(ax, bx):
                distance = max(by-(ay+ah), ay-(by+bh))
                if distance < gap:
                    errors.append(f"{a['id']}/{b['id']}: overlap or less than {gap} mm vertical gap")
            elif min(ay+ah, by+bh) > max(ay, by):
                distance = max(bx-(ax+aw), ax-(bx+bw))
                if distance < column_gap:
                    errors.append(f"{a['id']}/{b['id']}: less than {column_gap} mm column gap")
    return {'ok': not errors, 'errors': errors, 'measured_blocks': len(blocks),
            'note': 'Uses declared measured boxes; render and visually inspect both PDFs.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['sort', 'layout'])
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text())
        result = sort_tasks(data) if args.mode == 'sort' else check_layout(data)
    except (ValueError, KeyError, TypeError) as err:
        parser.exit(2, f'Invalid input: {err}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get('ok') is False:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
