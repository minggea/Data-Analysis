#!/usr/bin/python
# author guming
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 选择喜欢数比50万小的数据
t_uk = t_uk[t_uk[:, 1] <= 500000]  # 第一列是喜欢数
t_uk_comment = t_uk[:, -1]  # 最后一列是评论数
t_uk_like = t_uk[:, 1]

# 设置画布
plt.figure(figsize=(20, 8), dpi=80)
# 绘制散点图 -- scatter()  横轴喜欢数，纵轴评论数
plt.scatter(t_uk_like, t_uk_comment)
# 展示图片,一个点代表一个视频，可以找出喜欢数越多评论数也越多的视频
plt.show()
