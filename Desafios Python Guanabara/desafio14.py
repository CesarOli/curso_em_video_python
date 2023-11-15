c = float(input('Para converter a temperatura em fahrenheit, digite primeiro a temperatura em graus Celsius: '))
f = c * 1.8 + 32

print('A temperatura {:.1f} C° em Fahrenheit é {:.1f} F°.'.format(c, f))

fa = float(input('Para converter a temperatura em Celsius, digite primeirp a temperatura em fahrenheit: '))
c = (fa - 32) / 1.8
print('A temperatura {:.1f} F° em Celsius é {:.1f} Cº'. format(fa, c))