# -*- coding = utf-8 -*-
# @Time :2021-10-23 22.49
# @Author: LinJH
# @File : izhicheng.py
# @Software: PyCharm

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 无GUI
from selenium.webdriver.common.action_chains import ActionChains
import json
import re
import time
import datetime
import os


# 设置全局变量
stuID = 'stuID'
stuIDs = []
api_key = "API_KEY"
api_url = "https://sctapi.ftqq.com/"  #serverChan 不支持完整的markdown语法且每日请求次数极其有限，请考虑用其他push robot代替，也许这就是高性能的代价（雾
submit_time = 10

# 如果检测到程序在 github actions 内运行，那么读取环境变量中的登录信息
if os.environ.get('GITHUB_RUN_ID', None):
    stuID = os.environ['stuID']
    api_key = os.environ['API_KEY']  # server酱的api，填了可以微信通知打卡结果，不填没影响
    try:
        stuIDs = os.environ.get('stuIDs',stuIDs)
        submit_time = os.environ.get('submit_time', submit_time)
        api_url = os.environ.get('api_url',api_url)
    except:
        print('err: environment config error')
    
    
def message(key, title,content):
    """
    微信通知打卡结果
    """
    long_content = "%s<br>Time: %s<br>SchoolNumber: %s<br>" % (content,datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f UTC'),stuID)
    msg_url = "%s%s.send?text=%s&desp=%s" % (api_url,key,title,long_content)
    requests.get(msg_url)

def tianbiao(stuID):
    
    chrome_options = Options()  # 无界面对象
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('disable-dev-shm-usage')  # 禁用-开发-SHM-使用
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)



    #编程大忌之一：往try 里写业务逻辑:(
    #try
    # 表单地址
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID + '#/form'
    driver.get(url)  # 打开浏览器
    time.sleep(1)

    driver.maximize_window()  # 全屏
    time.sleep(5)

    # 滚动到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 确认
    checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]') #.click()
    ActionChains(driver).move_to_element(checkbox).click().perform()
    time.sleep(1)

    def submit_info():
        error=[]
        # 点击提交
        btn = driver.find_element_by_xpath('//div[@id="SUBMIT"]')
        if btn.text == "提交信息":
            #btn.click()
            ActionChains(driver).move_to_element(btn).click().perform()
            time.sleep(0.5)
            tip = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div/div/div[2]')
            if tip.text  == "提交成功！":
                pass
            else:
                error.append("err: %s" %  tip.text)
            time.sleep(0.5)
            confirm_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div')
            if confirm_btn.text  == "确定":
                ActionChains(driver).move_to_element(confirm_btn).click().perform()
                #confirm_btn.click()
            else:
                error.append( "err:can not find confim button")
        else:
            error.append("err:can not find SUBMIT button")
        if error == []:
            return []
        else:
            return error 

    content = ''
    for i in range(submit_time):
        tmp = ''
        info = submit_info()
        for j in range(len(info)):
            tmp += info[j] + '<br>'
        content += ('第%i次: <br>%s' % (i+1,tmp) )

    
    return content
    
    driver.quit()
    #except:
    #    message(api_key, "打卡失败")


def check_days():
    url='http://dw10.fdzcxy.edu.cn/datawarn/decision/view/report?viewlet=%252Fapp%252Fdkxq.cpt&__pi__=true&op=h5&xh='+ stuID+'&userno='+ stuID+'#/report'
    infoPage_data = requests.get(url)
    pattern = re.compile(r'[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}')
    uuid = re.search(pattern,infoPage_data.text).group()
    if len(uuid) != 36:
        print("error")
        return "error : can not get uuid to check sign data"
        #print(len(uuid))
    print(uuid)
    json_url = 'http://dw10.fdzcxy.edu.cn/datawarn/decision/view/report?toVanCharts=true&dynamicHyperlink=true&op=page_content&cmd=json&sessionID='+ uuid + '&fine_api_v_json=3&pn=1&__fr_locale__=zh_CN'
    json_data = requests.get(json_url).text
    try:
        data = json.loads(json_data)['pageContent']["detail"][0]["cellData"]["rows"]
    except:
        return 'err: can not decode json data'
    print(data[2]["cells"][6]["text"])
    days = int(data[2]["cells"][6]["text"])
    print(days)
    return days

def sign_and_check(stuID):
    days_before = check_days()
    #days_before = 48
    content = tianbiao(stuID)
    days_after = check_days()
    if days_after != days_before+1:
        title = "疑似打卡失败"
    else:
        title = "打卡成功"
    message(api_key, title , content )
    print(stuID + title)

if __name__ == '__main__':

    if stuIDs != []:
        for i in range(len(stuIDs)):
            stuID = stuIDs[i]
            sign_and_check(stuID)
            del(stuID)
    else:
        sign_and_check(stuID) 
        
