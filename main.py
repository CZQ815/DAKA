# -*- coding:utf-8 -*-
import ClockIn

# 校园网学号
username = 'xxxxxxxxxx'
# 校园网密码
password = 'xxxxxxxxxx'
# PushPlus个人token
token = 'xxxxxxxxxxxxx'
    
person = ClockIn.Daka(username, password, token)

for i in range(6):
    res = person.run()
    if res:
        break

if res:
    person.push('打卡成功！')
else:
    person.push('打卡失败！')
