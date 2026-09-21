"""
1、输出 “好好学习，天天向上”
需求：用 print() 函数将 “好好学习，天天向上” 输出的文本文件 text.txt 中
"""
fp = open('../out/text.txt', 'w', encoding='utf-8')  # 写入文件
print('好好学习，天天向上', file=fp)  # 输出内容到文件
fp.close()  # 关闭文件

"""
2、输出个人爱好
需求：使用 input()函数从键盘输出姓名，年龄，爱好，并用 print() 函数输出到控制台 
"""
name = input("请输入姓名：")
age = input("请输入年龄：")
hobby = input("请输入爱好：")
print("--------我的介绍：--------")
print(f"我是{name}，我今年{age}，我的爱好是{hobby}")
