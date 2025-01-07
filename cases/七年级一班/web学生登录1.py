from hytest import *
from cfg.cfg import *
from lib.API.Student import Student
from lib.API.teacher import *
from lib.web.web登录 import *
from lib.web.web学生 import *


class tc005081:
    name='tc005081'

    def teststeps(self):

        STEP(1,'老师账号登陆web界面')
        

        WS.student_login('AAlxz00233','888888')
        list=WS.GetHome()
        expected = ['AA李钟硕333', '白月学院00002', str(GSTORE["invitecode"])+'（注册码）', '0', '0']
        INFO(expected)
        INFO(list)
        CHECK_POINT('检查首页信息', list==expected)
        print(list)
        WS.Go_MissQ()


        # print(InfoList)




        STEP(2,"点击 班级学生 菜单")
        TLogin.Go_StudentGroup()

        TLogin.wd.find_element(By.CSS_SELECTOR,'.panel-green').click()
        getnum=TLogin.wd.find_element(By.CSS_SELECTOR,'.panel-green span[class="ng-binding ng-scope"]')
        print(getnum.text.strip())
        CHECK_POINT('检查学生列表为空', int(getnum.text.strip())==0)

    def setup(self):
            classid=GSTORE['cid']
            print(classid)

            add_response=Student.add_student(
                                        username='AAlxz00233',
                                        realname='AA李钟硕333',
                                        gradeid=5,
                                        classid=classid,
                                        phonenumber='13433335569'
                                    )
            add_r=add_response.json()
            print(add_r)
            sid=add_r['id']

            GSTORE['sid']=sid



    def teardown(self):
            Student.del_student(GSTORE['sid'])
            INFO('删除学生AA李钟硕333')