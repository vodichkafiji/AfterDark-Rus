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

screen mapweekdayparker_screen(g=mapweekdayparker_girls):
    add "mapweekdayparker_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekdayparker_button_animation
            action i.action
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("mapweekdayparker_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekdayparker_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekdayparker_bg = class_click("mapweekdayparker_bg", "mapweekdayparker_bg", None, (0, 0))
default mapweekdayparker_park = class_click("Park", "mapweekdayparker_park", Jump("mapweekdayparker_park"), (0, 5))
default mapweekdayparker_city = class_click("City", "mapweekdayparker_city", Jump("mapweekdayparker_city"), (1075, 0))
default mapweekdayparker_mall = class_click("Mall", "mapweekdayparker_mall", Jump("mapweekdayparker_mall"), (2890, 0))
default mapweekdayparker_smart = class_click("Smart", "mapweekdayparker_smart", Jump("mapweekdayparker_smart"), (1040, 790))
default mapweekdayparker_bar = class_click("Bar", "mapweekdayparker_bar", Jump("mapweekdayparker_bar"), (2120, 610))
default mapweekdayparker_apartment = class_click("Apartment", "mapweekdayparker_apartment", Jump("mapweekdayparker_apartment"), (296, 1230))
default mapweekdayparker_skate = class_click("Skate", "mapweekdayparker_skate", Jump("mapweekdayparker_skate"), (1310, 1000))
default mapweekdayparker_school = class_click("School", "mapweekdayparker_school", Jump("mapweekdayparker_school"), (2260, 1020))

default mapweekdayparker_girls = class_handler(
    [
        mapweekdayparker_bg, mapweekdayparker_park, mapweekdayparker_city, mapweekdayparker_mall, mapweekdayparker_smart, mapweekdayparker_bar, mapweekdayparker_apartment, mapweekdayparker_skate,  mapweekdayparker_school
  
    ]
    )

label mapweekdayparker_example:
    call screen mapweekdayparker_screen

label mapweekdayparker_park:
    scene mapweekdayparker_bg
    "Парк сейчас закрыт."
    jump mapweekdayparker_example

label mapweekdayparker_city:
    scene mapweekdayparker_bg
    if parkercityintro == 0:
        jump parkercityintro
    else:
        jump mondaycity_eveningparker
label mapweekdayparker_mall:
    scene mapweekdayparker_bg
    "Торговый центр сейчас закрыт."
    jump mapweekdayparker_example
label mapweekdayparker_skate:
    scene mapweekdayparker_bg
    "Скейтпарк сейчас закрыт."
    jump mapweekdayparker_example

label mapweekdayparker_apartment:
    scene mapweekdayparker_bg
    jump weekdaybedroomnoon_example

label mapweekdayparker_bar:
    scene mapweekdayparker_bg
    "Бар не открывается так рано."
    jump mapweekdayparker_example

label mapweekdayparker_smart:
    scene mapweekdayparker_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekdayparker_example

label mapweekdayparker_school:
    scene mapweekdayparker_bg
    jump firsthallway1_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
