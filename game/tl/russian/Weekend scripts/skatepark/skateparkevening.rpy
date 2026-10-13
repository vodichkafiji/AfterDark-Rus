



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

screen skateparkevening_screen(g=skateparkevening_girls):
    add "skateparkevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at skateparkevening_button_animation
            action i.action
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
        action Jump("skateparknight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("skateparkevening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform skateparkevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default skateparkevening_bg = class_click("skateparkevening_bg", "skateparkevening_bg", None, (0, 0))
default skateparkevening_zara = class_click("zara", "skateparkevening_zara", Jump("skateparkevening_zara"), (1245, 785))

default skateparkevening_girls = class_handler(
    [
        skateparkevening_bg, skateparkevening_zara,
  
    ]
    )

label skateparkevening_example:
    if intro_zara == 1 and zaraskateintro == 0:
        jump zara_skate_intro
    else:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        call screen skateparkevening_screen


label skateparkevening_zara:
    if Zara.affection >= 5 and zaraskateintro == 1 and zaraskateeventone == 0:
        jump zara_skate_event1
    elif intro_zara == 1:
        play music "audio/Music/zara.mp3" volume 1.0 fadein 1.0
        jump zara_menu
    else:
        scene skateparkevening_bg



        "Чтобы попасть на выходные события Зары, сначала познакомься с ней."
        jump skateparkevening_example2

label skateparkevening_example2:
    call screen skateparkevening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
