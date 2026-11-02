## Лабораторная работа № 6

## Команды запуска

```bash
# Задание A
cd src
py -m lab_6.cli_text cat --input ../data/samples/people.csv -n
py -m lab_6.cli_text stats --input ../data/samples/people.txt --top 5

# Задание B
cd src
py -m lab_6.cli_convert json2csv --in ../data/samples/people.json --out ../data/out/people.csv
py -m lab_6.cli_convert csv2json --in ../data/samples/people.csv --out ../data/out/people.json
py -m lab_6.cli_convert csv2xlsx --in ../data/samples/people.csv --out ../data/out/people.xlsx

# Справка
cd src
py -m lab_6.cli_text stats --help
```

## Задание A
![cli_text](../../images/lab_6/img_04.png)

## Задание B

### JSON → CSV
![JSON → CSV](../../images/lab_6/img_01.png)
### CSV → JSON
![CSV → JSON](../../images/lab_6/img_02.png)
### CSV → XLSX
![CSV → XLSX](../../images/lab_6/img_03.png)

## Справка --help
![help](../../images/lab_6/img_05.png)