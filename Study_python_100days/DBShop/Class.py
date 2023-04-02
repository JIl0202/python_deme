import re
import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import *
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class procedures:
    # 初始化 并传入两个参数 一个浏览器 一个网址
    def __init__(self, browser, url):
        self.url = url
        self.browser = browser
        self.random_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    def random_str(self, e=''):
        str = ''.join(random.sample(self.random_list, random.randint(6, 10)))
        if e != '':
            str += '@qq.com'
        return str

    def random_user(self, n):
        self.userslist = []
        for i in range(n):
            self.strdict = {'name': self.random_str(), 'password': self.random_str(), 'email': self.random_str('e')}
            self.userslist.append(self.strdict)
        return self.userslist

    def save_users(self, user):
        with open(r'C:\Users\Administrator\Desktop\Users.txt', 'a', encoding='UTF-8') as b:
            b.write("%s----->用户名:%-12s密码:%-12s邮箱:%-20s\n" % (
                self.local_time(), user['name'], user['password'], user['email']))

    def get_driver(self, waittime=15):
        if self.browser == 'c':
            self.br = webdriver.Chrome()
        elif self.browser == 'f':
            self.br = webdriver.Firefox()
        else:
            raise
        self.br.maximize_window()
        self.br.implicitly_wait(waittime)

    def headless(self, waittime=15):
        if self.browser == 'c':
            self.op = Options()
            self.op.headless = True
            self.br = webdriver.Chrome(options=self.op)

        elif self.browser == 'f':
            self.op = Options()
            self.op.headless = True
            self.br = webdriver.Firefox(options=self.op)

        self.br.maximize_window()
        self.br.implicitly_wait(waittime)

    def local_time(self):
        return time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime())

    def write_log(self, message):
        with open(r'C:\Users\Administrator\Desktop\log.txt', 'a', encoding='UTF-8') as w:
            w.write('{}  {}\n'.format(self.local_time(), message))

    def logout(self):
        self.br.find_element(By.XPATH, r'//* [text() = "退出"]').click()

    def close(self):
        self.br.quit()

    def mouse(self):
        self.mm = webdriver.ActionChains(self.br)


