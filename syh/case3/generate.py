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

# 对于公式 F = ma
# 生成随机的质量 m 和加速度 a 的值
np.random.seed(0)  # 设置随机种子以保证结果可复现
m_values = np.random.uniform(0.1, 10.0, num_samples)  # 质量范围从0.1到10.0
a_values = np.random.uniform(0.1, 5.0, num_samples)   # 加速度范围从0.1到5.0

# 计算力 F
F_values = m_values * a_values

# 创建 DataFrame 并保存到 CSV 文件
df_F = pd.DataFrame({
    'mass': m_values,
    'acceleration': a_values,
    'force': F_values
})
df_F.to_csv(r'syh\case3\data\force_data.csv', index=False)

print("Force data saved to 'force_data.csv'")