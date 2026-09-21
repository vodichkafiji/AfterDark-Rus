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

screen livingroomnight_screen(g=livingroomnight_girls):
    add "livingroomnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at livingroomnight_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("bedroomnight_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

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
        action Jump("livingroomnight_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform livingroomnight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default livingroomnight_bg = class_click("livingroomnight_bg", "livingroomnight_bg", None, (0, 0))


default livingroomnight_girls = class_handler(
    [
        livingroomnight_bg
  
    ]
    )

label livingroomnight_example:
    call screen livingroomnight_screen
return