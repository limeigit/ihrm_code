import unittest

import app
from case.TestIhrmUser import TestUser

print(app.TOKEN)

# 组织测试套件
suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))  # 登陆成功测试方法的添加


# 执行测试测试套件
runner = unittest.TextTestRunner()
runner.run(suite)