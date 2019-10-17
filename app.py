# 导包
import os
import logging.handlers
import time


# 设置logging的一些配置
def set_my_log():
    # 1.创建日志器对象
    logger = logging.getLogger()
    # 1.1设置日志器的级别
    logger.setLevel(logging.INFO)
    # 2.创建处理器
    ls = logging.StreamHandler()  # 控制台处理器
    filename = pro_path + "/log/登陆、员工模块{}.log".format(time.strftime("%Y%m%D%H%M%S"))
    lh = logging.handlers.TimedRotatingFileHandler(filename=filename, when="M", interval=1, backupCount=3)
    # 3.设置格式器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 4.将格式器添加到处理器
    ls.setFormatter(formatter)
    lh.setFormatter(formatter)
    # 5.将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lh)


# 定义一个常用的url
base_url = "http://182.92.81.159/api/sys/"

# 动态获取绝对路径
pro_path = os.path.dirname(os.path.abspath(__file__))

# 定义一个空的全局TOKEN对象
TOKEN = None

# 定义一个全局的员工id
emp_id = None
