from selenium import webdriver
from bs4 import BeautifulSoup
from Items import Items
from Xpath import Xpath
import time
from datetime import datetime
from MyDb import MyDb
import SQLBundle as sql_list

url_gsshop = "http://www.gsshop.com/prd/prd.gs?prdid="

# Init ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)

items_list = []

# Collecting Item Data
for no in range(35558699, 35558699+2, 1):
    item_info = []
    item = Items()
    xpaths = Xpath()

    item.url = url_gsshop+"{nums}".format(nums=no)
    driver.get(item.url)

    driver.implicitly_wait(10)

    try:
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        # 상대 Xpath
        xpaths.title = "//p[@class='{0}']".format('product-title')
        xpaths.img = "//a[@class='{0}']//img".format('btn_img')
        xpaths.price = "//span[@class='{0}']//ins//strong".format('price-definition-ins')

        # element
        element_title = driver.find_element_by_xpath(xpaths.title)
        element_image = driver.find_element_by_xpath(xpaths.img)
        element_price = driver.find_element_by_xpath(xpaths.price)

        # item class
        item_info.append(datetime.today().strftime("%Y-%m-%d"))

        if len(element_title.text) > 100:
            item_info.append(element_title.text[:100])
        else:
            item_info.append(element_title.text)

        item_info.append(element_image.get_attribute("src"))
        item_info.append(element_price.text)

        items_list.append(item_info)
    except Exception as e:
        print(e)
        continue
    finally:
        print("next")

# 수집한 아이템 리스트
# print(items_list)

# DataBase 연결
my_db = MyDb()

print(sql_list.insert_item())
my_db.db_executemany(sql_list.insert_item(), items_list)

print(sql_list.select_all_items())
aa = my_db.db_select(sql_list.select_all_items())
print(aa)







