init python:

    class class_click:
        def __init__(self, name, image, action, pos):
            self.name = name
            self.image = image
            self.action = action
            self.pos = pos

    class class_handler:
        def __init__(self,clicks):
            self.clicks = clicks

screen mapweekdayevening_screen(g=mapweekdayevening_girls):
    add "mapweekdayevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekdayevening_button_animation
            action i.action
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("mapweekdayevening_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekdayevening_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekdayevening_bg = class_click("mapweekdayevening_bg", "mapweekdayevening_bg", None, (0, 0))
default mapweekdayevening_park = class_click("Park", "mapweekdayevening_park", Jump("mapweekdayevening_park"), (0, 5))
default mapweekdayevening_city = class_click("City", "mapweekdayevening_city", Jump("mapweekdayevening_city"), (1075, 0))
default mapweekdayevening_mall = class_click("Mall", "mapweekdayevening_mall", Jump("mapweekdayevening_mall"), (2880, 0))
default mapweekdayevening_smart = class_click("Smart", "mapweekdayevening_smart", Jump("mapweekdayevening_smart"), (1060, 800))
default mapweekdayevening_bar = class_click("Bar", "mapweekdayevening_bar", Jump("mapweekdayevening_bar"), (2030, 630))
default mapweekdayevening_apartment = class_click("Apartment", "mapweekdayevening_apartment", Jump("mapweekdayevening_apartment"), (296, 1250))
default mapweekdayevening_skate = class_click("Skate", "mapweekdayevening_skate", Jump("mapweekdayevening_skate"), (1260, 1000))
default mapweekdayevening_school = class_click("School", "mapweekdayevening_school", Jump("mapweekdayevening_school"), (2230, 1010))

default mapweekdayevening_girls = class_handler(
    [
        mapweekdayevening_bg, mapweekdayevening_park, mapweekdayevening_city, mapweekdayevening_mall, mapweekdayevening_smart, mapweekdayevening_bar, mapweekdayevening_apartment, mapweekdayevening_skate,  mapweekdayevening_school
  
    ]
    )

label mapweekdayevening_example:
    call screen mapweekdayevening_screen

label mapweekdayevening_park:
    scene mapweekdayevening_bg
    "Парк сейчас закрыт."
    jump mapweekdayevening_example

label mapweekdayevening_city:
    scene mapweekdayevening_bg
    "Город сейчас недоступен."
    jump mapweekdayevening_example
label mapweekdayevening_mall:
    scene mapweekdayevening_bg
    "Торговый центр сейчас закрыт."
    jump mapweekdayevening_example
label mapweekdayevening_skate:
    if junehallway1 == 1 and juneskatepark == 0:
        jump june_skatepark
    else:
        scene mapweekdayevening_bg
        "Скейтпарк сейчас закрыт."
        jump mapweekdayevening_example

label mapweekdayevening_apartment:
    scene mapweekdayevening_bg
    jump weekdaybedroomevening_example

label mapweekdayevening_bar:
    scene mapweekdayevening_bg
    "Бар не открывается так рано."
    jump mapweekdayevening_example

label mapweekdayevening_smart:
    scene mapweekdayevening_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekdayevening_example

label mapweekdayevening_school:
    scene mapweekdayevening_bg
    "На сегодня занятия закончились."
    jump mapweekdayevening_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
