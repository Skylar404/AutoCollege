from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.API.Sclass import *
from lib.API.Student import *


class tc002002:
    name="tc002002"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        list_response1= Student.list_student()
        list1=list_response1.json()['retlist']
        STEP(1,"创建一个学生，系统中不存在同登录名的学生")
        add_response=Student.add_student(
                                    username='lz00233',
                                    realname='李钟333',
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
                    "retlist": list1+[
                        {
                            "classid": classid,
                            "username": "lz00233",
                            "realname": "李钟333",
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
        INFO('删除学生李钟')

class tc002081:
    name="tc002081"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)

        STEP(1,"删除一个学生，使url中的ID为一个存在的学生ID号")
        delresponse=Student.del_student(self.sid)


        CHECK_POINT('删除学生A李钟',delresponse.json()['retcode']==0)


        list_response=Student.list_student()

        list_obj=list_response.json()

        print(list_obj['retlist'])

        status=True

        for dict in list_obj['retlist']:

            if dict['id'] == self.sid:
                INFO('该学生在列表中')
                status=False

        CHECK_POINT('检查返回结果中该学生已经不在列表中',status != False )





    def setup(self):
        classid=GSTORE['cid']
        print(classid)

        add_response=Student.add_student(
                                    username='Alz00233',
                                    realname='A李钟333',
                                    gradeid=5,
                                    classid=classid,
                                    phonenumber='13433335569'
                                )
        print(add_response.json())
        self.sid=add_response.json()['id']
        INFO('增加学生A李钟')
