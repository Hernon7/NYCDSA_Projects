from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re


driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')

driver.get("https://www.skyscrapercenter.com/cities")


csv_file = open('city.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True:
	try:
		print("Scraping Page number " + str(index))
		index = index + 1

		records = driver.find_elements_by_xpath('//*[@id="table-cities"]/tbody/tr')
		for record in records:
			i = records.index(record)+1
			# Initialize an empty dictionary for each review
			record_dict = {}

			try:
				city = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[2]/a' %i).text 
			except:
				continue

			country = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[3]/a' %i).text 
			building100 = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[5]' %i).text 
			building150 = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[6]' %i).text 
			building200 = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[7]' %i).text 
			building300 = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[8]' %i).text 
			buildingnum = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[10]' %i).text 
			


			record_dict['city'] = city
			record_dict['country'] = country
			record_dict['building100'] = building100
			record_dict['building150'] = building150
			record_dict['building200'] = building200
			record_dict['building300'] = building300
			record_dict['buildingnum'] = buildingnum


			writer.writerow(record_dict.values())

		# Locate the next button on the page.
		wait_button = WebDriverWait(driver, 10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'//a[@class="paginate_button next"]')))
		next_button.click()
	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break