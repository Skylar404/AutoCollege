from hytest import *
from cfg.cfg import *
from lib.API.Sclass import *

class 班级:
    name='tc000001'
    def teststeps(self):
        STEP(1,"创建一个班级")
        response=sclass.add_class(1,'实验1班',80)
        obj=response.json()
        CHECK_POINT('验证添加成功',obj['retcode']==0)

        self.retid=obj["id"]
        list_response=sclass.list_class(1)

        excepted={
                    "gradeid": 1,
                    "retlist": 
                        [{
                            "name": "实验1班",
                            "grade__name": "七年级",
                            "invitecode": obj["invitecode"],
                            "studentlimit": 80,
                            "studentnumber": 0,
                            "id": self.retid,
                            "teacherlist": []
                        }],

                    "retcode": 0}
        print(excepted)
        print(list_response.json())

        CHECK_POINT(
            '验证班级列表',list_response.json()==excepted
        )

    def teardown(self):
        sclass.del_class(self.retid)
        INFO("清除创建的班级")

class tc000081:
    name='tc000081'
    def teststeps(self):
        STEP(1,"删除一个不存在的id")
        response=sclass.del_class('0044324566')
        obj=response.json()
        CHECK_POINT('返回结果为404',obj['retcode']==404)