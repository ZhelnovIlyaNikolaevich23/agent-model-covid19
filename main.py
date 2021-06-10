import random
import numpy as np
import matplotlib.pyplot as plt


class Agent:
    def __init__(self):
        self.age = random.randint(1, 90)
        self.sick = False
        self.sick_day = 0
        self.recovered = False
        self.death = False
        self.symptoms = False
        # self.serious_illnesses =

    def sicked(self):
        self.sick = True

    def die(self):
        self.death = True

    def is_dead(self):
        return self.death

    def is_sick(self):
        return self.sick

    def is_symptoms(self):
        return self.symptoms

    def is_recovered(self):
        return self.recovered

    def get_age(self):
        return self.age

    def next_day_sick(self):
        self.sick_day += 1
        if self.sick_day > 5:
            self.symptoms = True
        if self.sick_day >= 20:
            self.sick = False
            self.sick_day = 0
            self.recovered = True


def make_agens(size):
    # list_of_agents = list()
    list_of_agents = np.zeros(size, dtype=Agent)
    for s in range(size):
        list_of_agents[s] = Agent()
    return list_of_agents


def sick_prob():
    p = 6
    probability = random.randint(0, 1000)
    if probability > 1000 - p:
        return True
    return False


def death_probability(a):
    p = random.randint(0, 90000)
    if a.get_age() <= 9:
        pb = 3
    elif 9 < a.get_age() <= 40:
        pb = 20
    elif 40 < a.get_age() <= 50:
        pb = 40
    elif 50 < a.get_age() <= 60:
        pb = 130
    elif 6 < a.get_age() <= 70:
        pb = 360
    elif 7 < a.get_age() <= 80:
        pb = 800
    elif a.get_age() > 80:
        pb = 1480
    if p <= pb:
        return True
    return False


def try_sick(a, list_of_agents, size, coef):
    count_of_contacts = random.randint(5, coef)
    people_at_risk = np.array([random.randint(0, size - 1) for c in range(count_of_contacts)])
    if a.is_sick():
        for p in people_at_risk:
            if sick_prob():
                list_of_agents[p].sicked()

    return list_of_agents


def draw_plot(c, days):
    off_data = [56, 80, 87, 119, 152, 194, 224, 292, 339, 404, 458, 517, 646, 759, 860, 929, 1002, 1096, 1214, 1367, 1574, 1663, 1794, 1944, 2123, 2443, 2695, 2852, 3026, 3298, 3610, 3886, 4180, 4442, 4733, 5087, 5358, 5596, 5903, 6132, 6413, 6692, 6952, 7209, 7413, 7615, 7826, 8047, 8276, 8504, 8735, 8963, 9244, 9533, 9834, 10149, 10503, 10850, 11169, 11499]
    plt.plot([i for i in range(days)], c)
    plt.plot([i for i in range(days)], off_data)
    plt.show()


def cycle(list_of_agents, days, size):
    coef = 34  # коэффицент, показывающий количество людей, которые передвигаются на общественном транспорте
    list_of_sicks = list()
    for d in range(days):
        count_of_sicked = 0
        count_of_dead = 0
        count_of_recovered = 0
        for a in list_of_agents:
            if d > 33:
                coef = 19
            if d > 46:
                coef = 15
            if a.is_dead():
                count_of_dead += 1
                continue
            if a.is_recovered():
                count_of_recovered += 1
            if a.is_sick():
                count_of_sicked += 1
                list_of_agents = try_sick(a, list_of_agents, size, coef)
                a.next_day_sick()
                if a.is_symptoms():
                    if death_probability(a):
                        a.die()
        list_of_sicks.append(count_of_sicked)
    print('число заболевших = ', count_of_sicked)
    print('число умерших = ', count_of_dead)
    print('число выздоровевших = ', count_of_recovered)
    draw_plot(list_of_sicks, days)


def choice_start_sick(list_of_agents, count, size):
    people_at_risk = np.array([random.randint(0, size)for c in range(count)])
    for p in people_at_risk:
        list_of_agents[p].sicked()
    return list_of_agents


def start():
    count_of_sick = 160  # изначальное число зараженных (на 5 апреля)
    size = 1200000  # общее число агентов
    days = 60  # длительность эксперимента
    list_of_agents = make_agens(size)
    list_of_agents = choice_start_sick(list_of_agents, count_of_sick, size)
    cycle(list_of_agents, days, size)



start()