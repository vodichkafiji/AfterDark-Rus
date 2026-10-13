



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

screen parkcrossroadsevening_screen(g=parkcrossroadsevening_girls):
    add "parkcrossroadsevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at parkcrossroadsevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("fountainevening_example")
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
        action Jump("parkcrossroadsnight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("parkcrossroadsevening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform parkcrossroadsevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default parkcrossroadsevening_bg = class_click("parkcrossroadsevening_bg", "parkcrossroadsevening_bg", None, (0, 0))
default parkcrossroadsevening_left = class_click("left", "parkcrossroadsevening_left", Jump("parkcrossroadsevening_left"), (0, 0))
default parkcrossroadsevening_right = class_click("right", "parkcrossroadsevening_right", Jump("parkcrossroadsevening_right"), (2530, 0))


default parkcrossroadsevening_girls = class_handler(
    [
        parkcrossroadsevening_bg, parkcrossroadsevening_left, parkcrossroadsevening_right
  
    ]
    )

label parkcrossroadsevening_example:
    call screen parkcrossroadsevening_screen

label parkcrossroadsevening_left:
    jump zooevening_example

label parkcrossroadsevening_right:
    jump hillevening_example

label parkcrossroadsevening_example2:
    call screen parkcrossroadsevening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
