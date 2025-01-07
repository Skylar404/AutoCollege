from hytest import *
from cfg.cfg import *
from lib.API.Sclass import *

class tc000002:
    name='tc000002'

    def teststeps(self):
        STEP(1,"创建一个班级")
        response=sclass.add_class(1,'实验3班',80)

        obj=response.json()
        self.retid=obj["id"]

        CHECK_POINT('验证添加成功',obj['retcode']==0)

        list_response=sclass.list_class(1)

        excepted={
                            "name": "实验3班",
                            "grade__name": "七年级",
                            "invitecode": obj['invitecode'],
                            "studentlimit": 80,
                            "studentnumber": 0,
                            "id": self.retid,
                            "teacherlist": []
                        }

        list=list_response.json()['retlist']
        INFO(list[1])

        CHECK_POINT(
            '验证班级列表',excepted == list[1]
        )

    def teardown(self):
        sclass.del_class(self.retid)
        INFO("清除创建的班级")
  




class tc000003:

    name="tc000003_已经存在同年级的同名班级"

    def teststeps(self):
        STEP(1,"创建一个班级")
        response=sclass.add_class(1,'实验2班',80)

        CHECK_POINT('验证添加失败',response.json()['retcode']==1)

        list_response=sclass.list_class(1)

        excepted={
                    "gradeid": 1,
                    "retlist": 
                        [{
                            "name": "实验2班",
                            "grade__name": "七年级",
                            "invitecode": GSTORE['invitecode'],
                            "studentlimit": 80,
                            "studentnumber": 0,
                            "id": GSTORE['cid'],
                            "teacherlist": []
                        }],

                    "retcode": 0}
        
        INFO(list_response.json())

        CHECK_POINT(
            '验证班级列表',list_response.json()==excepted
        )


class tc000051:

# '''{
#                     "gradeid": 2,
#                     "retlist": 
#                         [{
#                             "name": "普通4班",
#                             "grade__name": "八年级",
#                             "invitecode": self.obj['invitecode'],
#                             "studentlimit": 80,
#                             "studentnumber": 0,
#                             "id": self.obj['id'],
#                             "teacherlist": []
#                         }],
#                     "retcode": 0}'''
    ddt_cases= [
         {
              "name": "tc000051",
              "para": [None,'普通4班',80,0]

         },
         {
          "name": "tc000052",
          "para": [None,'实验4班',80,1]

         },
        {
          "name": "tc000053",
          "para": [1000051,'普通5班',80,404]
         }
        ]


    def teststeps(self):


        cid,cname,num,retcode=self.para
        
        if retcode ==1:
            STEP(1,"班级名为一个新的名字，并且和一个已有的班级同名")
            cid,cname,num,retcode=self.para
            cid=GSTORE['id']
            list_response=sclass.list_class(2)
            update_response=sclass.update_class(cid,cname,num)
            update_obj=update_response.json()
            INFO(update_obj)
            INFO(cname)
            INFO(list_response.json())
            CHECK_POINT('验证修改失败',update_response.json()['retcode']==1)

            STEP(2,"验证班级列表")

            INFO(list_response)
            CHECK_POINT(
                '验证班级列表',list_response.json()==self.listc
            )

        if retcode ==404:
            cid,cname,num,retcode=self.para
            update_response=sclass.update_class(cid,cname,num)  
            CHECK_POINT('验证修改失败',update_response.json()['retcode']==404)

            STEP(2,"验证班级列表")
            list_response=sclass.list_class(2)
            CHECK_POINT(
                '验证班级列表',list_response.json()==self.listc
            )

        if retcode == 0:
            STEP(1,"修改一个班级名为一个新的名字")
            # cid,cname,num,retcode=self.para
            cid=GSTORE['id']
            update_response=sclass.update_class(cid,cname,num)
            update_obj=update_response.json()
            INFO(update_obj)
            CHECK_POINT('验证修改成功',update_response.json()['retcode']==0)

            excepted={
                        "gradeid": 2,
                        "retlist": 
                            [{
                                "name": "普通4班",
                                "grade__name": "八年级",
                                "invitecode": self.obj['invitecode'],
                                "studentlimit": 80,
                                "studentnumber": 0,
                                "id": self.obj['id'],
                                "teacherlist": []
                            }],

                        "retcode": 0}
            
            # INFO(update_obj)
            list_response=sclass.list_class(2)
            INFO(list_response.json())
            CHECK_POINT(
                '验证班级列表',list_response.json()==excepted
            )
        
         
    def setup(self):
            response=sclass.add_class(2,'实验4班',80)
            self.obj=response.json()
            GSTORE['id']=self.obj['id']
            print(GSTORE['id'])
            listc=sclass.list_class(2)
            self.listc=listc.json()
            INFO("添加八年实验4班")

    def teardown(self):
            cid=self.obj['id']
            sclass.del_class(cid)
            INFO("清除八年实验4班")


class tc000082:
    name='tc000082'
    def teststeps(self):
        STEP(1,"删除一个存在的id")
        response=sclass.del_class(GSTORE['id'])
        obj=response.json()
        CHECK_POINT('返回结果正确',obj['retcode']==0)
    
    def setup(self):
        response=sclass.add_class(1,'实验4班',80)
        self.obj=response.json()
        GSTORE['id']=self.obj['id']
        print(GSTORE['id'])
        listc=sclass.list_class(1)
        self.listc=listc.json()
        INFO("添加七年实验4班")