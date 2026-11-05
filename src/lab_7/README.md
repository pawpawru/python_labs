## Лабораторная работа № 7

## Команды запуска

```bash
cd src
py -m lab_7.bech
```

## Таблица бенчмарка

'''
task,n,impl,seconds
sorting,1000,sorted,0.000215
sorting,1000,insertion_sort,0.041272
sorting,1000,selection_sort,0.039325
sorting,1000,bubble_sort,0.087035
sorting,10000,sorted,0.002193
sorting,10000,insertion_sort,4.479609
sorting,10000,selection_sort,4.046065
sorting,10000,bubble_sort,9.234403
sorting,100000,sorted,0.028429
sorting,100000,insertion_sort,> 60
sorting,100000,selection_sort,> 60
sorting,100000,bubble_sort,> 60
search,100000,linear_search,42.982766
search,100000,binary_search,0.040820
two_sum,1000,two_sum_brute,0.000006
two_sum,1000,two_sum_fast,0.000010
two_sum,10000,two_sum_brute,0.000005
two_sum,10000,two_sum_fast,0.000005
'''

## Выводы

### Почему пузырёк при росте n в 10 раз замедляется в ~100 раз, а sorted — в ~12?

Потому, что пузырёк работает за O(n^2), а sorted за O(n * log(n))

### Почему бинарный поиск бесполезен без предварительной сортировки, и когда она окупается?

Бинарный поиск работает только при условии, что все числа больше X лежат справа, а все числа меньше X - слева.
Без предварительной сортировки такой гарантии нет.
Бинарный поиск в целом очень эффективен так, как работает за O(log(n)), эта разница особенно заметна на больших массивах.

### Что показал check.py: сколько прогонов, нашёл ли расхождения, как исправили?

500 прогонов, расхождений нет.