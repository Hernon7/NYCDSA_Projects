from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')

driver.get("https://www.skyscrapercenter.com/compare-data/submit?type%5B%5D=building&status%5B%5D=COM&material%5B%5D=steel&material%5B%5D=concrete&material%5B%5D=composite&material%5B%5D=concrete%2Fsteel&material%5B%5D=steel%2Fconcrete&material%5B%5D=precast&material%5B%5D=masonry&function%5B%5D=office&function%5B%5D=residential&function%5B%5D=hotel&function%5B%5D=mixed-use&base_region=0&base_country=0&base_city=0&base_height_range=3&base_company=All&base_min_year=0&base_max_year=9999&comp_region=0&comp_country=0&comp_city=0&comp_height_range=0&comp_company=All&comp_min_year=0&comp_max_year=9999&skip_comparison=on&output%5B%5D=list&dataSubmit=%E6%98%BE%E7%A4%BA%E7%BB%93%E6%9E%9C")
# Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
# review_button.click()

csv_file = open('building.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True:
	try:
		print("Scraping Page number " + str(index))
		index = index + 1
		# Find all the reviews on the page
		# wait_review = WebDriverWait(driver, 10)
		# reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
		# 							'//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')))
		records = driver.find_elements_by_xpath('//*[@id="table-baseList"]/tbody/tr')
		for record in records:
			i = records.index(record)+1
			# Initialize an empty dictionary for each review
			record_dict = {}
			# Use relative xpath to locate the title, text, username, date, rating.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			try:
				building = record.find_element_by_xpath('.//td[@class = "building-hover"]').text
			except:
				continue

			city = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[4]/a[1]' %i).text
			country = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[4]/a[2]' %i).text
			height = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[5]' %i).text
			floor = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[7]' %i).text
			year = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[8]' %i).text
			marterial = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[9]' %i).text
			use = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[10]' %i).text


			record_dict['building'] = building
			record_dict['city'] = city
			record_dict['country'] = country
			record_dict['height'] = height
			record_dict['floor'] = floor
			record_dict['year'] = year
			record_dict['marterial'] = marterial
			record_dict['use'] = use

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