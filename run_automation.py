# coding=utf-8
import json
import os
from jsonpath import jsonpath

# 提取json文件中所有的device_id值
with open('./device/device.json') as f:
    data = json.loads(f.read())
device_list = jsonpath(data, '$.devices[*].device_id')


# 列表平均分组函数,[*list]可以将元组转换成列表
def list_group(step, *group):
    group_device = [[*group[i:i + step]] for i in range(0, len(group), step)]
    return group_device


# 将云平台设备分页，每页50台,共10页[0,9]
m = list_group(10, *device_list)
# 将每页的云设备再次分组，每组3台执行自动化测试,要执行哪一页改索引即可[0,50,16]
n = list_group(1, *m[16])
# n = list_group(3, *device_list)
a = 'curl -u c7ba273d5c7f4841bc041f25c74ae38d:caun663mane72o2ent5g --request POST "https://api.paas.wetest.net/cloudtest/v1/tests/automation" -d '
b = '{"login":"none","project":"XWr3B6qz","devices":'
c = ',"cloud_id":5,"script_id":18321,"app_hash_id":"3ye3x3qP","frame_type":"appium","email_notify":false,"device_number":0,"max_test_runtime":7200,"max_device_runtime":600,"device_choose_type":"deviceids"}'
q = "'"
# 拼接提交自动化测试curl命令
d = [f'{a}{q}{b}{n[x]}{c}{q}' for x in range(0, len(n))]
test_id_list = []

if __name__ == '__main__':
    for cu in d:
        # 读取每次curl命令的执行结果
        result = os.popen(cu).readlines()[0]
        print("\r")
        # 提取每次结果的test_id
        test_id = json.loads(result)["test_info"]["test_id"]
        # 将每次的test_id收集起来方便下载测试报告使用
        test_id_list.append(test_id)
    print(test_id_list, len(test_id_list))
