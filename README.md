# **scrapy_parser_pep** 

Парсер документов PEP формирует файлы со следующим содержанием:

- спиcок всех PEP (номер, название, статус): pep_ДатаВремя.csv
- сводка по статусам PEP (статус, количество): status_summary_ДатаВремя.csv

---

## Стек технологий

- Python 3.9
- Scrapy 

---

## Как запустить проект локально

1. Клонировать репозиторий:

```bash
git clone https://github.com/VyacheslavGizov/scrapy_parser_pep.git
```

2. В корневой папке создать и активировать виртуальное окружение, установить зависимости:

```bash
cd scrapy_parser_pep/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

3. Запустить парсер:

```bash
scrapy crawl pep
```

4. Файлы с результатами парсинга формируются в директории:

```bash
scrapy_parser_pep/results/
```

---

## Авторы:

[Вячеслав Гизов](https://github.com/VyacheslavGizov).
