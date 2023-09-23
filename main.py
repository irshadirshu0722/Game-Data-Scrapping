from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep
import csv

with open("data.csv", 'a',newline='',encoding='utf-8') as file:
    row_data = ['name','rating',"price"]
    writer = csv.writer(file)

    writer.writerow(row_data)
driver = Service(
    r"C:\development\geckodriver.exe"
)
driver = webdriver.Firefox(service=driver)
driver.get("https://steamdb.info/")
driver.maximize_window()

explore_click = driver.find_elements(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr")

for game_data in explore_click:
    rows = game_data.find_elements(By.TAG_NAME,"td")
    with open("data.csv",'a',newline='',encoding='utf-8') as file:
        row_data = [rows[1].text,rows[2].text,rows[3].text]
        writer = csv.writer(file)

        writer.writerow(row_data)


driver.close()