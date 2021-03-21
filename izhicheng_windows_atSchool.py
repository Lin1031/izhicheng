# -*- coding = utf-8 -*-
# @Time :2021-03-02 19:11
# @Author: LinJH
# @File : izhicheng_windows_atSchool.py
# @Software: PyCharm


from selenium import webdriver
import time

stuID = '21xxxxxxx'


def tianbiao(stuID):
    driver = webdriver.Chrome()
    # 表单地址
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/yibao.frm&op=h5&xh=' + stuID + '#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(2)

    driver.maximize_window()  # 全屏
    time.sleep(5)

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
    tianbiao(stuID)
    print(stuID, "填报成功！")
