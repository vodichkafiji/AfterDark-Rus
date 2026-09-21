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

screen mapweekendnoon_screen(g=mapweekendnoon_girls):
    add "mapweekendnoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekendnoon_button_animation
            action i.action
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mapweekendevening_example")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("mapweekendnoon_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekendnoon_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekendnoon_bg = class_click("mapweekendnoon_bg", "mapweekendnoon_bg", None, (0, 0))
default mapweekendnoon_park = class_click("Park", "mapweekendnoon_park", Jump("mapweekendnoon_park"), (0, 5))
default mapweekendnoon_city = class_click("City", "mapweekendnoon_city", Jump("mapweekendnoon_city"), (1075, 0))
default mapweekendnoon_mall = class_click("Mall", "mapweekendnoon_mall", Jump("mapweekendnoon_mall"), (2875, 7))
default mapweekendnoon_smart = class_click("Smart", "mapweekendnoon_smart", Jump("mapweekendnoon_smart"), (1060, 770))
default mapweekendnoon_bar = class_click("Bar", "mapweekendnoon_bar", Jump("mapweekendnoon_bar"), (2085, 585))
default mapweekendnoon_apartment = class_click("Apartment", "mapweekendnoon_apartment", Jump("mapweekendnoon_apartment"), (275, 1225))
default mapweekendnoon_skate = class_click("Skate", "mapweekendnoon_skate", Jump("mapweekendnoon_skate"), (1300, 1000))
default mapweekendnoon_school = class_click("School", "mapweekendnoon_school", Jump("mapweekendnoon_school"), (2260, 1020))

default mapweekendnoon_girls = class_handler(
    [
        mapweekendnoon_bg, mapweekendnoon_park, mapweekendnoon_city, mapweekendnoon_mall, mapweekendnoon_smart, mapweekendnoon_bar, mapweekendnoon_apartment, mapweekendnoon_skate,  mapweekendnoon_school
  
    ]
    )

label mapweekendnoon_example:
    scene mapweekendnoon_bg
    if renpy.music.get_playing(channel="music") is None:
        play music "audio/Music/Acting.mp3"

    call screen mapweekendnoon_screen

label mapweekendnoon_park:
    if jordyntrackintro == 1:
        jump jordynparkevents
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        scene black
        scene park with fade
        "The park is quiet today. You decide to go for a walk"
        jump parkcrossroadsnoon_example

label mapweekendnoon_city:
    if yejinclassintro == 1:

        jump yejindojoevents
    else:
        play ambient "audio/ambient/City.mp3" volume 0.5
        scene black
        scene city with fade
        "Сегодня в парке тихо. Ты решаешь прогуляться."
        "Ты бродишь без дела. Хотя в одиночестве это довольно скучно."
        jump mapweekendnoon_example
label mapweekendnoon_mall:
    if noragymintro == 1:
        jump noramallevents
    else:

        play ambient "audio/ambient/Mall.mp3" volume 0.5
        scene mall with fade
        "Ты бродишь по торговому центру, но ничего интересного так и не находишь."
        jump mall1noon_example

label mapweekendnoon_skate:

    if autumntvintro == 1:
        jump autumnskateevents
    else:
        play ambient "audio/ambient/Skatepark.mp3" volume 0.5
        scene black
        scene skatepark with fade
        "Ты направляешься в скейтпарк."
        jump skateparknoon_example


label mapweekendnoon_apartment:
    jump bedroomnoon_example

label mapweekendnoon_bar:
    scene mapweekendnoon_bg
    "Бар не открывается так рано."
    jump mapweekendnoon_example

label mapweekendnoon_smart:
    scene mapweekendnoon_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekendnoon_example

label mapweekendnoon_school:
    scene mapweekendnoon_bg
    "Школа недоступна по выходным"
    jump mapweekendnoon_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
