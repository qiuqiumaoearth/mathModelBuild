import numpy as np
from scipy.optimize import linprog

# 定义目标函数的系数（取负值，因为我们需要求解的是最大化问题）
c = np.array([-3, -2])

# 定义约束条件矩阵 A 和向量 b
A = np.array([[1, 1], [-1, 1]])
b = np.array([4, -1])

# 定义变量的边界
x_bounds = (0, None)
y_bounds = (0, None)

# 求解线性规划问题
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

print("Optimal value:", -res.fun)
print("Optimal solution:", res.x)
