from lib.API.Sclass import *
from hytest import *
from lib.API.teacher import *
from lib.API.Student import *


def suite_setup():
    sclass.clear_all_class()
    INFO("删除所有班级")
    ST.clear_all_teacher()
    INFO("删除所有老师")
    Student.clear_all_student()
    INFO("删除所有学生")