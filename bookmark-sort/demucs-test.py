import subprocess

# 定义可执行文件的路径
executable_path = "demucs"


# 使用subprocess调用可执行文件并获取输出
output = subprocess.call([executable_path,"--two-stems=vocals","./result/BV1Hc411n7pu/全自动AI来了？教你安装AutoGPT，解放生产力.mp3"], encoding="gbk")

# 打印输出
print(output)
