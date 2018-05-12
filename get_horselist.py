# coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import csv


# 出馬表がほしいレースのnetkeibaのurlをコピペ
url = input('レースURLを入力：')

#ブラウザを開く
driver = webdriver.Chrome()

# netkeibaのページを開く
driver.get(url)

# 確認
assert 'レース情報' in driver.title

#ヘッダー取得

table = []
h_li = []
for n in range(1,9):
    if n == 3:
        pass
    else:
        h_li.append(driver.find_element_by_css_selector('#shutuba > diary_snap > table > tbody > tr:nth-child(1) > th:nth-child({})'.format(str(n))).text.replace('\n', ''))
table.append(h_li)

#table取得
try:
    for i in range(4, 22):
        element = driver.find_element_by_css_selector('#shutuba > diary_snap > table > tbody > tr:nth-child({})'.format(str(n)))
        e_li = []
        for j in range(1,9):
            if j == 3:
                pass
            else:
                e_li.append(driver.find_element_by_css_selector('#shutuba > diary_snap > table > tbody > tr:nth-child({}) > td:nth-child({})'.format(str(i), str(j))).text.replace('\n', ''))
        table.append(e_li)
except:
    pass

title = driver.title.rstrip('/ 出馬表｜レース情報(JRA) - netkeiba.com').replace('/', '_')


with open('{}.csv'.format(title), 'w') as file:
    for row in table:
        file.write(','.join(row) + '\n')

driver.quit()
