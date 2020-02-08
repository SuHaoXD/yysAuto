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
	x = random.randint(10,1800)
	y = random.randint(10,900)
	t = random.random()+0.2
	pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)

def Auto(T,handle,imgx1,imgy1,imgx2,imgy2,fs,fe):
	i,j = 0,0
	start = time.time()
	while True:
		spend = time.time() - start
		print(i,j,spend)
		if spend > T:
			sys.exit(0)
		time.sleep(random.randint(3,8)+random.random())
		getGameScreen(handle)
		f = getScreenMean(imgx1,imgy1,imgx2,imgy2)
		print(f)
		if abs(f-fs)<0.1:  #开始按钮：971, 549 1068, 646
			MouseClick(971,549,1068,646)
			j +=1
			time.sleep(random.randint(2,4)+random.random())
			MouseMove()
		if abs(f-fe)<0.1:  #结束画面 左上角 197, 222  右下角 836, 518
			MouseClick(197,434,836,518)
			j = 0
			time.sleep(random.randint(1,3)+random.random())
			MouseMove()
		print("")
		i +=1
		if j>2:
			sys.exit(0)


def Model(m,T):
	handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	if m=="yulin1":  #神龙 
		Auto(T,handle,485,460,635,560,114.40,99.7)
	if m=="yulin2":  #白藏主
		Auto(T,handle,485,460,635,560,120.36,99.7)
	if m=="yulin3":	  #黑豹
		Auto(T,handle,485,460,635,560,116.18,99.7)
	if m=="yulin4":	  #孔雀
		Auto(T,handle,485,460,635,560,116.97,99.7)
	if m=="yeyuanhuo":  #业原火
		Auto(T,handle,485,460,635,560,115.75,99.7)
	else:
		print("模式输入错误")
		sys.exit(0)


if __name__ == '__main__':
	Model("yulin4",5000)

	# handle = win32gui.FindWindow(0,"阴阳师-网易游戏")
	# getGameScreen(handle)
	# print(getScreenMean(485,460,635,560))
	# a = pyautogui.position()
	# print(a)

