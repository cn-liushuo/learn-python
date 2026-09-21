# 查看 python 中的关键字
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))  # 获取关键字的个数

# 关键字严格区分大小写
true = '真'

# True = '真' # True 是 python 中的关键字
