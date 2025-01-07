import json
import requests
from cfg.cfg import *
from lib.API.Sclass import *

# 
class Student:

    def printResponse(self,response):
        for j,r in response.headers.items():
            print(f'{j}:{r}')

        print('------response--------------')
        print(response.content.decode('utf8'))    

        # obj=response.json()

        # return obj


    def list_student(self):
        urlparams={
            'vcode':vcode,
            'action':'search_with_pagenation',
        }


        list_response= requests.get(f'{host}{s_url}',params=urlparams)

        # obj=response.json()
        self.printResponse(list_response)
        
        return list_response


    def add_student(self,username,realname,gradeid,classid,phonenumber):
        
        data={
            'vcode':vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'gradeid':gradeid,
            'classid':classid,
            'phonenumber':phonenumber,

        }
        response=requests.post(f'{host}{s_url}',data=data)

        self.printResponse(response)
        return response


    def update_student(self,studentid,realname=None,phonenumber=None):

        data={
            'vcode':vcode,
            'action':'modify',
            'realname':realname,
            'phonenumber':phonenumber,


        }
        response=requests.put(f'{host}{s_url}/{studentid}',data=data)
        print("修改学生信息")
        self.printResponse(response)

        return response
    
    def del_student(self,studentid):
        data={
            'vcode':vcode,
        }
        response=requests.delete(f'{host}{s_url}/{studentid}',data=data)

        self.printResponse(response)
        return response


    def clear_all_student(self):
        response=self.list_student()
        obj=response.json()
        for i in obj["retlist"]:
            self.del_student(i["id"])
        print("清除全部学生")


        #     
Student=Student()

if __name__ == '__main__':
    # sclass.add_class(1,'实验1班',80)

    # sclass.list_class(1)
    Student.add_student('zz','张三',5,20283,13451813456)
    # Student.list_student()

    # Student.del_student(2122)

    Student.clear_all_student()