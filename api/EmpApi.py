"""
    定义员工的增删改查的请求业务
"""
import app


class EmpCRUD():

    # 定义初始化方法
    def __init__(self):
        self.header = {"Authorization":"Bearer {}".format(app.TOKEN)}

    # 定义添加员工的请求业务
    def add_emp(self, session,username,mobile,workNumber):
        emp_data ={
                     "username": username,
                     "mobile": mobile,
                     "workNumber": workNumber
                    }
        return session.post(app.base_url + "user", json=emp_data,headers = self.header)

    # 定义员工的修改请求业务headers = myHeard
    def update_emp(self, session, emp_data):
        return session.put(app.base_url + "user/" + app.emp_id, json=emp_data,headers = self.header)

    # 定义员工的查询请求业务
    def get_emp(self, session):
        return session.get(app.base_url + "user/" + app.emp_id,headers = self.header)

    # 定义员工的删除请求
    def delete_emp(self, session):
        return session.delete(app.base_url + "user/" + app.emp_id,headers = self.header)
