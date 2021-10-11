# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import pandas as pd

region = 'Tainan'


def crawler():
    date = []
    time = []
    temp = []
    weather = []
    prb_precipitation = []
    feel_like_temp = []
    relative_hum = []
    wind_force = []
    wind_speed = []
    wind_direction = []
    comfort = []

    global region
    # 台南測站觀測資料
    url = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1001801'

    # 啟動模擬瀏覽器
    driver = webdriver.Chrome()

    # 取得網頁代碼
    driver.get(url)
    open(region+'.html', 'wb').write(driver.page_source.encode('utf-8'))

    # 指定 lxml 作為解析器
    soup = BeautifulSoup(driver.page_source, features='lxml')

    # <tbody> 抓預測資料的table
    table = soup.find('table', {'id': 'TableId3hr'})

    # <tbody>内所有<tr>標籤
    trs = table.find_all('tr')
    th = table.find('th', {'id': 'PC3_D1'})

    # 使用datetime取得時間年分
    date.append(th.text)
    time.append(trs[1].find_all('th')[1].text)

    # #對list中的每一項 <tr>
    weather.append(
        trs[2].find_all('td')[1].find('img')['title'])
    temp.append(
        trs[3].find_all('td')[1].find_all('span')[0].text)
    feel_like_temp.append(
        trs[4].find_all('td')[1].find_all('span')[0].text)
    prb_precipitation.append(
        trs[5].find_all('td')[1].text)
    relative_hum.append(
        trs[6].find_all('td')[1].text)
    wind_force.append(
        trs[7].find_all('td')[1].text)
    wind_speed.append(
        trs[8].find_all('td')[1].text)
    wind_direction.append(
        trs[9].find_all('td')[1].text)
    comfort.append(
        trs[10].find_all('td')[1].text)
# 關閉模擬瀏覽器
    driver.quit()
# ---------------------------------------------------------------

    table = {
        "日期": date,
        "時間": time,
        "天氣": weather,
        "溫度(°C)": temp,
        "體感溫度(°C)": feel_like_temp,
        "降雨機率(%)": prb_precipitation,
        "相對溼度(%)": relative_hum,
        "風級": wind_force,
        "風力 (m/s)": wind_speed,
        "風向": wind_direction,
        "舒適度": comfort,
    }
    # print(table)
    return table


if __name__ == '__main__':
    crawler()
