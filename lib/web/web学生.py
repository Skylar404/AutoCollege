import time
from cfg.cfg import *
from lib.API.Sclass import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import *
from selenium.webdriver.common.action_chains import *
from lib.web.web登录 import *

class Webstudent:

    def student_login(self,username,passwd):

        # chrome_options=Options()
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # wd=webdriver.Chrome(options=chrome_options)
        # wd.implicitly_wait(5)
        # wd.get(host+'student'+login)
        # GSTORE['swd']=wd

        self.wd=open_Loginpage('student')
        input_username=self.wd.find_element(By.ID,"username")
        input_username.send_keys(username)

        input_passwd=self.wd.find_element(By.ID,"password")
        input_passwd.send_keys(passwd)

        self.wd.find_element(By.ID,'submit').click()

        self.wd.implicitly_wait(5)

    def GetHome(self):


        self.wd.find_element(By.CSS_SELECTOR,"a[href='#/home']>li").click()

        time.sleep(2)

        eles = self.wd.find_elements(By.CSS_SELECTOR,'#div-home .ng-binding')

        return [ele.text for ele in eles]


    def Go_MissQ(self):
        # time.sleep(2)
        self.wd.find_element(By.CSS_SELECTOR,"[href*=wrong]>li").click()
        # titleActions=ActionChains(self.wd)
        # titleActions.move_to_element(title).perform()
        # self.wd.find_element(By.CSS_SELECTOR,'a[href*="student_group"]>li').click()    



WS=Webstudent()

if __name__=='__main__':

    WS.student_login('guanyu',' sdfsdf5%')
    list=WS.GetHome()
    print(list)
    WS.Go_MissQ()


