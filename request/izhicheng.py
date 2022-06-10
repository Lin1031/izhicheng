import datetime
import json
import os
import re
import time
from urllib.parse import quote

import requests

# 全局变量
students = []
api_key = "API_KEY"
api_url = "https://sctapi.ftqq.com/"
MAX_TRY = 20  # 最大重试次数


# 如果检测到程序在 github actions 内运行，那么读取环境变量中的登录信息
if os.environ.get('GITHUB_RUN_ID', None):
    api_key = os.environ['API_KEY']  # server酱的api，填了可以微信通知打卡结果，不填没影响
    try:
        if not students:
            tmp_students = os.environ.get('students', '').split('\n')
            if "".join(tmp_students) == '':
                students = []
            else:
                students = tmp_students
            del tmp_students
        api_url = os.environ.get('api_url', api_url)
    except:
        print('err: environment config error')


def message(key, title, content):
    """
    微信通知打卡结果
    """
    long_content = "%s<br>Time: %s<br>SchoolNumber: %s<br>" % (
        content, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f UTC'), stuID)
    msg_url = "%s%s.send?text=%s&desp=%s" % (api_url, key, title, long_content)
    requests.get(msg_url)


# 构建表单
def processing_data(stuID, name, jsConfId, callbackConfId, province, city, region):
    parameters = {"jsConfId": jsConfId,
                  "callbackConfId": callbackConfId, "LABEL2": "  每日健康上报", "XH": stuID,
                  "XM": name, "LABEL12": "", "LABEL0": "1. 目前所在位置:", "SHENG": province, "SHI": city, "QU": region,
                  "LABEL11": "2.填报时间:", "SJ": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                  "LABEL1": "3. 今日体温是否正常？(体温小于37.3为正常)",
                  "TWZC": "正常", "LABEL6": "目前体温为：", "TW": "0", "TXWZ": province + city + region, "LABEL9": "4. 昨日午检体温:",
                  "WUJ": "36.4", "LABEL8": "5. 昨日晚检体温:", "WJ": "36.5", "LABEL10": "6. 今日晨检体温:", "CJ": "36.4",
                  "LABEL3": "7. 今日健康状况？", "JK": ["健康"], "JKZK": "", "QTB": "请输入具体症状：", "QT": " ",
                  "LABEL4": "8. 近14日你和你的共同居住者(包括家庭成员、共同租住的人员)是否存在确诊、疑似、无症状新冠感染者？", "WTSQK": ["无以下特殊情况"], "SFXG": "",
                  "LABEL5": "9. 今日隔离情况？", "GLQK": "无需隔离", "LABEL7": "* 本人承诺以上所填报的内容全部真实，并愿意承担相应责任。", "CHECK": True,
                  "WZXXXX": "2", "DWWZ": {}, "SUBMIT": "提交信息"}
    return json.dumps(parameters)


def main(stuID, province, city, region):
    # 正则表达式
    pattern = re.compile(r'[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}')
    pattern_name = re.compile(r'"value":"(.*?)"')

    # 开始连接
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID
    # 获取 sessionID
    res = requests.get(url)
    sessionID = pattern.search(res.text)[0]

    # 获取 jsConfId callbackConfId name
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/decision/view/form?sessionID=' + sessionID + '&op=fr_form&cmd=load_content&toVanCharts=true&fine_api_v_json=3&widgetVersion=1'
    res = requests.get(url)
    name = pattern_name.findall(res.text)[2]
    jsConfId = pattern.findall(res.text)[-2]
    callbackConfId = pattern.findall(res.text)[-1]

    # 获取 cookie
    cookie = 'JSESSIONID=' + requests.utils.dict_from_cookiejar(res.cookies)['JSESSIONID']

    # 提交表单
    url = 'http://dw10.fdzcxy.edu.cn/datawarn/decision/view/form'
    reffer = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + stuID
    new_json = processing_data(stuID, name, jsConfId, callbackConfId, province, city, region)
    headers = {
        'Host': 'dw10.fdzcxy.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36 SuperApp',
        'sessionID': sessionID,
        'Referer': reffer,
        'Cookie': cookie,
    }
    data = {
        'op': 'dbcommit',
        '__parameters__': quote(new_json)
    }
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if res.text:
            message(api_key, stuID[-3:] + "打卡成功", stuID[-3:] + "打卡成功")
            return print(stuID[-3:] + "打卡成功")
    except:
        message(api_key, stuID[-3:] + "打卡失败", stuID[-3:] + "打卡失败")
        return print(stuID[-3:] + "打卡失败")


if __name__ == '__main__':
    print('共有 ' + str(len(students)) + ' 人等待打卡')
    for i in range(len(students)):
        list_temp = students[i].split(' ')
        stuID = list_temp[0]
        if len(list_temp) == 4:
            province = list_temp[1]
            city = list_temp[2]
            region = list_temp[3]
        else:
            # 默认地区
            province = "福建省"
            city = "福州市"
            region = "鼓楼区"

        has_try = 0  # 尝试次数

        while has_try < MAX_TRY:
            try:
                main(stuID, province, city, region)
                break
            except:
                has_try += 1
                time.sleep(10)
                print("重试次数" + str(has_try))
    del stuID
    time.sleep(2)
    print("打卡任务全部完成！")
