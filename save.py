import csv


def save_to_file(news):
    file = open("google_news.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["link", "title", "content", "agency", "date", "time"])
    print(news)
    for item in news:
        writer.writerow(list(item.values()))
        # print(news.values())
    return
