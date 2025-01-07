from hytest import *
from cfg.cfg import *
from lib.API.teacher import *
from lib.web.web登录 import *


class tc005002:
    name='tc005002'

    def teststeps(self):

        STEP(1,'老师账号登陆web界面')
        TLogin.teacher_login('lihua',first_passwd)
        InfoList=TLogin.GetHome()
        print(InfoList)
        expected = ['白月学院00002', '丽华', '初中科学', '0', '0', '0']

        CHECK_POINT('检查首页信息', InfoList==expected)

        STEP(2,"点击 班级学生 菜单")
        TLogin.Go_StudentGroup()

        namelist=TLogin.student_list()
        print(namelist)

        CHECK_POINT('检查学生列表正确', namelist==['AA李钟硕333'])


class tc00051:
    ddt_cases= [
         {
              "name": "tc0005102",
              "para": ['']

         },
         {
          "name": "tc0005103",
          "para": ['a']

         },
        {
          "name": "tc0005104",
          "para": ['系统中已经有数学老师，已经有学生，已经有班级1. 以数学老师的账号和密码登录 web系统2. 发布一个作业，作业名称为100个字符，中间包含汉字，英文，*（）这样的字符3.查看已发布作业']
         }
        ]
    
    def teststeps(self):
        STEP(1,'老师账号登陆web界面')
        TLogin.teacher_login('lihua',first_passwd)

        TLogin.Go_addhomework()
        para=self.para
        TLogin.add_homework(para)
        time.sleep(4)
        if para=='':
            alert = TLogin.wd.switch_to.alert()
            text=alert.text
            CHECK_POINT('跳出弹窗',text=='请输入作业名称')
        
        else:
            alert = TLogin.wd.switch_to.alert()
            dont_publish_button = TLogin.wd.find_element(By.XPATH, "//button[text()='暂不发布']")
            dont_publish_button.click()

            title=TLogin.wd.find_element(By.CSS_SELECTOR,"#serach_result_table>div:first-child>div:first-child").text
            CHECK_POINT('检查名字',title==para)

            



        