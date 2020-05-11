
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.emporis.com/statistics/most-expensive-buildings")
records = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr')
csv_file = open('building_cost.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
record_dict = {}



for record in records:
    i = records.index(record)+1
    name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr[%d]/td[3]/a' %i).text
    year = int(driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr[%d]/td[7]' %i).text.replace("$","").replace(",",""))
    cost = int(driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr[%d]/td[8]' %i).text.replace("$","").replace(",",""))
    print("working on",i+1)
    record_dict['name'] = name
    record_dict['year'] = year
    record_dict['cost'] = cost
    writer.writerow(record_dict.values())

csv_file.close()
driver.close()

