#export PATH=$PATH:/home/leo/Downloads/geckodriver-v0.24.0-linux32


# from selenium import webdriver
# from xvfbwrapper import Xvfb
#
# display = Xvfb()
# display.start()
#
# # now Firefox will run in a virtual display.
# # you will not see the browser.
# driver = webdriver.Firefox()
# driver.get('http://www.google.com')
#
# print(driver.title)
# driver.quit()
#
# display.stop()

#https://www.facebook.com/groups/1621345418078039/
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.keys import Keys
import pickle
import traceback
import time
from selenium.webdriver.common.action_chains import ActionChains

# assert "No results found." not in driver.page_source
# driver.close()
# binary = FirefoxBinary('/home/leo/Downloads/geckodriver-v0.24.0-linux32/geckodriver')
#
# driver = webdriver.Firefox()
# # driver.maximize_window()
# driver.implicitly_wait(10)

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

from selenium import webdriver
from xvfbwrapper import Xvfb
def auth_fb():


    display = Xvfb()
    display.start()

    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(firefox_profile=_browser_profile)
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    time.sleep(3)

    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys("fdd")
    elem1 = driver.find_element_by_name("pass")
    elem1.clear()
    elem1.send_keys("ds")
    elem1.send_keys(Keys.RETURN)
    time.sleep(3)

    driver.get("https://www.facebook.com/groups/1621345418078039/")
    time.sleep(10)

    elem2 = driver.find_element_by_xpath('//li[@class="_1tm3"]')
    elem2.click()

    elem3 = driver.find_element_by_xpath('//div[@class=" _4h97 _30z _4h96"]')
    elem3.click()
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys('Test data')
    actions.perform()

    time.sleep(2)
    elem4 = driver.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]')
    elem4.click()
    display.stop()
#
# def open_group(url):
#     try:
#         load_cookie(driver, 'fb.ck')
#     except:
#         traceback.print_exc()
#     driver.get(url)
auth_fb()
# driver.execute_script("window.history.go(-1)")
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# open_group('https://www.facebook.com/groups/1621345418078039/')
