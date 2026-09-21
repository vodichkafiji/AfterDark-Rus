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

screen weekdaylivingroomevening_screen(g=weekdaylivingroomevening_girls):
    add "weekdaylivingroomevening_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaylivingroomevening_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("weekdaybedroomevening_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0

    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("demo_mapeve")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("weekdaylivingroomnight_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("livingroomevening_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaylivingroomevening_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default weekdaylivingroomevening_bg = class_click("weekdaylivingroomevening_bg", "weekdaylivingroomevening_bg", None, (0, 0))
default weekdaylivingroomevening_autumn = class_click("Autumn", "weekdaylivingroomevening_autumn", Jump("weekdaylivingroomevening_autumn"), (2340, 660))



default weekdaylivingroomevening_girls = class_handler(
    [
        weekdaylivingroomevening_bg, weekdaylivingroomevening_autumn
  
    ]
    )

label weekdaylivingroomevening_example:
    call screen weekdaylivingroomevening_screen

label weekdaylivingroomevening_autumn:
    if intro3 == 1:
        jump autumntvevents
    else:
        scene weekdaylivingroomevening_bg
        "Сначала тебе нужно поговорить с Отэм в классе."
        jump weekdaylivingroomevening_example
return