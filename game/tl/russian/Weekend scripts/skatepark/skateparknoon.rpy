



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

screen skateparknoon_screen(g=skateparknoon_girls):
    add "skateparknoon_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at skateparknoon_button_animation
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
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("skateparkevening_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("skateparknoon_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform skateparknoon_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default skateparknoon_bg = class_click("skateparknoon_bg", "skateparknoon_bg", None, (0, 0))
default skateparknoon_autumn = class_click("Autumn", "skateparknoon_autumn", Jump("skateparknoon_autumn"), (515, 710))

default skateparknoon_girls = class_handler(
    [
        skateparknoon_bg, skateparknoon_autumn,
  
    ]
    )

label skateparknoon_example:
    if autumntvintro == 1 and autumnskateintro == 0:
        jump autumn_skate_intro
    else:
        play ambient "audio/ambient/skatepark.mp3" volume 0.5
        call screen skateparknoon_screen


label skateparknoon_autumn:
    if autumntvintro == 1:
        play music "audio/Music/autumn.mp3" volume 1.0 fadein 1.0
        jump autumn_menu
    else:
        scene skateparknoon_bg
        "Чтобы попасть на выходные события Отэм, поговори с ней у себя дома."
        jump skateparknoon_example2

label skateparknoon_example2:
    call screen skateparknoon_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
