from math import ceil

a = (input("a: "))
b = (input("b: "))

a = a.replace(',', '.')
b = b.replace(',', '.')

a = float(a)
b = float(b)

su = a+b
av = (a+b) / 2

print(f"sum={ceil(su*100)/100}; avg={ceil(av*100)/100}")