# 변수 기본
n = 1
name = 'Sung'
n = n + 2
value = 1.2 * n

# print('{0} = 1.2 * {1}'.format(value, n))
# print(name)

# 문자(배열) 인덱스 방법
greeting = 'Hello World'
# print(greeting[0])  # H
# print(greeting[2:5]) # llo
# print(greeting[:2])  # l
# print(greeting[-2:])    # ld
# print(greeting * 2)

# List
numbers = [0, 1, 2, 3]
# print(numbers)
# print(numbers[0])
# print(numbers[2:4])
names = ['Kim', 'Lee', 'Park', 'Choi']
array = numbers + names
# print(array)
# print(array[-1])
# print(array * 2)
array[3] = 7
# print(array)

# Tuple
person = ('Kim', 24, 'male')
print(person)
print(person[1])
#person[1] = 45
name, age, gender = person
print(gender)

print('github 추가 내용입니다.')