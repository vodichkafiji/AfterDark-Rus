



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

screen mall2evening_screen(g=mall2evening_girls):
    add "mall2evening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at mall2evening_button_animation
            action i.action
    imagebutton:
        idle "arrowback2_idle.png"
        hover "arrowback2_hover.png"
        action Jump("mall1evening_example")
        xpos 0.7
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
    imagebutton:
        idle "arrowright_idle.png"
        hover "arrowright_hover.png"
        action Jump("cafeevening_example")
        xpos 0.95
        ypos 0.7
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
        action Jump("mall2night_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("mall2evening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform mall2evening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default mall2evening_bg = class_click("mall2evening_bg", "mall2evening_bg", None, (0, 0))
default mall2evening_grace = class_click("grace", "mall2evening_grace", Jump("mall2evening_grace"), (1575, 195))


default mall2evening_girls = class_handler(
    [
        mall2evening_bg, mall2evening_grace
  
    ]
    )

label mall2evening_example:
    if intro_grace == 1 and gracemallintro == 0:
        jump grace_poster_intro
    else:
        play ambient "audio/ambient/mall.mp3" volume 0.5
        call screen mall2evening_screen

label mall2evening_grace:
    if gracemallintro == 1:
        play music "audio/Music/grace.mp3" volume 1.0 fadein 1.0
        scene black with fade
        jump grace_menu
    else:
        scene mall2evening_bg
        "Чтобы попасть на выходные события Грейс, поговори с ней после уроков."
        jump mall2evening_example2

label mall2evening_example2:
    call screen mall2evening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
