import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import holiday


def main():
    if holiday.isHoliday(dt.now().strftime('%Y%m%d')):
        return

    html_data = requests.get('https://kabutan.jp/warning/?mode=2_1&market=0&capitalization=-1&stc=&stm=0&page=')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "rankingTable"})[0]
    thead = table.find("thead").findAll("tr")
    tbody = table.find("tbody").findAll("tr")

    # 日次別ファイル作成
    file = open('./rise_rate_ranking/rise_rate_ranking_' + dt.now().strftime('%Y%m%d') + '.csv', 'w', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    # ヘッダー
    for index, row in enumerate(thead):
        cell = row.findAll(['th'])
        writer.writerow(["日付",
                         "コード",
                         "銘柄名"
                         "市場",
                         "株価",
                         "前日比(%)",
                         "前日比",
                         "出来高",
                         "ＰＥＲ",
                         "ＰＢＲ",
                         "利回り"])
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer.writerow([dt.now().strftime('%Y/%m/%d'),
                         cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[6].get_text(),
                         cell[7].get_text()])
    file.close()

    # 累積ファイル作成
    file = open('./data/limit_high.csv', 'a', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer.writerow([dt.now().strftime('%Y/%m/%d'),
                         cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[6].get_text(),
                         cell[7].get_text()])
    file.close()


if __name__ == '__main__':
    main()
