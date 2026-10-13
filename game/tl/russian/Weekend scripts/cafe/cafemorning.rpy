



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

screen cafemorning_screen(g=cafemorning_girls):
    add "cafemorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafemorning_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("mall2morning_example")
        xpos 0.15
        ypos 0.9
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
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("cafenoon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("cafemorning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafemorning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafemorning_bg = class_click("cafemorning_bg", "cafemorning_bg", None, (0, 0))
default cafemorning_door = class_click("Door", "cafemorning_door", Jump("cafemorning_door"), (1525, 695))


default cafemorning_girls = class_handler(
    [
        cafemorning_bg, cafemorning_door
  
    ]
    )

label cafemorning_example:
    call screen cafemorning_screen

label cafemorning_door:
    play sound "audio/Sound/dooropen.mp3" volume 1.0 
    play music "audio/Music/cafe.mp3" volume 1.0 fadein 1.0
    scene black with fade
    jump cafe2morning_example

label cafemorning_example2:
    stop music fadeout 1.0
    call screen cafemorning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
