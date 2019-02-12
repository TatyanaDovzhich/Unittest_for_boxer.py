class Boxer():
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height
        self.boxer = []
        self.boxerSC = []
        self.boxerHG = []
        self.boxerSA = []

    def List_SergeyCovalev(self):
        return [SergeyCovalev for SergeyCovalev in self.boxerSC]

    def List_HennadiyGolovkin(self):
        return [HennadiyGolovkin for HennadiyGolovkin in self.boxerHG]

    def List_SaulAlvarez(self):
        return [SaulAlvarez for SaulAlvarez in self.boxerSA]

SergeyCovalev = Boxer(33, 78, 180)
HennadiyGolovkin = Boxer(28, 72, 185)
SaulAlvarez = Boxer(35, 69, 182)


SergeyCovalev.boxerSC.append(33)
SergeyCovalev.boxerSC.append(78)
SergeyCovalev.boxerSC.append(180)
HennadiyGolovkin.boxerHG.append(28)
HennadiyGolovkin.boxerHG.append(72)
HennadiyGolovkin.boxerHG.append(185)
SaulAlvarez.boxerSA.append(35)
SaulAlvarez.boxerSA.append(69)
SaulAlvarez.boxerSA.append(182)

print (SergeyCovalev.List_SergeyCovalev())
print (HennadiyGolovkin.List_HennadiyGolovkin())
print (SaulAlvarez.List_SaulAlvarez())

