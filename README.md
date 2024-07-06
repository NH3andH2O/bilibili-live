# ***警告: 不要泄露自己的 cookie和 token！如果泄露，请立刻修改b站账号密码！***

## 简介
这个小程式只是为了实现小于50粉丝的up主在直播时获取到推流地址和推流码以便直接在obs上直播，如果你可以直接获取到推流码的话这个程式基本上没有任何用处
## 如何使用
1.打开bilibili_live.exe所在的文件夹，在文件夹空白处按住Shift并单击右键，选择在终端中打开
![](https://github.com/NH3andH2O/bilibili-live/blob/main/png/5.png?raw=true)

2.使用PowerShell，执行bilibili_live.exe

开始直播：

	.\bilibili_live.exe --cookie '你账户的cookie' --token '你账户的token' --room_id 你的房间号 --area 直播分区号 --startlive 

如果成功，你的账号将会开启直播，并且在终端中你可以看到自己账号的推流地址及推流码。将推流地址及推流码复制到obs上，即可使用obs推流直播。
 
结束直播：

 	.\bilibili_live.exe --cookie '你账户的cookie' --token '你账户的token' --room_id 你的房间号 --area 直播分区号 --stoplive

如果成功，你的账号将会结束直播

(如果使用命令行，请把cookie、token参数中的单引号去掉)
## cookie、token、分区号获取

1.使用Google Chrome游览器打开b站web直播平台（https://live.bilibili.com/p/html/web-hime/index.html）

2.选择你要播的分区

3.单击鼠标右键，选择最下面的“检查”，或者按下F12

4.单击“Network”
![](https://github.com/NH3andH2O/bilibili-live/blob/main/png/1.png?raw=true)

5.单击“开始直播”

6.找到“startLive”，右键startLive -> Copy -> Copy as fetch(Node.js),并粘贴到记事本上
![](https://github.com/NH3andH2O/bilibili-live/blob/main/png/2.png?raw=true)
![](https://github.com/NH3andH2O/bilibili-live/blob/main/png/3.png?raw=true)

7.分析代码，你应该可以得到cookie（字符串）、token（字符串）、分区号（2~4位数字）
![](https://github.com/NH3andH2O/bilibili-live/blob/main/png/4.jpg?raw=true)
