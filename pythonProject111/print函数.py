# print 函数基础语法
# 基本语法：print('输入内容')，用于在控制台显示指定文本或数据；扩展语法：print(内容1, 内容2, ..., sep="分隔符", end="结尾符", file=None)，支持多内容输出及参数配置。

# sep 参数：自定义分隔符
# sep 用于设置多个输出内容之间的分隔符号，默认值为空格。示例：print("Hello", "World", sep="-")，输出结果为 "Hello World"。

# end 参数：控制结尾字符
# end 用于定义输出语句的结尾字符，默认值换行符"n"。示例print("Hello", end="!");print("World")，输出结果为 "Hello!World" (两行内容合并为一行)。

a = 10  # a是变量 10是值
b = 20  # b是变量 20是值
print(111)
print(a + b)  # 做运算
print(330)
print('我爱中国 中国也爱我')
print('我爱中国 中国也爱我')
print('我爱中国 中国也爱我')
print('我爱中国 中国也爱我')

print(a, b, '好好学习，天天向上', 100)

print('湖南', end='--->')
print('欢迎你')

aa = open('1.txt', 'w', encoding='utf-8')  # 写入文件
print('hello world 你好世界', file=aa)  # 输出内容到文件中
aa.close()  # 关闭文件
