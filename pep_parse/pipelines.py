from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS_DIRNAME


SUMMARY_FILENAME = 'status_summary_{timestamp}.csv'
RESULT_HEADLINES = ('Статус', 'Количество')
RESULT_FOOTER = 'Всего'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def __init__(self):
        result_dir = BASE_DIR / RESULTS_DIRNAME
        result_dir.mkdir(exist_ok=True)
        self.file_path = result_dir / SUMMARY_FILENAME.format(
            timestamp=dt.datetime.now().strftime(DATETIME_FORMAT))

    def open_spider(self, spider):
        self.status_counters = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counters[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.file_path, 'w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows((
                RESULT_HEADLINES,
                *self.status_counters.items(),
                (RESULT_FOOTER, sum(self.status_counters.values()))
            ))
