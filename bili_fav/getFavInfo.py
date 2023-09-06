# 收藏夹ID: 84522106
# 收藏夹标题: 默认收藏夹
# 收藏夹内容数量: 2506
import requests

# 替换成你的收藏夹ID和Cookie
media_id = 84522106  # 替换成你的收藏夹ID
cookie = "SESSDATA=b_nut=1656246493; buvid3=F13A0432-0E8F-135C-F3F4-E3DA6788004093993infoc; buvid4=AB2392AB-3256-23EB-BD89-A17DBA99379693993-022062620-GOOdGaSrX6d74gstQGDZ7w%3D%3D; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; LIVE_BUVID=AUTO5916563824297765; rpdid=|(k)YmR)lmuk0J'uYY))R~))J; header_theme_version=CLOSE; hit-new-style-dyn=0; CURRENT_PID=aa8de9c0-cde7-11ed-a3a5-b9de548b693c; CURRENT_QUALITY=116; CURRENT_FNVAL=4048; PVID=1; home_feed_column=5; _uuid=68D47C6C-5FB9-125F-E1D5-CD4ECC951102839766infoc; DedeUserID=26602906; DedeUserID__ckMd5=6ae7a406be2f20a1; b_ut=5; FEED_LIVE_VERSION=V8; nostalgia_conf=-1; innersign=0; b_lsid=212228C7_18A4FBB2DF4; browser_resolution=1715-829; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTM4MTM5ODYsImlhdCI6MTY5MzU1NDc4NiwicGx0IjotMX0.AP_mDHkT-essMcPdK0GxwY6Q6umHw5VnwcT8ZvDgroM; bili_ticket_expires=1693813986; SESSDATA=2ad98909%2C1709106786%2Cde1de%2A91XtSfADhuSKUGarPB9jMpDW8o21NfX4T-aIjZLD-BDezd_VZIhaUhGskx1dKXBI1l5ho-CAAABgA; bili_jct=d871dd23bf72291e57d3bfc3ca0aad7a; sid=oz157ro2; fingerprint=2402fc544234ca23a48ebc5e6360e447; buvid_fp=F13A0432-0E8F-135C-F3F4-E3DA6788004093993infoc"  # 替换成你的Cookie

# 构建请求参数
params = {
    'media_id': media_id
}

# 构建请求头部
headers = {
    'Cookie': cookie
}

# 发送GET请求
url = 'https://api.bilibili.com/x/v3/fav/folder/info'
response = requests.get(url, params=params, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()

    # 检查是否成功
    if data['code'] == 0:
        # 获取收藏夹信息
        folder_info = data['data']

        # 打印收藏夹元数据信息
        print("收藏夹ID:", folder_info['id'])
        print("收藏夹标题:", folder_info['title'])
        print("收藏夹封面图片url:", folder_info['cover'])
        print("创建者昵称:", folder_info['upper']['name'])
        print("创建者头像url:", folder_info['upper']['face'])
        print("收藏夹类型:", folder_info['type'])
        print("创建时间:", folder_info['ctime'])
        print("收藏时间:", folder_info['mtime'])
        print("收藏夹内容数量:", folder_info['media_count'])
        print("收藏夹收藏状态:", folder_info['fav_state'])
        print("点赞状态:", folder_info['like_state'])

        cnt_info = folder_info['cnt_info']
        print("收藏数:", cnt_info['collect'])
        print("播放数:", cnt_info['play'])
        print("点赞数:", cnt_info['thumb_up'])
        print("分享数:", cnt_info['share'])
    else:
        print(f"请求失败，错误信息：{data['message']}")
else:
    print(f"请求失败，状态码：{response.status_code}")
