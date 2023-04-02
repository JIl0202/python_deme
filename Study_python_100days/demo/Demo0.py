from DBShop.Class import testcase

url = r'http:\localhost\dbshop'
browser = 'c'

test = testcase(browser, url)
test.get_driver()
n = 2

for i in range(n):
    try:
        test.regist(test.random_user(10)[i])

        test.logout()
        test.save_users(test.random_user(10)[i])
    except:
        test.write_log('执行失败')
        raise
test.close()

