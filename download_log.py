# coding=utf-8
import os

# 此变量为run_automation.py文件中的test_id_list值
list_test_id = [2022102000683505, 2022102000883507, 2022102000983508, 2022102000083509, 2022102000183510,
                2022102000283511, 2022102000483513, 2022102000883517, 2022102000083519, 2022102000183520,
                2022102000883527, 2022102000283531, 2022102000483533, 2022102000683535, 2022102000983538,
                2022102000083539, 2022102000183540, 2022102000283541, 2022102000583544, 2022102000683545]

a = 'curl -u c7ba273d5c7f4841bc041f25c74ae38d:caun663mane72o2ent5g "https://api.paas.wetest.net/cloudtest/v1/tests/'
b = '/devices?log=true" > /Users/ceshi/PycharmProjects/apiBdd/log/'
c = '.json'
z = [f'{a}{i}{b}{i}{c}' for i in list_test_id]

if __name__ == '__main__':
    # 下载每次test_id对应的json文件
    for j in z:
        result = os.popen(j).readlines()
        print("\r")
