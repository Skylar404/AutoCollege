import json
import requests
from cfg.cfg import *

# 
class teacher:

    def printResponse(self,response):
        for j,r in response.headers.items():
            print(f'{j}:{r}')

        print('------response--------------')
        print(response.content.decode('utf8'))    

        # obj=response.json()

        # return obj


    def list_teacher(self,subjectid=None):
        urlparams={
            'vcode':vcode,
            'action':'search_with_pagenation',
        }

        if subjectid != None:
            urlparams['subjectid']=subjectid

        list_response= requests.get(f'{host}{t_url}',params=urlparams)

        # obj=response.json()
        self.printResponse(list_response)
        
        return list_response


    def add_teacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber):
        """
        Add a teacher to the system.
        classlist: 1, 2, 3, ... (format of class IDs)
        """
        
        classid=str(classlist).split(',')
        classlist=[{'id':int(cid.strip())} for cid in classid]
        print(classlist)
        
        data={
            'vcode':vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':subjectid,
            'classlist':json.dumps(classlist),
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber

        }
        response=requests.post(f'{host}{t_url}',data=data)

        self.printResponse(response)
        return response


    def update_teacher(self,teacherid,realname,subjectid,classlist,phonenumber,email,idcardnumber):
        """
        Add a teacher to the system.
        classlist: [1, 2, 3, ...] (List of class IDs)
        """
        classid=str(classlist).split(',')
        classlist=[{'id':int(cid.strip())} for cid in classid]
        print(classlist)

        data={
            'vcode':vcode,
            'action':'modify',
            # 'username':username,
            'realname':realname,
            'subjectid':subjectid,
            'classlist':json.dumps(classlist),
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber

        }
        response=requests.put(f'{host}{t_url}/{teacherid}',data=data)
        print("修改教师")
        self.printResponse(response)

        return response
    
    def del_teacher(self,teacherid):
        data={
            'vcode':vcode,
        }
        response=requests.delete(f'{host}{t_url}/{teacherid}',data=data)

        self.printResponse(response)
        return response


    def clear_all_teacher(self):
        response=self.list_teacher()
        obj=response.json()
        for i in obj["retlist"]:
            self.del_teacher(i["id"])
        print("清除全部老师")


        #     
ST=teacher()


if __name__ == '__main__':
    ST.add_teacher('test123','李世民',1,'20320',13451813456,'jcysdf@123.com','3209251983090987899')
    # steacher.clear_all_teacher()
    ST.list_teacher(1)

    # ST.del_teacher(5214)

