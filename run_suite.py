# 导包
import unittest
import app
from case.TestIhrmEmp import TestEmp
from case.TestIhrmUser import TestUser


# 组织测试套件
suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))  # 登陆成功测试方法的添加
suite.addTest(unittest.makeSuite(TestEmp))  # 添加员工管理模块的整个测试用例
# suite.addTest(TestEmp("test_1_emp_add"))  # 添加员工的实现
# suite.addTest(TestEmp("test_2_emp_update"))  # 添加员工的实现

# 执行测试测试套件
runner = unittest.TextTestRunner()
runner.run(suite)

