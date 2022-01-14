# -*- coding = utf-8 -*-
# @Time :2021-10-23 22.49
# @Author: LinJH
# @File : izhicheng.py
# @Software: PyCharm

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
# from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import json
import re
import datetime
from selenium.webdriver.common.action_chains import ActionChains

# 设置全局变量
stuIDs = []
stuIDsHome = []
api_key = "API_KEY"
api_url = "https://sctapi.ftqq.com/"  # serverChan 不支持完整的markdown语法且每日请求次数极其有限，请考虑用其他push robot代替，也许这就是高性能的代价（雾
submit_time = 3
check = 'NO'
atHome = 'NO'

# 如果检测到程序在 github actions 内运行，那么读取环境变量中的登录信息
if os.environ.get('GITHUB_RUN_ID', None):
    api_key = os.environ['API_KEY']  # server酱的api，填了可以微信通知打卡结果，不填没影响
    check = os.environ['check']
    atHome = os.environ['atHome']
    try:
        if not stuIDs:
            tmp_stuIDs = os.environ.get('stuIDs', '').split('\n')
            if "".join(tmp_stuIDs) == '':
                stuIDs = []
            else:
                stuIDs = tmp_stuIDs
            del tmp_stuIDs
        if not stuIDsHome:
            tmp_stuIDsHome = os.environ.get('stuIDsHome', '').split('\n')
            if "".join(tmp_stuIDsHome) == '':
                stuIDsHome = []
            else:
                stuIDsHome = tmp_stuIDsHome
            del tmp_stuIDsHome
        submit_time = os.environ.get('submit_time', submit_time)
        api_url = os.environ.get('api_url', api_url)
    except Exception as err:
        print('err: environment config error.Info: ', err.args)


