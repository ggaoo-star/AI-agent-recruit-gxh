# 完成任务
import numpy as np
student_score = {"王林":670,"利姆湾":608,"徐立国":580,"韩立":680}
def calc_stats(data):
    values = list(data.values())
    avg = sum(values)/ len(values)
    high= max(values)
    return avg,high
avg_score,max_score = calc_stats(student_score)
print("平均分是:",avg_score)
print("最高分是:",max_score)
# 矩阵相乘(借助AI等工具学习)
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])
C = np.dot(A,B)
print("矩阵A的形状:",A.shape)
print("矩阵B的形状:",B.shape)
print("乘积结果:\n",C)
print("结果形状:",C.shape)

# 在之前自己学习Python的过程在另外一个笔记中
# 学习和写代码参照网上资料和AI工具