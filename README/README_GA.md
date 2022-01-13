使用步骤:

- 点击右上角 `star` :)<img src="https://img2020.cnblogs.com/blog/1535189/202110/1535189-20211024011444420-1054435861.png" alt="image-20211023223415973"  />

- 克隆这个仓库到你名下

  <img src="https://img2020.cnblogs.com/blog/1535189/202110/1535189-20211024011444220-574369804.png" alt="image-20211023223437524"  />

- 第一次使用需要确认

![屏幕截图 2021-10-24 012114](https://img2020.cnblogs.com/blog/1535189/202110/1535189-20211024012336869-1205037702.png)

![image-20211024012249533](https://img2020.cnblogs.com/blog/1535189/202110/1535189-20211024012336425-986933813.png)

- 在仓库设置里面, 设置 secrets 如下

  **最简单就是只设置 stuIDs 就能用了！！** 

  - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用(类似的操作)

  - `stuIDs`: 批量打卡的学号
      ![批量打卡](https://images.cnblogs.com/cnblogs_com/Lin1031/1924181/o_211128122132_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20211128202040.png)

  - `check`:是否需要检查是否打卡成功，默认不检查，若使用 输入 YES（大写！！）

      **这个其实可以不用设置，看需求吧，打卡人多的时候容易挂**

      ![image-20220113222003563](https://s2.loli.net/2022/01/13/gYUWCqkepiVfZ8b.png)

      

      **下面两个要一起设置！否则会失败，设置了下面两个就不用设置 stuIDs **

      ![image-20220113222249140](https://s2.loli.net/2022/01/13/E4xcYbjqH1WCm59.png)

  - `stuIDsHome`:在家设置（学号 省份 市 区），若使用一定要输入和 i至诚 上一模一样

      ![image-20220113222138517](https://s2.loli.net/2022/01/13/X4jgd1eprk3zGD2.png)

  - `atHome`: 默认在校即鼓楼区，若使用 输入 YES（注意大小写）

      ![image-20220113222214573](https://s2.loli.net/2022/01/13/2TmBM5AP4CLHEnt.png)


代码如果已经更改过的，需要保持代码的更新，同步即可

![image-20211024003508381](https://img2020.cnblogs.com/blog/1535189/202110/1535189-20211024011443314-1404804501.png)

