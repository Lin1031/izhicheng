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
            tianbiao(stuID)
            break
        except:
            has_try += 1
            time.sleep(10)
            print("重试次数" + str(has_try))

    print(stuID, "填报成功！")
