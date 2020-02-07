# -*- coding: utf-8 -*-
import win32api
import win32gui
import win32con
import random
import numpy
import cv2
from pymouse import PyMouse
from win32gui import *
from PyQt5.QtWidgets import QApplication
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

def getScreenMean():  # 485 460   635 560   
	img = cv2.imread("yys.jpg")
	# img = img[500:620,960:1100]
	img = img[460:560,485:635]
	cv2.imshow("img",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	print(img.shape)
	f = img[:,:,0]+img[:,:,1]+img[:,:,2]
	return f.mean()

def MouseClick(x1,y1,x2,y2):
	x = random.randint(x1,x2)
	y = random.randint(y1,y2)
	m = PyMouse()
	m.click(x,y)
	print("点击了："+str(x)+","+str(y))

def MouseMove(): #随机移动鼠标
	x = random.randint(10,1300)
	y = random.randint(10,700)
	m = PyMouse()
	m.move(x,y)

def yeyuanhuo(a,handle):#业原火图片特征  开始均值115   结束状态均值116
	i,j = 0,0  #结束画面 左上角 197, 222  右下角 836, 518 开始按钮：971, 549 1068, 646
	while i<a:
		print(i,j)
		time.sleep(random.randint(3,8))
		getGameScreen(handle)
		f = getScreenMean()
		print(f)
		if abs(f-115)<1:  #开始
			MouseClick(971,549,1068,646)
			j +=1
			time.sleep(random.randint(2,4)+random.random())
			MouseMove()
		if abs(f-104)<1:  #结束
			MouseClick(197,222,836,518)
			j = 0
			time.sleep(random.randint(2,4)+random.random())
			MouseMove()
		i +=1
		if j>3: #自动退出机制
			sys.exit(0)

def yulin(a,handle):  #御灵特征开始均值116.9  结束99.78(孔雀)
	i,j = 0,0
	while i<a:
		print(i,j)
		time.sleep(random.randint(3,8)+random.random())
		getGameScreen(handle)
		f = getScreenMean()
		print(f)
		if abs(f-116)<1:  #开始
			MouseClick(971,549,1068,646)
			j +=1
			time.sleep(random.randint(2,4)+random.random())
			MouseMove()
		if abs(f-99)<1:  #结束
			MouseClick(197,434,836,518)
			j = 0
			time.sleep(random.randint(1,3)+random.random())
			MouseMove()
		i +=1
		if j>2:
			sys.exit(0)

if __name__ == '__main__':
	handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	# yeyuanhuo(500,handle)
	# yulin(500,handle)
	# m = PyMouse()   #结束画面 左上角 197, 222  右下角 836, 518 开始按钮：971, 549 1068, 646
	# a = m.position()
	# print(a)
	# MouseClick(300,320,843,518)
	# MouseClick(1071,567,1139,642)
	getGameScreen(handle)
	print(getScreenMean())

