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

screen bedroomnoon_screen(g=bedroomnoon_girls):
    add "bedroomnoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at bedroomnoon_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("livingroomnoon_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_noonmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("bedroomevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("bedroomnoon_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/Bedroomnoon/bedroomnoon_computer.webp"
        hover "images/point and click room/Bedroomnoon/bedroomnoon_computer.webp"
        action Jump("bedroomnoon_computer")
        xpos 5
        ypos 1150
        at bedroomnoon_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform bedroomnoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define bedroomnoon_bg = class_click("bedroomnoon_bg", "bedroomnoon_bg", None, (0, 0))
define bedroomnoon_skelly = class_click("Skelly", "bedroomnoon_skelly", Jump("bedroomnoon_skelly"), (1138, 103))
define bedroomnoon_kitsune = class_click("Kitsune", "bedroomnoon_kitsune", Jump("bedroomnoon_kitsune"), (1730, 385))



define bedroomnoon_girls = class_handler(
    [
        bedroomnoon_bg,
        bedroomnoon_skelly, bedroomnoon_kitsune, 
    ]
    )

label bedroomnoon_example:
    $ computer == 0
    call screen bedroomnoon_screen

label bedroomnoon_skelly:
    scene bedroomnoon_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump bedroomnoon_example
label bedroomnoon_kitsune:

    scene bedroomnoon_bg
    "Похоже, Кицунэ медитирует... или практикует магию... или...{w} типа того."
    mc "(Была бы она такой же полезной в моих тренировках.)"
    jump bedroomnoon_example

label bedroomnoon_computer:
    scene computer_day with fade
    $ computer = 2
    "Ты подходишь к компьютеру."
    play sound "audio/sound/pcon.mp3"
    jump computerscreen

label bedroomnoon_exitcomputer:
    scene black
    scene computer_day with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump bedroomnoon_example
return