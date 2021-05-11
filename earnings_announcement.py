import csv
from datetime import datetime as dt

import requests
from bs4 import BeautifulSoup

import time

def main():
    file = open('./data/earnings_announcement.csv', 'w', encoding="utf-8")
    writer = csv.writer(file, lineterminator='\n')
    html_data = requests.get('https://kabutan.jp/warning/?mode=4_2&market=0&capitalization=-1&stc=&stm=0&page=1')
    time.sleep(5)
    writer.writerow(html_data)
    soup = BeautifulSoup(html_data.content, "html.parser")
    table = soup.findAll("table", {"class": "stock_table"})[0]
    thead = table.find("thead").findAll("tr")
    tbody = table.find("tbody").findAll("tr")

    for index, row in enumerate(tbody):
        th = row.findAll(['th'])
        td = row.findAll(['td'])
        writer.writerow([td[0].get_text().strip(),
                         th[0].get_text().strip(),
                         td[1].get_text().strip(),
                         td[2].get_text().strip(),
                         td[3].get_text().strip(),
                         td[4].get_text().strip(),
                         td[5].get_text().strip(),
                         td[6].get_text().strip(),
                         td[7].get_text().strip(),
                         td[8].get_text().strip()])
    file.close()


if __name__ == '__main__':
    main()
