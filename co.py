from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#import pandas as pd
#import dbm
import time
import sys


browser = webdriver.Chrome('./chromedriver')  # disini letak driver ente

# akun shopee isi nama passwordnya
shopee_name = "double.88"
shopee_pass = "Asukirik1822"

# login shopee , pastikan autenfikasi 2 faktor mati biar gampang
browser.get('https://shopee.co.id/buyer/login')
time.sleep(1)

# send keys ke email /usernem ke colom login
browser.find_element_by_name("loginKey").send_keys(shopee_name)
browser.find_element_by_name("password").send_keys(shopee_pass)
time.sleep(3)

# klik tombol login
browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
print('cek siapa tau ada captha, punya waktu 30 detik')
time.sleep(30)
print("login done")


# link produk flash sale yg akan di beli ubah aja
browser.get('https://shopee.co.id/user/purchase/list/?type=3')

time.sleep(5)
print("mengambil data checkout....")
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

time.sleep(5)

# Once we are in, let us extract all of the product elements then names
seller_name = browser.find_elements_by_class_name(
    'order-content__header__seller__name')
for title in seller_name:
    print(title.text)

print('DONE..')

links = browser.find_elements_by_class_name(
    'order-content__header__seller__name')
print('TOTAL CHECKOUT: ', len(links))

product_containers = browser.find_elements_by_class_name(
    'order-card__container')

seller_name = list()
total_checkout = list()

for container in product_containers:
    seller_name.append(container.find_element_by_class_name(
        'order-content__header__seller__name').text)
    total_checkout.append(
        container.find_element_by_class_name('purchase-card-buttons__total-price').text)

data = {'Nama Seller': seller_name, 'Nilai checkout': total_checkout.translate(
    {ord(i): None for i in '. Rp'})}

#df_product = pd.DataFrame.from_dict(data)

# print(df_product.head())

# -------------------------------EXPORT and SAVE-------------------------------
# Exporting the data into csv
# df_product.to_csv('total_checkout.csv')

# Inserting into sqlite
# dbm.write_from_df_with_sqlite3(df_product)

# Inserting into sqlite with alchemy
# dbm.write_from_df_with_alchemy(df_product)


print(data)
