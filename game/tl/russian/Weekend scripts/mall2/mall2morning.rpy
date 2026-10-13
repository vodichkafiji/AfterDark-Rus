



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

screen mall2morning_screen(g=mall2morning_girls):
    add "mall2morning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall2morning_button_animation
            action i.action
    imagebutton:
        idle "arrowback2_idle.png"
        hover "arrowback2_hover.png"
        action Jump("mall1morning_example")
        xpos 0.7
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
    imagebutton:
        idle "arrowright_idle.png"
        hover "arrowright_hover.png"
        action Jump("cafemorning_example")
        xpos 0.95
        ypos 0.7
        xanchor 1.0
        yanchor 1.0
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_morningmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mall2noon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("mall2morning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall2morning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall2morning_bg = class_click("mall2morning_bg", "mall2morning_bg", None, (0, 0))


default mall2morning_girls = class_handler(
    [
        mall2morning_bg, 
  
    ]
    )

label mall2morning_example:
    play ambient "audio/ambient/mall.mp3" volume 0.5
    call screen mall2morning_screen

label mall2morning_example2:
    call screen mall2morning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
