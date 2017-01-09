from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib import urlretrieve
from time import sleep

baseURL = "https://atariage.com/system_items.php?SystemID=2600&ItemTypeID=BOX"
localPath = "/Users/rgregorio01/Repos/Boxes/Atari2600/"

driver = webdriver.Chrome()
driver.get(baseURL)

Select(driver.find_element_by_name('recordsPerPage')).select_by_value('All')
driver.find_element_by_name('btnSubmit').click()

games = driver.find_elements_by_css_selector('table.standard tr td:first-of-type a')

try:

    gamePages = []
    frontImages = []
    backImages = []

    for game in games:

        if game.text != "Title" and game.text != " " and game.text != "":

            gamePages.append(game.text)

    for gamePage in gamePages:

        driver.find_element_by_link_text(gamePage).click()

        images = driver.find_elements_by_tag_name('img')

        front = images[21].get_attribute("src")
        back = images[22].get_attribute("src")

        if front[-3:] == 'jpg':
            urlretrieve(front, localPath + front[32:])

        driver.back()
    
    driver.quit()


finally:
    driver.quit()
