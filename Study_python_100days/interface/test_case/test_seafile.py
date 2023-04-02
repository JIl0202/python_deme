import pytest
import requests
'''
requests一般有2种情况方法组成，一个是post，一个是get，因此不同的请求类型需要调用不同的方法
requests.post
requests.get
'''

'''
assert函数的检查方式
1.测试是否包含某些内容assert b in a
2.检查不包含某些内容  assert b not in a
3.检查是否相等   assert b == a
当然还有其他检查方式，自行百度查询即可
'''

'''HTTP的返回内容获取方式
print ('HTTP状态码:',r.status_code)   
print (u'请求的URL:',r.url)
print (u'获取Headers:',r.headers)
print (u'响应体内容:',r.text)
print ('请求时间',r.elapsed.total_seconds())
'''

class TestSimple(object):
    @classmethod
    def setup_class(cls): #setup前置脚本，也就是在所有测试脚本执行之前会先运行一次。
        """
        这是一个class级别的setup函数，它会在这个测试类TestSohu里
        所有test执行之前，被调用一次.
        注意它是一个@classmethod
        """
        print("------ setup before class TestSohu ------")

    def test_login_success(self):
        url = r'http://42.192.62.88:80/api2/auth-token/'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'

        }
        bodys = {'username':'hexuan@micsoft.com','password':'123456'}
        respon = requests.post(url=url,headers=headers,data=bodys)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'token' in respon.text
        jsondata = respon.json()
        global Token
        Token = jsondata['token']

    def test_account_info(self):
        url = r'http://42.192.62.88:80/api2/account/info/'
        headers = {
            'Accept':'application/json; indent=4',
            'Authorization':'Token '+Token
        }
        respon = requests.get(url=url,headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'hexuan' in respon.text

    def test_createrepos(self):
        url = r'http://42.192.62.88:80/api2/repos/'
        headers = {
            # 'content-type':'application/x-www-form-urlencoded',
            'Authorization': 'Token ' + Token
        }
        bodys = {'name':'newrepo'}
        respon = requests.post(url=url,headers=headers,data=bodys)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'newrepo' in respon.text
        jsondata = respon.json()
        global  repoID
        repoID = jsondata['repo_id']

    def test_reposinfo(self):
        url = r'http://42.192.62.88:80/api2/repos/'
        headers = {
            'Authorization': 'Token ' + Token
        }
        respon = requests.get(url=url, headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        # print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'hexuan@micsoft.com' in respon.text

    def test_createfile(self):
        url = r'http://42.192.62.88:80/api2/repos/{}/file/?p=/newfile&reloaddir=true'.format(repoID)
        headers = {
            'Authorization': 'Token ' + Token
        }
        bodys = {'operation':'create'}
        respon = requests.post(url=url,headers=headers,data=bodys)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'newfile' in respon.text


    def test_staredfiles(self):
        url = r'http://42.192.62.88:80/api2/starredfiles/'
        headers = {
            'Authorization': 'Token ' + Token
        }
        bodys = {'repo_id':repoID,'p':'/newfile'}
        respon = requests.post(url=url,headers=headers,data=bodys)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'success' in respon.text

    def test_searchstarfile(self):
        url = r'http://42.192.62.88:80/api2/starredfiles/'
        headers = {
            'Authorization': 'Token ' + Token
        }
        respon = requests.get(url=url,headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'newfile' in respon.text

    def test_del_starfile(self):
        url = r'http://42.192.62.88:80/api2/starredfiles/?repo_id={}&p=/newfile'.format(repoID)
        headers = {
            'Authorization': 'Token ' + Token
        }
        respon = requests.delete(url=url,headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'success' in respon.text

    def test_delfile(self):
        url = r'http://42.192.62.88:80/api2/repos/{}/file/?p=/newfile&reloaddir=true'.format(repoID)
        headers = {
            'Authorization': 'Token ' + Token
        }
        respon = requests.delete(url=url,headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert '[]' in respon.text

    def test_delrepos(self):
        url = r'http://42.192.62.88:80/api2/repos/{}/'.format(repoID)
        headers = {
            'Authorization': 'Token ' + Token
        }
        respon = requests.delete(url=url,headers=headers)
        print('HTTP状态码:', respon.status_code)
        print(u'请求的URL:', respon.url)
        print(u'获取Headers:', respon.headers)
        print(u'响应体内容:', respon.text)
        print('请求时间', respon.elapsed.total_seconds())
        assert 'success' in respon.text



    #以下就是你要编写的测试用例，如案例所示是编写的登录成功的接口
    #def test_login_success(self):
        #编写接口请求三部曲（跟接口测试三要素遥相呼应）
        #首先第一步定义接口的地址
        #url = 'http://172.31.63.253:1182/api2/auth-token/'#一般从文档里获取
        # 第二步定义接口的请求内容，其中包括2个内容，一个是请求头，一个是请求体
        # 当然根据情况，如果接口对头部没有要求可以不用管头部，像本接口对头部就没有特殊要求，
        # 可以不管，当然体也是一样的道理
        #根据本接口的请求参数要求，必须要传入用户名和密码因此需要有体
        # headers = {'content-type': 'application/json',
        #           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        #body = {'username': '18833019@qq.com', 'password': '51testing'}
        #利用如下代码将构造的请求消息发送到对应的服务端的地址，返回的结果则存储在r变量里。
		#若是https请求，可以添加这一句requests.packages.urllib3.disable_warnings()，再发送请求，记得在地址后的面加上verify=False ，就是这样r = requests.post(url, data=body)
        #r = requests.post(url, data=body)
        # 第三步利用pytest自带的assert表达式进行结果检查，也就是断言
        #assert 'token' in r.text
        #根据文档已经知道返回的结果里是json格式，因此利用r.json()函数进行格式化，方便获取内容
        #result = r.json()
        #global gc_token  #定义全局变量，后续需要进行参数化使用
        #gc_token = result['token']#从json格式里获取token的值，并保存到全局变量gc_token里，同postman和jmeter里参数化一个意思
        #print(gc_token)  #打印全局变量里保存的token的值，方便观察结果

    #def test_getaccountinfo_success(self):
        #还是接口测试的三部曲
        #第一步定义url,地址从文档获取
        #url='http://172.31.63.253:1182/api2/account/info/'
        #第二步，构造请求消息的头和体
        #根据本接口用例分析，请求头部是有必填项的Authorization，但是没有体，因此可以不管体
        #头部构造，只需要设置我们关心的内容即可，其他默认
        #print(gc_token)
        #headers = {'Authorization': 'Token '+gc_token}
        #r = requests.get(url, headers=headers)
        # 第三步利用assert表达式检查结果是否正确，也就是断言
        #assert '188330119' in r.text
        #print(r.text)

    @classmethod
    def teardown_class(cls):#teardown后置脚本，也就是在所有测试脚本执行之后会先运行一次。
        """
        这是一个class级别的teardown函数，它会在这个测试
        类里所有test执行完之后，被调用一次.
       注意它是一个@classmethod
       """
        print("------ teardown after class TestSohu ------")