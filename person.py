class Person(object):

    total = 0

    def __init__(self, name , age): # self만 있을시 기본 생성자
        self.name = name
        self.age = age

    def getAge(self):
        return self.age