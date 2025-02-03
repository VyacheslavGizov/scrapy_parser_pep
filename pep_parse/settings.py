from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIRNAME = 'results'
PEP_FILENAME = 'pep_%(time)s.csv'

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIRNAME}/{PEP_FILENAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
