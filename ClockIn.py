# encoding:utf-8
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Daka(object):
    def __init__(self, un, pd, token):
        self.url = 'https://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start'
        self.un = un  # GZHU学号
        self.pd = pd  # GZHU密码
        self.token = token  # Pushplus个人token
        # 设置驱动执行路径
        self.service = Service("/usr/local/bin/chromedriver")
        # 设置webdriver不弹窗
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')

    def run(self):
        # 执行打卡
        driver = webdriver.Chrome(service=self.service, options=self.options)
        try:
            driver.get(self.url)
            # 账号登录界面
            driver.find_element(By.ID, 'un').send_keys(self.un)
            driver.find_element(By.ID, 'pd').send_keys(self.pd)
            driver.find_element(By.ID, 'index_login_btn').click()
            time.sleep(3)
            # 疫情上报界面
            driver.find_element(By.XPATH, '//*[@id="preview_start_button"]').click()
            time.sleep(3)
            # 疫情表单填报界面
            # 是否接触过半个月内有疫情重点地区旅居史的人员，点击否
            driver.find_element(By.XPATH, '//*[@name="fieldYQJLsfjcqtbl" and @value="2"]').click()
            # 健康码是否为绿码，点击是
            driver.find_element(By.XPATH, '//*[@name="fieldJKMsfwlm" and @value="1"]').click()
            # 半个月内是否到过疫情重点地区，点击否
            driver.find_element(By.XPATH, '//*[@name="fieldCXXXsftjhb" and @value="2"]').click()
            # 勾选本人填报真实性承诺
            driver.find_element(By.XPATH, '//*[@name="fieldCNS"]').click()
            # 点击提交
            driver.find_element(By.XPATH, '//*[@class="command_button_content"]').click()
            time.sleep(3)
            driver.close()
            result = True
        except Exception:
            result = False
        return result

    def push(self, content):
        # pushplus推送加消息推送接口
        title = '打卡结果'  # 标题内容
        push_url = 'http://www.pushplus.plus/send'
        data = {
            "token": self.token,
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        requests.post(push_url, data=body, headers=headers)
        
