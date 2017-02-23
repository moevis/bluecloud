# bluecloud（现更名为 Monocloud）

## bluecloud 代理服务查询脚本

在 config.ini 中配置好 username 和 password 后，运行 bluecloud.py 就可以了。
也可以第一次运行时输入用户名和密码，会自动生成 config.ini

## openconnect 配置脚本（for macOS/linux）

若要使用的话，请安装完毕 openconnect，确保你有这个套餐。

运行 connect.py 后，会在代码目录生成一个 openconnect 文件夹，里面按服务器生成了连接脚本，想要连接的话，运行脚本就可以了。用户名和密码都是配置好的，只要用 root 权限执行即可。可添加参数 1,2,3 来指定运行模式，1 为 smart，2 为 global，3 为 smart-blacklist，默认 smart. **由于脚本里面已经存储了密码，请不要随便传播**。

openconnect 至少要 6.0 版本，因为需要免输入密码登陆，在 ubuntu 14.04 及以下经 apt-get 是运行不了的。可以将 openconnect 升级到 6.0 (backport)解决，或者 7.0 (daily)。

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

### Shadowsocks 配置脚本(for window / linux / macOs)

需要先下载命令行版 shadowsocks，方法为

```pip install shadowsocks```

本脚本还依赖 requests 和 lxml，建议也一并通过 pip 下载。

然后运行 `shadowsocks.py`，将会在目录下生成以你套餐名为名的文件夹，进入文件夹运行脚本即可。本地端口默认1080.

## License
WTFPL
