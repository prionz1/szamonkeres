''' #1.feladat
a1 = input('vezetéknév   ')
a2 = input('keresztnév   ')

print('Üdv!',a1,a2)
'''''' #2.feladat
szam = int(input('adj meg egy számot '))

print('A megelöző szám:', (szam - 1))
print('A rákövetkező szám:', (szam + 1))
''''''#3Feladat
a1 = int(input('Adj meg egy számot'))
a2 = int(input('Adj meg egy számot'))
print('összegük:',(a1 + a2))
print('különbségük:', (a1 - a2))
print('szorzatuk:' ,(a1 * a2))
print('hányadosuk:' (a1 % a2))
''''''#4feladat
szam = int(input('Adj meg egy számot'))
szam2 = int(input('Adj meg egy számot'))
c =(2* szam + 3*szam2)
d =(2* szam - 3*szam2)
print('C változó:'(c))
print('D változó: '(d))
''''''#5feladat
for szam in range(1,21):
    if szam % 2 == 0:
        print('Páros 1-20',szam,end=',')
print()
for szam2 in range(1,21):
    if szam2 % 2 == 1:
        print('Páratlan 1-20-ig',szam2,end=',')
'''
