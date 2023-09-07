from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

base_root = "result/BV1Vh4y1n7gA"

# Example usage
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
mp3_file_path = os.path.splitext(mp4_file_path)[0] + ".mp3"
convert_mp4_to_mp3(mp4_file_path,mp3_file_path)
