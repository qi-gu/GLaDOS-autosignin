# GLaDOS-签到脚本
一个Python签到的脚本，可以加入系统自启目录做到启动时自动签到。
登陆GLaDOS，按F12-`应用程序-存储-cookie-https://glados.rocks/`，复制koa开头两个cookie，分别填入py文件中对应的字典值内。打开clash，将如图中的端口值填入port后的引号内：
![image](https://user-images.githubusercontent.com/50322671/228266971-5f1265ec-8dc9-4837-abf9-b9a06c869f41.png)

双击运行即可签到。
可以将文件移入C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup目录，并将py文件打开方式绑定为python解释器，即可启动时自动签到。
如果不愿意更改py文件打开方式，也可以写一个bat文件放入启动目录，在里面用python启动该文件。
