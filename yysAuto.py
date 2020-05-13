# -*- coding: utf-8 -*-
#author:SuHaoXD
#E-mail:suhaoxd@qq.com
import win32api,win32gui,win32con
import random,threading,time,sys
import numpy
import cv2
import pyautogui
from win32gui import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout,QHBoxLayout,QDesktopWidget

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

def getWinName(a):
	titles = set()
	def foo(hwnd,mouse):  #寻找标题文本
		if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
			titles.add(GetWindowText(hwnd))
	EnumWindows(foo, 0)
	lt = [t for t in titles if t]
	for t in lt:
		if str(a) in t:
			print(t)
			return t

def getGameScreen(handle):
	app = QApplication(sys.argv)
	screen = QApplication.primaryScreen()
	img = screen.grabWindow(handle).toImage()
	img.save("yys.jpg")

def getScreenMean(imgp,show=False):  # 截取位置 
	x1,y1,x2,y2 = imgp[0],imgp[1],imgp[2],imgp[3]
	img = cv2.imread("yys.jpg")
	if img.shape[0]<5:
		return 0
	img = img[y1:y2,x1:x2]
	if show:
		cv2.imshow("img",img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	f = img[:,:,0]+img[:,:,1]+img[:,:,2]
	return f.mean()

# def MouseClick(x1,y1,x2,y2):  #鼠标点击
# 	x = random.randint(x1,x2)
# 	y = random.randint(y1,y2)
# 	t = random.random()+0.2
# 	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInBounce)
# 	time.sleep(random.random())
# 	pyautogui.click()
# 	print("点击了："+str(x)+","+str(y))

def MouseClick(*args):  #鼠标点击
	if len(args)==4:
		x = random.randint(args[0],args[2])
		y = random.randint(args[1],args[3])
		# print(x,y)
	if len(args)==1:
		x = random.randint(args[0][0],args[0][2])
		y = random.randint(args[0][1],args[0][3])
		# print(x,y)
	t = random.random()+0.2
	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInBounce)
	time.sleep(random.random())
	pyautogui.click()
	print("点击了："+str(x)+","+str(y))

def MouseMove():  #随机移动鼠标
	x = random.randint(900,1400)
	y = random.randint(200,700)
	t = random.random()+0.2
	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInBounce)


def SetLive(zhibo,handle):  #获取焦点
	if not zhibo or handle==0:
		return
	win32gui.SetForegroundWindow(handle)


def Auto(T,handle,imgstart,imgend,ts,te,zhibo=False,hzhibo=0,startbutton=(921,526,999,608)):
	i,j,k,l = 1,0,0,0    #截图次数，自动停止参数，战斗完成次数  截图无反应次数
	start = time.time()
	try:
		while True:
			spend = time.time() - start
			spend = round(spend,2)
			print("第"+str(i)+"次截图	",end="")
			print("已完成"+str(k)+"次战斗"+"(设定"+str(T[0])+"次)		",end="")
			print("已挂机"+str(spend)+"秒"+"(设定"+str(T[1])+"秒)")
			if (k>=T[0]) or (spend > T[1]):        #超时停止
				print("已达挂机时长，停止运行")
				print("\a")
				time.sleep(1)
				print("\a")
				time.sleep(1)
				print("\a")
				sys.exit(0)
			time.sleep(random.randint(1,2)+random.random())  #每次截图间隔为随机2秒到4秒之间
			getGameScreen(handle)

			xs = getScreenMean((469,133,580,162))  #检测悬赏，悬赏位置 499,141,646,171
			if abs(xs-154.6)<1:          #特征153.12
			   win32gui.SetForegroundWindow(handle) 
			   time.sleep(random.random())
			   MouseClick(696,361,817,398)     # 点击位置  739,383,854,422
			   continue

			fs = getScreenMean(imgstart)
			fe = getScreenMean(imgend)
			print("特征值:"+ str(fs)+" "+str(fe))

			if (T[0]!=999) and abs(fs-ts)<0.05:  #开始按钮：921,526,999,608  组队模式T0=999
				win32gui.SetForegroundWindow(handle)
				time.sleep(random.random())
				MouseClick(startbutton)
				j +=1
				k +=1
				l = 0
				time.sleep(random.randint(0,2)+random.random())
				MouseMove()  #随机移动鼠标
				time.sleep(random.random())
				SetLive(zhibo,hzhibo)

			if T[0] == 999:  #结算胜利画面
				sl = getScreenMean((360,70,450,150))
				if abs(sl-140.35)<0.05:          
					win32gui.SetForegroundWindow(handle) 
					# time.sleep(random.random())
					MouseClick(30,424,266,539)     # 点击位置  739,383,854,422
					MouseClick(30,424,266,539)
					time.sleep(0.5+random.random())
					MouseClick(30,424,266,539)
					time.sleep(random.random())
					MouseMove()


			if abs(fe-te)<0.05:  #结束画面 
				win32gui.SetForegroundWindow(handle)
				MouseClick(372,475,839,539)
				j,l = 0,0
				time.sleep(1+random.random())
				MouseMove()
			print("")
			i +=1
			l +=1   #截图无操作限制
			if (T[0]!=999) and (j>2 or l>100):   #终止机制，连续点开始按钮3次终止程序
				print("点击开始按钮无响应，停止运行")
				print("\a")
				time.sleep(1)
				print("\a")
				time.sleep(1)
				print("\a")
				sys.exit(0)
	except KeyboardInterrupt:
		print("手动停止")

