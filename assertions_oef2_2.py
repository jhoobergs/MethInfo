from oef2_2 import KonijnenOor

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