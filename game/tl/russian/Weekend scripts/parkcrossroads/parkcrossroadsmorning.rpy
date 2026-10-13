



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

screen parkcrossroadsmorning_screen(g=parkcrossroadsmorning_girls):
    add "parkcrossroadsmorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at parkcrossroadsmorning_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("fountainmorning_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0
    use oscar_freeroam_inventory_button2

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
        action Jump("parkcrossroadsnoon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("parkcrossroadsmorning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform parkcrossroadsmorning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default parkcrossroadsmorning_bg = class_click("parkcrossroadsmorning_bg", "parkcrossroadsmorning_bg", None, (0, 0))
default parkcrossroadsmorning_left = class_click("left", "parkcrossroadsmorning_left", Jump("parkcrossroadsmorning_left"), (0, 0))
default parkcrossroadsmorning_right = class_click("right", "parkcrossroadsmorning_right", Jump("parkcrossroadsmorning_right"), (2530, 0))


default parkcrossroadsmorning_girls = class_handler(
    [
        parkcrossroadsmorning_bg, parkcrossroadsmorning_left, parkcrossroadsmorning_right
  
    ]
    )

label parkcrossroadsmorning_example:
    call screen parkcrossroadsmorning_screen

label parkcrossroadsmorning_left:
    jump zoomorning_example

label parkcrossroadsmorning_right:
    jump hillmorning_example

label parkcrossroadsmorning_example2:
    call screen parkcrossroadsmorning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
