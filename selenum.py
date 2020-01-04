from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time


def order(menu):

    driver = webdriver.Chrome('./chromedriver')
    waiting = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        ElementNotInteractableException, NoSuchElementException])

    menuList = menu.split()
    c = '고려대학교안암캠퍼스'
    b = '중국집'
    lis = []
    for realmenu in menuList:
        lis.append(realmenu)
    for food in lis:
        print(food)

    driver.get('https://www.yogiyo.co.kr/')

    # driver.find_element_by_tag_name("body").send_keys("Keys.ESCAPE")

    waiting.until(EC.invisibility_of_element_located(
        (By.XPATH, "//*[@id=\"spinner\"]")))

    # driver.("window.stop();")

    element0 = waiting.until(
        EC.visibility_of_element_located((By.NAME, "address_input")))
    #element0 = waiting.until(EC.text_to_be_present_in_element((By.NAME, "address_input"), "*"))

    element0.clear()
    element0.send_keys(c)

    driver.find_element_by_xpath(
        "//*[@id=\"button_search_address\"]/button[2]").click()
    try:
        driver.find_element_by_xpath(
            "//*[@id=\"search\"]/div/form/ul/li[3]/a").click()
        driver.find_element_by_xpath("//li[contains(string(), \"%s\")]" %
                                     b).click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/div[4]/div[2]/div").click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        size = len(driver.find_elements_by_xpath("//*[@id=\"menu\"]/div/div"))

        for i in range(3, size - 1):
            driver.find_element_by_xpath("//*[@id=\"menu\"]/div/div[%i]" %
                                         i).click()

        for food in lis:
            size2 = len(
                driver.find_elements_by_xpath(
                    "//li[contains(string(), \"%s\")]" % food))

            for i in range(0, size2):
                try:
                    driver.find_elements_by_xpath(
                        "//li[contains(string(), \"%s\")]" % food)[i].click()
                    break
                except ElementNotInteractableException:
                    continue

            driver.find_element_by_class_name('btn-add-cart').click()

        driver.find_element_by_xpath("//a[@ng-click=\"checkout()\"]").click()
    except NoSuchElementException:
        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        # time.sleep(1)

        element1 = waiting.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(string(), \"%s\")]" % b)))

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))
        element1.click()

        element2 = waiting.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id=\"content\"]/div/div[4]/div[2]/div")))
        element2.click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))
        size = len(driver.find_elements_by_xpath("//*[@id=\"menu\"]/div/div"))

        for i in range(3, size - 1):
            driver.find_element_by_xpath("//*[@id=\"menu\"]/div/div[%i]" %
                                         i).click()

        for food in lis:
            size2 = len(
                driver.find_elements_by_xpath(
                    "//li[contains(string(), \"%s\")]" % food))

            for i in range(0, size2):
                try:
                    driver.find_elements_by_xpath(
                        "//li[contains(string(), \"%s\")]" % food)[i].click()
                    break
                except ElementNotInteractableException:
                    continue

            driver.find_element_by_class_name('btn-add-cart').click()

        driver.find_element_by_xpath("//a[@ng-click=\"checkout()\"]").click()


#menu = "짜장면 탕수육 짬뽕"
# order(menu)
