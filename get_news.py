import requests
from bs4 import BeautifulSoup


def get_news(origin_url, search_url, limit):
    news_result = requests.get(search_url)
    news_soup = BeautifulSoup(news_result.text, "html.parser")
    news_items = news_soup.select('div[class="xrnccd"]')
    news_links = []
    news_titles = []
    news_contents = []
    news_agencies = []
    news_dates = []
    news_times = []

    for item in news_items[:limit]:
        link = item.find("a", attrs={"class": "VDXfz"}).get("href")
        news_link = origin_url + link[1:]
        news_links.append(news_link)

        news_title = item.find("a", attrs={"class": "DY5T1d"}).getText()
        news_titles.append(news_title)

        news_content = item.find("span", attrs={"class": "xBbh9"}).text
        news_contents.append(news_content)

        news_agency = item.find("a", attrs={"class": "wEwyrc AVN2gc uQIVzc Sksgp"}).text
        news_agencies.append(news_agency)

        news_datetime = (
            item.find("time", attrs={"class": "WW6dff uQIVzc Sksgp"})
            .get("datetime")
            .split("T")
        )
        news_date = news_datetime[0][:-1]
        news_time = news_datetime[1][:-1]
        news_dates.append(news_date)
        news_times.append(news_time)

    result = {
        "link": news_links,
        "title": news_titles,
        "content": news_contents,
        "agency": news_agencies,
        "date": news_dates,
        "time": news_times,
    }
    return result


# print(news_soup)

#
# news_result = requests.get(search_url)
# news_soup = BeautifulSoup(news_result.text, "html.parser")

# news_items = news_soup.select('div[class="xrnccd"]')
# print(len(news_items))
# print(news_items[0])
# print("\n")

# #
# for item in news_items[:3]:
#     link = item.find("a", attrs={"class": "VDXfz"}).get("href")
#     # print(link)
#     news_link = origin_url + link[1:]
#     print("-----------------------------")
#     print(news_link)

#     news_title = item.find("a", attrs={"class": "DY5T1d"}).getText()
#     print("-----------------------------")
#     print(news_title)

#     news_content = item.find("span", attrs={"class": "xBbh9"}).text
#     print("-----------------------------")
#     print(news_content)

#     news_agency = item.find("a", attrs={"class": "wEwyrc AVN2gc uQIVzc Sksgp"}).text
#     print("-----------------------------")
#     print(news_agency)

#     news_datetime = (
#         item.find("time", attrs={"class": "WW6dff uQIVzc Sksgp"})
#         .get("datetime")
#         .split("T")
#     )
#     # print(news_datetime)
#     news_date = news_datetime[0][:-1]
#     news_time = news_datetime[1][:-1]
#     print("-----------------------------")
#     print(news_date, news_time)
#     print("\n")
