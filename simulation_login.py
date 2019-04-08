# import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#chromePath = r'D:\Download\Compressed\Panda_learning-32\chrome\chromedriver.exe'
chrome_options=Options()
chrome_options.add_argument('--headless')
wd = webdriver.Chrome(chrome_options=chrome_options)
#wd = webdriver.Chrome(executable_path= chromePath)
loginUrl = 'http://10.16.0.12:8081/login'
wd.get(loginUrl) #进入登陆界面
wd.find_element_by_xpath('//*[@id="username"]').send_keys('2017110022') #输入用户名
wd.find_element_by_xpath('//*[@id="password"]').send_keys('12344566') #输入密码
wd.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/form/div[2]/div/div/span/button').click() #点击登陆
req = requests.Session() #构建Session
cookies = wd.get_cookies() #导出cookie
for cookie in cookies:
     req.cookies.set(cookie['name'],cookie['value']) #转换cookies
wd.get('http://www.baidu.com')
print(wd.page_source)
wd.quit()
Net_Flag = os.system('ping www.baidu.com -n 1')
print(Net_Flag)
# if Net_Flag:
#     print("Fail")
# else:
#     print("Connect Successfully")