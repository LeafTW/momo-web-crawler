from selenium import webdriver
from selenium.webdriver.common.by import By

user={'uid':'40831231','pwd':'4227205t'}

driver=webdriver.Edge()

url='https://siw.tpcu.edu.tw/tsint/'

driver.get(url)

driver.switch_to.default_content()
frame=driver.find_element(By.XPATH,'//frame[@id="Main"]')
driver.switch_to.frame(frame)

for data in user.items():
    driver.find_element(By.XPATH,"//input[@name=\'"+ data[0] + "\']").send_keys(data[1])

codemath=driver.find_element(By.XPATH,"(//tbody)[2]/tr[5]//td[2]/font")
print(codemath.text[0])
if codemath.text[0] == "0":
    codemathans = eval(codemath.text[1:4])
else:
    codemathans = eval(codemath.text[0:4])

driver.find_element(By.XPATH,"//tbody[1]/tr[5]//td[2]/input").send_keys(codemathans)
driver.find_element(By.XPATH,"//tbody[1]/tr[6]/td/input[2]").click()

import time
time.sleep(100)