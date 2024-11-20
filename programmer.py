from enum import Enum
import random
import math
from constants import name_list

SALARY_BASE = 100

class Programmer():
    def __init__(self, score):
        self.rank = Rank.choose_rank(score)
        self.name = random.choice(name_list.names)
        self.age = random.randint(20, 65)
        self.salary = Rank.calculate_salary(SALARY_BASE, self.rank)
        skills = self.split_points(self.rank)
        self.creativity = skills[0]
        self.productivity = skills[1]
        self.teamwork = skills[2]
        self.leadership = skills[3]
        self.knowledge = skills[4]
        self.innovation = skills[5]

    @classmethod
    def split_points(self, rank):
        result = []
        points = Rank[rank].value[1]
        for i in range(5):
            skill_value = random.randint(1, math.ceil(points*0.8))
            result.append(skill_value)
            points -= skill_value
        result.append(points)
        random.shuffle(result)
        return result


class Rank(Enum):
    INTERN = (500, 100)
    JUNIOR = (2000, 200)
    MID = (5000, 400)
    SENIOR = (10000, 600)
    LEAD = (50000, 800)
    MANAGER = (200000, 1000)
    DIRECTOR = (500000, 1500)

    @classmethod
    def choose_rank(cls, score):
        ranks = list(cls)
        for idx in range(len(ranks)):
            if score < ranks[0].value[0]:
                return random.choice([ranks[0].name, ranks[1].name])
            elif score >= ranks[idx].value[0]:
                if idx == len(ranks) - 1 or score < ranks[idx + 1].value[0]:
                    choice = random.randint(1, 10)
                    if choice <= 6:
                        return ranks[idx].name
                    elif choice <= 9 and idx + 1 < len(ranks):
                        return ranks[idx + 1].name
                    elif idx + 2 < len(ranks):
                        return ranks[idx + 2].name
                    else:
                        return ranks[idx].name
        return None

    @classmethod
    def calculate_salary(cls, base, rank):
        return base * Rank[rank].value[1] * (random.randint(70, 130) / 100)