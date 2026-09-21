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

screen mapweekendevening_screen(g=mapweekendevening_girls):
    add "mapweekendevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mapweekendevening_button_animation
            action i.action
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mapweekendnight_example")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("mapweekendevening_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform mapweekendevening_button_animation:
    on idle:
        matrixcolor None
    on hover:
        matrixcolor BrightnessMatrix(0.3)

default mapweekendevening_bg = class_click("mapweekendevening_bg", "mapweekendevening_bg", None, (0, 0))
default mapweekendevening_park = class_click("Park", "mapweekendevening_park", Jump("mapweekendevening_park"), (0, 5))
default mapweekendevening_city = class_click("City", "mapweekendevening_city", Jump("mapweekendevening_city"), (1075, 0))
default mapweekendevening_mall = class_click("Mall", "mapweekendevening_mall", Jump("mapweekendevening_mall"), (2805, -45))
default mapweekendevening_smart = class_click("Smart", "mapweekendevening_smart", Jump("mapweekendevening_smart"), (960, 805))
default mapweekendevening_bar = class_click("Bar", "mapweekendevening_bar", Jump("mapweekendevening_bar"), (2030, 625))
default mapweekendevening_apartment = class_click("Apartment", "mapweekendevening_apartment", Jump("mapweekendevening_apartment"), (275, 1225))
default mapweekendevening_skate = class_click("Skate", "mapweekendevening_skate", Jump("mapweekendevening_skate"), (1300, 1000))
default mapweekendevening_school = class_click("School", "mapweekendevening_school", Jump("mapweekendevening_school"), (2255, 1000))

default mapweekendevening_girls = class_handler(
    [
        mapweekendevening_bg, mapweekendevening_park, mapweekendevening_city, mapweekendevening_mall, mapweekendevening_smart, mapweekendevening_bar, mapweekendevening_apartment, mapweekendevening_skate,  mapweekendevening_school
  
    ]
    )

label mapweekendevening_example:
    scene mapweekendevening_bg
    if renpy.music.get_playing(channel="music") is None:
        play music "audio/Music/eveweek.mp3"
    call screen mapweekendevening_screen

label mapweekendevening_park:
    if lilyroofintro == 1:
        jump lilyzooevents
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        jump zooevening_example

label mapweekendevening_city:
    if junesmokeintro == 1:
        jump junealleyevents
    else:
        play ambient "audio/ambient/City.mp3" volume 0.5
        scene black
        scene city2 with fade
        "Ты начинаешь исследовать город."
        "Ты бродишь без цели. Хотя в одиночку это довольно скучно."
        "Уже довольно поздно, и ты решаешь закончить на этом."
        jump mapweekendevening_example

label mapweekendevening_mall:
    if intro_grace == 1:
        jump gracemallevents
    else:
        play ambient "audio/ambient/Mall.mp3" volume 0.4
        scene black
        scene mallevening with fade
        "Ты приезжаешь в торговый центр."
        "Уже становится довольно поздно, и магазины сейчас закрываются."
        jump mall1evening_example

label mapweekendevening_skate:

    if intro_zara == 1:
        jump zaraskateevents
    else:
        play ambient "audio/ambient/Skatepark.mp3" volume 0.5
        scene black
        scene skatepark1 with fade
        "Ты направляешься в скейтпарк."
        jump skateparkevening_example


label mapweekendevening_apartment:
    jump bedroomevening_example

label mapweekendevening_bar:
    scene mapweekendevening_bg
    "Бар не открывается так рано."
    jump mapweekendevening_example

label mapweekendevening_smart:
    if yukilibraryintro == 1:
        jump yukiconevents
    else:
        scene mapweekendevening_bg
        play ambient "audio/ambient/City.mp3" volume 0.5
        "Ты бродишь без дела. Хотя в одиночку это довольно скучно."
        "Ты уже собирался пойти в круглосуточный магазин, но вспомнил, что случилось в прошлый раз."
        mc "Похоже, придётся найти другое место, куда пойти."
        "Ты решаешь, что это проблема на другой день."
        jump mapweekendevening_example

label mapweekendevening_school:
    scene mapweekendevening_bg
    "Школа недоступна по выходным"
    jump mapweekendevening_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
