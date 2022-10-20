# coding=utf-8
import os

# 获取云设备json文件
get_device = 'curl -u c7ba273d5c7f4841bc041f25c74ae38d:caun663mane72o2ent5g "https://api.paas.wetest.net/cloudtest/v1/clouds/5/devices" > /Users/ceshi/PycharmProjects/apiBdd/device/device.json'
if __name__ == '__main__':
    os.popen(get_device)
