import os
import json

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
            adps.append(data['delay']*data['area'])
            if(data['drv'] == 0):
                adps_clean.append(data['delay']*data['area'])


# 输出 delays 数组的大小
# print("Size of delays array:", len(delays))
# print(num)
# print("Delays:", delays)
# print("Areas:", areas)
# print("Drvs:", drvs)
# print("Adps:", adps)

# 计算最小值、最大值和平均值
min_delay = min(delays)
max_delay = max(delays)
avg_delay = sum(delays) / len(delays)

min_area = min(areas)
max_area = max(areas)
avg_area = sum(areas) / len(areas)

min_drv = min(drvs)
max_drv = max(drvs)
avg_drv = sum(drvs) / len(drvs)

min_adp = min(adps)
max_adp = max(adps)
avg_adp = sum(adps) / len(adps)

num_clean = len(adps_clean)

min_adp_clean = min(adps_clean)
max_adp_clean = max(adps_clean)
avg_adp_clean = sum(adps_clean) / len(adps_clean)

# 将结果写入文件
with open('baseline_result.txt', 'w') as f:
    f.write(f"Here are all {num} testcases:\n")
    f.write(f"Min Delay: {min_delay}\n")
    f.write(f"Max Delay: {max_delay}\n")
    f.write(f"Avg Delay: {avg_delay}\n\n")
    f.write(f"Min Area: {min_area}\n")
    f.write(f"Max Area: {max_area}\n")
    f.write(f"Avg Area: {avg_area}\n\n")
    f.write(f"Min Drv: {min_drv}\n")
    f.write(f"Max Drv: {max_drv}\n")
    f.write(f"Avg Drv: {avg_drv}\n\n")
    f.write(f"Min Adp: {min_adp}\n")
    f.write(f"Max Adp: {max_adp}\n")
    f.write(f"Avg Adp: {avg_adp}\n\n")
    f.write(f"Here are {num_clean} clean testcases:\n")
    f.write(f"Min Adp: {min_adp_clean}\n")
    f.write(f"Max Adp: {max_adp_clean}\n")
    f.write(f"Avg Adp: {avg_adp_clean}\n\n")
print("Results saved in baseline_result.txt")