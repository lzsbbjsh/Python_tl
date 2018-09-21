'''
定义一个学生类,形容学生
'''

#空的类,使用pass
class Student():
    #如果pass没有,会报错
    pass

#定义一个对象
mingyue = Student()

class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #注意doHomework的缩进的层级,
    #seld参数需注意

    def doHomework(self):
        print("I 在做作业")

        #在函数末尾,使用return
        return None

yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)


#注意调用的时候没有传入参数
yueyue.doHomework()
