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

screen mapweekendmorning_screen(g=mapweekendmorning_girls):
    add "mapweekendmorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekendmorning_button_animation
            action i.action
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mapweekendnoon_example")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("mapweekendmorning_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekendmorning_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekendmorning_bg = class_click("mapweekendmorning_bg", "mapweekendmorning_bg", None, (0, 0))
default mapweekendmorning_park = class_click("Park", "mapweekendmorning_park", Jump("mapweekendmorning_park"), (0, 5))
default mapweekendmorning_city = class_click("City", "mapweekendmorning_city", Jump("mapweekendmorning_city"), (1120, 75))
default mapweekendmorning_mall = class_click("Mall", "mapweekendmorning_mall", Jump("mapweekendmorning_mall"), (2930, 7))
default mapweekendmorning_smart = class_click("Smart", "mapweekendmorning_smart", Jump("mapweekendmorning_smart"), (1060, 770))
default mapweekendmorning_bar = class_click("Bar", "mapweekendmorning_bar", Jump("mapweekendmorning_bar"), (2085, 585))
default mapweekendmorning_apartment = class_click("Apartment", "mapweekendmorning_apartment", Jump("mapweekendmorning_apartment"), (275, 1225))
default mapweekendmorning_skate = class_click("Skate", "mapweekendmorning_skate", Jump("mapweekendmorning_skate"), (1300, 947))
default mapweekendmorning_school = class_click("School", "mapweekendmorning_school", Jump("mapweekendmorning_school"), (2260, 1020))

default mapweekendmorning_girls = class_handler(
    [
        mapweekendmorning_bg, mapweekendmorning_park, mapweekendmorning_city, mapweekendmorning_mall, mapweekendmorning_smart, mapweekendmorning_bar, mapweekendmorning_apartment, mapweekendmorning_skate,  mapweekendmorning_school
  
    ]
    )

label mapweekendmorning_example:
    scene mapweekendmorning_bg
    if renpy.music.get_playing(channel="music") is None:
        play music "audio/Music/Acting.mp3"
    call screen mapweekendmorning_screen

label mapweekendmorning_park:
    if meipaintintro == 1:
        jump meihillevents
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        scene black
        scene park with fade
        "Сегодня в парке тихо. Ты решаешь прогуляться."
        "Щебетание птиц — приятный звук. Хотя, честно говоря, тебе хотелось бы быть дома."
        jump parkcrossroadsmorning_example

label mapweekendmorning_city:
    if rileylibraryintro == 1:
        jump rileyarcadeevents
    else:

        play ambient "audio/ambient/City.wav" volume 0.5
        scene black
        scene city with fade
        "Ты отправляешься в город."
        "В это время суток нигде не открыто, чтобы развеять скуку."
        "Если хочешь чем-то заняться, придётся поближе познакомиться с людьми."
        jump mapweekendmorning_example
label mapweekendmorning_mall:

    if brooklynhallintro == 1:
        jump brooklyncafeevents
    else:

        play ambient "audio/ambient/Mall.mp3" volume 0.5
        scene black
        scene mall with fade
        "Ты приезжаешь в торговый центр."
        jump mall1morning_example

label mapweekendmorning_skate:
    if izraballetintro == 1 and izra20event == 0:
        scene skatepark with fade
        "Ты направляешься в скейтпарк."
        jump izracityevents
    elif izra20event == 1 and izra25event == 0 and izra30event == 0:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        scene skatepark with fade
        "Ты пытаешься найти Изру в скейтпарке."
        "Похоже, она тебя избегает."
        jump skateparknoon_example
    elif izra30event == 1 and izraclimaxevent == 0:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        scene skatepark with fade
        mc "...."
        mc "Я не хочу здесь находиться."
        mc "Я не могу смотреть ей в глаза после того, что произошло."
        jump skateparknoon_example
    else:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        scene black
        scene skatepark with fade
        "Ты направляешься в скейтпарк."
        jump skateparkmorning_example

label mapweekendmorning_apartment:
    jump bedroommorning_example

label mapweekendmorning_bar:
    scene mapweekendmorning_bg
    "Бар не открывается так рано."
    jump mapweekendmorning_example

label mapweekendmorning_smart:
    scene mapweekendmorning_bg
    "Тебе сейчас ничего не нужно в магазине."
    jump mapweekendmorning_example

label mapweekendmorning_school:
    scene mapweekendmorning_bg
    "Школа недоступна по выходным"
    jump mapweekendmorning_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
