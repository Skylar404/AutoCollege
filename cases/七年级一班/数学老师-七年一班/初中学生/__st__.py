from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.API.Sclass import *
from lib.API.Student import *


def suite_setup():
        classid=GSTORE['cid']
        print(classid)

        add_response=Student.add_student(
                                    username='AAlxz00233',
                                    realname='AA李钟硕333',
                                    gradeid=5,
                                    classid=classid,
                                    phonenumber='13433335569'
                                )
        print(add_response.json())
        sid=add_response.json()['id']
        GSTORE['sid']=sid


def suite_teardown():
        Student.del_student(GSTORE['sid'])
        INFO('删除学生AA李钟硕333')

