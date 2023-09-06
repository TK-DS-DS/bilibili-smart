import openai

import random

api_list = [
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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"
]

random_api = random.choice(api_list)

print(random_api)

# 设置访问凭证
# openai.api_key = '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'
openai.api_key = str(random_api)
# response = openai.Completion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
#     {"role": "user", "content": "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"}
#   ]
# )
rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "接下来，我将告诉你一些事情，你判断是属于哪一类，只需要回复我对应的数字序号。1、购物，2、高铁票，3、酒店，4、音乐，5、其他。请只回复数字，不要多余"},
    {"role": "user", "content": "我要吃油炸大虾"}]
        )
print(rsp.get("choices")[0]["message"]["content"])
# print(response.choices[0])
