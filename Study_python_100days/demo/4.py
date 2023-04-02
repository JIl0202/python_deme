import time as t  # 导入sleep包
from selenium import webdriver  # 导入web驱动包
from selenium.webdriver.common.by import By  # 导入元素定位包
import sys

url = r'http:\\localhost\dbshop'
# br = webdriver.Chrome()
user_password = '123456'
n, m = 1, 1


def log():
    return t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())


def result(message):
    l = open(r'C:\Users\Administrator\Desktop\log.txt', 'a', encoding='UTF-8')
    l.write("{}\t{}\n".format(log(), message))
    l.close()


def registered(n, m):
    br = webdriver.Chrome()
    br.get(url)
    br.maximize_window()
    br.implicitly_wait(2)
    br.find_element(By.XPATH, r'//* [text() = "注册"]').click()
    br.find_element(By.XPATH, r'//* [@id = "user_name"]').send_keys('tester%d' % n)
    br.find_element(By.XPATH, r'//* [@id = "user_password"]').send_keys(user_password)
    br.find_element(By.XPATH, r'//* [@id = "user_com_passwd"]').send_keys(user_password)
    br.find_element(By.XPATH, r'//* [@id = "user_email"]').send_keys('micsoft%d@outlook.com' % m)
    br.find_element(By.XPATH, r'//* [@id = "agreement"]').click()
    br.find_element(By.XPATH, r'//button').click()
    if br.find_element(By.XPATH, r'//* [text() = "退出"]'):
        result('注册成功')
    t.sleep(5)
    br.quit()


"""
def login ():
    br = webdriver.Chrome()
    br.get(url)   
    br.maximize_window()
    br.implicitly_wait(2)
    br.find_element(By.XPATH,r'//* [text() = "登录"]').click()
    br.find_element(By.XPATH,r'//* [@id = "user_name"]').send_keys(user_name)
    br.find_element(By.XPATH,r'//* [@id = "user_password"]').send_keys(user_password)
    br.find_element(By.XPATH,r'//button [text() = "会员登录"]').click()
    if br.find_element(By.XPATH,r'//* [text() = "退出"]'):
        result('登录成功')
    br.
    t.sleep(5)
    br.quit()
"""

if __name__ == '__main__':
    try:
        for a in range(5):
            registered(n, m)
            n += 1
            m += 1
            t.sleep(5)

    except:
        result('注册失败\t报错代码' + str(sys.exc_info()))
