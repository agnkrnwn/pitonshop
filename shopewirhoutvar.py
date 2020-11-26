from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# checkoutshopee python

# diaman ente naruh drivernya klo bisa jadikan 1 folder
browser = webdriver.Chrome('./chromedriver')


# akun shopee isi nama passwordnya
shopee_name = "double.88"
shopee_pass = "Asukirik1822"


# login shopee , pastikan autenfikasi 2 faktor mati biar gampang dan cepet
browser.get('https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F')
time.sleep(1)

# send keys ke emaial dan passsword
browser.find_element_by_name("loginKey").send_keys(shopee_name)
browser.find_element_by_name("password").send_keys(shopee_pass)
time.sleep(1)

# klik login button
browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
time.sleep(1)
print("login done....")

# link produk flash sale yg akan di beli
browser.get(
    'https://shopee.co.id/Celana-Senam-Legging-Polos-Pendek-i.4296506.2591926102')  # copas disisini halaman produk yg mau ente beli , klo halaman ada variasnya , pakai yg satunya jangan ini

# grab nama produk untuk estetik aja
for person in browser.find_elements_by_class_name('qaNIZv'):
    title = person.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span').text
print("produk " + title)
time.sleep(1)

# klik beli sekarang di halaman produk
print("membeli " + title)
time.sleep(1)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
browser.execute_script("arguments[0].click();", element)
print("done....")

# checkout produk
time.sleep(3)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
browser.execute_script("arguments[0].click();", element)
print("checkout " + title)

# klo mau metode pambayaran tf bank uncomment line di bawah ini , shopepay aja udah paling cepet, pke metode bank butuh time.sleep lamaa

"""
# klik metode transfer bank
time.sleep(2)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button')
browser.execute_script("arguments[0].click();", element)

# klik radio button bank bca cek otomtatis, klo mau yg lain ubah aja value xpath nya
time.sleep(5)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div')
browser.execute_script("arguments[0].click();", element)
"""

# klik buat pesanan .
# kasi waktu 5 detik untul loading button biar bisa di klik klo pke metode pambayarn bank tergnatung internet kalian
time.sleep(3)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')
browser.execute_script("arguments[0].click();", element)

print("PRODUK " + title +
      " BERHASIL DI BELI, SILAHKAN LANJUTKAN PEMBAYARAN DI APLIKASI SHOPEE")
time.sleep(2)
print('MADE WITH LOVE FROM IZZABAGS ')
time.sleep(1)
browser.close()
