import requests
from cfg.cfg import *

# 
class Sclass:

    def printResponse(self,response):
        for j,r in response.headers.items():
            print(f'{j}:{r}')

        print('------response--------------')
        print(response.content.decode('utf8'))    

        # obj=response.json()

        # return obj


    def list_class(self,gradeid=None):
        urlparams={
            'vcode':vcode,
            'action':'list_classes_by_schoolgrade',
        }

        if gradeid != None:
            urlparams['gradeid']=gradeid

        response= requests.get(f'{host}{a_url}',params=urlparams)

        # obj=response.json()
        self.printResponse(response)
        
        return response


    def add_class(self,grade,name,studentlimit):
        data={
            'vcode':vcode,
            'action':'add',
            'grade':grade,
            'name':name,
            'studentlimit':studentlimit

        }
        response=requests.post(f'{host}{a_url}',data=data)

        self.printResponse(response)
        return response


    def update_class(self,classid,name,studentlimit):
        data={
            'vcode':vcode,
            'action':'modify',
            'name':name,
            'studentlimit':studentlimit

        }
        response=requests.put(f'{host}{a_url}/{classid}',data=data)
        print("修改班级名称")
        self.printResponse(response)

        return response
    
    def del_class(self,classid):
        data={
            'vcode':vcode,
        }
        response=requests.delete(f'{host}{a_url}/{classid}',data=data)

        self.printResponse(response)
        return response


    def clear_all_class(self):
        response=self.list_class()
        obj=response.json()
        for i in obj["retlist"]:
            self.del_class(i["id"])
        print("清除全部班级")


        #     
sclass=Sclass()

if __name__ == '__main__':
    # 这里的代码仅在直接运行该文件时执行
    # sclass.add_class(1,'实验1班',80)
    sclass.clear_all_class()
    # sclass.list_class(1)

