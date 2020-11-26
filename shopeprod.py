from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

browser = webdriver.Chrome('./chromedriver')  # disini letak driver ente

# akun shopee isi nama passwordnya
shopee_name = "double.88"
shopee_pass = "Asukirik1822"

# login shopee , pastikan autenfikasi 2 faktor mati biar gampang
browser.get('https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2F&next=https%3A%2F%2Fshopee.co.id%2F')
time.sleep(1)

# send keys ke email /usernem ke colom login
browser.find_element_by_name("loginKey").send_keys(shopee_name)
browser.find_element_by_name("password").send_keys(shopee_pass)
time.sleep(1)

# klik tombol login
browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
time.sleep(1)
print("login done....")

# link produk flash sale yg akan di beli ubah aja
browser.get(
    'https://shopee.co.id/Sarirasa-Sate-Khas-Senayan-Soto-Ayam-Ambengan-380-gram-i.262464366.3936736842')

# grabbing nama produk niar uwu
for person in browser.find_elements_by_class_name('qaNIZv'):
    title = person.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span').text
print("produk " + title)

time.sleep(1)
# pilih variasi by xpath hnya ganti angka belakang untuk variasi lain dari kiri, untuk variasi lain klo gaada variasi nya pake yg satunya
browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[1]').click()  # ubah variasi disini copy aja xpath nya

print(" variasi done....")

# klik beli sekarang
print("membeli " + title)
time.sleep(1)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
browser.execute_script("arguments[0].click();", element)
print("done....")

# chkeout produk
time.sleep(1)
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
browser.execute_script("arguments[0].click();", element)
print("checkout " + title)

# klo mau metode pambayaran tf bank uncomment line di bawah ini , shopepay aja udah paling cepet
""" 

#klik metode transfer bank
time.sleep(5) #kasi jeda 5-6 setik klo pke metrode pambayaran bank
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button')
browser.execute_script("arguments[0].click();", element)

#klik radio button bank bca cek otomtatis, klo mau yg lain ubah aja value xpath nya
time.sleep(5) #kasi jeda 5-6 setik klo pke metrode pambayaran bank
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div')
browser.execute_script("arguments[0].click();", element)
"""


# klik buat pesanan
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)  # kasi jeda 5-6 setik klo pke metrode pambayaran bank
element = browser.find_element_by_xpath(
    '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')
browser.execute_script("arguments[0].click();", element)

print("PRODUK " + title +
      " BERHASIL DI BELI, SILAHKAN LANJUTKAN PEMBAYARAN DI APLIKASI SHOPEE")
time.sleep(2)
print('MADE WITH LOVE FROM IZZABAGS ')
time.sleep(1)
browser.close()

# JANGAN LUPA CEK TOKO IZZABAGS DI SHOPEEE DANBELI KLO ENTE DAPET
