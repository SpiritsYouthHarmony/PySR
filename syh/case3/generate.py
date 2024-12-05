import numpy as np
import pandas as pd

# 生成数据点的数量
num_samples = 100

# # 对于公式 F = ma
# # 生成随机的质量 m 和加速度 a 的值
# np.random.seed(0)  # 设置随机种子以保证结果可复现
# m_values = np.random.uniform(0.1, 10.0, num_samples)  # 质量范围从0.1到10.0
# a_values = np.random.uniform(0.1, 5.0, num_samples)   # 加速度范围从0.1到5.0

# # 计算力 F
# F_values = m_values * a_values

# # 创建 DataFrame 并保存到 CSV 文件
# df_F = pd.DataFrame({
#     'mass': m_values,
#     'acceleration': a_values,
#     'force': F_values
# })
# df_F.to_csv(r'syh\case3\data\force_data.csv', index=False)

# print("Force data saved to 'force_data.csv'")


# A=1/(100*sin(x^2)+exp(y))
# 设置随机种子以保证结果可复现
np.random.seed(0)

# 生成数据点的数量
num_samples = 1000

# 生成随机的 x 和 y 值
x_values = np.random.uniform(0, 3, num_samples)  # x 的范围从 1 到 10
y_values = np.random.uniform(0, 10, num_samples)    # y 的范围从 1 到 5

# 计算 A 根据给定公式
A_values = np.sin(x_values**2) + 0.05*np.exp(y_values)

# 创建 DataFrame
df = pd.DataFrame({
    'x': x_values,
    'y': y_values,
    'A': A_values
})

# 移除包含 NaN 的行（即那些会导致除以零的异常情况）
df_cleaned = df.dropna()

# 保存到 CSV 文件
df_cleaned.to_csv('syh\case3\data\generated_data.csv', index=False)

print(f"Data generated and saved to 'generated_data.csv' with {len(df_cleaned)} samples.")