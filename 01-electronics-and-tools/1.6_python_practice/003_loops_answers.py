# Problem 3 — go through values one at a time
#
# This file is the worked answer for 003_loops.py. Try that file first.

# ----- EXERCISE -----

def running_total(values):
    totals = []
    current = 0
    for value in values:
        current = current + value
        totals.append(current)
    return totals


def first_index_at_or_above(values, threshold):
    i = 0
    for value in values:
        if value >= threshold:
            return i
        i = i + 1
    return None


def countdown_steps(start):
    if start <= 0:
        return []
    steps = []
    n = start
    while n >= 1:
        steps.append(n)
        n = n - 1
    return steps


def every_nth(values, n):
    picked = []
    for i in range(0, len(values), n):
        picked.append(values[i])
    return picked


# ----- ASSERTION ------

assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []
assert running_total([5]) == [5]
assert running_total([1.5, 1.5]) == [1.5, 3.0]

assert first_index_at_or_above([1, 3, 7, 2], 7) == 2
assert first_index_at_or_above([1, 3, 7, 2], 8) is None
assert first_index_at_or_above([5, 1], 5) == 0
assert first_index_at_or_above([], 1) is None
assert first_index_at_or_above([0.4, 0.4, 0.9], 0.9) == 2

assert countdown_steps(4) == [4, 3, 2, 1]
assert countdown_steps(1) == [1]
assert countdown_steps(0) == []
assert countdown_steps(-3) == []

assert every_nth(["a", "b", "c", "d", "e"], 2) == ["a", "c", "e"]
assert every_nth([10, 20, 30], 1) == [10, 20, 30]
assert every_nth([10, 20, 30], 3) == [10]
assert every_nth([], 2) == []
assert every_nth([7], 5) == [7]

print("ok")
