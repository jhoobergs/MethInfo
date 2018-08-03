from oef2_6 import Konijn, KonijnenOor
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

oor1 = KonijnenOor(5, 7, 33)
oor2 = KonijnenOor(6,10)

konijn1 = Konijn("William", 12, oor1, oor2)
assert konijn1.getNaam() == "William"
assert konijn1.getLeeftijd() == 12
assert konijn1.getLinkerOor() == oor1
assert konijn1.getRechterOor() == oor2

konijn2 = Konijn("Jef", 8, oor2, oor1)
assert konijn2.getNaam() == "Jef"
assert konijn2.getLeeftijd() == 8
assert konijn2.getLinkerOor() == oor2
assert konijn2.getRechterOor() == oor1

konijn3 = Konijn("Louise", 9, oor2, oor2)
assert konijn3.getNaam() == "Louise"
assert konijn3.getLeeftijd() == 9
assert konijn3.getLinkerOor() == oor2
assert konijn3.getRechterOor() == oor2

konijn = Konijn(1, 12, oor1, oor2)
assert konijn.getNaam() == None
assert konijn.getLeeftijd() == 12
assert konijn.getLinkerOor() == oor1
assert konijn.getRechterOor() == oor2

konijn = Konijn("William", "twaalf", oor1, oor2)
assert konijn.getNaam() == "William"
assert konijn.getLeeftijd() == None
assert konijn.getLinkerOor() == oor1
assert konijn.getRechterOor() == oor2

konijn = Konijn("William", 12, "oor", oor2)
assert konijn.getNaam() == "William"
assert konijn.getLeeftijd() == 12
assert konijn.getLinkerOor() == None
assert konijn.getRechterOor() == oor2

konijn = Konijn("William", 12, oor1, 12)
assert konijn.getNaam() == "William"
assert konijn.getLeeftijd() == 12
assert konijn.getLinkerOor() == oor1
assert konijn.getRechterOor() == None

konijn1.addKind(konijn2)
assert konijn1.getKinderen() == [konijn2]
konijn1.addKind(konijn3)
assert konijn2 in  konijn1.getKinderen()
assert konijn3 in  konijn1.getKinderen()
assert 2 == len(konijn1.getKinderen())

assert konijn1.getJongsteKind() == konijn2

konijn4 = Konijn("K", 8, oor2, oor2)
assert konijn4.getNaam() == "K"
assert konijn4.getLeeftijd() == 8
assert konijn4.getLinkerOor() == oor2
assert konijn4.getRechterOor() == oor2

konijn3.addKind(konijn4)
konijn3.addKind(konijn2)
assert konijn3.getJongsteKind() == konijn2
assert konijn4.getJongsteKind() == None

print(konijn1)
assert str(konijn1) == "Hallo ik ben William en ik ben 12 jaar oud. Ik heb 2 kinderen. De afmetingen van mijn linkeroor zijn: 5 7 33 en van mijn rechteroor: 6 10 60."