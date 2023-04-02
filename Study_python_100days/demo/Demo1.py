from DBShop.Class import testcase

browser = 'c'
url = r'http://localhost/dbshop/'
url_1 = r'http://localhost/dbshop/admin'
name = 'tester1'
password = '123456'

test = testcase(browser, url)
test.get_driver()
test.login(name, password)
orderid = test.order_active_1()
test.close()

test = testcase(browser, url_1)
test.get_driver()
test.admin_login()
test.admin_active_2(orderid)
test.close()

test = testcase(browser, url)
test.get_driver()
test.login(name, password)
res = test.order_active_2(orderid)

