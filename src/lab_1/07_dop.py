'''
Первая заглавная буква в строке является первой буквой в оригинальной строке;
Символы оригинальной строки расположены в фиксированном шаге друг от друга;
Второй символ стоит сразу после цифры;
Последним символом оригинальной строки является точка .
'''
st = input()
ans = ''

# с помощью этого цикла я нашёл начало строки
big_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for i in st: 
    if i in big_letters:
        ans += i
        break 

# с помощью этого цикла я нашёл второй символ строки
digits = '0123456789'
for i in st: 
    if i in digits:
        indx = st.index(i) + 1
        ans += st[indx]
        break

# теперь мы можем найти шаг с которым символы стоят
if st.index(ans[0]) > st.index(ans[1]):
    space = st.index(ans[0]) - st.index(ans[1])
else:
    space = st.index(ans[1]) - st.index(ans[0])

#print(space)
#print(ans[0], ans[1]) проверка

st = st[st.index(ans[1])+1:]
count = 0
for i in st:
    count += 1
    if i != '.':
        if count == space:
            ans += i
            count = 0
    else:
        ans += i
        break
print(ans)