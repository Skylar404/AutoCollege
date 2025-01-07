from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.API.Sclass import *


class tc001002:
    name="tc001002"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"创建一个老师，教授学科为初中数学（ID为1）")
        add_response=ST.add_teacher(
                                    username='lishiming3',
                                    realname='李世民3',
                                    subjectid=5,
                                    classlist=classid,
                                    phonenumber='12451813456',
                                    email='jcysdf@123.com',
                                    idcardnumber='3209251983090987799'
                                )
        print(add_response.json())
        self.tid=add_response.json()['id']

        CHECK_POINT("添加老师成功",add_response.json()['retcode']==0)
        
        
        STEP(2,"返回结果包含了刚刚创建的老师信息，ID号和第一步返回的相同")
        list_response= ST.list_teacher(5)

        expected={
            "retlist": [
        {
            "username": "lishiming3",
            "teachclasslist": [GSTORE['cid']], 
            "realname": "李世民3",
            "id": self.tid,
            "phonenumber": "12451813456",
            "email": "jcysdf@123.com",
            "idcardnumber": "3209251983090987799"
        }

    ],
    "retcode": 0
}
        INFO(list_response.json())
        INFO(expected)
        CHECK_POINT('检查列表结果',list_response.json()==expected)

    def teardown(self):
        ST.del_teacher(self.tid)
        INFO('删除数学老师李世民3')


class tc001003:
    name="tc001003"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"创建一个老师，系统中存在同登录名的老师")
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
        # self.tid=add_response.json()['id']

        CHECK_POINT("添加老师成功",add_response.json()['retcode']== 1)
        
        
        STEP(2,"返回结果里面没有添加步骤1指定的老师")
        list_response= ST.list_teacher(1)

        expected={
            "retlist": [
        {
            "username": "lihua",
            "teachclasslist": [GSTORE['cid']], 
            "realname": "丽华",
            "id":  GSTORE['tid'],
            "phonenumber": "13451813444",
            "email": "jcysdf1@123.com",
            "idcardnumber": "3209251983090987111"
        }

    ],
    "retcode": 0
}
        INFO(list_response.json())
        INFO(expected)
        CHECK_POINT('检查列表结果',list_response.json()==expected)


class tc001051:
    name="tc001051"
    def teststeps(self):
        teacherid1=4444444444
        classid=GSTORE['cid']

        STEP(1,"修改一老师，使url中的ID为一个不存在的老师ID号")

        update_response=ST.update_teacher(
                                    teacherid=teacherid1,
                                    realname='丽华1',
                                    subjectid=11,
                                    classlist=classid,
                                    phonenumber='13551813444',
                                    email='jcysdf12@123.com',
                                    idcardnumber='3209251083090987111')


        print(update_response.json())
        # self.tid=add_response.json()['id']

        CHECK_POINT("添加老师失败返回结果1",update_response.json()['retcode']== 1)

class tc001052:
    name="tc001052"
    def teststeps(self):

        classid=GSTORE['cid']
        classid2=GSTORE['cid2']

        STEP(1,"同时修改真实名和授课班级。授课班级原来是1个班，改为两个班")

        update_response=ST.update_teacher(
                                    teacherid=GSTORE['tid'],
                                    realname='丽华1',
                                    subjectid=5,
                                    classlist=f'{classid},{classid2}',
                                    phonenumber='13551813444',
                                    email='jcysdf12@123.com',
                                    idcardnumber='3209251083090987111')


        print(update_response.json())
        # self.tid=add_response.json()['id']

        CHECK_POINT("修改成功，返回结果0",update_response.json()['retcode']== 0)

        STEP(2,"返回结果中刚刚修改的老师，信息更新正确")
        list_response= ST.list_teacher(5)

        expected={
            "retlist": [
        {
            "username": "lihua",
            "teachclasslist": [GSTORE['cid'],classid2], 
            "realname": "丽华1",
            "id":  GSTORE['tid'],
            "phonenumber": "13551813444",
            "email": "jcysdf12@123.com",
            "idcardnumber": "3209251083090987111"
        }

    ],
    "retcode": 0
}
        INFO(list_response.json())
        INFO(expected)
        CHECK_POINT('检查列表结果',list_response.json()==expected)

    def setup(self):
                
        cresponse=sclass.add_class(3,'实验1班',80)
        self.cid2=cresponse.json()['id']
        GSTORE['cid2']=self.cid2
    
    def teardown(self):

        sclass.del_class(self.cid2)
        update_response=ST.update_teacher(    
                                    teacherid=GSTORE['tid'],                               
                                    realname='丽华',
                                    subjectid=5,
                                    classlist=GSTORE['cid'],
                                    phonenumber='13451813444',
                                    email='jcysdf1@123.com',
                                    idcardnumber='3209251983090987111'
                                )
        
        CHECK_POINT("修改老师为初始状态",update_response.json()['retcode']== 0)

    
class tc001081:
    name='tc001081'

    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"删除一个老师，使url中的ID为一个不存在的老师ID号")

        del_response=ST.del_teacher(44444444444444)

        INFO(del_response.json())

        reason='id 为`44444444444444`的老师不存在'
        CHECK_POINT('检查列表结果',del_response.json()['retcode']==404 and del_response.json()['reason']==reason)
    
class tc001082:
    name='tc001082'

    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"来删除一个老师，使url中的ID为一个存在的老师ID号")

        tid2=GSTORE['tid2']
        del_response=ST.del_teacher(tid2)

        INFO(del_response.json())

        CHECK_POINT('检查列表结果',del_response.json()['retcode']==0)

        list_response=ST.list_teacher(12)

        list_obj=list_response.json()

        print(list_obj['retlist'])
        CHECK_POINT('检查返回结果中该老师已经不在老师列表中',list_obj['retlist']==[] )
    
    def setup(self):
            classid=GSTORE['cid']
            print(classid)
            add_response=ST.add_teacher(
                                        username='lihua5',
                                        realname='李华',
                                        subjectid=12,
                                        classlist=classid,
                                        phonenumber='13451814444',
                                        email='jcysdf12@123.com',
                                        idcardnumber='3209251983090988111'
                                    )
            print(add_response.json())

            obj=add_response.json()
            GSTORE['tid2']=obj['id']
            INFO("添加初中体育的老师-李华")
            # list_response=ST.list_teacher(12)
            # list_obj=list_response.json()
            # CHECK_POINT('检查返回结果中该老师已经不在老师列表中',list_obj['retlist']['id'] ==obj['id'] )

            

    def teardown(self):
            list_response=ST.list_teacher(12)
            list_obj=list_response.json()
            if list_obj['retlist']!=[]:
                tid=GSTORE['tid2']
                ST.del_teacher(tid)
                INFO("清除七年实验2班的科学老师-丽华")
    




