import whisper

model = whisper.load_model("base")
result = model.transcribe("./result/BV1Vh4y1n7gA/【AI帝宝】 勾指起誓 - 东海帝皇.mp4")
# print(result)
# print(result["text"])
results=result["segments"]
for i in results:
    print(i)