def message(key, title, content):
    """
    微信通知打卡结果
    """
    long_content = "%s<br>Time: %s<br>SchoolNumber: %s<br>" % (
        content, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f UTC'), stuID)
    msg_url = "%s%s.send?text=%s&desp=%s" % (api_url, key, title, long_content)
    requests.get(msg_url)


class AtSchool():
    def __init__(self):
        self.stuID = stuID

    def tianbiao(stuID):
        driver = webdriver.Chrome()

        # 表单地址
        url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + str(
            stuID) + '#/form'
        driver.get(url)  # 打开浏览器
        time.sleep(1)

        driver.maximize_window()  # 全屏
        time.sleep(5)

        # 滚动到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 确认
        checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')  # .click()
        ActionChains(driver).move_to_element(checkbox).click().perform()
        time.sleep(2)

        def submit_info():
            error = []
            # 点击提交
            btn = driver.find_element_by_xpath('//div[@id="SUBMIT"]')
            if btn.text == "提交信息":
                # 执行成功，成功悬停在页面元素
                ActionChains(driver).move_to_element(btn).click().perform()
                time.sleep(2)
                # 获取提交信息
                tip = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/div/div[2]')
                if tip.text == "提交成功！":
                    pass
                else:
                    error.append("err: %s" % tip.text)
                time.sleep(2)
                # 确定
                confirm_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div')
                if confirm_btn.text == "确定":
                    ActionChains(driver).move_to_element(confirm_btn).click().perform()
                    # confirm_btn.click()
                else:
                    error.append("err:can not find confim button")
            else:
                error.append("err:can not find SUBMIT button")
            if error == []:
                return []
            else:
                return error

        # 提交重试
        content = ''
        for i in range(submit_time):
            tmp = ''
            info = submit_info()
            for j in range(len(info)):
                tmp += info[j] + '<br>'
            content += ('第%i次: <br>%s' % (i + 1, tmp))

        return content

    def sign_and_check(stuID):
        days_before = check_days()
        # days_before = 48
        content = AtSchool.tianbiao(stuID)
        days_after = check_days()
        # 打卡前日期与打开后日期对比
        if days_after != days_before + 1:
            title = stuID[-3:] + "学号不存在"
        elif days_after != days_before + 1:
            title = stuID[-3:] + "疑似打卡失败"
        else:
            title = stuID[-3:] + "打卡成功"
        message(api_key, title, content)
        print(title)


class AtHome():
    def __init__(self):
        self.stuID = stuID
        self.province = province
        self.city = city
        self.region = region

    def tianbiao(stuID, province, city, region):
        driver = webdriver.Chrome()

        # 表单地址
        url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + str(
            stuID) + '#/form'
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
        checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')  # .click()
        ActionChains(driver).move_to_element(checkbox).click().perform()
        time.sleep(2)

        def submit_info():
            error = []
            # 点击提交
            btn = driver.find_element_by_xpath('//div[@id="SUBMIT"]')
            if btn.text == "提交信息":
                # 执行成功，成功悬停在页面元素
                ActionChains(driver).move_to_element(btn).click().perform()
                time.sleep(2)
                # 获取提交信息
                tip = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/div/div[2]')
                if tip.text == "提交成功！":
                    pass
                else:
                    error.append("err: %s" % tip.text)
                time.sleep(2)
                # 确定
                confirm_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div')
                if confirm_btn.text == "确定":
                    ActionChains(driver).move_to_element(confirm_btn).click().perform()
                    # confirm_btn.click()
                else:
                    error.append("err:can not find confim button")
            else:
                error.append("err:can not find SUBMIT button")
            if error == []:
                return []
            else:
                return error

        # 提交重试
        content = ''
        for i in range(submit_time):
            tmp = ''
            info = submit_info()
            for j in range(len(info)):
                tmp += info[j] + '<br>'
            content += ('第%i次: <br>%s' % (i + 1, tmp))

        return content

    def sign_and_check(stuID, province, city, region):
        days_before = check_days()
        # days_before = 48
        content = AtHome.tianbiao(stuID, province, city, region)
        days_after = check_days()
        # 打卡前日期与打开后日期对比
        if days_before == -1:
            title = stuID[-3:] + "学号不存在"
        elif days_after != days_before + 1:
            title = stuID[-3:] + "疑似打卡失败"
        else:
            title = stuID[-3:] + "打卡成功"
        message(api_key, title, content)
        print(title)


def check_days():
    # 初始化日期，用于后续检测学号是否存在
    days = -1
    # 检测是否打卡成功链接
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/decision/view/report?viewlet=%252Fapp%252Fdkxq.cpt&__pi__=true&op=h5&xh=' + stuID + '&userno=' + stuID + '#/report'
    infoPage_data = requests.get(url)
    # 正则表达式获取uuid
    pattern = re.compile(r'[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}')
    uuid = re.search(pattern, infoPage_data.text).group()
    if len(uuid) != 36:
        print("error")
        return "error : can not get uuid to check sign data"
        # print(len(uuid))
    print(uuid)
    # 获取确认数据 json
    json_url = 'http://dw10.fdzcxy.edu.cn/datawarn/decision/view/report?toVanCharts=true&dynamicHyperlink=true&op=page_content&cmd=json&sessionID=' + uuid + '&fine_api_v_json=3&pn=1&__fr_locale__=zh_CN'
    json_data = requests.get(json_url).text
    try:
        data = json.loads(json_data)['pageContent']["detail"][0]["cellData"]["rows"]
    except:
        return 'err: can not decode json data'
    try:
        days = int(data[2]["cells"][6]["text"])
    except:
        return days
    return days


if __name__ == '__main__':
    if atHome == 'YES':
        if check == 'YES':
            print('共有 ' + str(len(stuIDsHome)) + ' 人等待打卡')
            for i in range(len(stuIDsHome)):
                list_temp = stuIDsHome[i].split(' ')
                stuID = list_temp[0]
                province = list_temp[1]
                city = list_temp[2]
                region = list_temp[3]
                AtHome.sign_and_check(stuID, province, city, region)
                del (stuID)
        else:
            print('共有 ' + str(len(stuIDsHome)) + ' 人等待打卡')
            for i in range(len(stuIDsHome)):
                list_temp = stuIDsHome[i].split(' ')
                stuID = list_temp[0]
                province = list_temp[1]
                city = list_temp[2]
                region = list_temp[3]
                AtHome.tianbiao(stuID, province, city, region)
                print(stuID[-3:] + ' 打卡完成')
                del (stuID)
    else:
        if check == 'YES':
            print('共有 ' + str(len(stuIDs)) + ' 人等待打卡')
            for i in range(len(stuIDs)):
                stuID = stuIDs[i]
                AtSchool.sign_and_check(stuID)
                del (stuID)
        else:
            print('共有 ' + str(len(stuIDs)) + ' 人等待打卡')
            for i in range(len(stuIDs)):
                stuID = stuIDs[i]
                AtSchool.tianbiao(stuID)
                print(stuID[-3:] + ' 打卡完成')
                del (stuID)
    print("打卡任务全部完成！")
