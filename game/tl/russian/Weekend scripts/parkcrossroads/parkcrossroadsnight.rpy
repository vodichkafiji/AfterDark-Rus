



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

screen parkcrossroadsnight_screen(g=parkcrossroadsnight_girls):
    add "parkcrossroadsnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at parkcrossroadsnight_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("fountainnight_example")
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
        action Jump("parkcrossroadsnight_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform parkcrossroadsnight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default parkcrossroadsnight_bg = class_click("parkcrossroadsnight_bg", "parkcrossroadsnight_bg", None, (0, 0))
default parkcrossroadsnight_left = class_click("left", "parkcrossroadsnight_left", Jump("parkcrossroadsnight_left"), (0, 0))
default parkcrossroadsnight_right = class_click("right", "parkcrossroadsnight_right", Jump("parkcrossroadsnight_right"), (2530, 0))


default parkcrossroadsnight_girls = class_handler(
    [
        parkcrossroadsnight_bg, parkcrossroadsnight_left, parkcrossroadsnight_right
  
    ]
    )

label parkcrossroadsnight_example:
    stop music fadeout 1.0
    call screen parkcrossroadsnight_screen

label parkcrossroadsnight_left:
    jump zoonight_example

label parkcrossroadsnight_right:
    jump hillnight_example

label parkcrossroadsnight_example2:
    call screen parkcrossroadsnight_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
