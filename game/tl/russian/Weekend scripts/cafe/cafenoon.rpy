



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

screen cafenoon_screen(g=cafenoon_girls):
    add "cafenoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafenoon_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("mall2noon_example")
        xpos 0.15
        ypos 0.9
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
        action Jump("cafeevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("cafenoon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafenoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafenoon_bg = class_click("cafenoon_bg", "cafenoon_bg", None, (0, 0))
default cafenoon_door = class_click("Door", "cafenoon_door", Jump("cafenoon_door"), (1525, 695))


default cafenoon_girls = class_handler(
    [
        cafenoon_bg, cafenoon_door
  
    ]
    )

label cafenoon_example:
    call screen cafenoon_screen

label cafenoon_door:
    play sound "audio/Sound/dooropen.mp3" volume 1.0 
    play music "audio/Music/cafe.mp3" volume 1.0 fadein 1.0
    scene black with fade
    jump cafe2noon_example

label cafenoon_example2:
    call screen cafenoon_screen

label cafenoon_example3:
    stop music fadeout 1.0
    call screen cafenoon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
