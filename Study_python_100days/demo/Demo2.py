import time
from DBShop.Class import testcase

browser = 'c'
url = r'http:\localhost\dbshop\admin'

test = testcase(browser,url)
print('实例化成功')
test.get_driver()
# test.headless()
print('打开网页成功,开始执行登录')
test.admin_login()
print('登录成功,开始执行勾选操作')
test.Products()
print('勾选操作已完成')
time.sleep(5)
print('等待5秒已完成,关闭浏览器')
test.close()



