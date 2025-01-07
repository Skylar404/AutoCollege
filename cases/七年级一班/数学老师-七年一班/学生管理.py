from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.API.Sclass import *
from lib.API.Student import *


class tc002001:
    name="tc002001"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"创建一个学生，系统中不存在同登录名的学生")
        add_response=Student.add_student(
                                    username='lxz00233',
                                    realname='李钟硕333',
                                    gradeid=5,
                                    classid=classid,
                                    phonenumber='13433335569'
                                )
        print(add_response.json())
        self.sid=add_response.json()['id']

        CHECK_POINT("添加学生成功",add_response.json()['retcode']==0)
        
        
        STEP(2,"返回结果包含了刚刚创建的学生信息，ID号和第一步返回的相同")
        list_response= Student.list_student()

        expected={
                    
                    "retcode": 0,
                    "retlist": [
                        {
                            "classid": classid,
                            "username": "lxz00233",
                            "realname": "李钟硕333",
                            "phonenumber": "13433335569",
                            "id": self.sid
                        }
                    ]

                }

        INFO(list_response.json())
        INFO(expected)
        CHECK_POINT('检查列表结果',list_response.json()==expected)

    def teardown(self):
        Student.del_student(self.sid)
        INFO('删除学生李钟硕33')

