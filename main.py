from get_news import get_news
from save import save_to_file

origin_url = "https://news.google.com"
search_url = origin_url + "/search?q=python&hl=en-GB&gl=GB&ceid=GB%3Aen"
limit = 5

news = get_news(origin_url, search_url, limit)
save_to_file(news)