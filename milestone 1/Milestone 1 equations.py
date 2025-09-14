eq = '4x^2 +4x + (-8) = 0'

eq = eq.replace(' ', '').replace('+', '').replace('(', '').replace(')', '') #прибираемо усі знаки
print(eq)

x2_index = eq.find('x^2')   #знаходимо індекс де починается x^2
print(x2_index)
a = eq[:x2_index] # видаляемо частину до x^2 це коєфіціент а
print(a)
a == '1' if a == '' else '-1' if a == '-' else a #якшо перед x^2 або -x^2 , то а = 1 або -1
a = int(a)
print(a)
remaining_eq = eq[x2_index + 3:]  #разбираемо на частини, дістаємо коєфіцієнти
print(remaining_eq)
x_index = remaining_eq.find('x') #знаходимо індекс x між x^2 і x
b = remaining_eq[:x_index]
b = '1' if b == '' else '-1' if b == '-' else b
b = int(b)
remaining_eq = remaining_eq[x_index + 1:]  #тут залишается частина після x "=0'

c = remaining_eq.replace('=0', '') #прибираемо "=0" щоб залишити число
c = int(c)
print(c)

print(a,b,c)

a = 4
b = 4
c = -8


x1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)   # **0.5 це корінь квадратрний # x1 = (-4 + √(16 - (-128))) / 8 = (-4 + 12) / 8 = 1.0
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)   # **0.5 це корінь квадратрний # x2 = (-4 - √(16 - (-128))) / 8 = (-4 - 12) / 8 = -2.0


print(x1, x2)

