from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re


driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')

driver.get("https://www.skyscrapercenter.com/cities")


index = 1
urls = []
while True:
	try:
		print("Scraping Page number " + str(index))
		index = index + 1
		records = driver.find_elements_by_xpath('//*[@id="table-cities"]/tbody/tr')
		for record in records:
			i = records.index(record)+1
			url = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[2]/a' %i).get_attribute('href')
			urls.append(url)
   
		wait_button = WebDriverWait(driver, 10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="paginate_button next"]')))
		next_button.click()
		print(len(urls))
	except Exception as e:
		print(e)        
		break



csv_file = open('city_detail.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
record_dict = {}


for url in urls:
	driver.get(url)
	try:
		population = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]').text.split()[0].replace(",","")
		if len(population) <=3:
			population = None
		else:
			population = int(population)
	except:
		population = None
    
	try:
		area = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[2]').text.split()[0].replace(",","")
		if len(area) <=2:
			area = None
		else:
			area = int(area)
	except:
		area = None

	record_dict['population'] = population
	record_dict['area'] = area
	writer.writerow(record_dict.values())
csv_file.close()
driver.close()

