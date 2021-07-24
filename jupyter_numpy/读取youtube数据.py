#!/usr/bin/python3
# author guming
import numpy as np
import matplotlib.pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# 注意：虽然是 .csv 文件，还是要用np.loadtxt()去加载
"""
np.loadtxt()参数说明：
    delimiter：str, 可选
        用于分隔值的字符串。为了向后兼容，字节字符串将被解码为' latin1 '。默认是空格
        
    dtype：data-type, 可选
        默认值:float
        结果数组的数据类型
        如果这是一个结构化数据类型，那么结果数组将是一维的
        每一行将被解释为数组的一个元素
        在这种情况下，使用的列数必须与数据类型中的字段数匹配
        
    unpack: bool类型，可选
        默认值: False  
        如果为True，返回的数组将被转置
        因此参数可以使用x, y, z = loadtxt(…)解包
        当与结构化数据类型一起使用时，将为每个字段返回数组
"""
t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int")

# print(t1)
print("-" * 100)
print(t2)
print("-" * 100)

# 查看文件中的数据是不是有空值
# print(np.isnan(t2))  # 将t2数组显示为只有True和False的样子（元素是nan的地方为True），这样看不到全部数据，也太麻烦
# 因为np把False判定为0，只有nan才不等于自身从而被判定为True,统计非0个数即nan个数
print('t2读到的数据中,nan有 ', np.count_nonzero(t2 != t2), ' 个')
print("-" * 100)

# 取评论的数据
# np的二维数组切片操作，第一个参数是行，第二个参数是列，[:,-1]表示取所有行的倒数第一列元素（也就是评论）
t_us_comments = t2[:, -1]

# 选择比5000小的数据,因为数据主要集中在5000以下（二位数组的 逻辑表达式切片操作）
t_us_comments = t_us_comments[t_us_comments <= 5000]  # 条件切片，筛选符合条件的元素留下

# 怎么知道分多少组: 打印最大和最小值
print(t_us_comments.max(), t_us_comments.min())

# 设置组距
d = 100
# 计算组数
bin_nums = (t_us_comments.max() - t_us_comments.min()) // d  # //是python的取整除法
# 设置画布
plt.figure(figsize=(20, 8), dpi=80)
# 绘制直方图
plt.hist(t_us_comments, bin_nums)
# 展示直方图
plt.show()
