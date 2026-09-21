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

screen danceroom_screen(g=danceroom_girls):
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at danceroom_button_animation
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
        action Jump("danceroom_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform danceroom_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default danceroom_bg = class_click("danceroom_bg", "danceroom_bg", None, (0, 0))
default danceroom_izra = class_click("izra", "danceroom_izra", Jump("danceroom_izra"), (1765, 420))


default danceroom_girls = class_handler(
    [
        danceroom_bg,
        danceroom_izra,
    ]
    )

label danceroom_example:
    call screen danceroom_screen

label danceroom_izra:
    if Izra.affection >= 15 and totaldays >= 15 and izra10event == 1 and izra15event == 0:
        jump izra_15_event
    elif izrabj == 1:
        jump Izrafun
    else:
        jump ballet_with_izra

    jump danceroom_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
