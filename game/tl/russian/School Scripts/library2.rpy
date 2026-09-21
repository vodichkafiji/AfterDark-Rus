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

screen library2_screen(g=library2_girls):
    add "library2_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at library2_button_animation
            action i.action

    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("library1_example")
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
        action Jump("library2_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform library2_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default library2_bg = class_click("library2_bg", "library2_bg", None, (0, 0))
default library2_riley = class_click("Riley", "library2_riley", Jump("library2_riley"), (1380, 335))



default library2_girls = class_handler(
    [
        library2_bg,
        library2_riley, 
    ]
    )
label library2_example:
    scene library2_bg
    call screen library2_screen


label library2_riley:
    if intro_2 == 1:
        jump rileylibraryevents
    else:
        scene library2_bg
        "В первую очередь, тебе нужно представиться Райли в классе."
        jump library2_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
