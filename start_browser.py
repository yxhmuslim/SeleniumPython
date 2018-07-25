#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
EC.title_contains("注册")
email_element=driver.find_element_by_id("register_email")
driver.save_screenshot("e:/imooc.png")
code_element=driver.find_element_by_id("getcode_num")
print(code_element.location)
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("e:/imooc.png")
img=im.crop((left,top,right,height))
img.save("e:/imooc1.png")
print(img)

# email_name=driver.find_element_by_id("register_email")
# for i in range(6):
#     user_email=''.join(random.sample('1234567890abcdefg',8))
#     print(user_email)


#element=driver.find_element_by_class_name("controls")
# locator=(By.CLASS_NAME,"controls")
# WebDriverWait(driver,1).until(EC.visibility_of_any_elements_located(locator))
# email_name=driver.find_element_by_id("register_email")




# print(email_name.get_attribute("placeholder"))
# email_name.send_keys("yxhmuslim@126.com")
# print(email_name.get_attribute("value"))
# driver.close()

#EC.presence_of_all_elements_located()
# driver.find_element_by_id("register_email").send_keys("yxhmuslim@126.com")
# user_name_element_node=driver.find_elements_by_class_name("controls")[1]
# user_name_element=user_name_element_node.find_element_by_class_name("form-control")
# user_name_element.send_keys("yangxiaohua")
# driver.find_element_by_name("password").send_keys("111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(11111)
