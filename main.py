# encoding:utf-8
import ClockIn

# 校园网学号
username = 'xxxxxxxxxx'
# 校园网密码
password = 'xxxxxxxxxx'
# PushPlus个人token
pushplus_token = 'xxxx'

if __name__ == '__main__':
    
    daka = ClockIn.DAKA(username, password, pushplus_token)
    
    for i in range(6):
        result = daka.run()
        if result == True:
            break
    
    if result == True:
        daka.pushplus('打卡成功！')
    else:
        daka.pushplus('打卡失败！')
