<p align="center">

# Tieba-Manager

[![gitee](https://img.shields.io/badge/mirror-gitee-red)](https://gitee.com/Starry-OvO/Tieba-Manager)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Starry-OvO/Tieba-Manager?logo=lgtm)](https://lgtm.com/projects/g/Starry-OvO/Tieba-Manager/context:python)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</p>

## 简介

`aiotieba`库是一个使用`aiohttp`实现的**异步贴吧客户端**

封装了下列实用接口并额外添加了一些数据库和图像处理功能以方便自动化的吧务管理

封装的官方接口包括：

+ 按**回复时间**/**发布时间**/**热门序**获取贴吧**主题帖**/**精华帖列表**。支持获取带**转发**/**投票**/**转发嵌套投票**/**各种卡片**的主题帖信息
+ 获取带**图片链接**/**小尾巴内容**/**点赞情况**/**用户信息**（**用户名**/**user_id**/**portrait**/**等级**/**性别**/**是否锁回复**）/每条回复的**前排楼中楼**（支持按或不按点赞数排序）的**回复列表**
+ 获取带所有前述用户信息的**楼中楼列表**
+ 根据**用户名**/**昵称**/**portrait**/**user_id**中的任一项反查其他用户信息，或通过用户主页的**tieba_uid**反查其他用户信息
+ 使用小吧主、语音小编的`BDUSS`**删帖**/**屏蔽**/**封禁**任意用户3天或10天
+ 使用已被大吧主分配解封/恢复/处理申诉权限的吧务`BDUSS`**解封**/**恢复**/**处理申诉**
+ 使用大吧主`BDUSS`**推荐帖子到首页**/**移动帖子到指定分区**/**加精**/**撤精**/**置顶**/**撤置顶**/**添加黑名单**/**查看黑名单**/**取消黑名单**
+ 获取用户**主页信息**/**关注贴吧列表**/**屏蔽贴吧列表**/**关注用户列表**/**粉丝列表**/**发帖历史**/**回复历史**
+ 获取贴吧**最新关注用户列表**/**等级排行榜**/**吧务列表**/**吧详情**
+ 使用`BDUSS`**关注贴吧**/**取关贴吧**/**关注用户**/**取关用户**/**移除粉丝**/**屏蔽贴吧**/**取消屏蔽贴吧**/**签到**/**水帖**/**发送私信**

额外功能包括：

+ 数据库功能：**缓存贴吧常量**（如贴吧名到fid的映射关系）/**为用户添加标记**/**为帖子或回复添加标记**/**为图像hash添加标记**
+ 图像处理功能：**图像解码**/**二维码解析**/**图像hash计算**

在`aiotieba`的基础上，我开发了多种自动化吧务管理工具，如[云审查工具](wikis/cloud_review_introduction.md)和[指令管理器](../../wiki/%E6%8C%87%E4%BB%A4%E7%AE%A1%E7%90%86%E5%99%A8%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E4%B9%A6)，以及一些[自动化脚本的案例](wikis/many_utils.md)

## 入门教程

+ 确保你的[`Python`](https://www.python.org/downloads/)版本在`3.9`及以上

+ 下载仓库并安装依赖

```bash
git clone https://github.com/Starry-OvO/Tieba-Manager.git
cd ./Tieba-Manager
pip install -r requirements.txt
```

+ 实操教程请参考[aiotieba入门教程](wikis/tutorial.md)

+ 云审查教程请参考[云审查教程](wikis/cloud_review_tutorial.md)

## 友情链接

+ [另一个仍在活跃更新的贴吧管理器（有用户界面）](https://github.com/dog194/TiebaManager)
+ [用户反馈（我的个人吧）](https://tieba.baidu.com/f?ie=utf-8&kw=starry)

## 客户名单

云审查工具&指令管理器已在以下贴吧应用（2022.07.09更新，按启用时间先后排序）

|      吧名      | 关注用户数 | 最近29天日均访问量 | 日均主题帖数 | 日均回复数 |
| :------------: | :--------: | :----------------: | :----------: | :--------: |
| vtuber自由讨论 |   16,476   |       2,496        |      3       |     75     |
|     asoul      |  159,365   |       74,301       |     781      |   7,215    |
|      嘉然      |   54,756   |       23,550       |     207      |   2,956    |
|      宫漫      | 1,261,932  |       45,440       |     264      |   3,316    |
|    lol半价     | 1,947,864  |      154,479       |     572      |   9,657    |
|     孙笑川     | 2,040,532  |      561,378       |    6,183     |  165,882   |
|    新孙笑川    |  244,286   |       41,479       |     384      |   14,236   |
|      向晚      |   28,048   |       21,302       |     227      |   2,959    |
|      贝拉      |   21,430   |       15,141       |      83      |   1,585    |
|    王力口乐    |   12,961   |       37,185       |     381      |   4,992    |
|      乃琳      |   16,677   |       6,917        |      49      |    803     |
| asoul一个魂儿  |   15,003   |       3,081        |      42      |    465     |
|     贝贝珈     |   1,661    |       1,411        |      7       |     81     |
|    抗压背锅    | 3,723,373  |      977,471       |    2,635     |   71,561   |
