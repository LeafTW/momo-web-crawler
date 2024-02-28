from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.EdgeOptions()
options.add_argument('--headless')
brows=webdriver.Edge(options)
# url='https://investanchors.com/'
# url="https://m.momoshop.com.tw/category.momo?cn=2132000145&sourcePageType=4&imgSH=itemizedType&sortType=6"

url="https://m.momoshop.com.tw/category.momo?cn=2132000145&sourcePageType=4&imgSH=itemizedType&sortType=6"
brows.get(url)
dates=brows.find_elements(By.XPATH,'//div[@class="swiper-slide swiper-slide-active"]/img/@data-original')

# dates=brows.find_elements(By.XPATH,'//div[@id="content"]//div[@class="col-md-4"]//div[@class="date"]/p')

for data in dates:
    print(data.text)

# print(brows)