## Описание:

Парсер документов PEP формирует файлы со следующим содержанием:
- спиcок всех PEP (номер, название, статус): pep_ДатаВремя.csv
- сводка по статусам PEP (статус, количество): status_summary_ДатаВремя.csv

## Стек:
- Scrapy
- Python 3.9

## Как запустить проект локально:
1. Клонировать репозиторий:
```
git clone https://github.com/VyacheslavGizov/scrapy_parser_pep.git
```
2. В корневой папке создать и активировать виртуальное окружение, установить зависимости:
```
cd scrapy_parser_pep/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
3. Запустить парсер:
```
scrapy crawl pep
```
4. Файлы с результатами парсинга формируются в директории:
```
scrapy_parser_pep/results/
```

## Авторы:
- [Vyacheslav Gizov](https://github.com/VyacheslavGizov).
