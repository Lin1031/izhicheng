# -*- coding = utf-8 -*-
# @Time :2021-02-13 16:09
# @Author: LinJH
# @File : izhicheng_Linux.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
from selenium.webdriver.common.by import By
import time
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def tianbiao(stuID, province, city, region):
    chrome_options = Options()#无界面对象
    chrome_options.add_argument('--headless')  #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')#禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox') #解决DevToolsActivePort文件不存在的报错
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    
    # 表单地址
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID + '#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(1)

    driver.maximize_window()  # 全屏
    time.sleep(5)

    # 输入省
    driver.find_element_by_xpath('//div[@id="SHENG"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-1pi2tsx"]//input').send_keys(province)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n"]/div[@class="css-901oao css-cens5h"]/span').click()
    time.sleep(2)

    # 输入市
    driver.find_element_by_xpath('//div[@id="SHI"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-1pi2tsx"]//input').send_keys(city)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n"]/div[@class="css-901oao css-cens5h"]/span').click()
    time.sleep(1)

    # 输入区
    driver.find_element_by_xpath('//div[@id="QU"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-1pi2tsx"]//input').send_keys(region)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="css-1dbjc4n"]/div[@class="css-901oao css-cens5h"]/span').click()
    time.sleep(1)

    # 滚动到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 确认
    driver.find_element_by_xpath('//input[@type="checkbox"]').click()
    time.sleep(1)

    # 点击提交
    driver.find_element_by_xpath('//div[@id="SUBMIT"]').click()
    time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    has_try = 0
    MAX_TRY = 20
    while has_try < MAX_TRY:
        try:
            tianbiao(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
            break
        except:
            has_try += 1
            time.sleep(10)
            print("重试次数" + str(has_try))

    print(sys.argv[1], "填报成功！")

