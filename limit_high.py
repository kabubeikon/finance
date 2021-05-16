import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import holiday


def main():
    if holiday.isHoliday(dt.now().strftime('%Y%m%d')):
        return

    html_data = requests.get('https://info.finance.yahoo.co.jp/ranking/?kd=27&mk=1&tm=d&vl=a')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "rankingTable"})[0]
    thead = table.find("thead").findAll("tr")
    tbody = table.find("tbody").findAll("tr")

    # 日次別ファイル作成
    file1 = open('./limit_high/limit_high_' + dt.now().strftime('%Y%m%d') + '.csv', 'w', encoding="utf-8")
    writer1 = csv.writer(file1, lineterminator='\n')
    # 累積ファイル作成
    file2 = open('./data/limit_high.csv', 'a', encoding="utf-8")
    writer2 = csv.writer(file2, lineterminator='\n')

    # ヘッダー
    for index, row in enumerate(thead):
        cell = row.findAll(['th'])
        writer1.writerow(["日付",
                          "コード",
                          "市場",
                          "名称",
                          "取引値",
                          "前日比(%)",
                          "前日比",
                          "高値"])
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer1.writerow([dt.now().strftime('%Y/%m/%d'),
                          cell[0].get_text(),
                          cell[1].get_text(),
                          cell[2].get_text(),
                          cell[4].get_text(),
                          cell[5].get_text(),
                          cell[6].get_text(),
                          cell[7].get_text()])
        writer2.writerow([dt.now().strftime('%Y/%m/%d'),
                          cell[0].get_text(),
                          cell[1].get_text(),
                          cell[2].get_text(),
                          cell[4].get_text(),
                          cell[5].get_text(),
                          cell[6].get_text(),
                          cell[7].get_text()])
    file1.close()
    file2.close()


if __name__ == '__main__':
    main()
