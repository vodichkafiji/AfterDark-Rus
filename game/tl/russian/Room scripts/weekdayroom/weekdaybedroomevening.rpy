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

screen weekdaybedroomevening_screen(g=weekdaybedroomevening_girls):
    add "weekdaybedroomevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaybedroomevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action If(junepolice == 1, Jump("weekdaylivingroomeveningjune_example"), Jump("weekdaylivingroomevening_example"))
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0


    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("demo_mapeve")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("weekdaybedroomnight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("weekdaybedroomevening_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/weekdayBedroomevening/weekdaybedroomevening_computer.webp"
        hover "images/point and click room/weekdayBedroomevening/weekdaybedroomevening_computer.webp"
        action Jump("weekdaybedroomevening_computer")
        xpos 5
        ypos 1150
        at weekdaybedroomevening_button_animation

    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaybedroomevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define weekdaybedroomevening_bg = class_click("weekdaybedroomevening_bg", "weekdaybedroomevening_bg", None, (0, 0))
define weekdaybedroomevening_skelly = class_click("Skelly", "weekdaybedroomevening_skelly", Jump("weekdaybedroomevening_skelly"), (1180, 140))
define weekdaybedroomevening_kitsune = class_click("Kitsune", "weekdaybedroomevening_kitsune", Jump("weekdaybedroomevening_kitsune"), (1380, 775))
define weekdaybedroomevening_wallofshit = class_click("Wallofshit", "weekdaybedroomevening_wallofshit", Jump("weekdaybedroomevening_wallofshit"), (1850,0))

define weekdaybedroomevening_girls = class_handler(
    [
        weekdaybedroomevening_bg,
        weekdaybedroomevening_skelly, weekdaybedroomevening_kitsune,  weekdaybedroomevening_wallofshit, 
    ]
    )

label weekdaybedroomevening_example:
    call screen weekdaybedroomevening_screen

label weekdaybedroomevening_skelly:
    scene weekdaybedroomevening_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump weekdaybedroomevening_example
label weekdaybedroomevening_kitsune:
    if storydream2 == 1 and pillowtrain == 0:
        jump brighttalk
    elif firstfight == 1 and yukibook2event == 1 and yukikitsunebook == 0:
        jump Kitsune_book
    else:
        scene weekdaybedroomevening_bg
        k "Чёрт, зацени, какой красивый закат."
        k "А ты опять решил провести его запершись в своей комнате."
        jump weekdaybedroomevening_example
label weekdaybedroomevening_wallofshit:
    scene weekdaybedroomevening_bg
    "Ах, моя пресловутая «Стена с дерьмом, которое я считаю крутым»."
    "Непрактично? {w} Да."
    "Нёсет ли она какую-то пользу? {w} Нет."
    "Будет ли туда и дальше безнадобно добавляться всякий хлам? {w} Чёрт возьми, да."
    "Но там есть ещё парочка игр, в которые тебе стоит заглянуть, если ещё этого не сделал."
    jump weekdaybedroomevening_example

label weekdaybedroomevening_computer:
    scene computer_day with fade
    $ computer = 5
    play sound "audio/sound/pcon.mp3"
    "Ты подходишь к компьютеру."
    jump computerscreen


label weekdaybedroomevening_exitcomputer:
    scene computer_day with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump weekdaybedroomevening_example
return