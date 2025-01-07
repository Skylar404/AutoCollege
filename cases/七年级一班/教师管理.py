from hytest import *
from cfg.cfg import *
from lib.API.teacher import *


class tc001001:
    name="tc001001"
    def teststeps(self):
        classid=GSTORE['cid']
        print(classid)
        STEP(1,"创建一个老师，教授学科为初中数学（ID为1）")
        add_response=ST.add_teacher(
                                    username='lishiming2',
                                    realname='李世民',
                                    subjectid=1,
                                    classlist=classid,
                                    phonenumber='13451813456',
                                    email='jcysdf@123.com',
                                    idcardnumber='3209251983090987899'
                                )
        print(add_response.json())
        self.tid=add_response.json()['id']

        CHECK_POINT("添加老师成功",add_response.json()['retcode']==0)
        
        
        STEP(2,"返回结果包含了刚刚创建的老师信息，ID号和第一步返回的相同")
        list_response= ST.list_teacher(1)

        expected={
            "retlist": [
        {
            "username": "lishiming2",
            "teachclasslist": [GSTORE['cid']], 
            "realname": "李世民",
            "id": self.tid,
            "phonenumber": "13451813456",
            "email": "jcysdf@123.com",
            "idcardnumber": "3209251983090987899"
        }

    ],
    "retcode": 0
}
        INFO(list_response.json())
        INFO(expected)
        CHECK_POINT('检查列表结果',list_response.json()==expected)

    def teardown(self):
        ST.del_teacher(self.tid)
        INFO('删除老师')



