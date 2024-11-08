import random

'''
print("Kérek egy egész számot 1 és 100 között :" ,end=" ")
szam = int(input())
'''
# szam = int(input("Kérek egy egész számot 1 és 100 között :"))
'''
while True:
    be = input("Kérek egy egész számot 1 és 100 között : ")
    if (be.isnumeric()) :
        szam =  int(be)
        break
    else:
        print("Nem jó formátum")
'''


def beker():
    ismeteld = True
    while ismeteld:
        be = input("Kérek egy egész számot 1 és 100 között : ")
        if (be.isnumeric()) :
            szam =  int(be)
            ismeteld = False
        else:
            print("Nem jó formátum")
    return szam

# print(beker())

# random.seed(1)
'''
for i in range(100):
    velszam = random.randint(1,100)
    print(velszam,end=", ")
'''


def jatek():
    ismetles = True
    proba = 0
    gondolt = random.randint(1,100)
    while ismetles:
        tipp = beker()
        proba += 1
        if (tipp == gondolt):
            print("Talált!")
            print(str(proba ) + " Próbálkozásod volt")
            ismetles = False
            '''
            asd = input("Akarsz még játszani? (I/N) : ")
            if asd == "I":
                ismetles = True
            else :
                print("Köszönöm a játékot!")
            '''
        elif (tipp < gondolt):
            print("A szám kicsi!")
        else :
            print("A szám nagy!")



valasz = input("Akarsz velem játszani? (I/N): ").upper()
while valasz == "I" or valasz == "igen":
    jatek()
    valasz = input("Akarsz velem még játszani? (I/N): ").upper()