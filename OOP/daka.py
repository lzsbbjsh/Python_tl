'''
作用网易云课堂打卡
'''

class PythonStudent():
    teacher = "大拿"
    def daka(self):
        print("{0}拿教的好,每天打个卡".format(self.teacher))

Jack = PythonStudent()
Jack.daka()