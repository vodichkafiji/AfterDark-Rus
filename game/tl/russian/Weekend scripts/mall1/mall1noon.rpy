



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

screen mall1noon_screen(g=mall1noon_girls):
    add "mall1noon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall1noon_button_animation
            action i.action
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_noonmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("mall1evening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("mall1noon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall1noon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall1noon_bg = class_click("mall1noon_bg", "mall1noon_bg", None, (0, 0))
default mall1noon_nora = class_click("Nora", "mall1noon_nora", Jump("mall1noon_nora"), (2582, 650))
default mall1noon_stairs = class_click("stairs", "mall1noon_stairs", Jump("mall1noon_stairs"), (0, 263))


default mall1noon_girls = class_handler(
    [
        mall1noon_bg, mall1noon_nora, mall1noon_stairs
  
    ]
    )

label mall1noon_example:
    if noragymintro == 1 and noramallintro == 0:
        jump noramallevents
    else:
        play ambient "audio/ambient/mall.mp3" volume 0.5
        call screen mall1noon_screen


label mall1noon_nora:
    if noragymintro == 1:
        play music "audio/Music/nora.mp3" volume 1.0 fadein 1.0
        jump noramallevents
    else:
        scene mall1noon_bg
        "Чтобы попасть на выходные события Норы, поговори с ней после уроков."
        jump mall1noon_example2

label mall1noon_stairs:
    jump mall2noon_example

label mall1noon_example2:
    call screen mall1noon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
