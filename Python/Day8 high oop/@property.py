class Student(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
s.score  # OK，实际转化为s.get_score()
""" s.score = 9999 报错，因为不符合11行条件"""

# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
