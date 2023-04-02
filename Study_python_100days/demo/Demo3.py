import time
from DBShop.Class import testcase

browser = 'c'
url = r'http:\localhost\dbshop\admin'

t = testcase(browser,url)
t.get_driver()
t.admin_login()
t.content_management()
time.sleep(20)
t.close()
