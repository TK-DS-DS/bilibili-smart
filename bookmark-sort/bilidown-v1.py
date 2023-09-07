import os

import whisper

# 输入时间的秒数，返回时间对应的时分秒（包含ms）
def time_format(timestamp):
    if timestamp is None:
        return ''
    # 转换为字符串，并截取小数点前的所有数字
    second_part = int(str(timestamp).split(".")[0])
    # 获取小数点后的数字，并保留三位小数
    ms_part = str(timestamp).split(".")[1][:3].ljust(3, '0')

    hour=second_part//3600
    minute=(second_part - hour *3600) //60
    second = second_part - hour * 3600 - minute * 60
    # 对时分秒进行补全
    if(hour>=10):
        hour=str(hour)
    else:
        hour="0"+str(hour)
    if(minute>=10):
        minute=str(minute)
    else:
        minute="0"+str(minute)
    if(second>=10):
        second=str(second)
    else:
        second="0"+str(second)
    return str(hour) + ":" + str(minute) + ":" + str(second)+","+str(ms_part)


def write_srt_to_txt(srt_id,srt_time, srt_text,filename):
    with open(filename, 'a') as file:
        # file.write(srt_id,"\n",srt_time,"\n",srt_text,"\n")
        file.write(f"{srt_id}\n{srt_time}\n{srt_text}\n\n")


if __name__ == '__main__':
    import subprocess

    # 定义可执行文件的路径
    executable_path = "./BBDown.exe"
    bv = "BV1Vh4y1n7gA"
    # 使用subprocess调用可执行文件
    # subprocess.call(executable_path)
    # output=subprocess.call([executable_path, "BV1ML41117fT", "-app","-F","<aid><res>"])
    output_path = "./result/" + bv
    output = subprocess.call([executable_path, str(bv), "--work-dir", str(output_path)])

    print(output)

    # 字幕下载or生成
    # 判断字幕有没有成功下载
    # 成功下载
    if(0):
        print("jump")

    # 没有成功下载
    else:
        # 删除现有的 srt 文件
        srt_pathname = output_path+"/"+str(bv)+".srt"
        if os.path.exists(srt_pathname):
            os.remove(srt_pathname)
            print("delete")
        model = whisper.load_model("medium")
        #获取mp4文件名
        import os
        # folder_path = "./your_folder_path"  # 替换为实际的文件夹路径
        # 获取文件夹下所有的文件名
        files = os.listdir(output_path)
        # 遍历文件列表，找到以 .mp4 结尾的文件
        for file in files:
            if file.endswith(".mp4"):
                mp4_file_name = file
                print("get mp4 name:",str(mp4_file_name))
                break
        mp4_file_path=output_path+"/"+mp4_file_name
        print(str(mp4_file_path))
        result = model.transcribe(str(mp4_file_path))
        results = result["segments"]

        for i in results:
            # print(i)
            id = str(i['id'])
            # start =
            start = str(time_format(i['start']))
            end = str(time_format(i['end']))
            text = str(i['text'])
            srt_time = str(str(start) + " --> " + str(end))
            write_srt_to_txt(id, srt_time, text, srt_pathname)

            print(id, start, end, text)

