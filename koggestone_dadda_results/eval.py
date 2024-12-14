import json
import os

# 获取当前工作目录
folder_path = os.getcwd()

def eval_results(drv_clean=True) -> float:
    """
        Evaluate the results from the experiment, we use Area-Delay Product (ADP) as final metric
    """
    best_adp = float('inf')
    best_dir = None

    for data_dir in os.listdir(folder_path):
        result_json_path = os.path.join(folder_path, data_dir, 'result.json')
        if not os.path.exists(result_json_path):
            continue
        with open(result_json_path, 'r') as f:
            result_json = json.load(f)

        if drv_clean and result_json['drv'] != 0:
            print(f'Dir: {data_dir} Invalid')
            continue

        adp = result_json['area'] * result_json['delay']
        print(f'Dir: {data_dir} with ADP: {adp}')
        best_adp = min(best_adp, adp)
        if adp == best_adp:
            best_dir = data_dir

    return best_adp, best_dir

if __name__ == '__main__':
    best_adp, best_dir = eval_results()
    print(f'Best ADP: {best_adp}')
    print(f'Best Directory: {best_dir}')