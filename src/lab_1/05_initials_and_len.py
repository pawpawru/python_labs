FIO = input("ФИО: ")
ans = ''
fio = [i for i in FIO.split()]
l = [len(i) for i in fio]
for i in fio:
    ans += i[0]
print(f'Инициалы: {ans}.')
print(f'Длина (символов): {sum(l)+2}')