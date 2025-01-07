from lib.API.Sclass import *
from hytest import *


def suite_setup():
        response=sclass.add_class(1,'实验2班',80)
        obj=response.json()
        GSTORE['cid']=obj['id']
        GSTORE['invitecode']=obj["invitecode"]
        INFO("添加七年实验2班")

def suite_teardown():
        cid=GSTORE['cid']
        sclass.del_class(cid)
        INFO("清除七年实验2班")
