class PartTimer:
    hour_rate = 7500
    total_part_timers = 0

    def __init__(self, name, place = '113동'):
        self.nickname = name
        self.total_wage = 0
        self.workplace = place
        self.total_part_timers += 1

    def getnickname() :
        return '저의 닉네임은 {}입니다.'.format(self.nickname)

    def calculate_wage(self, h):
        daily_wage = PartTimer.hour_rate * h
        self.total_wage += daily_wage
        return self.total_wage