class testcase(procedures):

    def regist(self, user):
        self.br.get(self.url)
        self.br.find_element(By.XPATH, r'//* [text() = "注册"]').click()
        self.br.find_element(By.XPATH, r'//* [@id = "user_name"]').send_keys(user['name'])
        self.br.find_element(By.XPATH, r'//* [@id = "user_password"]').send_keys(user['password'])
        self.br.find_element(By.XPATH, r'//* [@id = "user_com_passwd"]').send_keys(user['password'])
        self.br.find_element(By.XPATH, r'//* [@id = "user_email"]').send_keys(user['email'])
        self.br.find_element(By.XPATH, r'//* [@id = "agreement"]').click()
        self.br.find_element(By.XPATH, r'//button').click()

    def login(self, user_name, user_password):
        self.br.get(self.url)
        self.br.find_element(By.XPATH, r'//* [text() = "登录"]').click()
        self.br.find_element(By.XPATH, r'//* [@id = "user_name"]').send_keys(user_name)
        self.br.find_element(By.XPATH, r'//* [@id = "user_password"]').send_keys(user_password)
        self.br.find_element(By.XPATH, r'//button [text() = "会员登录"]').click()

    def admin_login(self):
        self.br.get(self.url)
        self.br.find_element(By.XPATH, r'//*[@id = "user_name"]').send_keys('admin')
        self.br.find_element(By.XPATH, r'//*[@id = "user_passwd"]').send_keys('123456')
        self.br.find_element(By.XPATH, r'//* [@class = "btn"]').click()

    def admin_active_1(self):
        self.br.find_element(By.XPATH, r'//* [text()= "客户管理 "]').click()
        self.mm.move_to_element(self.br.find_element(By.XPATH, r'//* [text()="客户余额"]')).perform()
        self.br.find_element(By.XPATH, r'//* [text() = "余额记录"]').click()

    def order_active_1(self):
        self.br.find_element(By.XPATH, r'//input [@name = "keywords"]').send_keys('小米')
        self.br.find_element(By.XPATH, r'//input [@type = "submit"]').click()

        self.br.find_element(By.LINK_TEXT, '小米Mix3 全网通版 8GB+128GB 黑色 磁动力滑盖全面屏').click()

        self.br.switch_to.window(self.br.window_handles[-1])

        self.br.find_element(By.XPATH, r'//* [@id="add_cart_submit"]').click()
        self.br.find_element(By.XPATH, r'//* [text()= "去购物车结算"]').click()
        self.br.find_element(By.XPATH, r'//* [text()= "去结算"]').click()
        self.br.find_element(By.XPATH, r'//* [@class="btn btn-small btn-primary"]').click()

        self.br.find_element(By.XPATH, r'//* [@class="span2"]').send_keys('张三')

        self.sl1 = Select(self.br.find_element(By.XPATH, r'//*[@id="show_address_area"]'))
        self.sl1.select_by_visible_text('湖北省')
        # Select(self.br.find_element(By.XPATH, r'//* [@id="show_address_area"]')).select_by_visible_text('湖北省')

        self.sl2 = Select(self.br.find_element(By.XPATH, r'//*[ @id="region"]/ elect[2]'))
        self.sl2.select_by_visible_text('武汉市')
        # Select(self.br.find_element(By.XPATH, r'// *[ @ id = "region"] / select[2]')).select_by_visible_text('武汉市')

        self.sl3 = Select(self.br.find_element(By.XPATH, r'//*[@id="region"]/select[3]'))
        self.sl3.select_by_visible_text('洪山区')
        # Select(self.br.find_element(By.XPATH, r'//*[@id="region"]/select[3]')).select_by_value('洪山区')

        self.br.find_element(By.XPATH, r'//* [@id="address"]').send_keys('杨园街道友谊大道君临国际')
        self.br.find_element(By.XPATH, r'//* [@id="zip_code"]').send_keys('430000')
        self.br.find_element(By.XPATH, r'//* [@id="mod_phone"]').send_keys('13800000000')
        self.br.find_element(By.XPATH, r'//* [@class="btn btn-primary"]').click()

        time.sleep(5)
        self.br.find_element(By.XPATH, r'/html/body/div[3]/div[2]/form/div/div[3]/div/input[2]').click()
        self.br.find_element(By.XPATH, r'//* [@value="xxzf"]').click()
        self.br.find_element(By.XPATH, r'//* [@id="order_message"]').send_keys('线下付款')
        self.br.find_element(By.XPATH, r'//* [@class="btn btn-large btn-primary"]').click()

        self.orderid = self.br.find_element(By.XPATH, r'//*[@id="dbshop-body"]/div[3]/div[2]/p[2]/strong/font').text
        print('订单编号为:{}'.format(self.orderid))
        self.br.find_element(By.XPATH, r'//* [@value="马上去支付"]').click()
        self.br.find_element(By.XPATH, r'//* [@id="state_info"]').send_keys('客户已支付成功')
        self.br.find_element(By.XPATH, r'//button [@class="btn btn-primary btn-large"]').click()
        return self.orderid

    def admin_active_2(self, orderid):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '销售管理').click()
        self.br.find_element(By.LINK_TEXT, '订单管理').click()
        self.br.find_element(By.XPATH, r'//* [@name="order_sn"]').send_keys(orderid)
        self.br.find_element(By.XPATH, r'//* [@class="btn btn-small btn-primary"]').click()
        self.br.find_element(By.LINK_TEXT, '编辑查看').click()
        self.br.find_element(By.LINK_TEXT, '付款操作').click()
        Select(self.br.find_element(By.XPATH, r'//* [@id="pay_state"]')).select_by_visible_text('已付款')
        self.br.find_element(By.XPATH, r'//* [@id="state_info"]').send_keys('客户已付款完成')
        self.br.find_element(By.XPATH, r'//* [@class="icon-ok icon-white"]').click()
        self.br.find_element(By.LINK_TEXT, '发货操作').click()
        self.Courierid = ''.join(random.sample('12345678901234567890', 12))
        self.br.find_element(By.XPATH, r'//* [@id="express_number"]').send_keys(self.Courierid)
        self.br.find_element(By.XPATH, r'//* [@id="state_info"]').send_keys(self.local_time() + '\t已发货')
        self.br.find_element(By.XPATH, r'//* [@class="btn btn-small btn-primary"]').click()

        self.br.find_element(By.LINK_TEXT, '完成订单').click()
        self.br.find_element(By.CLASS_NAME, "span8").send_keys('订单已完成')
        self.br.find_element(By.XPATH, r'//button [@class="btn btn-small btn-primary"]').click()

    def order_active_2(self, orderid):
        self.br.find_element(By.LINK_TEXT, '我的订单').click()
        self.br.find_element(By.PARTIAL_LINK_TEXT, '交易完成').click()
        self.br.find_element(By.XPATH, r'//input [@placeholder="输入订单号"]').send_keys(orderid)
        self.br.find_element(By.XPATH, r'//button [@class="btn btn-small btn-primary"]').click()
        return self.br.find_element(By.CLASS_NAME, "order-status").text

    def close_reg(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '系统管理').click()
        self.br.find_element(By.LINK_TEXT, '客户设置').click()
        self.br.find_element(By.XPATH, r'//input [@value="false"]').click()
        self.br.find_element(By.XPATH, r'//button [@class="btn btn-small btn-primary"]').click()

    def openreg(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '系统管理').click()
        self.br.find_element(By.LINK_TEXT, '客户设置').click()
        self.br.find_element(By.XPATH, r'//input [@value="true"]').click()
        self.br.find_element(By.XPATH, r'//button [@class="btn btn-small btn-primary"]').click()

    def Products(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '商品管理').click()
        self.br.find_element(By.LINK_TEXT, '管理商品').click()
        self.checkboxl = self.br.find_elements(By.NAME, "goods_id[]")

        for c in self.checkboxl:
            if c.get_property('checked') == False:
                c.click()

        time.sleep(5)

        for c in self.checkboxl:
            if c.get_property('checked') == True:
                c.click()

    def content_management(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '系统管理').click()
        self.br.find_element(By.LINK_TEXT, '系统设置').click()
        self.br.find_element(By.LINK_TEXT, '内容信息').click()

        self.br.switch_to.frame(self.br.find_element(By.ID, "ueditor_0"))
        time.sleep(2)
        self.br.find_element(By.XPATH, r'//body[@class="view"]').clear()
        self.br.find_element(By.XPATH, 'r//body[@class="view"]').send_keys('明知山有虎,\n要去明知山.')
        self.br.switch_to.default_content()
        time.sleep(2)

        self.br.switch_to.frame(self.br.find_element(By.ID, "ueditor_1"))
        time.sleep(2)
        self.br.find_element(By.XPATH, r'//body[@class="view"]').clear()
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys('床前明月光')
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys(Keys.ENTER)
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys('疑似地上霜')
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys(Keys.ENTER)
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys('举头望明月')
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys(Keys.ENTER)
        self.br.find_element(By.XPATH, r'//body[@class="view"]').send_keys('低头思故乡')

        for i in range(23):
            self.br.find_element(By.XPATH, '//body[@class="view"]').send_keys(Keys.BACKSPACE)

    def evaluation(self):
        self.br.find_element(By.LINK_TEXT, '我的订单').click()
        self.br.find_element(By.PARTIAL_LINK_TEXT, '交易完成').click()
        self.br.find_elements(By.PARTIAL_LINK_TEXT, '尚未评价')[0].click()
        self.br.find_element(By.XPATH, "//input[@value='1']").click()
        self.br.find_element(By.CLASS_NAME, "span8").send_keys('商品质量很差, 再也不买小米的产品了')
        self.br.find_element(By.XPATH, r'//*[@id="goods_comment"]/div[3]/button').click()

    def admin_evaluation(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '商品管理').click()
        self.br.find_element(By.LINK_TEXT, '商品评价').click()
        self.br.find_element(By.LINK_TEXT, '编辑查看').click()
        self.br.find_element(By.LINK_TEXT, '评价回复').click()
        self.br.find_element(By.NAME, "reply_comment_content").send_keys('谢谢亲的好评,祝亲事业顺利,生活如意!')
        self.br.find_element(By.XPATH, r'//*[@id="myModal"]/div[3]/button[2]').click()
        self.evaluation = self.br.find_element(By.XPATH, r'/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td').text
        self.result = re.search('谢谢', self.evaluation)
        self.br.find_element(By.LINK_TEXT, '删除').click()
        self.br.switch_to.alert.accept()
        return self.result

    def change_price(self):
        self.br.find_element(By.PARTIAL_LINK_TEXT, '商品管理').click()
        self.br.find_element(By.LINK_TEXT, '管理商品').click()
        self.br.find_elements(By.PARTIAL_LINK_TEXT, '编辑')[-1].click()
        self.price = self.br.find_element(By.ID, 'goods_shop_price')
        self.p1 = self.price.get_property('value')
        print('修改前价格为{}'.format(self.p1))
        self.p1 = int(self.p1) + 100
        self.price.clear()
        self.price.send_keys(self.p1)
        self.br.find_element(By.XPATH, r'//*[@id="sticky_navigation_right"]/button[2]').click()
        self.br.find_element(By.XPATH, r'/html/body/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/p/button').click()
        self.p2 = self.br.find_element(By.XPATH, r'/html/body/div[2]/div/div[2]/table/tbody/tr[9]/td[5]').text
        print('修改后价格为{}'.format(self.p1))
        return self.p1, self.p2
