



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

screen cafe2morning_screen(g=cafe2morning_girls):
    add "cafe2morning_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafe2morning_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("cafemorning_example2")
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
        action Jump("cafe2noon_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    use oscar_freeroam_inventory_button2
    imagebutton:
        idle "morning_idle.png"
        hover "morning_idle.png"
        action Jump("cafe2morning_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafe2morning_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafe2morning_bg = class_click("cafe2morning_bg", "cafe2morning_bg", None, (0, 0))
default cafe2morning_brooklyn = class_click("Brooklyn", "cafe2morning_brooklyn", Jump("cafe2morning_brooklyn"), (500, 625))


default cafe2morning_girls = class_handler(
    [
        cafe2morning_bg, cafe2morning_brooklyn
  
    ]
    )

label cafe2morning_example:

    if brooklynhallintro == 1 and brooklyncafeintro == 0:
        jump brooklyn_cafe_intro
    else:
        call screen cafe2morning_screen

label cafe2morning_brooklyn:
    if brooklynhallintro == 1:
        scene black with fade



        jump brooklyn_menu
    else:
        scene cafe2morning_bg
        "Чтобы попасть на выходные события Бруклин, поговори с ней после уроков."
        jump cafe2morning_example2

label cafe2morning_example2:
    call screen cafe2morning_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
