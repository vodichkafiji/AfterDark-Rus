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

screen thirdhallway2_screen(g=thirdhallway2_girls):
    add "thirdhallway2_bg"

    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at thirdhallway2_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("thirdhallway1_example")
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
        idle "quest_idle.png"
        hover "quest_hover.png"
        action ShowMenu("quests")
        xpos 0.63
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
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
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("thirdhallway2_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform thirdhallway2_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default thirdhallway2_bg = class_click("thirdhallway2_bg", "thirdhallway2_bg", None, (0, 0))
default thirdhallway2_ayako = class_click("ayako", "thirdhallway2_ayako", Jump("thirdhallway2_ayako"), (0, 340))
default thirdhallway2_left = class_click("left", "thirdhallway2_left", Jump("thirdhallway2_left"), (690, 0))


default thirdhallway2_girls = class_handler(
    [
        thirdhallway2_bg,
        thirdhallway2_ayako, thirdhallway2_left,
    ]
    )

label thirdhallway2_example:
    scene thirdhallway2_bg
    call screen thirdhallway2_screen

label thirdhallway2_ayako:
    scene thirdhallway2_bg
    "Сначала тебе нужно представиться Миссис Аяко"
    "(Недоступно в текущем обновлении.)"
    jump thirdhallway2_example

label thirdhallway2_left:
    jump thirdhallway3_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
