import time
import unittest
from appium import webdriver


class MyTests(unittest.TestCase):

    # 测试开始前执行的方法
    @classmethod
    def setUpClass(self):
        print("我是前置脚本, 即将开始跑自动化用例\n")
        a = {'platformName': 'Android',  # 平台名称
             'platformVersion': '7.1.1',  # 系统版本号
             'deviceName': 'emulator-5554',  # 设备名称。如果是真机，adb devices里查看
             'appPackage': 'com.seafile.seadroid2',  # apk的包名
             'appActivity': '.ui.activity.BrowserActivity',  # activity 名称
             'sessionOverride': 'true',  # 每次启动时覆盖session，否则第二次后运行会报错不能新建session
             'unicodeKeyboard': 'true',  # 设置为标准键盘，这样不会因为厂商键盘导致输入编码格式不兼容
             'resetKeyboard': 'false',  # 设置不重启键盘，免得又使用默认的厂商键盘了
             'noSign': 'true',  # nosign和noreset是配合使用，设置app不要弹出首次启动的欢迎页面，确保可以直接打开首页
             'noReset': 'true',  # 同上
             }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", a, keep_alive=True)  # 连接Appium
        self.driver.implicitly_wait(10)

    # 测试结束后执行的方法
    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print("我是后置脚本, 自动化用例即将结束\n")
        self.driver.quit()
        print("webdrive已释放成功")

    # 场景1登录
    def test_1(self):
        time.sleep(2)
        print("登录测试")
        def panduan(self):
            #获取当前页面源码
            source = self.driver.page_source
            #判断当前页面中是否存在未登录页面元素
            if '欢迎使用Seafile' in source:
                self.driver.find_element_by_id("com.seafile.seadroid2:id/account_footer_btn").click()
                self.driver.find_element_by_xpath(
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
                self.driver.find_element_by_id("com.seafile.seadroid2:id/server_url").send_keys("42.192.62.88:80/")
                self.driver.find_element_by_id("com.seafile.seadroid2:id/email_address").click()
                self.driver.find_element_by_id("com.seafile.seadroid2:id/email_address").send_keys('hexuan@micsoft.com')
                self.driver.find_element_by_id("com.seafile.seadroid2:id/email_address").click()
                self.driver.find_element_by_id("com.seafile.seadroid2:id/password").click()
                self.driver.find_element_by_id("com.seafile.seadroid2:id/password").send_keys('123456')
                self.driver.find_element_by_id("com.seafile.seadroid2:id/login_button").click()
            #如果已登录则先执行退出登录操作
            else:
                self.driver.find_element_by_id('com.seafile.seadroid2:id/menu_overflow').click()
                self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                self.driver.find_element_by_xpath('	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout').click()
                self.driver.find_element_by_id('android:id/button1').click()
                time.sleep(2)
                panduan(self)
        panduan(self)
        time.sleep(2)
        result = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView').text
        self.assertEqual('我的资料库',result,msg='执行成功')


    # 场景2
    def test_2(self):
        time.sleep(2)
        print('新增资料库')

    # 场景99
    def test_99xxxxx(self):
        time.sleep(2)
        print(3)

if __name__ == "__main__":
    unittest.main()