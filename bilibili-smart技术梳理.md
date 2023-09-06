bilibili-fav技术梳理



av号是曾经的id，2020年3月23日，更改为bv，av仍然可以使用。

cv是专栏文章，bv是视频

哔哩哔哩ABCID（AV，A，BV，C）互转API  https://www.blueskyxn.com/202012/2873.html

Bilibili API	https://blog.muna.uk/archives/Bilibili_apis.html



计划将bv和cv作为可以所有装载源码用户共享的。

限定下载线程为一个。

up的是mid

## 需求整理



## 相关官方API

## 

## 数据存放设计

resources下设置bv和cv，如果没有bv或者cv怎么办？

这些是绝对的客观可观察统一性

bv下存放

每条bv对应id、bv、up_mid、title、describe、uptime、播放数、likes、收藏数、弹幕数、updtime 属于可以共享、时长

总结表： id 、bv、总结、updtime

评论表：

弹幕表：

资源表：id、bv、video_path、audio_path、总结_path、talk_path、danmu_path

默认0代表空，1代表正在下载中，如果是相对路径代表下载完成，相对路径是针对于resources的。



收藏表：id、收藏夹id、收藏夹标题、收藏夹封面图片url、创建者昵称、创建者头像url、收藏夹类型、创建时间、收藏时间、收藏内容数量、收藏夹状态

视频收藏表（连接表）：id、收藏夹id、视频bv（思考一下）、收藏时间



up表：id、mid、name、face_imgurl、

## 模块设计



BV1Vh4y1n7gA

### 解析下载模块

入参bv、cv、av任意一个，解析实现av、bv、cv记录



### 检查模块

依次检查路径，校验是否能查到文件，更新文件状态



感谢：

BBDown

bilibili野生