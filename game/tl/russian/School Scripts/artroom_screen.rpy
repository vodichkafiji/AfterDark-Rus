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

screen artroom_screen(g=artroom_girls):
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at artroom_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("thirdhallway3_example")
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
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("artroom_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform artroom_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default artroom_bg = class_click("artroom_bg", "artroom_bg", None, (0, 0))
default artroom_mei = class_click("mei", "artroom_mei", Jump("artroom_mei"), (1240, 375))


default artroom_girls = class_handler(
    [
        artroom_bg,
        artroom_mei,
    ]
    )

label artroom_example:
    if intro_mei == 1 and meipaintintro == 0:
        jump meipaintevents
    call screen artroom_screen

label artroom_mei:
    jump paint_room_mei
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
