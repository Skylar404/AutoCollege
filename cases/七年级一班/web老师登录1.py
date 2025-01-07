from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.web.web登录 import *


class tc005001:
    name='tc005001'

    def teststeps(self):

        STEP(1,'老师账号登陆web界面')
        TLogin.teacher_login(GSTORE['username'],first_passwd)
        InfoList=TLogin.GetHome()
        print(InfoList)
        expected = ['白月学院00002', '丽华', '初中数学', '0', '0', '0']

        CHECK_POINT('检查首页信息', InfoList==expected)

        STEP(2,"点击 班级学生 菜单")
        TLogin.Go_StudentGroup()

        TLogin.wd.find_element(By.CSS_SELECTOR,'.panel-green').click()
        getnum=TLogin.wd.find_element(By.CSS_SELECTOR,'.panel-green span[class="ng-binding ng-scope"]')
        print(getnum.text.strip())
        CHECK_POINT('检查学生列表为空', int(getnum.text.strip())==0)

    def setup(self):
        classid=GSTORE['cid']
        print(classid)
        self.username='lihuaaaa'
        add_response=ST.add_teacher(
                                    username=self.username,
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
        INFO("添加七年实验2班的数学老师-丽华")
        # ListResponse=ST.list_teacher(5)
        # ListResponse=ListResponse.json()
        GSTORE['username']=self.username
        




    def teardown(self):
        tid=GSTORE['tid']
        ST.del_teacher(tid)
        INFO("清除七年实验2班的数学老师-丽华")