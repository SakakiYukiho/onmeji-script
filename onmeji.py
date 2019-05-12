# coding=utf-8

import time
import win32api, win32gui, win32con, win32gui, win32ui
from ctypes import *
import numpy as np
import random
import cv2
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pyautogui

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
    
    time.sleep(10)
    # 阴阳寮相对坐标
    yyl_left = left + 468
    yyl_top = top + 730
    # 移动鼠标单击
    move_cursor(yyl_left, yyl_top)
    cursor_left_click()

    time.sleep(10)

    # 打开结界
    jj_left = left + 1110
    jj_top = top + 690
    move_cursor(jj_left, jj_top)
    cursor_left_click()

    time.sleep(10)

    # 打开寿司盒
    sushi_left = left + 1085
    sushi_top = top + 526
    move_cursor(sushi_left, sushi_top)
    cursor_left_click()

    time.sleep(10)

    # 把寿司拉到最大
    max_sushi_left = left + 1050
    max_sushi_top = top + 500
    move_cursor(max_sushi_left, max_sushi_top)
    cursor_left_click()

    time.sleep(10)

    # 取出寿司
    get_sushi_left = left + 730
    get_sushi_top = top + 620
    move_cursor(get_sushi_left, get_sushi_top)
    cursor_left_click()
 
    time.sleep(10)

    # 随机点击
    random_left = left + random.randint(100, 300)
    random_top = top + random.randint(300, 700)
    move_cursor(random_left, random_top)
    cursor_left_click()

    time.sleep(10)

    # 退出寿司盒
    exit_sushi_left = left + 1125
    exit_sushi_top = top + 200
    move_cursor(exit_sushi_left, exit_sushi_top)
    cursor_left_click()

    time.sleep(10)

    # 退出结界
    exit_jj_left = left + 60
    exit_jj_top = top + 60
    move_cursor(exit_jj_left, exit_jj_top)
    cursor_left_click()

    time.sleep(30)

    # 退出阴阳寮
    exit_yyl_left = left + 1325
    exit_yyl_top = top + 95
    move_cursor(exit_yyl_left, exit_yyl_top)
    cursor_left_click()

    time.sleep(10)

def auto_receive_sushi():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)

    time.sleep(10)
    # 领取体力
    gy_left = left + 865
    gy_top = top + 560
    move_cursor(gy_left, gy_top)
    cursor_left_click()

def auto_wish():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)
    
    time.sleep(10)
    # 阴阳寮相对坐标
    yyl_left = left + 468
    yyl_top = top + 730
    # 移动鼠标单击
    move_cursor(yyl_left, yyl_top)
    cursor_left_click()

    time.sleep(10)
    
    # 点击祈愿
    wish_left = left + 1370
    wish_top = top + 360
    move_cursor(wish_left, wish_top)
    cursor_left_click()
    time.sleep(10)

    # 点击碎片
    sp_left = left + 1104
    sp_top = top + 708
    move_cursor(sp_left, sp_top)
    cursor_left_click()
    time.sleep(10)

    # 选卡
    # 截图
    filename = "wish.jpg"
    window_capture(filename)
    # 读取截图文件
    srcimg = cv2.imread(filename)
    # 读取目标文件
    target_img = cv2.imread("want.jpg")
    target_img_gray = cv2.cvtColor(target_img, cv2.cv2.COLOR_BGR2GRAY)
    src_img_gray = cv2.cvtColor(srcimg, cv2.cv2.COLOR_BGR2GRAY)
    w= target_img.shape[0]
    h = target_img.shape[1]
    res = cv2.matchTemplate(src_img_gray, target_img_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    drag_left = left + 716
    drag_top = top + 680
    i = 1
    while len(loc[0]) == 0 and len(loc[1]) == 0 and i <= 5:
        move_cursor(drag_left, drag_top)
        pyautogui.dragTo(left + 810, top + 180, 2, button='left')
        move_cursor(drag_left, drag_top)
        window_capture(filename)
        # 读取截图文件
        srcimg = cv2.imread(filename)
        src_img_gray = cv2.cvtColor(srcimg, cv2.cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(src_img_gray, target_img_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        i = i + 1
        print(i)

    if len(loc[0]) == 0 or len(loc[1]) == 0:
        pass
    # 找到要祈愿的卡
    move_cursor(int(loc[1][0]) + random.randint(20, w - 50), int(loc[0][0]) + random.randint(20, h - 50))
    cursor_left_click()
    
    time.sleep(10)

    # 确定
    move_cursor(left+868, top+480)
    cursor_left_click()

    time.sleep(10)

    # 退出
    move_cursor(left+1322, left+94)
    cursor_left_click()
    time.sleep(10)

    # for pt in zip(*loc[::-1]): 
    #     cv2.rectangle(srcimg, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
    # cv2.imshow('Detected',srcimg)
    # cv2.waitKey (0)



    # 解决弹窗 边缘ob
    # random_left = left + random.randint(50, 100)
    # random_top = top + random.randint(50, 300)
    # move_cursor(random_left, random_top)
    # cursor_left_click()

    time.sleep(10)

# 刷新
# 实际上就是先进入町中然后再进入庭院
# 可以刷新人物位置 刷新签到等
def auto_refresh():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)
    time.sleep(10)

    refresh_left = left + 850
    refresh_top = top + 329
    move_cursor(refresh_left, refresh_top)
    cursor_left_click()

    time.sleep(30)

    exit_left = left + 1200
    exit_top = top + 300
    move_cursor(exit_left, exit_top)
    cursor_left_click()

    time.sleep(10)


# 自动签到
def auto_check():
    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)
    time.sleep(10)

    check_left = left + 310
    check_top = top + 497
    move_cursor(check_left, check_top)
    cursor_left_click()

    time.sleep(10)

    press_left = left + 742
    press_top = top + 322
    move_cursor(press_left, press_top)
    cursor_left_click()

    # 可能弹出动画
    time.sleep(30)

    random_left = left + random.randint(100, 300)
    random_top = top + random.randint(100, 300)
    move_cursor(random_left, random_top)
    cursor_left_click()

    time.sleep(10)

    close_left = left + 1000
    close_top = top + 132
    move_cursor(close_left, close_top)
    cursor_left_click()

    time.sleep(10)


def auto_receive_gy():
    time.sleep(10)

    onmeji_hwnd = get_hwnd_of_onmeji()
    left, top, right, bottom = win32gui.GetWindowRect(onmeji_hwnd)

    gy_left = left + 855
    gy_top = top + 555
    move_cursor(gy_left, gy_top)
    cursor_left_click()

    time.sleep(10)

    random_left = left + random.randint(100, 300)
    random_top = top + random.randint(100, 300)
    move_cursor(random_left, random_top)
    cursor_left_click()
    
    time.sleep(10)

def print_hello():
    print("hello, world")

if __name__ == "__main__":
    # window_capture("233.bmp")
    # sched = BlockingScheduler()

    # 每天六点半定时收体力
    sched.add_job(auto_get_sushi, 'cron', hour=6, minute=30)
    # 每天八点定时收勾玉
    sched.add_job(auto_receive_gy, 'cron', hour=8, minute=0)
    # 每隔1小时自动刷新
    sched.add_job(auto_refresh, 'cron', minute=10)
    # 每天7点定时祈愿
    sched.add_job(auto_wish, 'cron', hour=7)
    # # 每天5点半定时签到
    sched.add_job(auto_check, 'cron', hour=5, minute=30)
    sched.start()
    # pyautogui.dragTo(30, 0, 2, button='left')
    