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

screen mapweekdayutami_screen(g=mapweekdayutami_girls):
    add "mapweekdayutami_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekdayutami_button_animation
            action i.action
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("mapweekdayutami_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "Day [totaldays]" size 130 font "ArissaTypeface.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekdayutami_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekdayutami_bg = class_click("mapweekdayutami_bg", "mapweekdayutami_bg", None, (0, 0))
default mapweekdayutami_park = class_click("Park", "mapweekdayutami_park", Jump("mapweekdayutami_park"), (0, 5))
default mapweekdayutami_city = class_click("City", "mapweekdayutami_city", Jump("mapweekdayutami_city"), (1025, 0))
default mapweekdayutami_mall = class_click("Mall", "mapweekdayutami_mall", Jump("mapweekdayutami_mall"), (2890, 0))
default mapweekdayutami_smart = class_click("Smart", "mapweekdayutami_smart", Jump("mapweekdayutami_smart"), (1040, 790))
default mapweekdayutami_bar = class_click("Bar", "mapweekdayutami_bar", Jump("mapweekdayutami_bar"), (2120, 610))
default mapweekdayutami_apartment = class_click("Apartment", "mapweekdayutami_apartment", Jump("mapweekdayutami_apartment"), (296, 1230))
default mapweekdayutami_skate = class_click("Skate", "mapweekdayutami_skate", Jump("mapweekdayutami_skate"), (1310, 1000))
default mapweekdayutami_school = class_click("School", "mapweekdayutami_school", Jump("mapweekdayutami_school"), (2260, 1020))

default mapweekdayutami_girls = class_handler(
    [
        mapweekdayutami_bg, mapweekdayutami_park, mapweekdayutami_city, mapweekdayutami_mall, mapweekdayutami_smart, mapweekdayutami_bar, mapweekdayutami_apartment, mapweekdayutami_skate,  mapweekdayutami_school
  
    ]
    )

label mapweekdayutami_example:
    call screen mapweekdayutami_screen

label mapweekdayutami_park:
    scene mapweekdayutami_bg
    "Парк сейчас закрыт."
    jump mapweekdayutami_example

label mapweekdayutami_city:
    scene mapweekdayutami_bg
    if utamihairintro == 0:
        jump utami_hair_intro
    elif utamihairintro == 1 and utamisurf == 0:
        jump utami_beach_one
    elif utamisurf == 1 and utamibeachbj == 0:
        jump utami_beach_two
    else:
        jump city_noonutami

label mapweekdayutami_mall:
    scene mapweekdayutami_bg
    "Торговый центр сейчас закрыт."
    jump mapweekdayutami_example
label mapweekdayutami_skate:
    scene mapweekdayutami_bg
    "Скейтпарк сейчас закрыт."
    jump mapweekdayutami_example

label mapweekdayutami_apartment:
    scene mapweekdayutami_bg
    jump weekdaybedroomnoon_example

label mapweekdayutami_bar:
    scene mapweekdayutami_bg
    "Бар не открывается так рано."
    jump mapweekdayutami_example

label mapweekdayutami_smart:
    scene mapweekdayutami_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekdayutami_example

label mapweekdayutami_school:
    scene mapweekdayutami_bg
    jump firsthallway1_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
