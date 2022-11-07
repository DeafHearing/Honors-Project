import re

elementWeight = {
    'H': 1.01,
    'He': 4,
    'Li': 6.94,
    'Be': 9.01,
    'B': 10.81,
    'C': 12.011,
    'N': 14.01,
    'O': 16,
    'F': 19,
    'Ne': 20.18,
    'Na': 22.99,
    'Mg': 24.31,
    'Al': 26.98,
    'Si': 28.09,
    'P': 30.97,
    'S': 32.06,
    'Cl': 35.45,
    'Ar': 39.95,
    'K': 39.10,
    'Ca': 40.08,
    'Sc': 44.96,
    'Ti': 47.87,
    'V': 50.94,
    'Cr': 52,
    'Mn': 54.94,
    'Fe': 55.85,
    'Co': 58.93,
    'Ni': 58.69,
    'Cu': 63.55,
    'Zn': 65.38,
    'Ga': 69.72,
    'Ge': 72.63,
    'As': 74.92,
    'Se': 78.97,
    'Br': 79.9,
    'Kr': 83.8,
    'Rb': 85.47,
    'Sr': 87.62,
    'Y': 88.91,
    'Zr': 91.22,
    'Nb': 92.91,
    'Mo': 95.95,
    'Ru': 101.07,
    'Rh': 102.91,
    'Pd': 106.42,
    'Ag': 107.87,
    'Cd': 112.41,
    'In': 114.82,
    'Sn': 118.71,
    'Sb': 121.76,
    'Te': 127.6,
    'I': 126.9,
    'Xe': 131.29,
    'Cs': 132.91,
    'Ba': 137.33,
    'La': 138.91,
    'Ce': 140.12,
    'Pr': 140.91,
    'Nd': 144.24,
    'Sm': 150.36,
    'Eu': 151.96,
    'Gd': 157.25,
    'Tb': 158.93,
    'Dy': 162.5,
    'Ho': 164.93,
    'Er': 167.26,
    'Tm': 168.93,
    'Yb': 173.05,
    'Lu': 174.97,
    'Hf': 178.49,
    'Ta': 180.95,
    'W': 183.84,
    'Re': 186.21,
    'Os': 190.23,
    'Ir': 192.22,
    'Pt': 195.08,
    'Au': 196.97,
    'Hg': 200.59,
    'Ti': 204.38,
    'Pb': 207.2,
    'Bi': 208.98,
    'Th': 232.04,
    'Pa': 231.04,
    'U': 238.03
}

print ("Strictly state the number of each element in compound")
print ("example : H2O1")

string = input()
elementList = []
finalElementList = []
weightHold = []
finalWeight = 0

element = re.findall('[a-zA-Z][^A-Z]*', string)

for i in element:
    elementList.append(i)

for i in elementList:
    test = re.split('(\d+)', i)
    finalElementList.append(test)
    var1 = 0
    var2 = 1
    test = [i for i in test if i]

    for i in test:
        print(i)
        

        if elementWeight.get(i) == None:
            i = int(i)
            var1 = i

            

        else:
            value = elementWeight.get(i)
            var2 = value
            print (var2)
            

        weightHold.append(var1*var2)

for d in weightHold:
    finalWeight = finalWeight + d
    print (finalWeight)

print ("\n\n", "Atomic Mass:", finalWeight)

