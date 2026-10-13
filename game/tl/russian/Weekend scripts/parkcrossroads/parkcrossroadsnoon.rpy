



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

screen parkcrossroadsnoon_screen(g=parkcrossroadsnoon_girls):
    add "parkcrossroadsnoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at parkcrossroadsnoon_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("fountainnoon_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_noonmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("parkcrossroadsevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("parkcrossroadsnoon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform parkcrossroadsnoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default parkcrossroadsnoon_bg = class_click("parkcrossroadsnoon_bg", "parkcrossroadsnoon_bg", None, (0, 0))
default parkcrossroadsnoon_left = class_click("left", "parkcrossroadsnoon_left", Jump("parkcrossroadsnoon_left"), (0, 0))
default parkcrossroadsnoon_right = class_click("right", "parkcrossroadsnoon_right", Jump("parkcrossroadsnoon_right"), (2530, 0))


default parkcrossroadsnoon_girls = class_handler(
    [
        parkcrossroadsnoon_bg, parkcrossroadsnoon_left, parkcrossroadsnoon_right
  
    ]
    )

label parkcrossroadsnoon_example:
    call screen parkcrossroadsnoon_screen

label parkcrossroadsnoon_left:
    jump zoonoon_example

label parkcrossroadsnoon_right:
    jump hillnoon_example

label parkcrossroadsnoon_example2:
    call screen parkcrossroadsnoon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
