import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import holiday


def main():
    if holiday.isHoliday(dt.now().strftime('%Y%m%d')):
        return

    # 取引時間中、決算発表・業績修正銘柄
    url1 = "https://kabutan.jp/warning/?mode=4_2&market=0&capitalization=-1&stc=&stm=0&page="
    # 取引終了後、決算発表・業績修正銘柄
    url2 = "https://kabutan.jp/warning/?mode=4_3&market=0&capitalization=-1&stc=&stm=0&page="
    file = open('./data/earnings_announcement.csv', 'a', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    for i in range(1, 20):
        html_data = requests.get(url1 + str(i))
        soup = BeautifulSoup(html_data.content, "html.parser")
        table = soup.findAll("table", {"class": "stock_table"})[0]
        tbody = table.find("tbody").findAll("tr")
        for index, row in enumerate(tbody):
            th = row.findAll(['th'])
            td = row.findAll(['td'])
            writer.writerow([td[0].get_text().strip(),
                             th[0].get_text().strip(),
                             td[1].get_text().strip(),
                             td[3].get_text().strip(),
                             td[4].get_text().strip(),
                             td[6].get_text().strip(),
                             td[7].get_text().strip(),
                             td[8].get_text().strip(),
                             td[9].get_text().strip(),
                             dt.now().strftime('%Y/%m/%d')])
    for i in range(1, 60):
        html_data = requests.get(url2 + str(i))
        soup = BeautifulSoup(html_data.content, "html.parser")
        table = soup.findAll("table", {"class": "stock_table"})[0]
        tbody = table.find("tbody").findAll("tr")
        for index, row in enumerate(tbody):
            th = row.findAll(['th'])
            td = row.findAll(['td'])
            writer.writerow([td[0].get_text().strip(),
                             th[0].get_text().strip(),
                             td[1].get_text().strip(),
                             td[3].get_text().strip(),
                             td[4].get_text().strip(),
                             td[6].get_text().strip(),
                             td[7].get_text().strip(),
                             td[8].get_text().strip(),
                             td[9].get_text().strip(),
                             dt.now().strftime('%Y/%m/%d')])
    file.close()


if __name__ == '__main__':
    main()
