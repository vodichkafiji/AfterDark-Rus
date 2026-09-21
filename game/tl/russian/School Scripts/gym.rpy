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

screen gym_screen(g=gym_girls):
    add "gym_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at gym_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("firsthallway3_example")
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
        action Jump("gym_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform gym_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default gym_bg = class_click("gym_bg", "gym_bg", None, (0, 0))
default gym_zara = class_click("Zara", "gym_zara", Jump("gym_zara"), (2355, 340))
default gym_nora = class_click("Nora", "gym_nora", Jump("gym_nora"), (1340, 480))


default gym_girls = class_handler(
    [
        gym_bg,
        gym_zara, gym_nora
    ]
    )

label gym_example:
    scene gym_bg
    call screen gym_screen

label gym_zara:
    if storydream1 == 1 and storydream2 == 0:
        jump gym_coffee_for_zara
    if intro_zara == 0:
        jump zara_intro
    else:
        jump gym_coffee_for_zara


label gym_nora:
    if intro_nora == 1:
        jump noragymevents
    else:
        scene gym_bg
        "В первую очередь, тебе нужно представиться Норе в классе."
        jump gym_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
