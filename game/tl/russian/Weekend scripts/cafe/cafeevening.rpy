



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

screen cafeevening_screen(g=cafeevening_girls):
    add "cafeevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafeevening_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("mall2evening_example")
        xpos 0.15
        ypos 0.9
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
        action Jump("cafenight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("cafeevening_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafeevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafeevening_bg = class_click("cafeevening_bg", "cafeevening_bg", None, (0, 0))
default cafeevening_door = class_click("Door", "cafeevening_door", Jump("cafeevening_door"), (1535, 750))


default cafeevening_girls = class_handler(
    [
        cafeevening_bg, cafeevening_door
  
    ]
    )

label cafeevening_example:
    call screen cafeevening_screen

label cafeevening_door:
    scene cafeevening_bg
    "Кафе на сегодня закрыто."
    jump cafeevening_example2

label cafeevening_example2:
    call screen cafeevening_screen

label cafeevening_example3:
    scene black with fade
    stop music fadeout 1.0
    "Сегодня кафе было закрыто."
    call screen cafeevening_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
