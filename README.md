# bluecloud

## bluecloud 代理服务查询脚本

在 config.ini 中配置好 username 和 password 后，运行 bluecloud.py 就可以了。
也可以第一次运行时输入用户名和密码，会自动生成 config.ini

## openconnect 配置脚本（for macOS/linux）

若要使用的话，请安装完毕 openconnect，确保你有这个套餐。

运行 connect.py 后，会在代码目录生成一个 openconnect 文件夹，里面按服务器生成了连接脚本，想要连接的话，运行脚本就可以了。用户名和密码都是配置好的，只要用 root 权限执行即可。

openconnect 至少要 6.0 版本，因为需要免输入密码登陆，在 ubuntu 14.04 及以下经 ap-get 是运行不了的。可以将 openconnect 升级到 6.0 (backport)解决，或者 7.0 (daily)。

6.0 版
```bash
sudo add-apt-repository ppa:openconnect/backport
sudo apt-get update
```

7.0 版
```bash
sudo add-apt-repository ppa:openconnect/daily
sudo apt-get update
```

安装 openconnect
```bash
sudo apt-get install openconnect
```
