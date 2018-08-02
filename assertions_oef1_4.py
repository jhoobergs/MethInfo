from oef1_4 import william_find_longest

assert william_find_longest(230) == [110, 60, 60]
assert william_find_longest(60) == [60]
assert william_find_longest(110) == [110]
assert william_find_longest(50) == None
assert william_find_longest(130) == None

assert william_find_longest(1000) == [110, 110, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]
assert william_find_longest(1600) == [110, 110, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]

