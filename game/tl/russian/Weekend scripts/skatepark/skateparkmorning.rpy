



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

screen skateparkmorning_screen(g=skateparkmorning_girls):
    add "skateparkmorning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at skateparkmorning_button_animation
            action i.action
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
        action Jump("skateparknoon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("skateparkmorning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform skateparkmorning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default skateparkmorning_bg = class_click("skateparkmorning_bg", "skateparkmorning_bg", None, (0, 0))
default skateparkmorning_izra = class_click("izra", "skateparkmorning_izra", Jump("skateparkmorning_izra"), (1570, 1020))

default skateparkmorning_girls = class_handler(
    [
        skateparkmorning_bg, skateparkmorning_izra,
  
    ]
    )

label skateparkmorning_example:
    if izraballetintro == 1 and izraskateintro == 0:
        jump izra_skate_intro
    elif Izra.affection >= 10 and totaldays >= 15 and izra5event == 1 and izra10event == 0:
        jump izra_10_event
    else:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        call screen skateparkmorning_screen


label skateparkmorning_izra:
    if izraballetintro == 1:
        play music "audio/Music/izra.wav" volume 1.0 fadein 1.0



        jump izracityevents
    else:
        scene skateparkmorning_bg
        "Чтобы попасть на выходные события Изры, поговори с ней после уроков."
        jump skateparkmorning_example2

label skateparkmorning_example2:
    call screen skateparkmorning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
