from lib.API.Sclass import *
from hytest import *
from lib.API.teacher import *


def suite_setup():
        classid=GSTORE['cid']
        print(classid)
        add_response=ST.add_teacher(
                                    username='lihua',
                                    realname='丽华',
                                    subjectid=1,
                                    classlist=classid,
                                    phonenumber='13451813444',
                                    email='jcysdf1@123.com',
                                    idcardnumber='3209251983090987111'
                                )
        print(add_response.json())

        obj=add_response.json()
        GSTORE['tid']=obj['id']
        INFO("添加七年实验2班的科学老师-丽华")
        ListResponse=ST.list_teacher(1)
        ListResponse=ListResponse.json()
        GSTORE['ListResponse']=ListResponse
        

def suite_teardown():
        tid=GSTORE['tid']
        ST.del_teacher(tid)
        INFO("清除七年实验2班的科学老师-丽华")
