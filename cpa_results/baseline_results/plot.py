import os
import json
import matplotlib.pyplot as plt

root_path = os.getcwd()

# 初始化三个空数组
delays = []
areas = []
drvs = []
adps = []
adps_clean = []

# 获取当前文件夹下的所有文件夹
folders = [folder for folder in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, folder))]

# 统计文件夹数目
num = len(folders)

for folder in folders:
    folder_path = os.path.join(root_path, folder)
    
    # 构建result.json文件路径
    json_file_path = os.path.join(folder_path, 'result.json')
    
    # 检查文件是否存在
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            delays.append(data['delay'])
            areas.append(data['area'])
            drvs.append(data['drv'])
            adps.append(data['delay'] * data['area'])
            if data['drv'] == 0:
                adps_clean.append(data['delay'] * data['area'])

# 绘制散点图
plt.figure(figsize=(10, 6))
for i in range(len(delays)):
    if drvs[i] == 0:
        plt.scatter(delays[i], areas[i], color='blue', label='drv = 0')
    else:
        plt.scatter(delays[i], areas[i], color='red', label='drv != 0')
plt.xlabel('Delay')
plt.ylabel('Area')
plt.title('Scatter Plot for Baseline Results')
plt.grid(True)
plt.savefig('baseline_scatter_plot.png')
plt.show()
