# -*- coding = utf-8 -*-
# @Time :2021-02-13 16:09
# @Author: LinJH
# @File : izhicheng_windows.py
# @Software: PyCharm

from selenium import webdriver
import time

stuID = '21xxxxxxx'
province = '福建省'
city = '福州市'
region = '鼓楼区'


def tianbiao(stuID, province, city, region):
    driver = webdriver.Chrome()
    # 表单地址
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/yibao.frm&op=h5&xh=' + stuID + '#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(2)

    driver.maximize_window()  # 全屏
    time.sleep(5)
    # 选择地区

    # 选择省
    driver.implicitly_wait(10)
    flag1 = False
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    driver.implicitly_wait(10)
    a1 = driver.find_elements_by_xpath(
        '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input')
    while not flag1:
        if len(a1) != 0:
            # 点击搜索
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag1 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/span').click()
            time.sleep(2)
            driver.implicitly_wait(30)
            a1 = driver.find_elements_by_xpath(
                '/html/body/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div')

    # 输入省
    a1 = driver.find_elements_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
    flag1 = False
    while not flag1:
        if len(a1) != 0:
            s1 = driver.find_element_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
            s1.send_keys(province)
            time.sleep(2)
            driver.implicitly_wait(10)
            flag1 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a1 = driver.find_elements_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")

    # 选择
    time.sleep(2)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div.css-901oao.css-cens5h").click()
    time.sleep(2)
    driver.implicitly_wait(10)

    # 选择市
    flag2 = False
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]').click()
    time.sleep(2)
    driver.implicitly_wait(10)
    a2 = driver.find_elements_by_xpath(
        '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input')
    while not flag2:
        if len(a2) != 0:
            # 点击搜索
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag2 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a2 = driver.find_elements_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input')
    # 输入市
    a2 = driver.find_elements_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
    flag2 = False
    while not flag2:
        if len(a2) != 0:
            s2 = driver.find_element_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
            s2.send_keys(city)
            time.sleep(2)
            driver.implicitly_wait(10)
            flag2 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a2 = driver.find_elements_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")

    # 选择
    time.sleep(2)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div.css-901oao.css-cens5h").click()
    time.sleep(2)
    driver.implicitly_wait(10)

    # 选择区
    flag3 = False
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[3]/div[2]').click()
    time.sleep(2)
    driver.implicitly_wait(10)
    a3 = driver.find_elements_by_xpath(
        '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input')
    while not flag3:
        if len(a3) != 0:
            # 点击搜索
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            flag3 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[3]/div[2]').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a3 = driver.find_elements_by_xpath(
                '/html/body/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/input')
    # 输入区
    a3 = driver.find_elements_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
    flag3 = False
    while not flag3:
        if len(a3) != 0:
            s3 = driver.find_element_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")
            s3.send_keys(region)
            time.sleep(2)
            driver.implicitly_wait(10)
            flag3 = True
        else:
            driver.find_element_by_xpath(
                '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[4]/div[2]/div/div[3]/div[2]/div[1]').click()
            time.sleep(2)
            driver.implicitly_wait(10)
            a3 = driver.find_elements_by_css_selector(
                "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > input")

    # 选择
    time.sleep(2)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector(
        "#app > div > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div.css-901oao.css-cens5h").click()
    time.sleep(2)
    driver.implicitly_wait(30)

    # 滚动到底部
    target = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[26]/div[2]")
    driver.execute_script("arguments[0].scrollIntoView();", target)

    # 确认
    driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[25]/div[2]/div[2]/input').click()
    time.sleep(1)

    # 点击提交
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div[26]/div[2]').click()
    time.sleep(1)

    driver.quit()


if __name__ == '__main__':
    tianbiao(stuID, province, city, region)
    print(stuID, "填报成功！")
