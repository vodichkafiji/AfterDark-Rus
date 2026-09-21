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

screen track_screen(g=track_girls):
    add "track_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at track_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action Jump("entrance3_example")
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
        idle "gui/quicknav_idle.png"
        hover "gui/quicknav_hover.png"
        action Call("show_quicknav")
        xpos 0.73
        ypos 0.1
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_2
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
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("track_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform track_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default track_bg = class_click("track_bg", "track_bg", None, (0, 0))
default track_left = class_click("Left", "track_left", Jump("track_left"), (-5, -5))
default track_jordyn = class_click("Jordyn", "track_jordyn", Jump("track_jordyn"), (1939, 730))


default track_girls = class_handler(
    [
        track_bg,
        track_left, track_jordyn, 
    ]
    )

label track_example:
    scene track_bg
    if Yejin.affection >= 5 and yejindojointro == 1 and yejinbully == 0:
        jump Yejin_in_school
    else:
        call screen track_screen

label track_left:
    jump entrance1_example

label track_jordyn:
    if intro_jordyn == 1:
        jump jordyntrackevents
    else:
        scene track_bg
        "В первую очередь, тебе нужно представиться Джордину в классе."
        jump track_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
