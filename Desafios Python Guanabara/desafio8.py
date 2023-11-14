metros = float(input('Informe a medida em metros: '))

km = metros / 1000
he = metros / 100
de = metros / 10
dc = metros * 10
cm = metros * 100
mm = metros * 1000

print('A medida de {:.2f} metros corresponde a: \n{:.0f}km \n{:.0f}he \n{:.0f}de \n{:.0f}dc \n{:.0f}cm \n{:.0f}mm ' .format(metros, km, he, de, dc, cm, mm))

