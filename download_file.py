# coding=utf-8
import os
import json
import requests
from jsonpath import jsonpath

data = []
path = './log/'
files = os.listdir(path)
for file in files:
    filepath = f'{path}{file}'
    with open(filepath) as f1:
        js = json.loads(f1.read())
        data.append(js)

# 提取每个json文件里的device_id值
device_id = [jsonpath(data[i], '$.devices[*].device_id') for i in range(0, len(data))]
# 拆解多重列表
new_device_id = [di for e in device_id for di in e]
# 提取每个json文件里的mobile_log_url值
mobile_log = [jsonpath(data[i], '$.devices[*].mobile_log_url') for i in range(0, len(data))]
new_mobile_log = [ml for g in mobile_log for ml in g]
# 合并两个列表为字典
merge_dict = dict(zip(new_device_id, new_mobile_log))
# 将超时未执行的设备号保存为新列表
time_out_devices = [key for key, value in merge_dict.items() if value == '']
print(sorted(time_out_devices), len(time_out_devices))
# 过滤列表中的空字符
non_empty_log = list(filter(None, new_mobile_log))
# 获取url里的文件名
text = [os.path.basename(non_empty_log[i]) for i in range(0, len(non_empty_log))]
# 获取文件名里?的索引
que = [text[i].index("?") for i in range(0, len(text))]
# 替换文件名中%2F为_
new_text = [text[k][:que[0]].replace("%2F", "_") for k in range(0, len(text))]
# 将文件名和保存路径组成新列表
save_dir = '/Users/ceshi/Downloads/DeviceLog/'
new_save_path = [f'{save_dir}{new_text[k]}' for k in range(0, len(new_text))]


def download_url(url, save_path, chunk_size=1024):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


if __name__ == '__main__':
    # 同时循环多个列表
    for u, f in zip(non_empty_log, new_save_path):
        download_url(u, f)
