# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

# レース名入力
race_name = input('レース名を入力してください：')

#ブラウザを開く
driver = webdriver.Chrome()

# netkeibaのデータベースを開く
driver.get('http://db.netkeiba.com/?rf=navi')

# 確認
assert 'データベース' in driver.title

# 検索
driver.find_element_by_css_selector('#main > div.deta_search.fc > div.db_search_form_box.fc > form > input.field').send_keys(race_name)
element = driver.find_element_by_css_selector('#main > div.deta_search.fc > div.db_search_form_box.fc > form > select')
type_select = Select(element)
type_select.select_by_value('race')

driver.find_element_by_css_selector('#main > div.deta_search.fc > div.db_search_form_box.fc > form > input.button.imgover').click()

# 5秒待機
sleep(5)

# レース名のリンクのエレメントを取得
links = driver.find_elements_by_partial_link_text(race_name)

# 過去十年分のurlを取り出す
urls = []
for a in links[:10]:
    print(a.get_attribute('href'))
    urls.append(a.get_attribute('href'))

#1年分ずつアクセス
for url in urls:
    driver.get(url)
    sleep(5)

    title = driver.title
    wakuban = driver.find_element_by_css_selector('#contents_liquid > table > tbody > tr:nth-child(2) > td:nth-child(2) > span').text
    umaban = driver.find_element_by_css_selector('#contents_liquid > table > tbody > tr:nth-child(2) > td:nth-child(3)').text
    name = driver.find_element_by_css_selector('#contents_liquid > table > tbody > tr:nth-child(2) > td:nth-child(4) > a').text

    print('title :', title)
    print('wakuban :', wakuban)
    print('umaban :', umaban)
    print('name :', name)

driver.quit()
