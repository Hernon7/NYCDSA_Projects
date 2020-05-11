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
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="paginate_button next"]')))
        next_button.click()
        print(len(urls))
    except Exception as e:
        print(e)
        driver.close()
        break


