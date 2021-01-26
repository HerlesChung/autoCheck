# coding=utf-8

# https://stuhealth.jnu.edu.cn/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    print("Loading autoChecking program")
    while 1:
        # 获取现在时间
        now_time = datetime.datetime.now()
        # 获取明天日期
        next_time = now_time + datetime.timedelta(days=+1)
        next_year = next_time.date().year
        next_month = next_time.date().month
        next_day = next_time.date().day
        # 获取明天6点时间
        next_time = datetime.datetime.strptime(
            str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 06:00:00", "%Y-%m-%d %H:%M:%S")
        # 获得sleep时间
        sleep_time = (next_time - now_time).total_seconds()
        print("Start Sleeping")
        time.sleep(sleep_time)

        # getBrowser
        browser = webdriver.Chrome(chrome_options=chrome_options)
        print("getChrome")
        browser.get("https://stuhealth.jnu.edu.cn/")
        print("get2TheWeb")
        log_name = browser.find_element_by_id("zh")
        log_name.send_keys("")
        pwd = browser.find_element_by_id("passw")
        pwd.send_keys("")
        submit = browser.find_element_by_tag_name("button")
        submit.click()
        # You should stay enough time in case of the network flucuation.
        time.sleep(50)
        print("setAccount")
        browser.switch_to.window(browser.window_handles[-1])
        # phone = browser.find_element_by_id("phone")
        # phone.clear()
        # phone.send_keys(664996211)
        chBox = browser.find_element_by_id(10000)
        chBox.click()
        sbmButton = browser.find_element_by_id("tj")
        sbmButton.click()
        print("ok")
        browser.quit()
