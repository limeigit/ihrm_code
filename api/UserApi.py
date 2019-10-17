# 定义一个登陆的类
import app


class UserLogin:

    # 定义登陆的请求业务
    def login(self,session,login_data):
        # 登陆的请求业务
        return session.post(app.base_url + "login",json = login_data)