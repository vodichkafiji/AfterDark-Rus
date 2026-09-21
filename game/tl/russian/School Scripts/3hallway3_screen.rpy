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

screen thirdhallway3_screen(g=thirdhallway3_girls):
    add "thirdhallway3_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at thirdhallway3_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("thirdhallway2_example")
        xpos 0.15
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
        action Jump("weekday_evening")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "gui/quicknav_idle.png"
        hover "gui/quicknav_hover.png"
        action Call("show_quicknav")
        xpos 0.73
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
    imagebutton:
        idle "quest_idle.png"
        hover "quest_hover.png"
        action ShowMenu("quests")
        xpos 0.63
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("thirdhallway3_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform thirdhallway3_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default thirdhallway3_bg = class_click("thirdhallway3_bg", "thirdhallway3_bg", None, (0, 0))
default thirdhallway3_artdoor = class_click("artdoor", "thirdhallway3_artdoor", Jump("thirdhallway3_artdoor"), (1920, 440))
default thirdhallway3_dancedoor = class_click("Dancedoor", "thirdhallway3_dancedoor", Jump("thirdhallway3_dancedoor"), (1255, 510))



default thirdhallway3_girls = class_handler(
    [
        thirdhallway3_bg,
        thirdhallway3_dancedoor, thirdhallway3_artdoor,
    ]
    )

label thirdhallway3_example:
    scene thirdhallway3_bg
    call screen thirdhallway3_screen

label thirdhallway3_artdoor:
    if intro_mei == 1:
        jump meipaintevents
    else:
        scene thirdhallway3_bg
        "В первую очередь, тебе нужно представиться Мей в классе."
        jump thirdhallway3_example

label thirdhallway3_dancedoor:

    if intro3 == 1 and izra20event == 0:
        jump izraballetevents
    elif izra20event == 1 and izra25event == 0 and izra30event == 0:
        scene thirdhallway3_bg
        "Ты пытаешься найти Изу в классе."
        "Но здесь никого нет."
        "Похоже, она тебя избегает."
        jump thirdhallway3_example
    elif izra30event == 1 and izraclimaxevent == 0:
        scene thirdhallway3_bg
        mc "...."
        mc "Я не хочу здесь находиться."
        mc "Я не могу смотреть ей в глаза после того, что произошло."
        jump thirdhallway3_example
    elif izraclimaxevent == 1:
        jump izraballetevents
    else:
        scene thirdhallway3_bg
        "Дверь заперта. Но изнутри доносится причудливая музыка."
        jump thirdhallway3_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
