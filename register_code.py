#coding=utf-8
from selenium import webdriver
import time 
driver=webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)