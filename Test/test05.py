import time
import Person

# 클래스 객체
number = [10, 20, 30]
print(dir(number))

p = Person.Person('Sung', 44)
print(p.age)
print(p.name)
print(p.getAge())
print(p.total)

john = Person.Person("John Doe", 35)
print(john.name)


# https://code.visualstudio.com/docs/editor/settings-sync#_troubleshooting-keychain-issuese