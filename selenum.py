from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

driver = webdriver.Chrome('./chromedriver_MAC')


def order(menu):
    menuList = menu.split()
    c = '고려대학교안암캠퍼스'
    b = '중국집'
    a = menuList[0]
    # d = menuList[1]
    # e = menuList[2]
    lis = []
    lis.append(a)
    # lis.append(d)
    # lis.append(e)
    for food in lis:
        print(food)

    driver.implicitly_wait(3)
    driver.get('https://www.yogiyo.co.kr/mobile/#/327421/')

    time.sleep(3)

    driver.find_element_by_name('address_input').clear()
    driver.find_element_by_name('address_input').send_keys(c)

    driver.find_element_by_xpath(
        "//*[@id=\"button_search_address\"]/button[2]").click()
    try:
        driver.find_element_by_xpath(
            "//*[@id=\"search\"]/div/form/ul/li[3]/a").click()
        driver.find_element_by_xpath("//li[contains(string(), \"%s\")]" %
                                     b).click()

        time.sleep(3)

        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/div[4]/div[2]/div").click()

        time.sleep(3)

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
        driver.find_element_by_xpath("//li[contains(string(), \"%s\")]" %
                                     b).click()

        time.sleep(3)

        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/div[4]/div[2]/div").click()

        time.sleep(3)

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
