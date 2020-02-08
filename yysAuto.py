#author:SuHaoXD
#E-mail:suhaoxd@qq.com
# -*- coding: utf-8 -*-
import win32api
import win32gui
import win32con
import random
import numpy
import cv2
import pyautogui
from win32gui import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QVBoxLayout,QHBoxLayout,QDesktopWidget
from PyQt5.QtGui import *
import sys
import time

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

def getScreenMean(x1,y1,x2,y2):  # 截取位置 一般 485 460 635 560   
	img = cv2.imread("yys.jpg")
	img = img[y1:y2,x1:x2]
	# cv2.imshow("img",img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	# print(img.shape)
	f = img[:,:,0]+img[:,:,1]+img[:,:,2]
	return f.mean()

def MouseClick(x1,y1,x2,y2):  #鼠标点击
	x = random.randint(x1,x2)
	y = random.randint(y1,y2)
	t = random.random()+0.2
	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
	pyautogui.click()
	print("点击了："+str(x)+","+str(y))

def MouseMove():  #随机移动鼠标
	x = random.randint(900,1900)
	y = random.randint(10,1000)
	t = random.random()+0.2
	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)



def SetLive(zhibo,handle):  #获取焦点
	if not zhibo or handle==0:
		return
	win32gui.SetForegroundWindow(handle)

def Auto(T,handle,imgx1,imgy1,imgx2,imgy2,fs,fe,zhibo=False,hzhibo=0):
	i,j = 0,0
	start = time.time()
	while True:
		spend = time.time() - start
		print(i,j,spend)
		if spend > T:
			sys.exit(0)
		time.sleep(random.randint(3,8)+random.random())  #每次截图间隔为随机3秒到8秒之间
		getGameScreen(handle)
		f = getScreenMean(imgx1,imgy1,imgx2,imgy2)
		print(f)
		if abs(f-fs)<0.1:  #开始按钮：971, 549 1068, 646
			win32gui.SetForegroundWindow(handle)
			time.sleep(random.random())
			MouseClick(971,549,1068,646)
			j +=1
			time.sleep(random.randint(1,3)+random.random())
			MouseMove()  #随机移动鼠标
			time.sleep(random.random())
			SetLive(zhibo,hzhibo)
		if abs(f-fe)<0.1:  #结束画面 左上角 197, 222  右下角 836, 518
			win32gui.SetForegroundWindow(handle)
			MouseClick(197,434,836,518)
			j = 0
			time.sleep(1+random.random())
			MouseMove()
		print("")
		i +=1
		if j>2: 
			sys.exit(0)


def Model(m,T,zhibo=False):
	handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	if zhibo:
		hzhibo = win32gui.FindWindow(0,getWinName("斗鱼"))

	if m=="yulin1":  #神龙 
		Auto(T,handle,485,460,635,560,114.40,99.7,zhibo,hzhibo)
	if m=="yulin2":  #白藏主
		Auto(T,handle,485,460,635,560,120.36,99.7,zhibo,hzhibo)
	if m=="yulin3":	  #黑豹
		Auto(T,handle,485,460,635,560,116.18,99.7,zhibo,hzhibo)
	if m=="yulin4":	  #孔雀
		Auto(T,handle,485,460,635,560,116.97,99.7,zhibo,hzhibo)
	if m=="yeyuanhuo":  #业原火
		Auto(T,handle,485,460,635,560,115.75,99.7,zhibo,hzhibo)
	else:
		print("模式输入错误")
		sys.exit(0)

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
	Model("yulin4",5000,True)


	# app = QApplication(sys.argv)
	# A = App()
	# A.show()
	# sys.exit(app.exec_())
	# handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	# hzhibo = win32gui.FindWindow(0,getWinName("斗鱼"))
	# win32gui.SetForegroundWindow(hzhibo)
	# print(getWinName("斗鱼"))
	# print(hzhibo)
	# print(getScreenMean(485,460,635,560))
	# a = pyautogui.position()
	# print(a)

