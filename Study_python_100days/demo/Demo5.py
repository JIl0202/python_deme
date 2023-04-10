import time

from DBShop.Class import testcase

browser = 'c'
url = r'http://localhost/dbshop/admin'

t1 = time.time()
t = testcase(browser, url)
t.get_driver()
t.admin_login()
a, b = t.change_price()
if str(a) == b:
    t.write_log('修改操作执行成功,修改后价格为%s' % b)
else:
    t.write_log('修改操作执行失败')

t.close()
t2 = time.time()
print('执行用时总计%.2f' % (t2 - t1))
