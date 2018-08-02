from oef1_3 import william_find_shortest

assert william_find_shortest(230) == [60, 60, 110]
assert william_find_shortest(60) == [60]
assert william_find_shortest(110) == [110]
assert william_find_shortest(50) == None
assert william_find_shortest(130) == None

assert william_find_shortest(1000) == [60, 60, 110, 110, 110, 110, 110, 110, 110, 110]
assert william_find_shortest(1600) == [60, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110]

