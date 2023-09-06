import requests

# 替换成你的资源列表和Cookie
resources = '84522106:21'  # 替换成你的资源列表
cookie = "SESSDATA=b_nut=1656246493; buvid3=F13A0432-0E8F-135C-F3F4-E3DA6788004093993infoc; buvid4=AB2392AB-3256-23EB-BD89-A17DBA99379693993-022062620-GOOdGaSrX6d74gstQGDZ7w%3D%3D; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; LIVE_BUVID=AUTO5916563824297765; rpdid=|(k)YmR)lmuk0J'uYY))R~))J; header_theme_version=CLOSE; hit-new-style-dyn=0; CURRENT_PID=aa8de9c0-cde7-11ed-a3a5-b9de548b693c; CURRENT_QUALITY=116; CURRENT_FNVAL=4048; PVID=1; home_feed_column=5; _uuid=68D47C6C-5FB9-125F-E1D5-CD4ECC951102839766infoc; DedeUserID=26602906; DedeUserID__ckMd5=6ae7a406be2f20a1; b_ut=5; FEED_LIVE_VERSION=V8; nostalgia_conf=-1; innersign=0; b_lsid=212228C7_18A4FBB2DF4; browser_resolution=1715-829; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTM4MTM5ODYsImlhdCI6MTY5MzU1NDc4NiwicGx0IjotMX0.AP_mDHkT-essMcPdK0GxwY6Q6umHw5VnwcT8ZvDgroM; bili_ticket_expires=1693813986; SESSDATA=2ad98909%2C1709106786%2Cde1de%2A91XtSfADhuSKUGarPB9jMpDW8o21NfX4T-aIjZLD-BDezd_VZIhaUhGskx1dKXBI1l5ho-CAAABgA; bili_jct=d871dd23bf72291e57d3bfc3ca0aad7a; sid=oz157ro2; fingerprint=2402fc544234ca23a48ebc5e6360e447; buvid_fp=F13A0432-0E8F-135C-F3F4-E3DA6788004093993infoc"  # 替换成你的Cookie

# 构建请求参数
params = {
    'media_id': 84522106,
    'pn': 2,
    'ps': 20,
    'keyword': '',
    'order': 'mtime',
    'type': 0,
    'tid': 0,
    'platform': 'web'
}

# 构建请求头部
headers = {
    'Cookie': cookie
}

# 发送GET请求
url = 'https://api.bilibili.com/x/v3/fav/resource/list'
response = requests.get(url, params=params, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()

    # 检查是否成功
    if data['code'] == 0:
        # 获取内容信息列表
        content_list = data['data']['medias']
        print(content_list)
        # 遍历内容信息
        for resource in content_list:

            print(f"资源ID: {resource['id']}")
            print(f"资源类型: {resource['type']}")
            print(f"标题: {resource['title']}")
            print(f"封面URL: {resource['cover']}")
            print(f"简介: {resource['intro']}")
            print(f"视频分P数: {resource['page']}")
            print(f"音频/视频时长: {resource['duration']} 秒")
            print(f"UP主信息 - MID: {resource['upper']['mid']}")
            print(f"UP主信息 - 昵称: {resource['upper']['name']}")
            print(f"UP主信息 - 头像URL: {resource['upper']['face']}")
            print(f"属性: {resource['attr']}")
            print(f"状态数 - 收藏数: {resource['cnt_info']['collect']}")
            print(f"状态数 - 播放数: {resource['cnt_info']['play']}")
            print(f"状态数 - 弹幕数: {resource['cnt_info']['danmaku']}")
            print(f"VT: {resource['cnt_info']['vt']}")
            print(f"播放开关: {resource['cnt_info']['play_switch']}")
            print(f"回复数: {resource['cnt_info']['reply']}")
            print(f"观看文本: {resource['cnt_info']['view_text_1']}")
            print(f"链接: {resource['link']}")
            print(f"创建时间: {resource['ctime']}")
            print(f"发布时间: {resource['pubtime']}")
            print(f"收藏时间: {resource['fav_time']}")
            print(f"视频稿件bvid: {resource['bv_id']}")
            print(f"视频稿件bvid: {resource['bvid']}")
            print()
    else:
        print(f"请求失败，错误信息：{data['message']}")
else:
    print(f"请求失败，状态码：{response.status_code}")
