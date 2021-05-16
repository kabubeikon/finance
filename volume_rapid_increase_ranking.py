# -*- coding: utf-8 -*-
import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import holiday


def main():
    if holiday.isHoliday(dt.now().strftime('%Y%m%d')):
        return

    # テクニカル - 出来高急増銘柄
    url = "https://kabutan.jp/tansaku/?mode=2_0311&market=0&capitalization=-1&stc=v3&stm=1&page="
    # 日次別ファイル作成
    file1 = open(
        './volume_rapid_increase_ranking/volume_rapid_increase_ranking_' + dt.now().strftime('%Y%m%d') + '.csv', 'w',
        encoding="utf-8")
    writer1 = csv.writer(file1, lineterminator='\n')
    # 累積ファイル作成
    file2 = open('./data/volume_rapid_increase_ranking.csv', 'a', encoding="utf-8")
    writer2 = csv.writer(file2, lineterminator='\n')

    # ヘッダー
    writer1.writerow(["日付",
                      "順位",
                      "コード",
                      "銘柄名",
                      "市場",
                      "株価",
                      "S高",
                      "前日比",
                      "出来高",
                      "ＰＥＲ",
                      "ＰＢＲ",
                      "利回り"])
    rank = 1
    for i in range(1, 8):
        html_data = requests.get(url + str(i))
        soup = BeautifulSoup(html_data.content, "html.parser")
        table = soup.findAll("table", {"class": "stock_table st_market"})[0]
        tbody = table.find("tbody").findAll("tr")
        for index, row in enumerate(tbody):
            td = row.findAll(['td'])
            th = row.findAll(['th'])
            writer1.writerow([dt.now().strftime('%Y/%m/%d'),
                              rank,
                              td[0].get_text(),
                              th[0].get_text(),
                              td[1].get_text(),
                              td[4].get_text(),
                              td[5].get_text(),
                              td[6].get_text(),
                              td[7].get_text(),
                              td[8].get_text(),
                              td[9].get_text(),
                              td[10].get_text()])
            writer2.writerow([dt.now().strftime('%Y/%m/%d'),
                              rank,
                              td[0].get_text(),
                              th[0].get_text(),
                              td[1].get_text(),
                              td[4].get_text(),
                              td[5].get_text(),
                              td[6].get_text(),
                              td[7].get_text(),
                              td[8].get_text(),
                              td[9].get_text(),
                              td[10].get_text()])
            rank += 1
    file1.close()
    file2.close()


if __name__ == '__main__':
    main()
