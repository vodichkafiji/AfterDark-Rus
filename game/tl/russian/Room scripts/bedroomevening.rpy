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

screen bedroomevening_screen(g=bedroomevening_girls):
    add "bedroomevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at bedroomevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("livingroomevening_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_eveningmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("bedroomnight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("bedroomevening_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/Bedroomevening/bedroomevening_computer.webp"
        hover "images/point and click room/Bedroomevening/bedroomevening_computer.webp"
        action Jump("bedroomevening_computer")
        xpos 5
        ypos 1150
        at bedroomevening_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform bedroomevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define bedroomevening_bg = class_click("bedroomevening_bg", "bedroomevening_bg", None, (0, 0))
define bedroomevening_skelly = class_click("Skelly", "bedroomevening_skelly", Jump("bedroomevening_skelly"), (1180, 140))
define bedroomevening_kitsune = class_click("Kitsune", "bedroomevening_kitsune", Jump("bedroomevening_kitsune"), (1380, 775))
define bedroomevening_wallofshit = class_click("Wallofshit", "bedroomevening_wallofshit", Jump("bedroomevening_wallofshit"), (1850,0))
define bedroomevening_computer = class_click("Computer", "bedroomevening_computer", Jump("bedroomevening_computer"), (0,1130))

define bedroomevening_girls = class_handler(
    [
        bedroomevening_bg,
        bedroomevening_skelly, bedroomevening_kitsune,  bedroomevening_wallofshit, bedroomevening_computer,
    ]
    )

label bedroomevening_example:
    $ computer == 0
    call screen bedroomevening_screen

label bedroomevening_skelly:
    scene bedroomevening_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump bedroomevening_example
label bedroomevening_kitsune:

    scene bedroomevening_bg
    k "Чёрт, зацени, какой красивый закат."
    k "А ты опять решил провести его запершись в своей комнате."
    jump bedroomevening_example
label bedroomevening_wallofshit:
    scene bedroomevening_bg
    "Ах, моя пресловутая «Стена с дерьмом, которое я считаю крутым»."
    "Непрактично? {w} Да."
    "Нёсет ли она какую-то пользу? {w} Нет."
    "Будет ли туда и дальше безнадобно добавляться всякий хлам? {w} Чёрт возьми, да."
    "Но там есть ещё парочка игр, в которые тебе стоит заглянуть, если ещё этого не сделал."
    jump bedroomevening_example

label bedroomevening_computer:
    scene computer_day with fade
    $ computer = 3
    "Ты подходишь к компьютеру."
    play sound "audio/sound/pcon.mp3"
    jump computerscreen

label bedroomevening_exitcomputer:
    scene computer_day with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump bedroomevening_example
return