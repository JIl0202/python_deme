import time
from DBShop.Class import testcase

browser = 'c'
url = r'http:\localhost\dbshop'
url1 = r'http:\localhost\dbshop\admin'
name = 'tester1'
password = '123456'

try:
    t = testcase(browser, url)
    t.get_driver()
    t.login(name, password)
    t.evaluation()
    t.close()

    t = testcase(browser, url1)
    t.get_driver()
    t.admin_login()
    r = t.admin_evaluation()

    if r:
        t.write_log('评价功能测试成功')
    else:
        t.write_log('评价功能测试失败')
    time.sleep(5)
    t.close()
except:
    print('执行出错')
