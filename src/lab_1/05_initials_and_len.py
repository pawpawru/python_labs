FIO = input("ФИО: ")
fio = [i for i in FIO if i != ' ']
alphabet = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
for i in FIO:
    if i not in alphabet:
        FIO = FIO.replace(i, '')
print(f"Инициалы: {FIO}.")
print(len(fio)+2)