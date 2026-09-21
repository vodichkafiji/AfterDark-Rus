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

screen bedroommorning_screen(g=bedroommorning_girls):
    add "bedroommorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at bedroommorning_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("livingroommorning_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_morningmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("bedroomnoon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("bedroommorning_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/Bedroommorning/bedroommorning_computer.webp"
        hover "images/point and click room/Bedroommorning/bedroommorning_computer.webp"
        action Jump("bedroommorning_computer")
        xpos 5
        ypos 1150
        at bedroommorning_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5






transform bedroommorning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define bedroommorning_bg = class_click("bedroommorning_bg", "bedroommorning_bg", None, (0, 0))
define bedroommorning_skelly = class_click("Skelly", "bedroommorning_skelly", Jump("bedroommorning_skelly"), (1180, 200))
define bedroommorning_kitsune = class_click("Kitsune", "bedroommorning_kitsune", Jump("bedroommorning_kitsune"), (920, 716))
define bedroommorning_wallofshit = class_click("Wallofshit", "bedroommorning_wallofshit", Jump("bedroommorning_wallofshit"), (1775,-87))

define bedroommorning_girls = class_handler(
    [
        bedroommorning_bg,
        bedroommorning_skelly, bedroommorning_kitsune,  bedroommorning_wallofshit,
    ]
    )

label bedroommorning_example:
    call screen bedroommorning_screen

label bedroommorning_skelly:
    scene bedroommorning_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump bedroommorning_example
label bedroommorning_kitsune:

    scene bedroommorning_bg
    k "Вы, людишки, и ваша одержимость утрами. Солнце встаёт, птички поют, а вы всё такие же несчастные, как и когда ложились спать."
    mc "Ну ты уж точно не добавляешь мне оптимизма на сегодняшний день."
    jump bedroommorning_example

label bedroommorning_wallofshit:
    scene bedroommorning_bg
    "Ах, моя пресловутая «Стена с дерьмом, которое я считаю крутым»."
    "Непрактично? {w} Да."
    "Нёсет ли она какую-то пользу? {w} Нет."
    "Будет ли туда и дальше безнадобно добавляться всякий хлам? {w} Чёрт возьми, да."
    "Но там есть ещё парочка игр, в которые тебе стоит заглянуть, если ещё этого не сделал."
    jump bedroommorning_example

label bedroommorning_computer:
    scene computer_day with fade
    $ computer = 1
    "Ты подходишь к компьютеру."
    play sound "audio/sound/pcon.mp3"
    jump computerscreen


label bedroommorning_exitcomputer:
    scene computer_day with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump bedroommorning_example
return