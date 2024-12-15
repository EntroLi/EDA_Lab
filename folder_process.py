import os
import shutil
import json
import matplotlib.pyplot as plt

root_path = "."  # Root directory path

# Get all folders in the root directory
folders = [f for f in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, f))]

# Filter folders ending with "results"
results_folders = [folder for folder in folders if folder.endswith("results")]

# Print the identified folders
if results_folders:
    print("Folders ending with 'results':")
    for folder in results_folders:
        print(folder)
else:
    print("No folders ending with 'results' found.")

def folder_delete(result_path):
    print(f"Now process with {result_path} :")
    # 获取当前文件夹下的所有文件夹
    folders = [folder for folder in os.listdir(result_path) if os.path.isdir(os.path.join(result_path, folder))]
    count = 0

    # 遍历文件夹
    for folder in folders:
        count+=1
        folder_path = os.path.join(result_path, folder)
        
        # 获取当前文件夹下的所有文件
        files = os.listdir(folder_path)
        
        # 遍历文件
        for file in files:
            # 删除非 result.json 文件
            if file != 'result.json':
                file_path = os.path.join(folder_path, file)
                # 检查是否是文件夹，是的话直接删除文件夹
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted folder: {file_path}")
                else:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

    file_to_delete = "delete.py"

    file_path = os.path.join(result_path, file_to_delete)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File  {file_to_delete}  has been deleted.")
    # else:
    #     print(f"File  {file_to_delete}  not found.")

    file_to_delete = "eval.py"

    file_path = os.path.join(result_path, file_to_delete)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File  {file_to_delete}  has been deleted.")
    # else:
    #     print(f"File  {file_to_delete}  not found.")

    print(f"Found {count} folders here.")

def folder_eval(folder_path):
    adp_list = []
    with open(os.path.join(folder_path, 'invalid_summary.txt'), 'w') as invalid_summary_file:
        for data_dir in os.listdir(folder_path):
            result_json_path = os.path.join(folder_path, data_dir, 'result.json')
            if not os.path.exists(result_json_path):
                continue
            with open(result_json_path, 'r') as f:
                result_json = json.load(f)

            adp = result_json['area'] * result_json['delay']
            adp_list.append((adp, data_dir))

        adp_list.sort()  # 按照 ADP 值排序

        for adp, data_dir in adp_list:
            invalid_summary_file.write(f'ADP: {adp:16.4f}        in  Dir: {data_dir}\n')

    adp_list = []
    with open(os.path.join(folder_path, 'valid_summary.txt'), 'w') as valid_summary_file:
        for data_dir in os.listdir(folder_path):
            result_json_path = os.path.join(folder_path, data_dir, 'result.json')
            if not os.path.exists(result_json_path):
                continue
            with open(result_json_path, 'r') as f:
                result_json = json.load(f)
            if result_json['drv'] != 0:
                continue

            adp = result_json['area'] * result_json['delay']
            adp_list.append((adp, data_dir))
        
        adp_list.sort()  # 按照 ADP 值排序

        if not adp_list:
            valid_summary_file.write("No valid results found in this folder.")
        else:
            for adp, data_dir in adp_list:
                valid_summary_file.write(f'ADP: {adp:16.4f}        in  Dir: {data_dir}\n')

for result_folder in results_folders:
    folder_delete(result_folder)
    folder_eval(result_folder)

def merge_invalid_summaries(root_folder):
    adp_entries = []

    # 读取每个文件夹中的 invalid summary 文件，提取 ADP 值和目录名称
    for folder_name in os.listdir(root_folder):
        if os.path.isdir(os.path.join(root_folder, folder_name)):
            invalid_summary_path = os.path.join(root_folder, folder_name, 'invalid_summary.txt')
            if os.path.exists(invalid_summary_path):
                with open(invalid_summary_path, 'r') as invalid_summary_file:
                    for line in invalid_summary_file:
                        if line.startswith('ADP:'):
                            adp_value = float(line.split()[1])
                            directory_name = line.split()[-1]
                            adp_entries.append((adp_value, directory_name, folder_name))

    # 按照 ADP 值排序
    adp_entries.sort()

    # 写入到合并文件中
    with open(os.path.join(root_folder, 'merged_invalid_summary.txt'), 'w') as merged_file:
        for adp_value, directory_name, source_folder in adp_entries:
            merged_file.write(f'ADP: {adp_value:16.4f}    Source: {source_folder}    in  Dir: {directory_name}        \n')
    
    #Plot Scatter
    # 提取数据
    directory_names = [entry[2] for entry in adp_entries]
    adp_values = [entry[0] for entry in adp_entries]

    # 绘制散点图
    plt.figure(figsize=(12, 8))
    plt.scatter(directory_names, adp_values, color='blue')
    plt.xlabel('Directory Name')
    plt.ylabel('ADP Value')
    plt.title('Scatter Plot of ADP Values by Directory Name')
    plt.xticks(rotation=20)  # 使横坐标标签斜着显示，以免重叠
    plt.grid(True)
    # 保存图片
    plt.savefig(os.path.join(root_path, 'adp_scatter_plot.png'))
    plt.show()

def merge_valid_summaries(root_folder):
    adp_entries = []

    # 读取每个文件夹中的 valid summary 文件，提取 ADP 值和目录名称
    for folder_name in os.listdir(root_folder):
        if os.path.isdir(os.path.join(root_folder, folder_name)):
            valid_summary_path = os.path.join(root_folder, folder_name, 'valid_summary.txt')
            if os.path.exists(valid_summary_path):
                with open(valid_summary_path, 'r') as valid_summary_file:
                    for line in valid_summary_file:
                        if line.startswith('ADP:'):
                            adp_value = float(line.split()[1])
                            directory_name = line.split()[-1]
                            adp_entries.append((adp_value, directory_name, folder_name))

    # 按照 ADP 值排序
    adp_entries.sort()

    # 写入到合并文件中
    with open(os.path.join(root_folder, 'merged_valid_summary.txt'), 'w') as merged_file:
        for adp_value, directory_name, source_folder in adp_entries:
            merged_file.write(f'ADP: {adp_value:16.4f}    Source: {source_folder}    in  Dir: {directory_name}        \n')

merge_invalid_summaries(root_path)
merge_valid_summaries(root_path)