def Model(m,T,zhibo=False):
	handle = win32gui.FindWindow(0,"阴阳师-网易游戏")   ##窗口大小 1136X640
	win32gui.MoveWindow(handle,-7,0,1136,640,True)

	if handle==0:
		print("未检测到PC端游戏")
		sys.exit(0)

	hzhibo = 0
	if zhibo:
		hzhibo = win32gui.FindWindow(0,getWinName("直播"))
	if m=="yulin1":  #神龙 
		imgstart = (255,455,315,480)    ##89.79
		imgend = (485,460,635,560)
		Auto(T,handle,imgstart,imgend,86.41,89.6,zhibo,hzhibo)
	if m=="yulin2":  #白藏主
		imgstart = (255,455,315,480)    ##89.79
		imgend = (485,460,635,560)
		Auto(T,handle,imgstart,imgend,86.41,89.6,zhibo,hzhibo)
	if m=="yulin3":	  #黑豹
		imgstart = (243,428,294,450)     ##89.79
		imgend = (490,430,570,490)
		Auto(T,handle,imgstart,imgend,97.56,88.34,zhibo,hzhibo)
	if m=="yulin4":	  #孔雀
		imgstart = (245,425,330,450)    ##89.79
		imgend = (485,460,635,560)
		Auto(T,handle,imgstart,imgend,86.41,89.6,zhibo,hzhibo)
	if m=="yeyuanhuo":  #业原火
		imgstart = (233,398,310,423)     ##91.43
		imgend = (490,430,570,490)
		Auto(T,handle,imgstart,imgend,90.088,88.34,zhibo,hzhibo)
	if m=="rilun":  #日轮之城
		imgstart = (243,398,296,423)    ##87.4422
		imgend = (490,430,570,490)
		Auto(T,handle,imgstart,imgend,87.44,88.34,zhibo,hzhibo)
	if m=="hun10":   #魂10
		imgstart = (255,400,315,425)    ##89.79
		imgend = (485,460,635,560)
		Auto(T,handle,imgstart,imgend,89.79,89.6,zhibo,hzhibo)
	if m=="hun11":   #魂11
		imgstart = (255,497,315,523)    ##82.288
		imgend = (490,430,570,490)
		Auto(T,handle,imgstart,imgend,89.45,88.34,zhibo,hzhibo)
	# if m=="zudui":   #自动接组队
	# 	imgstart = (330,190,370,220)    #146.59
	# 	imgend = (490,430,570,490)
	# 	Auto(T,handle,imgstart,imgend,146.59,88.34,zhibo,hzhibo,startbutton=(100,228,139,265))
	if m=="diaoca":
		imgstart = (221,317,244,370)    ##87.4422
		imgend = (490,430,570,490)
		Auto(T,handle,imgstart,imgend,120.42,88.34,zhibo,hzhibo,startbutton=(873,469,939,529))
	else:
		print("模式输入错误")
		sys.exit(0)


def Main():
	if len(sys.argv) != 5:
		print("参数输入错误！")
		sys.exit(0)
	m = sys.argv[1]    #模式
	try:
		t = (int(sys.argv[2]),int(sys.argv[3]))   # 挂机战斗次数和挂机时间
		z = int(sys.argv[4])
	except KeyboardInterrupt:
		print("请输入整数！")
	Model(m,t,z)
# class App(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.title = "自动御灵"
# 		self.left = 10
# 		self.top = 10
# 		self.width = 320
# 		self.height = 200
# 		self.initUI()
# 		self.center()

# 	def center(self):
# 		screen = QDesktopWidget().screenGeometry()
# 		size = self.geometry()
# 		self.move((screen.width() - size.width()) / 2,  
#         (screen.height() - size.height()) / 2)

# 	def initUI(self):
# 		self.setWindowTitle(self.title)
# 		self.setGeometry(self.left, self.top, self.width, self.height)
# 		w = QVBoxLayout(self)
# 		byyh = QPushButton('业原火',self)
# 		byl1 = QPushButton('御灵青龙',self)
# 		byl2 = QPushButton('御灵白藏主',self)
# 		byl3 = QPushButton('御灵黑豹',self)
# 		byl4 = QPushButton('御灵朱雀',self)
# 		bexit = QPushButton('退出',self)
# 		w.addWidget(byyh)
# 		w.addWidget(byl1)
# 		w.addWidget(byl2)
# 		w.addWidget(byl3)
# 		w.addWidget(byl4)
# 		w.addWidget(bexit)
# 		byyh.clicked.connect(self.yyh)
# 		byl1.clicked.connect(self.yl1)
# 		byl2.clicked.connect(self.yl2)
# 		byl3.clicked.connect(self.yl3)
# 		byl4.clicked.connect(self.yl4)
# 		bexit.clicked.connect(self.ex)

# 	def yyh(self):
# 		Model("yeyuanhuo",5000)

# 	def yl1(self):
# 		Model("yulin1",5000)

# 	def yl2(self):
# 		Model("yulin2",5000)

# 	def yl3(self):
# 		Model("yulin3",5000)

# 	def yl4(self):
# 		Model("yulin4",5000)

# 	def ex(self):
# 		sys.exit(0)

if __name__ == '__main__':
	Main() 

	# MouseClick(221,317,244,370)
	# Model("rilun",2000)
	# print(120.63386666666666-120.0)
	# MouseClick(971,549,1068,646)
	# app = QApplication(sys.argv)
	# A = App()
	# A.show()
	# sys.exit(app.exec_())
	# handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	# hzhibo = win32gui.FindWindow(0,getWinName("斗鱼"))
	# win32gui.SetForegroundWindow(hzhibo)
	# print(getWinName("斗鱼"))
	# print(hzhibo)

	# # ##
	# handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	# getGameScreen(handle)
	# P = (360,70,450,150)
	# print(getScreenMean(P,1))    

	# print(int(sys.argv[2]))
	# print(win32gui.GetWindowRect(handle))
	# a = pyautogui.position()  
	# print(a)