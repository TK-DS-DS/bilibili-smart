import subprocess


# 输入bv号和保存路径进行保存视频
# 命名方式为bv号/bv号.mp4
def bilidown_video(bv="",path=""):
    # 定义可执行文件的路径
    executable_path = "./BBDown.exe"
    bv = "BV1Vh4y1n7gA"
    # 使用subprocess调用可执行文件
    # subprocess.call(executable_path)
    # output=subprocess.call([executable_path, "BV1ML41117fT", "-app","-F","<aid><res>"])
    output_path = "./result/" + bv
    output = subprocess.call([executable_path, str(bv), "--work-dir", str(output_path)])
    print(output)

if __name__ == '__main__':
    bilidown_video()