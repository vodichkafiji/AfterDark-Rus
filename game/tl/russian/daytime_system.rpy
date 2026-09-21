define time_names = ["День","Ночь"]
define max_time = 2
define day_names = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

default time = 0

init python:
    def pass_time():
            store.time += 1
            if store.time >= max_time-1:
                next_day(0)

    def next_day(at_time = 0):
        store.day += 1
        store.time = at_time




screen time_screen():
    hbox:
        spacing 20
        text "{}".format(day_names[day % 7])
        text "{}".format(time_names[time % max_time])