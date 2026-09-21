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

screen avoclass_screen(g=avoclass_girls):
    add "avoclass_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at avoclass_button_animation
            action i.action
    imagebutton:
        idle "arrow_idle.png"
        hover "arrow_hover.png"
        action Jump("secondhallway2_example")
        xpos 0.15
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
        idle "timewait_idle.png"
        hover "timewait_hover.png"
        action Jump("weekday_evening")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "noon_idle.png"
        hover "noon_idle.png"
        action Jump("avoclass_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5


transform avoclass_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default avoclass_bg = class_click("avoclass_bg", "avoclass_bg", None, (0, 0))
default avoclass_yejin = class_click("Yejin", "avoclass_yejin", Jump("avoclass_yejin"), (1865, 104))


default avoclass_girls = class_handler(
    [
        avoclass_bg,
        avoclass_yejin,
    ]
    )

label avoclass_example:
    scene avoclass_bg
    call screen avoclass_screen

label avoclass_yejin:
    if intro_yejin == 1:
        jump yejinafterclassevent
    else:
        "В первую очередь, тебе нужно представиться Йеджин в классе."
    jump avoclass_example


label show_quicknav:
    call screen quick_nav
default quicknav_items = [
      
    ("gym_idle.png",            "gym_example"),
    ("roof_idle.png",           "roof_example"),
    ("library_idle.png",        "library1_example"),
    ("secondhallway_idle.png",  "secondhallway1_example"),
    ("classroom_idle.png",      "avoclass_example"),
    ("thirdhallway_idle.png",   "thirdhallway3_example"),
    ("gate_idle.png",           "gate_example"),
    ("entrance_idle.png",       "entrance1_example"),
    ("track_idle.png",          "track_example"),
]

screen quick_nav():
    modal True
    add "gui/quicknav.png"

    $ cols = 3
    $ rows = (len(quicknav_items) + cols - 1) // cols
    $ total = cols * rows
    $ pad   = max(0, total - len(quicknav_items))

    grid cols rows spacing 30 align (0.5, 0.5):


        for img, label_name in quicknav_items:
            imagebutton:
                idle img
                focus_mask True
                action [Hide("quick_nav"), Jump(label_name)]

        for _ in range(pad):
            null width 10 height 10

    textbutton "Back":
        align (0.5, 0.95)
        action Rollback()



    key "game_menu" action Hide("quick_nav")
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
