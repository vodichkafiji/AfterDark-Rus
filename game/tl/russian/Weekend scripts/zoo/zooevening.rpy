



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

screen zooevening_screen(g=zooevening_girls):
    add "zooevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at zooevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback2_idle.png"
        hover "arrowback2_hover.png"
        action Jump("parkcrossroadsevening_example")
        xpos 0.7
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

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
        action Jump("zoonight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("zooevening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform zooevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default zooevening_bg = class_click("zooevening_bg", "zooevening_bg", None, (0, 0))
default zooevening_lily = class_click("Lily", "zooevening_lily", Jump("zooevening_lily"), (1379, 816))


default zooevening_girls = class_handler(
    [
        zooevening_bg, zooevening_lily
  
    ]
    )

label zooevening_example:
    if lilyroofintro == 1 and lilyzoointro == 0:
        jump lily_zoo_intro
    elif lilyflowerroof == 1 and lilyzooshed == 0:
        jump lily_zoofeed
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        call screen zooevening_screen


label zooevening_lily:
    if lilyroofintro == 1:
        play music "audio/Music/LilyTheme.mp3" volume 1.0 fadein 1.0
        jump lily_menu
    else:
        scene zooevening_bg
        "Чтобы попасть на выходные события Лили, поговори с ней после уроков."
        jump zooevening_example2

label zooevening_example2:
    call screen zooevening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
