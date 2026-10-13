



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

screen mall2night_screen(g=mall2night_girls):
    add "mall2night_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall2night_button_animation
            action i.action
    imagebutton:
        idle "arrowback2_idle.png"
        hover "arrowback2_hover.png"
        action Jump("mall1night_example")
        xpos 0.7
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
    imagebutton:
        idle "arrowright_idle.png"
        hover "arrowright_hover.png"
        action Jump("cafenight_example")
        xpos 0.95
        ypos 0.7
        xanchor 1.0
        yanchor 1.0
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
        action Jump("mall2night_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall2night_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall2night_bg = class_click("mall2night_bg", "mall2night_bg", None, (0, 0))


default mall2night_girls = class_handler(
    [
        mall2night_bg, 
  
    ]
    )

label mall2night_example:
    stop music fadeout 1.0
    play ambient "audio/ambient/night.mp3" volume 0.5
    call screen mall2night_screen


label mall2night_example2:
    call screen mall2night_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
