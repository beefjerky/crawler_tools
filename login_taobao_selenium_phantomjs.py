#coding:utf-8
from selenium import webdriver  
import time
headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}

for key, value in enumerate(headers):
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-linux-x86_64/bin/phantomjs')  


driver.get("https://login.taobao.com/member/login.jhtml")
#不扫描登陆
driver.find_element_by_id('J_Quick2Static').click()
driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_password_1").clear()
user = 'xxx'
passwd = 'xxx'
driver.find_element_by_id("TPL_username_1").send_keys(user)  
driver.find_element_by_id("TPL_password_1").send_keys(passwd)  
 
driver.find_element_by_id("J_SubmitStatic").click()
#等待执行完成
#TODO, 可以使用 selenium wait action，不必等待固定时间
time.sleep(15)
cookie = ";".join([item["name"] + "=" + item["value"] +"\n" for item in driver.get_cookies()])  
print cookie
#获取已购买的宝贝
ret = driver.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm")
print driver.page_source.encode('utf-8')
