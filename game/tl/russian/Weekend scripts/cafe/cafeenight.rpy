



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

screen cafenight_screen(g=cafenight_girls):
    add "cafenight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at cafenight_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("mall2night_example")
        xpos 0.15
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
    use oscar_freeroam_inventory_button3
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("weekend_nightmap")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "night_idle.png"
        hover "night_idle.png"
        action Jump("cafenight_example2")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    use day_tracker


transform cafenight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default cafenight_bg = class_click("cafenight_bg", "cafenight_bg", None, (0, 0))
default cafenight_door = class_click("Door", "cafenight_door", Jump("cafenight_door"), (1545, 715))


default cafenight_girls = class_handler(
    [
        cafenight_bg, cafenight_door
  
    ]
    )

label cafenight_example:
    stop music fadeout 1.0
    play ambient "audio/ambient/night.mp3" volume 0.5
    call screen cafenight_screen

label cafenight_door:
    scene cafenight_bg
    "Кафе на сегодня закрыто."
    jump cafenight_example2

label cafenight_example2:
    call screen cafenight_screen
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
