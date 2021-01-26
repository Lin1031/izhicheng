# -*- coding = utf-8 -*-
# @Time :2020-12-24 13:32
# @Author: LinJH
# @File : izhicheng.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options#无GUI
from selenium.webdriver.common.by import By
import time
import sys

def tianbiao(stuID,province,city,region):
    chrome_options = Options()#无界面对象
    chrome_options.add_argument('--headless')  #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')#禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox') #解决DevToolsActivePort文件不存在的报错
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')

    # 表单地址
    url = 'http://datawarn9.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sanbao.frm&op=h5&userno=' + stuID+'#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(2)

    driver.maximize_window()  # 全屏
    #选择地区
    # 选择省
    flag1=False
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/span').click()
    time.sleep(2)
    driver.implicitly_wait(30)
    a1=driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')
    while not flag1:
        if len(a1)!=0:
            # 点击搜索
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag1=True
        else:
            driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/span').click()
            time.sleep(2)
            driver.implicitly_wait(30)
            a1 = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')

    # 输入省
    a1 = driver.find_elements_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
    flag1 = False
    while not flag1:
        if len(a1)!=0:
            s1 = driver.find_element_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
            s1.send_keys(province)
            time.sleep(2)
            driver.implicitly_wait(30)
            flag1=True
        else:
            driver.find_element_by_xpath(  '/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(30)
            a1 = driver.find_elements_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")

    # 选择
    driver.find_element_by_css_selector( "#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div.react-view.no-scrollbar > div.react-view > div > div").click()
    time.sleep(2)
    driver.implicitly_wait(30)

    # 选择市
    flag2 = False
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div/input').click()
    time.sleep(2)
    driver.implicitly_wait(10)
    a2=driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')
    while not flag2:
        if len(a2)!=0:
            # 点击搜索
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag2=True
        else:
            driver.find_element_by_xpath( '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a2 = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')
    # 输入省
    a2 = driver.find_elements_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
    flag2 = False
    while not flag2:
        if len(a2)!=0:
            s2 = driver.find_element_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
            s2.send_keys(city)
            time.sleep(2)
            driver.implicitly_wait(10)
            flag2=True
        else:
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a2 = driver.find_elements_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")

    # 选择
    driver.find_element_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div.react-view.no-scrollbar > div.react-view > div > div").click()
    time.sleep(2)
    driver.implicitly_wait(10)

    #选择区
    flag3=False
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[3]/div[1]/div/div/input').click()
    time.sleep(2)
    driver.implicitly_wait(10)
    a3= driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')
    while not flag3:
        if len(a3)!=0:
            #点击搜索
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag3=True
        else:
            driver.find_element_by_xpath( '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[3]/div[1]/div/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a3 = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')
    #输入区
    a3=driver.find_elements_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
    flag3 = False
    while not flag3:
        if len(a3)!=0:
            s3 = driver.find_element_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")
            s3.send_keys(region)
            time.sleep(2)
            driver.implicitly_wait(10)
            flag3=True
        else:
            driver.find_element_by_xpath( '/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a3 = driver.find_elements_by_css_selector( "#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div > input[type=search]")

    #选择
    driver.find_element_by_css_selector("#app > div > div > div.react-view > div > div.react-view > div.react-view > div.react-view > div > div > div > div:nth-child(2) > div > div.react-view.no-scrollbar > div.react-view > div > div").click()
    time.sleep(2)
    driver.implicitly_wait(30)
    
    #滚动
    #target = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[9]/div[1]/div/input")
    #driver.execute_script("arguments[0].scrollIntoView();", target)

    #昨日午检
    #driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[9]/div[1]/div/input').send_keys('36.6')
    #time.sleep(1)

    #昨日晚检
    #driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[11]/div[1]/div/input').send_keys('36.6')
    #time.sleep(1)

    #今日晨检
    #driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[13]/div[1]/div/input').send_keys('36.6')
    #time.sleep(1)

    #今日健康状况
    #driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[15]/div[1]/div/div/div/div/div").click()
    #time.sleep(1)

    # 滚动到底部
    target = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[26]/div[1]/div/div/div[2]/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", target)

    #近14日情况
    #driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[20]/div[1]/div/div/div/div/div").click()
    #time.sleep(1)

    #今日状况
    #driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[23]/div[1]/div/div/div/div/div/div[1]/div/div/span[1]").click()
    #time.sleep(1)

    #确认
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[25]/div[1]/div/span[2]/small').click()
    time.sleep(1)

    # 点击提交
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[26]/div[1]/div/div/div[2]/div[2]').click()
    time.sleep(1)

    driver.quit()


if __name__ == '__main__':
    tianbiao(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    
