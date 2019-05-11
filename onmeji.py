# coding=utf-8

import time
import win32api, win32gui, win32con, win32gui, win32ui
from ctypes import *
import numpy
import random
import cv2

def move_cursor(x, y):
    windll.user32.SetCursorPos(x, y)

def cursor_left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_cursor_position():
    return win32gui.GetCursorPos()

def get_child_windows(parent):        
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''     
    if not parent:         
        return      
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    return hwndChildList 

def get_hwnd_of_onmeji():
    hwnd_of_blue_stacks = win32gui.FindWindow(0, u'BlueStacks')
    hwnds = get_child_windows(hwnd_of_blue_stacks)
    hwnd = 0
    for h in hwnds:
        text = win32gui.GetWindowText(h)
        if text == u"_ctl.Window":
            hwnd = h
            break 
    return hwnd


def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)



def auto_get_sushi():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)
    
    time.sleep(5)
    # 阴阳寮相对坐标
    yyl_left = left + 468
    yyl_top = top + 730
    # 移动鼠标单击
    move_cursor(yyl_left, yyl_top)
    cursor_left_click()

    time.sleep(5)

    # 打开结界
    jj_left = left + 1110
    jj_top = top + 690
    move_cursor(jj_left, jj_top)
    cursor_left_click()

    time.sleep(5)

    # 打开寿司盒
    sushi_left = left + 1085
    sushi_top = top + 526
    move_cursor(sushi_left, sushi_top)
    cursor_left_click()

    time.sleep(5)

    # 把寿司拉到最大
    max_sushi_left = left + 1050
    max_sushi_top = top + 500
    move_cursor(max_sushi_left, max_sushi_top)
    cursor_left_click()

    time.sleep(5)

    # 取出寿司
    get_sushi_left = left + 730
    get_sushi_top = top + 620
    move_cursor(get_sushi_left, get_sushi_top)
    cursor_left_click()
 
    time.sleep(5)

    # 随机点击
    random_left = left + random.randint(100, 300)
    random_top = top + random.randint(300, 700)
    move_cursor(random_left, random_top)
    cursor_left_click()

    time.sleep(5)

    # 退出寿司盒
    exit_sushi_left = left + 1125
    exit_sushi_top = top + 200
    move_cursor(exit_sushi_left, exit_sushi_top)
    cursor_left_click()

    time.sleep(5)

    # 退出结界
    exit_jj_left = left + 60
    exit_jj_top = top + 60
    move_cursor(exit_jj_left, exit_jj_top)
    cursor_left_click()

    time.sleep(10)

    # 退出阴阳寮
    exit_yyl_left = left + 1325
    exit_yyl_top = top + 95
    move_cursor(exit_yyl_left, exit_yyl_top)
    cursor_left_click()

    time.sleep(5)

def auto_receive_sushi():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)

    time.sleep(5)
    # 领取体力
    gy_left = left + 865
    gy_top = top + 560
    move_cursor(gy_left, gy_top)
    cursor_left_click()

def auto_wish():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)
    
    time.sleep(5)
    # 阴阳寮相对坐标
    yyl_left = left + 468
    yyl_top = top + 730
    # 移动鼠标单击
    move_cursor(yyl_left, yyl_top)
    cursor_left_click()

    time.sleep(5)
    
    # 点击祈愿
    wish_left = left + 1370
    wish_top = top + 360
    move_cursor(wish_left, wish_top)
    cursor_left_click()
    time.sleep(5)

    # 解决弹窗 边缘ob
    random_left = left + random.randint(50, 100)
    random_top = top + random.randint(50, 300)
    move_cursor(random_left, random_top)
    cursor_left_click()

    time.sleep(5)


if __name__ == "__main__":
    # window_capture("233.bmp")
   pass
    
    