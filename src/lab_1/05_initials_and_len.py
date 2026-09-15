FIO = input("ФИО: ")
ans = ''
fio = [i for i in FIO.split()]
for i in fio:
    ans += i[0]
print(ans)