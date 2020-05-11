#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#%%
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.skyscrapercenter.com/compare-data/submit?type%5B%5D=building&status%5B%5D=COM&material%5B%5D=steel&material%5B%5D=concrete&material%5B%5D=composite&material%5B%5D=concrete%2Fsteel&material%5B%5D=steel%2Fconcrete&material%5B%5D=precast&material%5B%5D=masonry&function%5B%5D=office&function%5B%5D=residential&function%5B%5D=hotel&function%5B%5D=mixed-use&base_region=0&base_country=0&base_city=0&base_height_range=3&base_company=All&base_min_year=0&base_max_year=9999&comp_region=0&comp_country=0&comp_city=0&comp_height_range=0&comp_company=All&comp_min_year=0&comp_max_year=9999&skip_comparison=on&output%5B%5D=list&dataSubmit=%E6%98%BE%E7%A4%BA%E7%BB%93%E6%9E%9C")
records = driver.find_elements_by_xpath('//*[@id="table-baseList"]/tbody/tr')
#%%


for record in records[:2]:
    i = records.index(record)+1
			
    building = record.find_element_by_xpath('.//td[@class = "building-hover"]').text
    city = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[4]/a[1]' %i).text
    country = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[4]/a[2]' %i).text
    height = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[5]' %i).text
    floor = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[7]' %i).text
    year = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[8]' %i).text
    marterial = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[9]' %i).text
    use = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[%d]/td[10]' %i).text

#%%
record = records[0]

#%%
city = record.find_element_by_xpath('//*[@id="table-baseList"]/tbody/tr[100]/td[3]/a').text
print(city)

#%%
for record in records:
    print(records.index(record)+1)
#%%
