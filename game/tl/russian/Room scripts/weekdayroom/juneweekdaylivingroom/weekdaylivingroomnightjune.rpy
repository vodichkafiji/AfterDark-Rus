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

screen weekdaylivingroomnightjune_screen(g=weekdaylivingroomnightjune_girls):
    add "weekdaylivingroomnightjune_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaylivingroomnightjune_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("weekdaybedroomnight_example")
        xpos 0.99
        ypos 0.99
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
        action Jump("weekdaylivingroomight_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5

    imagebutton:
        idle "images/point and click room/weekdaylivingroomnightjune/nightjune.png"
        hover "images/point and click room/weekdaylivingroomnightjune/nightjune.png"
        action Jump("nightjunecouch")
        xpos 2270
        ypos 470
        at weekdaylivingroomnightjune_button_animation


    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaylivingroomnightjune_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default weekdaylivingroomnightjune_bg = class_click("weekdaylivingroomnightjune_bg", "weekdaylivingroomnightjune_bg", None, (0, 0))


default weekdaylivingroomnightjune_girls = class_handler(
    [
        weekdaylivingroomnightjune_bg
  
    ]
    )

label weekdaylivingroomnightjune_example:
    scene weekdaylivingroomnightjune_bg
    call screen weekdaylivingroomnightjune_screen


label nightjunecouch:
    scene black with dissolve
    "Ты подходишь, чтобы посмотреть на Джун."
    scene nightjunecouch (1) with dissolve
    "Похоже, она крепко спит."

    mc "(Ей многое пришлось пережить... Интересно, сколько бессонных ночей было у неё самой.)"

    "Ты и сам не знаешь почему, но не имея возможности заснуть..."

    "Видя, как другие мирно спят, ты чувствуешь облегчение."

    mc "(Она...{w} красива даже когда видит сны.)"

    j "Если собрался дрочить на моё тело, смотри не кончи на диван."
    scene nightjunecouch (2) with hpunch
    mc "!!!"

    mc "Ты что, всё это время не спала!?"

    j "Хе-хе."

    j "Ну? Ты сделаешь это?"
    scene nightjunecouch (3) with dissolve
    j "Честно говоря, мне сейчас всё равно."

    mc "Э-эм, может в другой раз..."

    j "Как знаешь, [mcname]"

    "Тебе не хотелось ей отказывать, но то, что тебя поймали за жутковатым разглядыванием, немного испортило настрой."
    "{i}Джун получит больше H-контента в будущих обновлениях. Следите за новостями!{/i}"
    scene weekdaylivingroomnightjune_bg
    jump weekdaylivingroomnightjune_example
return