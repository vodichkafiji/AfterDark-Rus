



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

screen fountainnight_screen(g=fountainnight_girls):
    add "fountainnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at fountainnight_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("parkcrossroadsnight_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0
    use oscar_freeroam_inventory_button3
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_nightmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "night_idle.png"
        hover "night_idle.png"
        action Jump("fountainnight_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform fountainnight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default fountainnight_bg = class_click("fountainnight_bg", "fountainnight_bg", None, (0, 0))


default fountainnight_girls = class_handler(
    [
        fountainnight_bg, 
    ]
    )

label fountainnight_example:
    stop music fadeout 1.0
    play ambient "audio/ambient/night.mp3" volume 0.5
    call screen fountainnight_screen


label fountainnight_example2:
    call screen fountainnight_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
