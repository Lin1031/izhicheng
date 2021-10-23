# i至诚自动化打卡

## 源码开源，仅用于学习

### window自动定时使用 Windows 任务调度程序，可以自行百度
```
----------10月24日更新--------
更改无服务器可用版本 只需要 GitHub 账号

----------10月4日更新--------
更改打卡链接地址

----------7月13日更新--------
优化在家代码，可更改地区

----------6月8日更新--------
去除广告弹窗

----------3月30日更新--------
重构代码减少报错

----------3月26日更新--------
修复了在校代码bug

----------3月19日更新--------
修复了windows在校代码错误

----------3月19日更新--------
修复了批量打卡导致页面加载不出

----------3月2日更新--------
更新i至诚在校版，只需要学号

----------2月15日更新--------
更新了批量填报
更新了错误日志发送邮件

----------2月13日更新--------
更新了新版本
更新了windows版
修复了BUG
```

### 零、环境准备

centos7云服务准备：https://developer.aliyun.com/adc/student/

环境准备：https://www.cnblogs.com/Lin1031/p/14187135.html

博客园地址：https://www.cnblogs.com/Lin1031/p/14187137.html


### 一、在根目录下新建一个py文件
```
cd
touch tianbiao.py
vim tianbiao.py
```
### 二、编辑python程序(注意，要修改path地址为本地，driverchrome路径)


#### 开源不易，希望GitHub给个star
#### GitHub地址：https://github.com/Lin1031/izhicheng


### 三、在根目录下创建一个脚本
```
cd 
touch my.sh
vim my.sh
```
### 四、编辑脚本内容（路径修改为本地py文件路径，学号处修改为自己的学号）
```
#!/bin/bash
. /etc/profile
. ~/.bash_profile
python的绝对路径 /root/tianbiao.py 学号 省份 市 区（主要要和i至诚上面一模一样）
```
![](https://img2020.cnblogs.com/blog/1535189/202101/1535189-20210126182455451-1926330943.png)
```
whereis python3
```
![](https://img2020.cnblogs.com/blog/1535189/202012/1535189-20201225110258857-1147785979.png)

### 五、编辑python自启动
```
sudo vim /etc/crontab
```
![](https://img2020.cnblogs.com/blog/1535189/202012/1535189-20201225024612136-319055669.png)
```
crontab -e
```
crontab可能不能运行，因此在这里再次添加定时
![](https://img2020.cnblogs.com/blog/1535189/202012/1535189-20201225110424469-118105501.png)


### 六、修改my.sh的权限为777
```
cd 
sudo chmod -R 777 /root/my.sh
```

### 七、发送错误日志到邮箱
Centos7发错错误日志到邮箱：https://www.cnblogs.com/Lin1031/p/14401289.html#/c/subject/p/14401289.html
配置好环境之后，使用 empty.sh 脚本，在 shell 里设置自动启动的时间，如果之前的填报脚本出现错误日志，则会发送邮件。
注意：使用时，需要将 tiaobiao.py 最后一行输出注释掉。一般自动启动时间建议在设置自动填报时间之后的一小时。

### 八、批量填报
编写一个 sno.txt 文件，其内容为学号 省 市 区，使用 my.sh 脚本，进行批量读文件。
注意：sno.txt 中 学号为一行一个人，最后一行不能有空行。若使用批量填报，则定时则设置为该脚本。

###  无服务器使用（无脑，推荐）

### 使用 GitHub Actions（流程很简单 只要加个学号就行）

完成之后, 每天 UTC 0:10 (北京时间 8:10) 自动触发 github actions 进行填报 。

使用步骤:

- 点击右上角 `star` :)![image-20211023223415973](https://github.com/Lin1031/izhicheng/blob/main/image/image-20211023223415973.png)

- 克隆这个仓库到你名下

- ![image-20211023223437524](https://github.com/Lin1031/izhicheng/blob/main/image/image-20211023223437524.png)

- 点击 Actions 

  ![image-20211024005053964](https://github.com/Lin1031/izhicheng/blob/main/image/image-20211024005053964.png)

- 在仓库设置里面, 设置 secrets 如下

  - `stuID`: 你的学号

    ![image-20211024004751004](https://github.com/Lin1031/izhicheng/blob/main/image/image-20211024004751004.png)

  - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用(类似的操作)

代码如果已经更改过的，需要保持代码的更新，同步即可

![](https://github.com/Lin1031/izhicheng/blob/main/image/image-20211024003427980.png)

### 参考资料
https://blog.csdn.net/chengxun02/article/details/105187996

https://blog.csdn.net/a12355556/article/details/112163669

https://github.com/IanSmith123/ucas-covid19
