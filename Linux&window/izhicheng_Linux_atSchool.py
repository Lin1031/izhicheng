# -*- coding = utf-8 -*-
# @Time :2021-03-02 19:09
# @Author: LinJH
# @File : izhicheng_Linux_atSchool.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
from selenium.webdriver.common.by import By
import time
import sys


def tianbiao(stuID):
    chrome_options = Options()  # 无界面对象
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')  # 禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')

    # 表单地址
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID + '#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(2)

    driver.maximize_window()  # 全屏
    time.sleep(5)
    

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
            tianbiao(sys.argv[1])
            break
        except:
            has_try += 1
            time.sleep(10)
            print("重试次数" + str(has_try))

    print(sys.argv[1], "填报成功！")
