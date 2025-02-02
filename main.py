from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 15
time_interval = time.time() + 5
cookie = driver.find_element(By.ID, "cookie")

price = driver.find_elements(By.CSS_SELECTOR, "#store b")
price.pop(-1)
price_list = [int(item.text.split("-")[1].replace(",", "")) for item in price]
print(price_list)

while time.time() < timeout:
    cookie.click()
    # if time.time() > time_interval:
    #     index = 0
    #     balance = int(driver.find_element(By.XPATH, '//*[@id="money"]').text)
    #     affordable_upgrades = []
    #     for item in price_list:
    #         if balance > item:
    #             affordable_upgrades.append(item)
    #             highest_price_item = max(affordable_upgrades)
    #
    #             if balance < 0:
    #                 price[index].click()
    #         index += 1

