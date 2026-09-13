# Problem 3 — walk through values one at a time
# Write a single file, e.g. 003_loops.py. No external packages, only the stdlib.
#
# A loop repeats a piece of code. Robots spend most of their time in a loop:
# read, decide, act, repeat. You will use these same loop forms again in
# 004, 011, and later files.
#
# Do the files in this folder in numbered order. This is 003 of 013.
#
# What you will need
#
# Packages: none. Use only what Python gives you with no install.
#
# Ideas to have in place before you start:
# - A for loop takes each item from a list, one by one.
# - range(n) gives the numbers 0, 1, 2, ... up to but not including n.
#   range(start, stop, step) can skip; look that up if you need it.
# - A while loop keeps going as long as a condition is True.
# - You build a result list with append.
#
# Tools to look up if you do not know them yet:
# - for item in some_list
# - for i in range(...)
# - while
# - list.append
#
# Do not use: sum(), min(), max(), or a list comprehension (the one-line
# form [ ... for ... in ... ]). Write the long form so you can see each step.
# You may use len() on a list.
#
# 1. running_total(values)
#    values is a list of numbers.
#    Return a new list the same length. Each item is the sum of values
#    from the start up to and including that position.
#    An empty list returns an empty list.
#
# 2. first_index_at_or_above(values, threshold)
#    Walk values from the left. Return the position (starting at 0) of the
#    first number that is greater than or equal to threshold.
#    Return None if no number qualifies.
#
# 3. countdown_steps(start)
#    start is a positive integer.
#    Using a while loop, return a list [start, start - 1, ..., 1].
#    Do not include 0. If start is 0 or negative, return an empty list.
#
# 4. every_nth(values, n)
#    n is an integer greater than or equal to 1.
#    Return a new list of the items at positions 0, n, 2n, 3n, ... as long
#    as the position is still inside the list.
#    Use range to produce those positions. Do not walk every item and then
#    skip with if, unless you also use range for the positions.
#
#
# Examples
#
# running_total([1, 2, 3, 4])  ->  [1, 3, 6, 10]
# running_total([])            ->  []
# running_total([5])           ->  [5]
#
# first_index_at_or_above([1, 3, 7, 2], 7)   ->  2
# first_index_at_or_above([1, 3, 7, 2], 8)   ->  None
# first_index_at_or_above([5, 1], 5)         ->  0
#
# countdown_steps(4)   ->  [4, 3, 2, 1]
# countdown_steps(1)   ->  [1]
# countdown_steps(0)   ->  []
#
# every_nth(["a", "b", "c", "d", "e"], 2)  ->  ["a", "c", "e"]
# every_nth([10, 20, 30], 1)               ->  [10, 20, 30]
# every_nth([10, 20, 30], 3)               ->  [10]
#
#
# How you know you are done
#
# Put this at the bottom of the same file and run
#   python 003_loops.py
# All of it should print ok and not raise.
#

# ----- EXERCISE -----
# Write your code below.
#


# ----- ASSERTION ------
#

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
