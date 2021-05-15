import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import holiday


def main():
    if holiday.isHoliday(dt.now().strftime('%Y%m%d')):
        return

    url = "https://portal.morningstarjp.com/StockInfo/pts/ranking?kind=0&page="
    for i in range(3):
        html_data = requests.get(url + str(i))
        soup = BeautifulSoup(html_data.content, "html.parser")
        table = soup.findAll("table", {"class": "sr-tbl"})[0]
        tbody = table.find("tbody").findAll("tr")

        if i == 0:
            file = open('./data/pts.csv', "w", encoding="utf-8")
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(["順位",
                             "コード",
                             "銘柄名",
                             "主要",
                             "時刻",
                             "現在値",
                             "基準値比",
                             "基準値比(%)",
                             "出来高",
                             "売買代金"])
        else:
            file = open('./data/pts.csv', "a", encoding="utf-8")
            writer = csv.writer(file, lineterminator='\n')

        for index, row in enumerate(tbody):
            cell = row.findAll(['td'])
            writer.writerow([cell[0].get_text(),
                             cell[1].get_text(),
                             cell[2].get_text(),
                             cell[3].get_text(),
                             cell[4].get_text(),
                             cell[5].get_text(),
                             cell[6].get_text(),
                             cell[7].get_text(),
                             cell[8].get_text(),
                             cell[9].get_text()])
        file.close()


if __name__ == '__main__':
    main()
