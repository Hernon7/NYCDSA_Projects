
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#%%
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.skyscrapercenter.com/cities")

#%%

records = driver.find_elements_by_xpath('//*[@id="table-cities"]/tbody/tr')
len(records)
#%%
for record in records[:1]:
    i = records.index(record) + 1
    city = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[2]/a' %i).text 
    country = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[3]/a' %i).text 
    building100 = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[5]' %i).text 
    building150= driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[6]' %i).text 
    building200 = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[7]' %i).text 
    building300 = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[8]' %i).text 
    buildingnum = driver.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[10]' %i).text 
    print(city,country,building100,building150,building200,building300,buildingnum)




#%%

#%%
urls = []
for record in records:
    i = records.index(record) + 1
    url = record.find_element_by_xpath('//*[@id="table-cities"]/tbody/tr[%d]/td[2]/a' %i).get_attribute('href')
    urls.append(url)
urls

#%%
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
    print(population)

#%%
for url in urls:
    driver.get(url)
    try:
        area = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[2]').text.split()[0].replace(",","")
        if len(area) <=2:
            area = None
        else:
            area = int(area)
    except:
        area = None
    print(area)

#%%
url = urls[0]
driver.get(url)
population = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]').text.split()[0].replace(",","")

print(len(population))












#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.skyscrapercenter.com/compare-data/submit?type%5B%5D=building&status%5B%5D=COM&material%5B%5D=steel&material%5B%5D=concrete&material%5B%5D=composite&material%5B%5D=concrete%2Fsteel&material%5B%5D=steel%2Fconcrete&material%5B%5D=precast&material%5B%5D=masonry&function%5B%5D=office&function%5B%5D=residential&function%5B%5D=hotel&function%5B%5D=mixed-use&base_region=0&base_country=0&base_city=0&base_height_range=3&base_company=All&base_min_year=0&base_max_year=9999&comp_region=0&comp_country=0&comp_city=0&comp_height_range=0&comp_company=All&comp_min_year=0&comp_max_year=9999&skip_comparison=on&output%5B%5D=list&dataSubmit=%E6%98%BE%E7%A4%BA%E7%BB%93%E6%9E%9C")

index = 1
urls = []
while True:
	try:
        
		print("Scraping Page number " + str(index))
		index = index + 1
		
		records = driver.find_elements_by_xpath('//*[@id="table-baseList"]/tbody/tr')
        for record in records:
            url = record.find_element_by_xpath('.//td[@class = "building-hover"]//a').get_attribute('href')
            urls.append(url)
        wait_button = WebDriverWait(driver, 10)
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'//a[@class="paginate_button next"]')))
        next_button.click()
        print(len(urls))











#%%
driver.get(urls[0])


#%%
temp1 = driver.find_element_by_xpath('//a[@href="/definition/official-name"]/../../td[2]').text
temp = driver.find_element_by_xpath('//a[@href="/definition/construction"]/../..').text.split()[-1]
temp2 = driver.find_element_by_xpath('//a[@href="/definition/tower-gfa"]/../..').text.split()[2]

print(temp1,temp,temp2)

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.skyscrapercenter.com/compare-data/submit?type%5B%5D=building&status%5B%5D=COM&material%5B%5D=steel&material%5B%5D=concrete&material%5B%5D=composite&material%5B%5D=concrete%2Fsteel&material%5B%5D=steel%2Fconcrete&material%5B%5D=precast&material%5B%5D=masonry&function%5B%5D=office&function%5B%5D=residential&function%5B%5D=hotel&function%5B%5D=mixed-use&base_region=0&base_country=0&base_city=0&base_height_range=3&base_company=All&base_min_year=0&base_max_year=9999&comp_region=0&comp_country=0&comp_city=0&comp_height_range=0&comp_company=All&comp_min_year=0&comp_max_year=9999&skip_comparison=on&output%5B%5D=list&dataSubmit=%E6%98%BE%E7%A4%BA%E7%BB%93%E6%9E%9C")
records = driver.find_elements_by_xpath('//*[@id="table-baseList"]/tbody/tr')
urls = []
for record in records[:5]:
    url = record.find_element_by_xpath('.//td[@class = "building-hover"]//a').get_attribute('href')
    urls.append(url)
for url in urls:
    driver.get(url)
    try:
        name = driver.find_element_by_xpath('//a[@href="/definition/official-name"]/../../td[2]').text
    except:
        name = NULL
    try:
        start_year = driver.find_element_by_xpath('//a[@href="/definition/construction"]/../..').text.split()[-1]
    except:
        start_year = NULL
    try:
        area = driver.find_element_by_xpath('//a[@href="/definition/tower-gfa"]/../..').text.split()[2]
    except:
        area = NULL
    print(name,start_year,area)

#%%
