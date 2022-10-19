# i至诚自动化打卡（含视频教程）

i至诚疫情防控每日填报助手，用于解决忘记填写每日打卡的问题。

**推荐 方法一 和 方法二 同时使用**

***文字看不懂，可以看图文版或者视频教程***

**GitHub Action 每60天会自动关闭，需要手动重启** **（[重启教程 （点这里！！！具体截图）](https://github.com/Lin1031/izhicheng/blob/main/README/README_UPDATE.md)）**


# 注意

本人不对因为滥用此程序造成的后果负责，**请在合理且合法的范围内使用本程序**。

**本程序仅用于解决忘记打卡这一问题，如果填报表中任意情况发生变化，比如地点发生变化，处在居家隔离阶段等情况，请务手动打卡。**



打卡网站可能会经常更新，因此代码会做更改。*如果在使用过程中遇到问题或者发现 bug，可以提 issue*，代码更新也会在此处通知。
如果想要即时得知代码的更新请 *watch* 本仓库。



有特殊需求的同学可以修改本代码。



# 更新

```
2022.10.19 提示：推荐 方法一 和 方法二 同时使用
           修复：GitHub Action 缺少 packaging 库问题
2022.08.28 增加：GitHub Action 60天重启教程
2022.07.05 修复：selenium 缺少 typing_extensions 库的问题
2022.06.11 更新：增加 Windows/Linux 重试次数
2022.06.10 更新：添加请求头
           更新：增加重试次数，解决因服务器崩溃导致打卡失败问题
2022.03.30 增加：GitHub Action 使用操作视频
2022.03.18 提示：GitHub Action 每60天会自动关闭，需要手动重启
2022.01.17 更新：修改代码，学号和地区可以一起设置
2022.01.14 更新：增加 request 填报，两秒一个学号（方法三）
2022.01.13 更新：代码检查可选择，避免过多人使用代码程序报错
           更新：可以设置省份，使用家庭地址（虽然没啥用）
           修复：学号不存在报错问题
           更新：修改 README.md
           更新：修改打卡时间，北京时间凌晨3点5点7点进行打卡
2022.01.12 更新：关闭多余的连接
2021.11.28 更新：感谢 @miscdec 的帮助，实现在 GitHub Action 上的学号的批量打卡
2021.11.26 更新：修复 chrome 版本更新导致失效，使用 webdriver 自动更新一劳永逸 
2021.11.16 更新：感谢 @R-YaTian 的帮助，可以在顺利在凌晨进行打卡
2021.10.24 更新：更改无服务器可用版本 只需要 GitHub 账号 使用方法见文章末尾
2021.10.04 更新：更改打卡链接地址
2021.07.13 更新：优化在家代码，可更改地区
2021.06.08 更新：去除广告弹窗
2021.03.30 更新：重构代码减少报错
2021.03.26 更新：修复了在校代码bug
2021.03.19 更新：修复了windows在校代码错误
           更新：修复了批量打卡导致页面加载不出
2021.03.02 更新：新增在校版，只需要学号
2021.02.15 更修：增加了批量填报
           更新：增加错误日志发送邮件
2021.02.13 更新：增加了windows版并修复了BUG
```


# GitHub Actions 使用视频
**[使用步骤视频（点这里！！！）](https://www.bilibili.com/video/BV1NZ4y1a7He/)**

[![使用步骤视频](https://images.cnblogs.com/cnblogs_com/Lin1031/1924181/o_220827121244_izhicheng.png)](https://www.bilibili.com/video/BV1NZ4y1a7He?share_source=copy_web)


# 方法一： 使用自己的服务器运行
**[使用步骤（点这里！！！具体步骤截图）](https://github.com/Lin1031/izhicheng/blob/main/README/README_yun.md)**



# 方法二： 使用 GitHub Actions（推荐使用）
没有服务器的同学可以使用 GitHub Action 来进行运行此程序。

Github提供了一个secret功能，用于存储密钥等敏感信息，请按照以下步骤操作。

**[步骤截图 （点这里！！！具体截图）](https://github.com/Lin1031/izhicheng/blob/main/README/README_GA.md)**

**使用步骤:**

- 点击右上角 `star` :)
- 克隆这个仓库到你名下
- fork的仓库默认禁用了`workflow`，需要手动打开：点击 `actions`选项卡，点击`I understand my workflows, go ahead and run them`。
- 在仓库设置里面, 设置 secrets 如下
  - `students`: 你（们）的学号，也可以设置（学号 省份 市 区），若使用一定要输入和 i至诚 上一模一样
  - `check`:是否需要检查是否打卡成功，默认不检查，若使用 输入 YES（人多易报错）
  - server酱通知设置（需要server酱通知时设置 可选）：
    - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
- 测试actions是否可以正常工作

完成之后, 每天 北京时间 3点5点7点 自动触发 github actions 进行填报 。

## 建议：

建议更改` .github/workflows/main.yml `中的 schedule 时间设置，避免过的人使用导致打卡失败

# 方法三： 使用 GitHub Actions（推荐使用，适合20+人一起打卡）
**[步骤截图 （点这里！！！具体截图）](https://github.com/Lin1031/izhicheng/blob/main/README/README_RE.md)**

**使用步骤:**

- 点击右上角 `star` :)
- 克隆这个仓库到你名下
- fork的仓库默认禁用了`workflow`，需要手动打开：点击 `actions`选项卡，点击`I understand my workflows, go ahead and run them`。
- 在仓库设置里面, 设置 secrets 如下
  - `students`: 你（们）的学号，也可以设置（学号 省份 市 区），若使用一定要输入和 i至诚 上一模一样
  - server酱通知设置（需要server酱通知时设置 可选）：
    - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
- 测试actions是否可以正常工作

完成之后, 每天 北京时间 3点5点7点 自动触发 github actions 进行填报 。

## 参考项目
https://blog.zimo.wiki/posts/5a29fa14/
