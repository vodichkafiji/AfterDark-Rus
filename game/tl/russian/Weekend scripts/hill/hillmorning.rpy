



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

screen hillmorning_screen(g=hillmorning_girls):
    add "hillmorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at hillmorning_button_animation
            action i.action
    imagebutton:
        idle "arrowback2_idle.png"
        hover "arrowback2_hover.png"
        action Jump("parkcrossroadsmorning_example")
        xpos 0.7
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
        action Jump("hillnoon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("hillmorning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform hillmorning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default hillmorning_bg = class_click("hillmorning_bg", "hillmorning_bg", None, (0, 0))
default hillmorning_mei = class_click("Mei", "hillmorning_mei", Jump("hillmorning_mei"), (1670, 455))


default hillmorning_girls = class_handler(
    [
        hillmorning_bg, hillmorning_mei
  
    ]
    )

label hillmorning_example:
    if meipaintintro == 1 and meihillintro == 0:
        jump meihillevents
    else:
        play ambient "audio/ambient/Park.mp3" volume 0.5
        scene meipaint1
        "Ты поднимаешься на холм, чтобы полюбоваться видом."
        call screen hillmorning_screen

label hillmorning_mei:
    if meipaintintro == 1:
        play music "audio/Music/Mei.mp3" volume 1.0 fadein 1.0
        scene black with fade



        jump mei_menu
    else:
        scene hillmorning_bg
        "Чтобы попасть на выходные события Мэй, поговори с ней после уроков."
        jump hillmorning_example2

label hillmorning_example2:
    call screen hillmorning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
