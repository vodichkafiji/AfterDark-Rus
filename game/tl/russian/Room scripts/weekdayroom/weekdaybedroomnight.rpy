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

screen weekdaybedroomnight_screen(g=weekdaybedroomnight_girls):
    add "weekdaybedroomnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaybedroomnight_button_animation
            action i.action
    imagebutton:

        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action If(junepolice == 1, Jump("weekdaylivingroomnightjune_example"), Jump("weekdaylivingroomnight_example"))
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0


    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekday_nightmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "night_idle.png"
        hover "night_idle.png"
        action Jump("weekdaybedroomnight_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/weekdayBedroomnight/weekdaybedroomnight_computer.webp"
        hover "images/point and click room/weekdayBedroomnight/weekdaybedroomnight_computer.webp"
        action Jump("weekdaybedroomnight_computer")
        xpos 5
        ypos 1150
        at weekdaybedroomnight_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaybedroomnight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define weekdaybedroomnight_bg = class_click("weekdaybedroomnight_bg", "weekdaybedroomnight_bg", None, (0, 0))
define weekdaybedroomnight_skelly = class_click("Skelly", "weekdaybedroomnight_skelly", Jump("weekdaybedroomnight_skelly"), (1190, 190))
define weekdaybedroomnight_kitsune = class_click("Kitsune", "weekdaybedroomnight_kitsune", Jump("weekdaybedroomnight_kitsune"), (2150, 190))
define weekdaybedroomnight_bed = class_click("Bed", "weekdaybedroomnight_bed", Jump("weekdaybedroomnight_bed"), (839,972))


define weekdaybedroomnight_girls = class_handler(
    [
        weekdaybedroomnight_bg,
        weekdaybedroomnight_skelly, weekdaybedroomnight_kitsune,  weekdaybedroomnight_bed, 
    ]
    )

label weekdaybedroomnight_example:
    if junehelp == 1 and junepanick == 0:
        jump june_panick
    if kyra_recruitment == 1 and kyragangevent == 0:
        scene weekdaybedroomnight_bg
        stop music fadeout 1.0
        mc "Так, ладно, я всё приготовил."
        mc "Пора идти вступать в банду...{w} Наверное..."
        mc "(Это так глупо.)"
        jump kyra_initiation_night
    else:
        $ computer == 0
        play music "audio/Music/Nights.mp3"
        call screen weekdaybedroomnight_screen

label weekdaybedroomnight_skelly:
    scene weekdaybedroomnight_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump weekdaybedroomnight_example
label weekdaybedroomnight_kitsune:
    if pushupintro == 0:
        jump pushupintro
    elif pushupintro == 1 and main.strength >= 5 and intro_2 == 1 and intro3 == 1 and intro_jordyn == 1 and intro_brooklyn == 1 and intro_june == 1 and intro_mei == 1 and intro_nora == 1 and intro_yuki == 1 and intro_yejin == 1 and firstfight ==0:
        jump first_fight
    elif kyraalleyevent == 1 and firstdream == 0:
        jump thefirstdream
    elif pillowtrain == 1 and yejin_train == 1 and chromarkwarehouse == 0:
        jump warehouse_investigation
    else:
        scene bedroomnight_bg
        k "Ну так что, мы будем тренироваться? Или ты так и будешь весь вечер сопли на кулак наматывать?"
        mc "Я тебе чуть позже отвечу."
        jump bedroomnight_example

label weekdaybedroomnight_bed:
    scene weekdaybedroomnight_bg
    call screen bed_options
    jump weekdaybedroomnight_example

label weekdaybedroomnight_computer:
    scene black
    scene computer_night with fade
    $ computer = 7
    "Ты подходишь к компьютеру."
    play sound "audio/sound/pcon.mp3"
    jump computerscreen

label weekdaybedroomnight_exitcomputer:

    scene computer_night with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump weekdaybedroomnight_example
return