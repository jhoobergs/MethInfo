from oef2_3 import KonijnenOor

oor = KonijnenOor(5, 7, 33)
assert oor.getLengte() == 5
assert oor.getBreedte() == 7
assert oor.getOppervlakte() == 33

oor = KonijnenOor(5, 7)
assert oor.getLengte() == 5
assert oor.getBreedte() == 7
assert oor.getOppervlakte() == 35

oor.setLengte(20)
assert oor.getLengte() == 20
assert oor.getBreedte() == 7
assert oor.getOppervlakte() == 35

oor = KonijnenOor("vijf", 7, 30)
assert oor.getLengte() == 12
assert oor.getBreedte() == 7
assert oor.getOppervlakte() == 30

oor = KonijnenOor(5, "zeven", 30)
assert oor.getLengte() == 5
assert oor.getBreedte() == 6
assert oor.getOppervlakte() == 30

oor = KonijnenOor(5, 7, "dertig")
assert oor.getLengte() == 5
assert oor.getBreedte() == 7
assert oor.getOppervlakte() == 67