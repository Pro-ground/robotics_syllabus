# Problem 1 — unit vector
# Write a single file, e.g. 001_unit_vector.py. No extra libraries except the stdlib (math is fine).
# Spec
# Implement:
# textunit_vector(v) -> list[float]
# v is a list of three numbers [x, y, z] representing a 3D vector.
# Return a new list of three floats: the same direction, length 1.
# If v is the zero vector [0, 0, 0] (or close enough that the length is 0), return [0.0, 0.0, 0.0]. Do not crash.
# Do not mutate the input list.
# Examples
# textunit_vector([3, 0, 4])     ->  [0.6, 0.0, 0.8]
# unit_vector([0, 0, 0])     ->  [0.0, 0.0, 0.0]
# unit_vector([1, 0, 0])     ->  [1.0, 0.0, 0.0]
# unit_vector([-2, 0, 0])    ->  [-1.0, 0.0, 0.0]
# Floats will not be exact. Treat a component as correct if abs(got - expected) < 1e-9.
# How you know you are done
# Put this at the bottom of the same file and run python 001_unit_vector.py. All of it should print ok and not raise.
# Pythondef nearly_equal(a, b):
#     return all(abs(x - y) < 1e-9 for x, y in zip(a, b))

# assert nearly_equal(unit_vector([3, 0, 4]), [0.6, 0.0, 0.8])
# assert nearly_equal(unit_vector([0, 0, 0]), [0.0, 0.0, 0.0])
# assert nearly_equal(unit_vector([1, 0, 0]), [1.0, 0.0, 0.0])
# assert nearly_equal(unit_vector([-2, 0, 0]), [-1.0, 0.0, 0.0])

# original = [3, 0, 4]
# unit_vector(original)
# assert original == [3, 0, 4]

# print("ok")

import math

vector_1 = [3, 0, 4]

# def unit_vector_v1(vector):
#     squared_components = []
#     unit_vectors = []
#     for component in vector:
#         if component == 0:
#             squared_components.append(0)
#         else:
#             component = component * component
#             print("component: ", component)
#             squared_components.append(component)
#     total = sum(squared_components)
#     print("total: ", total)
#     square_root = math.sqrt(total)
#     for num in vector:
#         if num == 0:
#             unit_vectors.append(num)
#         else:
#             num = num / square_root
#             unit_vectors.append(num)
#     print(unit_vectors)
#     return unit_vectors
# unit_vector_v1(vector_1)

def unit_vector(vector):
    final = []
    if vector.length = 0:
        return [0,0,0]
    root = math.sqrt(sum(component * component for component in vector))
    for 

    print(final)
    return final

unit_vector(vector_1)




# def nearly_equal(a, b):
#     return all(abs(x - y) < 1e-9 for x, y in zip(a, b))

# assert nearly_equal(unit_vector([3, 0, 4]), [0.6, 0.0, 0.8])
# assert nearly_equal(unit_vector([0, 0, 0]), [0.0, 0.0, 0.0])
# assert nearly_equal(unit_vector([1, 0, 0]), [1.0, 0.0, 0.0])
# assert nearly_equal(unit_vector([-2, 0, 0]), [-1.0, 0.0, 0.0])

# original = [3, 0, 4]
# unit_vector(original)
# assert original == [3, 0, 4]

# print("ok")
