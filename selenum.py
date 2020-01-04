from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

driver = webdriver.Chrome('./chromedriver.exe')

def leastword(list1, food1):
    list2 = []
    for ele in list1:
        tex_lis = ele.text.split()
        try:
            if len(str(food1)) == len(tex_lis[0]):
                return list1.index(ele)
        except IndexError:
            continue
    for ele in list1:
        tex_lis = ele.text.split()
        try:
            if tex_lis[0] != None:
                return list1.index(ele)
        except IndexError:
            continue

def order(menu_list, adrs1, adrs2, store, num_list):

    waiting = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        ElementNotInteractableException, NoSuchElementException])

    # menuList = menu.split()
    #c = '고려대학교안암캠퍼스'
    #d = '맥도날드'
    #e = '상세주소'
    # lis = []
    # for realmenu in menuList:
    #     lis.append(realmenu)
    lis = menu_list

    driver.get('https://www.yogiyo.co.kr/')

    # driver.find_element_by_tag_name("body").send_keys("Keys.ESCAPE")

    waiting.until(EC.invisibility_of_element_located(
        (By.XPATH, "//*[@id=\"spinner\"]")))

    # driver.("window.stop();")

    element0 = waiting.until(
        EC.visibility_of_element_located((By.NAME, "address_input")))
    #element0 = waiting.until(EC.text_to_be_present_in_element((By.NAME, "address_input"), "*"))

    element0.clear()
    element0.send_keys(adrs1)

    driver.find_element_by_xpath(
        "//*[@id=\"button_search_address\"]/button[2]").click()
    try:
        driver.find_element_by_xpath(
            "//*[@id=\"search\"]/div/form/ul/li[3]/a").click()
        if(store):
            waiting.until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@id=\"spinner\"]")))

            element11 = waiting.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id=\"category\"]/ul/li[1]/a")))
            element11.click()
            driver.find_element_by_xpath(
                "//*[@id=\"category\"]/ul/li[15]/form/div/input").send_keys(store)

            time.sleep(1)

            driver.find_element_by_xpath(
                "//*[@id=\"category_search_button\"]").click()

        else:
            waiting.until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@id=\"spinner\"]")))

            element11 = waiting.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id=\"category\"]/ul/li[1]/a")))
            element11.click()
            driver.find_element_by_xpath(
                "//*[@id=\"category\"]/ul/li[15]/form/div/input").send_keys(lis[0])
            driver.find_element_by_xpath(
                "//*[@id=\"category_search_button\"]").click()
            # waiting.until(EC.invisibility_of_element_located(
            #     (By.XPATH, "//*[@id=\"spinner\"]")))

            # element1 = waiting.until(EC.element_to_be_clickable(
            # (By.XPATH, "//li[contains(string(), \"%s\")]" % b)))
            # waiting.until(EC.invisibility_of_element_located(
            # (By.XPATH, "//*[@id=\"spinner\"]")))
            # element1.click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        element2 = waiting.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id=\"content\"]/div/div[4]/div[2]/div")))
        element2.click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))
        size = len(driver.find_elements_by_xpath("//*[@id=\"menu\"]/div/div"))

        for i in range(3, size - 1):
            driver.find_element_by_xpath("//*[@id=\"menu\"]/div/div[%i]" %
                                         i).click()

        k = 0

        for food in lis:
            contain_list = driver.find_elements_by_xpath(
                "//li[contains(string(), \'%s\')]" % food)
            size2 = len(contain_list)

            ind = leastword(contain_list, food)

            driver.find_elements_by_xpath(
                "//li[contains(string(), \'%s\')]" % food)[int(ind)].click()
            for j in range(num_list[k]-1):
                try:
                    driver.find_element_by_xpath(
                    "/html/body/div[10]/div/div[2]/div[5]/div/a[2]").click()
                except NoSuchElementException:
                    driver.find_element_by_xpath(
                    "/html/body/div[10]/div/div[2]/div[4]/div/a[2]").click()

            # for i in range(0, size2):
            #     try:
            #         driver.find_elements_by_xpath(
            #             "//li[contains(string(), \'%s\')]" % food)[i].click()
            #         for j in range(num_list[k]-1):
            #             driver.find_element_by_xpath(
            #                 "/html/body/div[10]/div/div[2]/div[5]/div/a[2]").click()
            #         break
            #     except ElementNotInteractableException:
            #         continue

            k += 1

            driver.find_element_by_class_name('btn-add-cart').click()

        driver.find_element_by_xpath("//a[@ng-click=\"checkout()\"]").click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/form[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/input").send_keys(adrs2)
    except NoSuchElementException:
        if(store):
            waiting.until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@id=\"spinner\"]")))

            element11 = waiting.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id=\"category\"]/ul/li[1]/a")))
            element11.click()
            driver.find_element_by_xpath(
                "//*[@id=\"category\"]/ul/li[15]/form/div/input").send_keys(store)

            time.sleep(1)

            driver.find_element_by_xpath(
                "//*[@id=\"category_search_button\"]").click()

        else:
            waiting.until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@id=\"spinner\"]")))

            element11 = waiting.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id=\"category\"]/ul/li[1]/a")))
            element11.click()
            driver.find_element_by_xpath(
                "//*[@id=\"category\"]/ul/li[15]/form/div/input").send_keys(lis[0])
            driver.find_element_by_xpath(
                "//*[@id=\"category_search_button\"]").click()
            # waiting.until(EC.invisibility_of_element_located(
            #     (By.XPATH, "//*[@id=\"spinner\"]")))

            # element1 = waiting.until(EC.element_to_be_clickable(
            # (By.XPATH, "//li[contains(string(), \"%s\")]" % b)))
            # waiting.until(EC.invisibility_of_element_located(
            # (By.XPATH, "//*[@id=\"spinner\"]")))
            # element1.click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        element2 = waiting.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id=\"content\"]/div/div[4]/div[2]/div")))
        element2.click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))
        size = len(driver.find_elements_by_xpath("//*[@id=\"menu\"]/div/div"))

        for i in range(3, size - 1):
            driver.find_element_by_xpath("//*[@id=\"menu\"]/div/div[%i]" %
                                         i).click()

        k = 0

        for food in lis:
            contain_list = driver.find_elements_by_xpath(
                "//li[contains(string(), \'%s\')]" % food)
            size2 = len(contain_list)

            ind = leastword(contain_list, food)

            driver.find_elements_by_xpath(
                "//li[contains(string(), \'%s\')]" % food)[int(ind)].click()
            for j in range(num_list[k]-1):
                try:
                    driver.find_element_by_xpath(
                    "/html/body/div[10]/div/div[2]/div[5]/div/a[2]").click()
                except NoSuchElementException:
                    driver.find_element_by_xpath(
                    "/html/body/div[10]/div/div[2]/div[4]/div/a[2]").click()

            # for i in range(0, size2):
            #     try:
            #         driver.find_elements_by_xpath(
            #             "//li[contains(string(), \'%s\')]" % food)[i].click()
            #         for j in range(num_list[k]-1):
            #             driver.find_element_by_xpath(
            #                 "/html/body/div[10]/div/div[2]/div[5]/div/a[2]").click()
            #         break
            #     except ElementNotInteractableException:
            #         continue

            k += 1

            driver.find_element_by_class_name('btn-add-cart').click()

        driver.find_element_by_xpath("//a[@ng-click=\"checkout()\"]").click()

        waiting.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[@id=\"spinner\"]")))

        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/form[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/input").send_keys(adrs2)

store = "페리카나"
menu = ["후라이드", "양념치킨"]
num_list = [1, 3]
adrs1 = "고려대학교안암캠퍼스"
adrs2 = "홍보관"
order(menu, adrs1, adrs2, store, num_list)
