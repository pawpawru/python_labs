m = int(input("Минуты: "))
h = int(m / 60)
m = m - h*60
if h < 10:
    print(f"{h}:{m:02d}")
else:
    print(f'{h:02d}:{m:02d}')