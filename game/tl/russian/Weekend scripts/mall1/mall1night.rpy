



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

screen mall1night_screen(g=mall1night_girls):
    add "mall1night_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall1night_button_animation
            action i.action
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_nightmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    use oscar_freeroam_inventory_button3
    imagebutton:
        idle "night_idle.png"
        hover "night_idle.png"
        action Jump("mall1night_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall1night_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall1night_bg = class_click("mall1night_bg", "mall1night_bg", None, (0, 0))
default mall1night_stairs = class_click("stairs", "mall1night_stairs", Jump("mall1night_stairs"), (0, 209))


default mall1night_girls = class_handler(
    [
        mall1night_bg, mall1night_stairs
  
    ]
    )

label mall1night_example:
    stop music fadeout 1.0
    play ambient "audio/ambient/night.mp3" volume 0.5
    call screen mall1night_screen


label mall1night_stairs:
    jump mall2night_example

label mall1night_example2:
    call screen mall1night_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
