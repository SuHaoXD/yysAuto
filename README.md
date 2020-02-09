# yysAuto
阴阳师PC端自动挂业原火和御灵
```
```  

##更新2020-2-10：

1.已编译成pyc文件，加入cmd参数控制挂机模式，具体看使用方法

2.加入魂十、魂十一模式

##更新2020-2-9：

1.加入被拉悬赏封印检测机制,加入更多随机数，全程自动无压力

2.加入挂日轮参数

3.补充说明：很多参数不通用，需自己调试，游戏窗口与直播窗口均不能最小化

4.参考：屏幕分辨率1920X1080，游戏窗口大小调整至每次生成的截图yys.jpg分辨率为1136X640左右，游戏窗体移动至屏幕左上角对齐

##更新2020-2-8：

1.加入看直播功能 Model第三个参数写入True即可，默认看某鱼直播，需要提前用浏览器随便打开一个直播房间，会在点击开始按钮后切换到浏览器，检测到打完后会再切回来

2.修复随机移动鼠标可能移动到截图点，导致检测错误的bug

##更新：

1.改进了鼠标移动函数，不会瞬移，会模仿人为变速移动

2.加入了挂机时长参数，可以指定挂机时间

```

```  


##使用方法：

目前无图形界面,有bug

1.必须PC客户端，不能模拟器。win10系统清打开设置->系统->显示，将文本缩放调至100%

2.安装python环境，pip安装源所需库（pywin32,numpy,opencv,QT5,pyautogui等）

4.必须将游戏窗口左上角拖至屏幕左上角对齐，且不能把游戏窗口和直播窗口最小化，可以用其他窗口覆盖游戏窗口。用管理员权限打开cmd(必须)，进入代码所在的文件目录

5.执行【python yysAuto.pyc 参数1 参数2 参数3】指令运行脚本，按Ctrl+C键停止
  
  参数1表示挂机模式：
     yulin1:神龙   yulin2:白藏主   yulin3:黑豹    yulin4:朱雀    hun10:魂十   hun11:大蛇悲鸣  rilun:日轮之城
   
  参数2表示挂机时长，以秒计算
  
  参数3表示是否开启直播模式：1表示开启（需要浏览器打开某鱼直播窗口，且不能最小化窗口） 0表示不开启
  
  举例：
  
  python yysAuto.pyc yulin3 5000 1       ###表示挂御灵黑豹5000秒，开启看直播模式
  
  python yysAuto.pyc hun10 10000 0       ###表示挂魂十10000秒，不开启直播模式    

```

```  
##注意事项：

1.cmd输出的第一行分别表示截图次数，点开始无反应次数（3次自动停止），挂机时间（超时自动停止），第二行是截图特征值

2.游戏和浏览器窗口均不能最小化

3.有bug请反馈，欢迎一起交流学习
