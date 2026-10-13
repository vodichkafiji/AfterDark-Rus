



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

screen fountainevening_screen(g=fountainevening_girls):
    add "fountainevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at fountainevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("parkcrossroadsevening_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0
    use oscar_freeroam_inventory_button2
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
        action Jump("fountainnight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("fountainevening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform fountainevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default fountainevening_bg = class_click("fountainevening_bg", "fountainevening_bg", None, (0, 0))


default fountainevening_girls = class_handler(
    [
        fountainevening_bg, 
    ]
    )

label fountainevening_example:
    play ambient "audio/ambient/Park.mp3" volume 0.5
    call screen fountainevening_screen


label fountainevening_example2:
    call screen fountainevening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
