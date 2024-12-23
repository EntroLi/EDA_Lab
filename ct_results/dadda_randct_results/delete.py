import os
import shutil

# 获取当前工作目录
root_path = os.getcwd()

# 获取当前文件夹下的所有文件夹
folders = [folder for folder in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, folder))]

# 遍历文件夹
for folder in folders:
    folder_path = os.path.join(root_path, folder)
    
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
