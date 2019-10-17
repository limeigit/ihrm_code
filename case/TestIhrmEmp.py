# 导包
import unittest
import logging
import requests
import app
from api.EmpApi import EmpCRUD
import pymysql

# # 1.创建连接
# conncet = pymysql.connect(host = "182.92.81.159",username = "readuser",password = "iHRM_user_2019",port = 3306 )
# # 2.创建游标对象
# cursor = conncet.cursor()
# # 3.创建并执行sql语句
# cursor.execute("select id from bs_user where username = 'zbz'")
# # 4.获取查询结果
# result = cursor.fetchone()
# print("查询的结果为：",result)

# 创建测试类
class TestEmp(unittest.TestCase):
    # 定义初始化方法
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 定义资源销毁方法
    def tearDown(self):
        self.session.close()

    # 定义员工添加的测试方法
    def test_1_emp_add(self):
        # 1.请求业务
        response = self.emp_obj.add_emp(self.session, "te2s173345363", "15818122453", "146635")
        # 2.断言业务
        result = response.json()
        app.emp_id = result.get("data").get("id")
        self.assertEqual(10000,result.get("code"))
        self.assertIn("操作成功",result.get("message"))

    # 定义员工修改的测试方法
    def test_2_emp_update(self):
        # 1.请求业务
        data = {"username":"tom"}
        response = self.emp_obj.update_emp(self.session,data)
        # 2.断言业务
        print("修改员工的响应体为：",response.json())
        result = response.json()
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))

    # 定义员工查询的方法
    def test_3_emp_get(self):
        response = self.emp_obj.get_emp(self.session)
        print("查询员工的响应体：",response.json())
        result = response.json()
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))

    # 定义员工的删除
    def test_4_emp_delete(self):
        response = self.emp_obj.delete_emp(self.session)
        print("删除员工的响应体：",response.json())
        result = response.json()
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))
        logging.info("删除成功的日志")
