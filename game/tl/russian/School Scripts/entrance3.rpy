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

screen entrance3_screen(g=entrance3_girls):
    add "entrance3_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at entrance3_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("entrance1_example")
        xpos 0.95
        ypos 0.95
        xanchor 1.0
        yanchor 1.0
    imagebutton:
        idle "map_idle.png"
        hover "map_hover.png"
        action Jump("demo_menus")
        xpos 0.87
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_4
    imagebutton:
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("weekday_evening")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "quest_idle.png"
        hover "quest_hover.png"
        action ShowMenu("quests")
        xpos 0.63
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
    imagebutton:
        idle "gui/quicknav_idle.png"
        hover "gui/quicknav_hover.png"
        action Call("show_quicknav")
        xpos 0.73
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("entrance3_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5



transform entrance3_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default entrance3_bg = class_click("entrance3_bg", "entrance3_bg", None, (0, 0))
default entrance3_straight = class_click("Straight", "entrance3_straight", Jump("entrance3_straight"), (0, 0))
default entrance3_june = class_click("June", "entrance3_june", Jump("entrance3_june"), (1595, 725))


default entrance3_girls = class_handler(
    [
        entrance3_bg,
        entrance3_straight, entrance3_june
    ]
    )

label entrance3_example:
    scene entrance3_bg
    call screen entrance3_screen

label entrance3_straight:
    jump track_example

label entrance3_june:
    if juneskatepark == 1 and junebrotherintro == 0:
        "Она довольно ясно дала понять, что не хочет иметь со мной ничего общего..."
        "Похоже, мне ничего не остаётся, как дать ей немного свободы..."

        jump entrance3_example
    elif intro_june == 1:
        jump junesmokeevents
    else:
        scene entrance3_bg
        "В первую очередь, тебе нужно представиться Джун в классе."
        jump entrance3_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
