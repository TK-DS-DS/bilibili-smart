# 此版本为加入音频分离版本
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
def write_txt(text,filename):
    with open(filename, 'a') as file:
        # file.write(srt_id,"\n",srt_time,"\n",srt_text,"\n")
        file.write(f"{text}\n")

def convert_mp4_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

if __name__ == '__main__':
    import subprocess

    # 定义可执行文件的路径
    executable_path = "./BBDown.exe"
    bv = "BV1ep4y1H7gf"
    # 使用subprocess调用可执行文件
    # subprocess.call(executable_path)
    # output=subprocess.call([executable_path, "BV1ML41117fT", "-app","-F","<aid><res>"])
    output_path = "./result/" + bv
    output = subprocess.call([executable_path, str(bv), "--work-dir", str(output_path)])

    print(output)


    # #获取mp4文件名
    # import os
    # # folder_path = "./your_folder_path"  # 替换为实际的文件夹路径
    # # 获取文件夹下所有的文件名
    # files = os.listdir(output_path)
    # # 遍历文件列表，找到以 .mp4 结尾的文件
    # for file in files:
    #     if file.endswith(".mp4"):
    #         mp4_file_name = file
    #         print("get mp4 name:",str(mp4_file_name))
    #         break
    # mp4_file_path=output_path+"/"+mp4_file_name
    # print(str(mp4_file_path))


    #根据mp4生成mp3
    from moviepy.editor import VideoFileClip
    base_root = output_path
    # 获取mp4文件名
    import os
    # 获取文件夹下所有的文件名
    files = os.listdir(base_root)
    # 遍历文件列表，找到以 .mp4 结尾的文件
    for file in files:
        if file.endswith(".mp4"):
            mp4_file_name = file
            print("get mp4 name:", str(mp4_file_name))
            break
    mp4_file_path = base_root + "/" + mp4_file_name
    mp4_file_onlyname = os.path.splitext(os.path.basename(mp4_file_path))[0]
    mp3_file_path = os.path.splitext(mp4_file_path)[0] + ".mp3"
    convert_mp4_to_mp3(mp4_file_path, mp3_file_path)

    # # 复合mp3进行声音分离
    # import subprocess
    # # 定义可执行文件的路径
    # executable_path = "demucs"
    # # 使用subprocess调用可执行文件并获取输出
    # fixed_path = mp3_file_path.replace('\\', '/')
    # print(fixed_path)
    # demcus_mp3_path=str('"'+str(fixed_path)+'"')
    # # demcus_mp3_path=r'"R:\#myProject\bookmark-sort\result\BV1Hc411n7pu\BV1Hc411n7pu.mp3"'
    # print(demcus_mp3_path)
    # demucs_output = subprocess.call([executable_path, "--two-stems=vocals", demcus_mp3_path], encoding="gbk")
    # print(demucs_output)


    # #复制双mp3文件到对应文件夹下
    # import os
    # import shutil
    # vocals_file_path = "separated/htdemucs/"+str(mp4_file_onlyname)+"/vocals.wav"
    # novocals_file_path="separated/htdemucs/"+str(mp4_file_onlyname)+"/no_vocals.wav"
    # destination_folder = output_path+"/"
    # # 提取文件名（不包含扩展名）
    # vocal_name = os.path.splitext(os.path.basename(vocals_file_path))[0]
    # novocal_name =  os.path.splitext(os.path.basename(novocals_file_path))[0]
    # # 构建目标文件路径
    # destination_vocals_file = os.path.join(destination_folder, vocal_name + '.wav')
    # destination_novocals_file=os.path.join(destination_folder, novocal_name + '.wav')
    # # 复制文件并更改名称
    # shutil.copy2(vocals_file_path, destination_vocals_file)
    # shutil.copy2(novocals_file_path, destination_novocals_file)
    # print(f"文件已复制到：{destination_vocals_file}")
    # print(f"文件已复制到：{destination_novocals_file}")


    # 删除现有的 srt 文件
    srt_pathname = output_path+"/"+str(mp4_file_onlyname)+".srt"
    txt_pathname = output_path+"/"+str(mp4_file_onlyname)+".txt"
    if os.path.exists(srt_pathname):
        os.remove(srt_pathname)
        print("delete")
    #根据mp3生成字幕
    model = whisper.load_model("medium")
    whisper_file_path=mp3_file_path #路径
    # whisper_file_path = mp3_file_path  # 路径
    result = model.transcribe(str(whisper_file_path))
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
        write_txt(text,txt_pathname)
        print(id, start, end, text)




