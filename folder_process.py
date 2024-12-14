import os
import shutil

import os

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

for result_folder in results_folders:
    folder_delete(result_folder)