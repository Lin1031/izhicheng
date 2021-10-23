# -*- coding = utf-8 -*-
# @Time :2021-10-23 22.49
# @Author: LinJH
# @File : izhicheng.py
# @Software: PyCharm

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
import time
import os

# 设置全局变量
STUID = 'STUID'
api_key = "API_KEY"

# 如果检测到程序在 github actions 内运行，那么读取环境变量中的登录信息
if os.environ.get('GITHUB_RUN_ID', None):
    api_key = os.environ['API_KEY']  # server酱的api，填了可以微信通知打卡结果，不填没影响


def message(key, title):
    """
    微信通知打卡结果
    """
    # 错误的key也可以发送消息，无需处理 :)
    msg_url = "https://sc.ftqq.com/{}.send?text={}".format(key, title)
    requests.get(msg_url)


def tianbiao(STUID):
    chrome_options = Options()  # 无界面对象
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')  # 禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

    try:
        # 表单地址
        url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + STUID + '#/form'
        driver.get(url)  # 打开浏览器
        time.sleep(1)

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
    except:
        message(api_key, "打卡失败")


if __name__ == '__main__':
    tianbiao(STUID)
    print(STUID + "打卡成功")
