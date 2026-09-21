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

screen firsthallway2_screen(g=firsthallway2_girls):
    add "firsthallway2_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at firsthallway2_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("firsthallway1_example")
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
        action Jump("firsthallway2_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform firsthallway2_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default firsthallway2_bg = class_click("firsthallway2_bg", "firsthallway2_bg", None, (0, 0))
default firsthallway2_hall = class_click("Stairs", "firsthallway2_hall", Jump("firsthallway2_hall"), (450, 0))



default firsthallway2_girls = class_handler(
    [
        firsthallway2_bg,
        firsthallway2_hall,
    ]
    )

label firsthallway2_example:
    scene firsthallway2_bg
    call screen firsthallway2_screen

label firsthallway2_hall:
    jump firsthallway3_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
