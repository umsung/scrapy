
# 定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能

from enum import Enum,unique

# Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Month.Jan)


class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday.Sun.value)


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            raise ValueError('error')

s = Student('duan',Gender.Male)
print(s.gender)
print(s.gender == Gender.Male)