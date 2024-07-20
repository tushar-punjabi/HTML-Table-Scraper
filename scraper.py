from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()


urls = ["https://www.bayut.com/property-market-analysis/sale/?page={}".format(i) for i in range(2,3)]

text_file_path = 'output.txt'

result=[]



for url in urls:
    driver.get(url)
    date = driver.find_elements(By.XPATH, "[aria-label='Date']")
    location = driver.find_elements(By.XPATH, "[aria-label='Location']")
    price = driver.find_elements(By.CSS_SELECTOR, "[aria-label='Price']")
    beds = driver.find_elements(By.XPATH, "[aria-label='Beds']")
    area = driver.find_elements(By.XPATH, "[aria-label='Area']")
    unit = driver.find_elements(By.XPATH, "[class='_948d9e0a _65f1db20 d7383df5 _371e9918']")

    print(date.text)






'''
    for h4 in all_h4:
        with open('output.txt', 'w') as f:
            f.write(f"{h4.text}")


df_data=pd.DataFrame(result)
df_data


'''

print(result)

print('                                                                    ')
print('----------------------END OF SCRIPT---------------------------------')
print('                                                                    ')

driver.quit()