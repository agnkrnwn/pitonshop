from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys
import pandas as pd
import dbm

browser = webdriver.Chrome('./chromedriver')  # disini letak driver ente

# akun shopee isi nama passwordnya
shopee_name = "izzabags"
shopee_pass = "45Uk1r1k??>>"

# login shopee , pastikan autenfikasi 2 faktor mati biar gampang
browser.get('https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F')
time.sleep(1)

# send keys ke email /usernem ke colom login
browser.find_element_by_name("loginKey").send_keys(shopee_name)
browser.find_element_by_name("password").send_keys(shopee_pass)
time.sleep(3)

# klik tombol login
browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
time.sleep(1)
print("login done.")

# link produk flash sale yg akan di beli ubah aja
browser.get('https://shopee.co.id/user/purchase/list/?type=3')

print('mengambil data jumlah checkout')
time.sleep(10)
# Allow 2 seconds for the web page to open
# You can set your own pause time. My laptop is a bit slow so I use 1 sec
scroll_pause_time = 3
screen_height = browser.execute_script(
    "return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    browser.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = browser.execute_script(
        "return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break


print('suckkk')


time.sleep(10)

# Once we are in, let us extract all of the product elements then names
product_titles = browser.find_elements_by_class_name(
    'order-content__header__seller__name')
for title in product_titles:
    print(title.text)

product_containers = browser.find_elements_by_class_name(
    'order-card__container')

product_titles = list()
product_prices = list()

for container in product_containers:
    product_titles.append(container.find_element_by_class_name(
        'order-content__header__seller__name').text)
    product_prices.append(
        container.find_element_by_class_name('purchase-card-buttons__total-price').text)

data = {'nama_toko': product_titles, 'total_checkout': product_prices}
df_product = pd.DataFrame.from_dict(data)

print(df_product.head())

# -------------------------------EXPORT and SAVE-------------------------------
# Exporting the data into csv
df_product.to_csv('hasil.csv')
