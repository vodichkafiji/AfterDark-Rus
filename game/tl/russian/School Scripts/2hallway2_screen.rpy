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

screen secondhallway2_screen(g=secondhallway2_girls):
    add "secondhallway2_bg"

    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at secondhallway2_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("secondhallway1_example")
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
        action Jump("secondhallway2_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform secondhallway2_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default secondhallway2_bg = class_click("secondhallway2_bg", "secondhallway2_bg", None, (0, 0))
default secondhallway2_brooklyn = class_click("Brooklyn", "secondhallway2_brooklyn", Jump("secondhallway2_brooklyn"), (317, 415))
default secondhallway2_door = class_click("Door", "secondhallway2_door", Jump("secondhallway2_door"), (1500, 210))


default secondhallway2_girls = class_handler(
    [
        secondhallway2_bg,
        secondhallway2_brooklyn, secondhallway2_door,
    ]
    )

label secondhallway2_example:
    if brooklyntalent2 == 1 and brooklyntalent_signup == 0:
        jump brooklyn_talentshow_signup
    else:
        scene secondhallway2_bg
        call screen secondhallway2_screen

label secondhallway2_brooklyn:
    if intro_brooklyn == 1:
        jump brooklynhallevents
    else:
        scene secondhallway2_bg
        "В первую очередь, тебе нужно представиться Бруклину в классе."
    jump secondhallway2_example

label secondhallway2_door:
    scene avoclass_bg with dissolve
    jump avoclass_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
