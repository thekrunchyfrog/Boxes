from selenium import webdriver
from selenium.webdriver.support.ui import Select

baseURL = "https://atariage.com/system_items.php?SystemID=2600&ItemTypeID=BOX"

driver = webdriver.Chrome()
driver.get(baseURL)

recordsPerPage = Select(driver.find_element_by_name('recordsPerPage'))
recordsPerPage.select_by_value('All')
driver.find_element_by_name('btnSubmit').click()

games = driver.find_elements_by_css_selector('table.standard tr')

for game in games:
    print(game.text)