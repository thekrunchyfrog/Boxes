from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

baseURL = "https://atariage.com/system_items.php?SystemID=2600&ItemTypeID=BOX"

driver = webdriver.Chrome()
driver.get(baseURL)

Select(driver.find_element_by_name('recordsPerPage')).select_by_value('All')
driver.find_element_by_name('btnSubmit').click()

games = driver.find_elements_by_css_selector('table.standard tr td:first-of-type a')

try:

    gamePages = []

    for game in games:

        if game.text != "Title" and game.text != " " and game.text != "":

            gamePages.append(game.text)

    for gamePage in gamePages:

        driver.find_element_by_link_text(gamePage).click()

        images = driver.find_elements_by_tag_name('img')

        front = images[21].get_attribute("src")
        back = images[22].get_attribute("src")

        print front
        print back

        driver.back()

finally:
    driver.quit()
