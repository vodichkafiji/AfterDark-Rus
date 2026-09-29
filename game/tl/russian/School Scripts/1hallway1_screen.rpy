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

screen firsthallway1_screen(g=firsthallway1_girls):
    add "firsthallway1_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at firsthallway1_button_animation
            action i.action
    use day_tracker
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
        action Jump("firsthallway1_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "arrowangle_idle.png"
        hover "arrowangle_hover.png"
        action Jump("firsthallway2_example")
        xpos 2750
        ypos 1953
        xanchor 1.0
        yanchor 1.0
    use day_tracker


transform firsthallway1_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default firsthallway1_bg = class_click("firsthallway1_bg", "firsthallway1_bg", None, (0, 0))
default firsthallway1_stairs = class_click("Stairs", "firsthallway1_stairs", Jump("firsthallway1_stairs"), (1670, 0))
default firsthallway1_left = class_click("Lift", "firsthallway1_left", Jump("firsthallway1_left"), (420, 0))


default firsthallway1_girls = class_handler(
    [
        firsthallway1_bg,
        firsthallway1_stairs, firsthallway1_left,
    ]
    )

label firsthallway1_example:
    if yejinblackmail == 1 and yejinpatrol == 0:
        jump yejin_blackmail_patrol
    else:
        scene firsthallway1_bg
        call screen firsthallway1_screen

label firsthallway1_stairs:
    call screen secondhallway1_screen

label firsthallway1_left:
    jump firsthallway4_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
