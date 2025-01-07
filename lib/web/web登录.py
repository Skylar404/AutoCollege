import json
import time
import requests
from cfg.cfg import *
from lib.API.Sclass import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import *
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.chrome.options import Options




def open_Loginpage(type='teacher'):

    chrome_options=Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    wd=webdriver.Chrome(options=chrome_options)
    wd.implicitly_wait(5)
    wd.get(host+type+login)
    GSTORE['wd']=wd
    return wd



class teacherLogin:

    def teacher_login(self,username,passwd):

        self.wd=open_Loginpage()
        input_username=self.wd.find_element(By.ID,"username")
        input_username.send_keys(username)

        input_passwd=self.wd.find_element(By.ID,"password")
        input_passwd.send_keys(passwd)

        self.wd.find_element(By.ID,'submit').click()

        self.wd.implicitly_wait(5)

    def GetHome(self):


        self.wd.find_element(By.CSS_SELECTOR,"a[href='#/home']>li").click()

        time.sleep(2)

        eles = self.wd.find_elements(By.CSS_SELECTOR,'#home_div .ng-binding')

        return [ele.text for ele in eles]


    def Go_StudentGroup(self):
        time.sleep(2)
        title=self.wd.find_element(By.CSS_SELECTOR,".main-menu>ul li:nth-of-type(4)")
        titleActions=ActionChains(self.wd)
        titleActions.move_to_element(title).perform()
        self.wd.find_element(By.CSS_SELECTOR,'a[href*="student_group"]>li').click()


    def student_list(self):
        panel=self.wd.find_element(By.CSS_SELECTOR,'.panel-green')
        panel.click()
        time.sleep(4)
        names=panel.find_elements(By.CSS_SELECTOR,'.panel-body tbody>tr .ng-binding')

        namelist=[ name.text for name in names]

        return namelist

    def Go_addhomework(self):
        time.sleep(2)
        title=self.wd.find_element(By.CSS_SELECTOR,".main-menu>ul li:nth-of-type(2)")
        titleActions=ActionChains(self.wd)
        titleActions.move_to_element(title).perform()
        self.wd.find_element(By.XPATH,'//span[text()="创 建 作 业"]').click()

    
    def add_homework(self,name,num=None):
        self.wd.implicitly_wait(5)
        inputname=self.wd.find_element(By.ID,'exam_name_text')
        inputname.send_keys(name)

        self.wd.find_element(By.ID,'btn_pick_question').click()
        time.sleep(10)
        # self.wd.switch_to.alert.accept()
        if num is not None:
            picksup=self.wd.find_elements(By.CSS_SELECTOR,'.div-search-question .btn_pick_question')
            for i in range(1,num):
                picksup[i].click()

        if num == None:

                self.wd.find_element(By.CSS_SELECTOR,'#cart_footer>div:nth-child(2)').click()

                
        
        self.wd.find_element(By.CSS_SELECTOR,'.btn-blue').click()
        time.sleep(2)
        self.wd.find_element(By.ID,'btn_submit').click()

        
        time.sleep(10)




TLogin=teacherLogin()


if __name__ == '__main__':

    TLogin.teacher_login('jcyrss','sdfsdf5%')
    TLogin.Go_addhomework()
    TLogin.add_homework('2131222')
    # print(InfoList)