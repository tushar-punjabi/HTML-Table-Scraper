import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the web browser (use Chrome or Firefox)
driver = webdriver.Chrome()

# Navigate to the webpage with the table
driver.get("https://www.bayut.com/property-market-analysis/sale/?page=2")

# Locate the table (modify the selector as needed)
table = driver.find_element(By.CSS_SELECTOR,'table')

# Extract rows and cells from the table
rows = table.find_elements(By.TAG_NAME,'tr')

# Initialize an empty list to store table data
table_data = []

for row in rows:
    cells = row.find_elements_by_tag_name('td')
    row_data = [cell.text for cell in cells]
    table_data.append(row_data)

# Save data to a CSV file
with open('table_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in table_data:
        csv_writer.writerow(row)

# Close the browser
driver.quit()