



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

screen mall1morning_screen(g=mall1morning_girls):
    add "mall1morning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall1morning_button_animation
            action i.action
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_morningmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mall1noon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("mall1morning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall1morning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall1morning_bg = class_click("mall1morning_bg", "mall1morning_bg", None, (0, 0))
default mall1morning_stairs = class_click("stairs", "mall1morning_stairs", Jump("mall1morning_stairs"), (0, 310))


default mall1morning_girls = class_handler(
    [
        mall1morning_bg, mall1morning_stairs
  
    ]
    )

label mall1morning_example:
    if noragymintro == 1 and noramallintro == 0:
        jump nora_mall_intro
    else:
        play ambient "audio/ambient/mall.mp3" volume 0.5
        call screen mall1morning_screen


label mall1morning_stairs:
    jump mall2morning_example

label mall1morning_example2:
    call screen mall1morning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
