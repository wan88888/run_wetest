# coding=utf-8
import os
import json
from jsonpath import jsonpath

data1 = []
path1 = './log/'
files1 = os.listdir(path1)
for file in files1:
    filepath = f'{path1}{file}'
    with open(filepath) as f2:
        js1 = json.loads(f2.read())
        data1.append(js1)
device_id = [jsonpath(data1[i], '$.devices[*].device_id') for i in range(0, len(data1))]
new_device_id = [x for e in device_id for x in e]
mobile_url = [jsonpath(data1[j], '$.devices[*].mobile_log_url') for j in range(0, len(data1))]
new_mobile_url = [y for g in mobile_url for y in g]
non_mobile_url = list(filter(None, new_mobile_url))
merge_dict = dict(zip(new_device_id, new_mobile_url))
left_device = [key for key, value in merge_dict.items() if value == '']
