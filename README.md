# 1、下载代码

```shell
~$ git clone https://github.com/CZQ815/DAKA.git && cd DAKA
```

# 2、安装所需软件

```shell
~/DAKA$ sudo apt update && sudo apt upgrade
~/DAKA$ sudo apt install unzip  # 如已安装，请忽略
~/DAKA$ sudo apt install python3-pip  # 如已安装，请忽略
```

# 3、安装依赖

```shell
~/DAKA$ pip3 install -r requirements.txt
```

# 4、服务器安装chrome

```shell
~/DAKA$ sudo apt-get install libxss1 libappindicator1 libindicator7  # 安装chrome依赖
~/DAKA$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  # 拉取最新稳定版google-chrome
~/DAKA$ sudo apt-get -f install
~/DAKA$ sudo dpkg -i google-chrome*.deb
~/DAKA$ rm google-chrome-stable_current_amd64.deb && google-chrome --version  # 查看所安装google-chrome版本
```

（当前最新稳定版为96.0.4664.110）

# 5、服务器安装驱动chromedriver

chromedriver须与google-chrome版本一致，所提供的驱动版本为96.0.4664.45

(目前来看，与110的google-chrome能兼容，但后期最好将版本统一)

1）若版本与第3步所下google-chrome版本一致，直接授予可执行权限即可。

```shell
~/DAKA$ sudo chmod +x chromedriver && sudo cp ./chromedriver /usr/local/bin
```

2）若版本不一致，下载对应驱动的方法如下：

```shell
# 先打开网页https://registry.npmmirror.com/binary.html?path=chromedriver/，查找并复制对应版本的下载链接
~/DAKA$ cd /usr/local/bin && wget http://npm.taobao.org/mirrors/chromedriver/96.0.4664.45/chromedriver_linux64.zip
/usr/local/bin$ unzip chromedriver_linux64.zip && sudo chmod +x chromedriver && rm chromedriver_linux64.zip
```

# 6、注册推送加

打开网页http://www.pushplus.plus/ 或者关注微信公众号“pushplus 推送加”，注册账号并激活消息，保存个人token。

# 7、修改信息

修改`main.py`文件里的用户名、密码和个人token。

# 8、设置Linux自带定时任务

例：设置每日早上8:15打卡如下

```shell
~/DAKA$ pwd  # 查看main.py所在路径
~/DAKA$ sudo vi /etc/crontab
# 文末添加定时任务
15 8 * * * user-name python3 PATH/main.py  # user-name为主机当前用户名，PATH为main.py所在路径，保存并退出
```
