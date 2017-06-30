чтобы выполнить скрипт по удалению тегов:
python -c "import spider_utils as s; s.remove_hml_tags('comments.csv')"

чтобы собрать данные:
scrapy runspider spider.py -o comments.csv -s DOWNLOAD_DELAY=1
