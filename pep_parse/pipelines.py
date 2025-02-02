from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


RESULTS_DIR = 'results'
RESULT_FILENAME = 'status_summary_{timestamp}.csv'
RESULT_HEADLINES = ['Статус', 'Количество']
RESULT_FOOTER = 'Всего'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.quantity_per_status = defaultdict(int)

    def process_item(self, item, spider):
        self.quantity_per_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / RESULTS_DIR
        result_dir.mkdir(exist_ok=True)
        file_path = result_dir / RESULT_FILENAME.format(
            timestamp=dt.datetime.now().strftime(DATETIME_FORMAT))
        with open(file_path, 'w', encoding='utf-8') as csvfile:
            csv.writer(csvfile, dialect=csv.unix_dialect).writerows([
                RESULT_HEADLINES,
                *self.quantity_per_status.items(),
                [RESULT_FOOTER, sum(self.quantity_per_status.values())]
            ])
