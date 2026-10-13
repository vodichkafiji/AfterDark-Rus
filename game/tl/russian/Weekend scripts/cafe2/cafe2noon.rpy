



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

screen cafe2noon_screen(g=cafe2noon_girls):
    add "cafe2noon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafe2noon_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("cafenoon_example3")
        xpos 0.15
        ypos 0.9
        xanchor 1.0
        yanchor 1.0

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
        action Jump("cafeevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("cafe2noon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafe2noon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafe2noon_bg = class_click("cafe2noon_bg", "cafe2noon_bg", None, (0, 0))


default cafe2noon_girls = class_handler(
    [
        cafe2noon_bg, 
  
    ]
    )

label cafe2noon_example:
    call screen cafe2noon_screen

label cafe2noon_example2:
    call screen cafe2noon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
