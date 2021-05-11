import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup


def main():
    file = open('./data/limit_high.csv', 'a', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    html_data = requests.get('https://info.finance.yahoo.co.jp/ranking/?kd=27&mk=1&tm=d&vl=a')
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "rankingTable"})[0]

    thead = table.find("thead").findAll("tr")
    for index, row in enumerate(thead):
        cell = row.findAll(['th'])
        print(cell[0].get_text())
        writer.writerow(["日付",
                         cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[3].get_text(),
                         cell[4].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text()])
    tbody = table.find("tbody").findAll("tr")
    for index, row in enumerate(tbody):
        cell = row.findAll(['td'])
        writer.writerow([dt.now().strftime('%Y/%m/%d'),
                         cell[0].get_text(),
                         cell[1].get_text(),
                         cell[2].get_text(),
                         cell[3].get_text(),
                         cell[4].get_text(),
                         cell[5].get_text(),
                         cell[6].get_text()])
    file.close()


if __name__ == '__main__':
    main()
