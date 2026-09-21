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

screen weekdaybedroomnoon_screen(g=weekdaybedroomnoon_girls):
    add "weekdaybedroomnoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaybedroomnoon_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("weekdaylivingroomnoon_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("demo_menus")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("weekdaybedroomevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("weekdaybedroomnoon_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/weekdayBedroomnoon/weekdaybedroomnoon_computer.webp"
        hover "images/point and click room/weekdayBedroomnoon/weekdaybedroomnoon_computer.webp"
        action Jump("weekdaybedroomnoon_computer")
        xpos 5
        ypos 1150
        at weekdaybedroomnoon_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaybedroomnoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default weekdaybedroomnoon_bg = class_click("weekdaybedroomnoon_bg", "weekdaybedroomnoon_bg", None, (0, 0))
default weekdaybedroomnoon_skelly = class_click("Skelly", "weekdaybedroomnoon_skelly", Jump("weekdaybedroomnoon_skelly"), (1138, 103))
default weekdaybedroomnoon_kitsune = class_click("Kitsune", "weekdaybedroomnoon_kitsune", Jump("weekdaybedroomnoon_kitsune"), (1730, 385))


default weekdaybedroomnoon_girls = class_handler(
    [
        weekdaybedroomnoon_bg,
        weekdaybedroomnoon_skelly, weekdaybedroomnoon_kitsune, 
    ]
    )

label weekdaybedroomnoon_example:
    call screen weekdaybedroomnoon_screen

label weekdaybedroomnoon_skelly:
    scene weekdaybedroomnoon_bg
    "Подпишись на @skelly.art в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump weekdaybedroomnoon_example
label weekdaybedroomnoon_kitsune:

    scene weekdaybedroomnoon_bg
    "Похоже, Кицунэ медитирует... или практикует магию... или...{w} типа того."
    mc "(Была бы она такой же полезной в моих тренировках.)"
    jump weekdaybedroomnoon_example

label weekdaybedroomnoon_computer:
    scene computer_day with fade
    $ computer = 6
    "Ты подходишь к компьютеру."
    jump computerscreen

label weekdaybedroomnoon_exitcomputer:
    scene computer_day with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump weekdaybedroomnoon_example
return