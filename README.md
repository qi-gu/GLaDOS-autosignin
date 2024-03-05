# GLaDOS-autosignin
一个Python签到的脚本，可以加入系统自启目录做到启动时自动签到。
登陆GLaDOS，按F12-`应用程序-存储-cookie-https://glados.rocks/`，复制koa开头两个cookie，分别填入py文件中对应的字典值内。假如没有修改代理端口，默认执行即可；否则请自行修改字典proxy内的端口号。

双击运行即可签到。
可以将文件移入C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup目录，并将py文件打开方式绑定为python解释器，即可启动时自动签到。
如果不愿意更改py文件打开方式，也可以写一个bat文件放入启动目录，在里面用python启动该文件。
