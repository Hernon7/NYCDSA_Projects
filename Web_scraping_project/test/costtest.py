

%##
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#%%
driver = webdriver.Chrome(r'C:/Users/60223/Desktop/pythonproject/chromedriver.exe')
driver.get("https://www.emporis.com/statistics/most-expensive-buildings")
records = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr')

#%%
record = records[5]
name = driver.find_element_by_xpath('//*[@class = "header-link "  ]').text
print(name)

#%%
for record in records[:5]:
    i = records.index(record)+1
    name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr[%d]/td[3]/a' %i).text
    cost = int(driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/table/tbody/tr[%d]/td[8]' %i).text.replace("$","").replace(",",""))
    print(name,cost)


#%%
