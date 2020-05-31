import random
from statistics import mean


# Интенсивность поступления закеазов в минуту
prob = 0.95
# Среднее время обслуживания в минутах
handle_time = 1
# Величина интервала моделирования в минутах
minutes_for_model = 60 * 24 * 365  # год


# Массив со временами обслуживания в минутах отсчитывамых с нуля
rings = []
last_ring_time = 0.0
for minute in range(0, minutes_for_model - 1):
    rnd = random.expovariate(prob)
    if(rnd <= 0.0):
        print("rnd = ", str(rnd), " < 0")
    last_ring_time += rnd
    rings.append(last_ring_time)

rings.sort()  # Выставим заказы в порядке возрастания

handles = []
lambd = 1.0 / handle_time  # Интенсивность потока для времени разговора
for ring in rings:
    rnd = random.expovariate(lambd)
    handles.append(rnd)


reject_count = 0
for ring in range(0, len(rings) - 2):
    handle_end = rings[ring] + handles[ring]  # Время окончания обслуживания
    # Если заявка поступила во время обслуживания предыдущей
    if rings[ring + 1] < handle_end:
        reject_count += 1  # то ей отказано в обслуживании

reject_prob = reject_count / len(rings)
print("Вероятность отказа в обслуживании = " + str(reject_prob))

all_time_of_work = (rings[-1] + handles[-1])

work_percent = sum(handles) / all_time_of_work
print("Нагрузка устройства обслуживания = " + str(work_percent))

# Среднее время пребывания заявки в системе равно времени обслуживания
# (заявки начинают обслуживаться немедленно,
#  заявки недообслуживаются и очередь отсутствует)
avg_time = mean(handles)
print("Среднее время пребывания заявки в системе = {} минут".format(avg_time))

print("=================================")
print("Минимальное время обслуживания в минутах " + str(min(handles)))
print("Максимальное время обслуживания в минутах " + str(max(handles)))