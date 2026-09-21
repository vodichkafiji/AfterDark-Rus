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

screen mapweekdaynoon_screen(g=mapweekdaynoon_girls):
    add "mapweekdaynoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekdaynoon_button_animation
            action i.action
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("mapweekdaynoon_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekdaynoon_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekdaynoon_bg = class_click("mapweekdaynoon_bg", "mapweekdaynoon_bg", None, (0, 0))
default mapweekdaynoon_park = class_click("Park", "mapweekdaynoon_park", Jump("mapweekdaynoon_park"), (0, 5))
default mapweekdaynoon_city = class_click("City", "mapweekdaynoon_city", Jump("mapweekdaynoon_city"), (1075, 0))
default mapweekdaynoon_mall = class_click("Mall", "mapweekdaynoon_mall", Jump("mapweekdaynoon_mall"), (2890, 0))
default mapweekdaynoon_smart = class_click("Smart", "mapweekdaynoon_smart", Jump("mapweekdaynoon_smart"), (1040, 790))
default mapweekdaynoon_bar = class_click("Bar", "mapweekdaynoon_bar", Jump("mapweekdaynoon_bar"), (2120, 610))
default mapweekdaynoon_apartment = class_click("Apartment", "mapweekdaynoon_apartment", Jump("mapweekdaynoon_apartment"), (296, 1230))
default mapweekdaynoon_skate = class_click("Skate", "mapweekdaynoon_skate", Jump("mapweekdaynoon_skate"), (1310, 1000))
default mapweekdaynoon_school = class_click("School", "mapweekdaynoon_school", Jump("mapweekdaynoon_school"), (2260, 1020))

default mapweekdaynoon_girls = class_handler(
    [
        mapweekdaynoon_bg, mapweekdaynoon_park, mapweekdaynoon_city, mapweekdaynoon_mall, mapweekdaynoon_smart, mapweekdaynoon_bar, mapweekdaynoon_apartment, mapweekdaynoon_skate,  mapweekdaynoon_school
  
    ]
    )

label mapweekdaynoon_example:
    call screen mapweekdaynoon_screen

label mapweekdaynoon_park:
    scene mapweekdaynoon_bg
    "Парк сейчас закрыт."
    jump mapweekdaynoon_example

label mapweekdaynoon_city:
    scene mapweekdaynoon_bg
    "Город сейчас недоступен."
    jump mapweekdaynoon_example
label mapweekdaynoon_mall:
    scene mapweekdaynoon_bg
    "Торговый центр сейчас закрыт."
    jump mapweekdaynoon_example
label mapweekdaynoon_skate:
    scene mapweekdaynoon_bg
    "Скейтпарк сейчас закрыт."
    jump mapweekdaynoon_example

label mapweekdaynoon_apartment:
    scene mapweekdaynoon_bg
    jump weekdaybedroomnoon_example

label mapweekdaynoon_bar:
    scene mapweekdaynoon_bg
    "Бар не открывается так рано."
    jump mapweekdaynoon_example

label mapweekdaynoon_smart:
    scene mapweekdaynoon_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekdaynoon_example

label mapweekdaynoon_school:
    scene mapweekdaynoon_bg
    jump firsthallway1_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
