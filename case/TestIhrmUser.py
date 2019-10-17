import json
import unittest
import requests
from parameterized import parameterized
import app
from api.UserApi import UserLogin


# 定义构建登陆数据
def build_data():
    login_data = []
    with open(app.pro_path + "/data/login_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for value in data.values():
            login_data.append((value.get("mobile"), value.get("password"), value.get("success"),
                               value.get("code"), value.get("message")))
        return login_data


# 定义测试类
class TestUser(unittest.TestCase):
    # 定义初始化方法
    def setUp(self):
        # 初始化session
        self.session = requests.Session()

        # 实例化api登陆请求对象
        self.user_login = UserLogin()

    # 定义资源销毁方法
    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # 定义登陆的测试方法
    @parameterized.expand(build_data())
    def test_login(self, mobile, password, success, code, message):
        # print("*"*10)
        # print(mobile,password,success,code,message)
        # print("*" * 10)
        login_data = {"mobile": mobile, "password": password}
        # 1.请求业务
        reponse = self.user_login.login(self.session, login_data)

        # 2.断言业务
        self.assertEqual(success, reponse.json().get("success"))
        self.assertEqual(code, reponse.json().get("code"))
        self.assertIn(message, reponse.json().get("message"))

    # 登陆成功测试用例实现
    def test_login_success(self):
        login_data = {"mobile": "13800000002", "password": "123456"}

        # 1.请求业务
        response = self.user_login.login(self.session, login_data)
        result = response.json()
        print("登陆成功的响应体为：", result)
        # 2.断言业务
        self.assertEqual(10000, result.get("code"))
        self.assertEqual(True, result.get("success"))
        self.assertIn("操作成功", result.get("message"))
        token = result.get("data")
        app.TOKEN = token
        # print(app.TOKEN)
