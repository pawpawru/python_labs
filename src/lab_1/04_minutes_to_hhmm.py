m = int(input("Минуты: "))
h = int(m / 60)
m = m - h*60
print(f'{h:02d}:{m:02d}')