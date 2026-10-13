



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

screen mall1evening_screen(g=mall1evening_girls):
    add "mall1evening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall1evening_button_animation
            action i.action
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_eveningmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mall1night_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("mall1evening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall1evening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall1evening_bg = class_click("mall1evening_bg", "mall1evening_bg", None, (0, 0))
default mall1evening_stairs = class_click("stairs", "mall1evening_stairs", Jump("mall1evening_stairs"), (0, 250))


default mall1evening_girls = class_handler(
    [
        mall1evening_bg, mall1evening_stairs
  
    ]
    )




label mall1evening_example:
    if noragymintro == 1 and noramallintro == 0:
        jump nora_mall_intro
    else:
        play ambient "audio/ambient/mall.mp3" volume 0.5
        call screen mall1evening_screen


label mall1evening_stairs:
    jump mall2evening_example

label mall1evening_example2:
    call screen mall1evening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
