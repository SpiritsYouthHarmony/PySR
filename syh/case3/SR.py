import numpy as np
from pysr import PySRRegressor

# 假设CSV文件有表头，使用 genfromtxt 可以跳过表头
data_F = np.genfromtxt(r'syh\case3\data\force_data.csv', delimiter=',', names=True)

# 提取输入特征和目标变量
X_F = np.vstack([data_F['mass'], data_F['acceleration']]).T  # 力的数据集特征
y_F = data_F['force']  # 数据集目标变量


# 对于 F = ma
model_F = PySRRegressor(
    binary_operators=["+", "*"],  # 允许的二元操作符
    unary_operators=["sin", "cos", "exp"],  # 允许的一元操作符
    niterations=40,  # 迭代次数，可以根据需要增加以获得更好的结果
    extra_sympy_mappings={},  # 如果没有自定义运算符，可以保持为空
)

# 训练模型
model_F.fit(X_F, y_F)

print("Force equation:")
print(model_F.sympy())
