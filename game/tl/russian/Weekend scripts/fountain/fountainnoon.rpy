



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

screen fountainnoon_screen(g=fountainnoon_girls):
    add "fountainnoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at fountainnoon_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("parkcrossroadsnoon_example")
        xpos 0.95
        ypos 0.95
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
        action Jump("fountainevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("fountainnoon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform fountainnoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default fountainnoon_bg = class_click("fountainnoon_bg", "fountainnoon_bg", None, (0, 0))
default fountainnoon_jordyn = class_click("jordyn", "fountainnoon_jordyn", Jump("fountainnoon_jordyn"), (1515, 580))


default fountainnoon_girls = class_handler(
    [
        fountainnoon_bg, fountainnoon_jordyn
  
    ]
    )

label fountainnoon_example:
    if jordyntrackintro == 1 and jordynparkintro == 0:
        jump jordyn_park_intro
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        call screen fountainnoon_screen


label fountainnoon_jordyn:
    if jordyntrackintro == 1:
        play music "audio/Music/jordyn.mp3" volume 1.0 fadein 1.0
        jump jordyn_menu
    else:
        scene fountainnoon_bg
        "Чтобы попасть на выходные события Джордин, поговори с ней после уроков."
        jump fountainnoon_example2

label fountainnoon_example2:
    call screen fountainnoon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
