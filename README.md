# bluecloud（现更名为 Monocloud）

## bluecloud 代理服务查询脚本

在 config.ini 中配置好 username 和 password 后，运行 bluecloud.py 就可以了。
也可以第一次运行时输入用户名和密码，会自动生成 config.ini

### Shadowsocks 配置脚本(for window / linux / macOs)

需要先下载命令行版 shadowsocks ,还有 lxml 和 requests 库，方法为

```pip install shadowsocks requests lxml```

然后运行 `shadowsocks.py`，将会在目录下生成以你套餐名为名的文件夹，进入文件夹运行脚本即可。本地端口默认1080.

## License
WTFPL
