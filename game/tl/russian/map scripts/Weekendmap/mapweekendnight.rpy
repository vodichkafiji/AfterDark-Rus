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

screen mapweekendnight_screen(g=mapweekendnight_girls):
    add "mapweekendnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekendnight_button_animation
            action i.action
    imagebutton:
        idle "night_idle.png"
        hover "night_idle.png"
        action Jump("mapweekendnight_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekendnight_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekendnight_bg = class_click("mapweekendnight_bg", "mapweekendnight_bg", None, (0, 0))
default mapweekendnight_park = class_click("Park", "mapweekendnight_park", Jump("mapweekendnight_park"), (0, 3))
default mapweekendnight_city = class_click("City", "mapweekendnight_city", Jump("mapweekendnight_city"), (1085, 0))
default mapweekendnight_mall = class_click("Mall", "mapweekendnight_mall", Jump("mapweekendnight_mall"), (2860, 0))
default mapweekendnight_smart = class_click("Smart", "mapweekendnight_smart", Jump("mapweekendnight_smart"), (1020, 760))
default mapweekendnight_bar = class_click("Bar", "mapweekendnight_bar", Jump("mapweekendnight_bar"), (2060, 625))
default mapweekendnight_apartment = class_click("Apartment", "mapweekendnight_apartment", Jump("mapweekendnight_apartment"), (260, 1235))
default mapweekendnight_skate = class_click("Skate", "mapweekendnight_skate", Jump("mapweekendnight_skate"), (1300, 1000))


default mapweekendnight_girls = class_handler(
    [
        mapweekendnight_bg, mapweekendnight_park, mapweekendnight_city, mapweekendnight_mall, mapweekendnight_smart, mapweekendnight_bar, mapweekendnight_apartment, mapweekendnight_skate, 
  
    ]
    )

label mapweekendnight_example:
    scene mapweekendnight_bg
    if renpy.music.get_playing(channel="music") is None:
        play music "audio/Music/Nights.mp3"
    elif renpy.music.get_playing(channel="ambient") is None:
        play ambient "audio/ambient/night.mp3"
    call screen mapweekendnight_screen

label mapweekendnight_park:
    jump parkcrossroadsnight_example

label mapweekendnight_city:
    "Город сейчас недоступен."
    jump mapweekendnight_example

label mapweekendnight_mall:
    jump mall1night_example

label mapweekendnight_skate:
    jump skateparknight_example

label mapweekendnight_apartment:
    jump bedroomnight_example

label mapweekendnight_bar:
    scene mapweekendnight_bg
    if intro_2 == 1:
        jump tamarabarevents
    else:
        mc "Что? Зачем мне идти в бар? Мне ещё недостаточно лет, чтобы пить."
        mc "Если я не знаю кого-то, кто владеет баром, то в этом нет смысла."
        jump mapweekendnight_example

label mapweekendnight_smart:
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekendnight_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
