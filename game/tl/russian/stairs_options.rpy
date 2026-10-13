



screen stairs_options_screen():
    imagebutton:
        idle "arrowup_idle.png"
        hover "arrowup_hover.png"
        action Jump("thirdhallway1_example")
        xpos 0.1
        ypos 0.2

    imagebutton:
        idle "arrowdown_idle.png"
        hover "arrowdown_hover.png"
        action Jump("firsthallway1_example")
        xpos 0.1
        ypos 0.45

screen stairs_options_screen2():
    imagebutton:
        idle "arrowup_idle.png"
        hover "arrowup_hover.png"
        action Jump("roof_example")
        xpos 0.1
        ypos 0.2

    imagebutton:
        idle "arrowdown_idle.png"
        hover "arrowdown_hover.png"
        action Jump("secondhallway1_example")
        xpos 0.1
        ypos 0.45

screen bed_options():
    frame:
        xpos 1000
        ypos 1100
        has hbox
        spacing 40

        imagebutton:
            idle "rest_idle.png"
            hover "rest_hover.png"
            action Jump("rest")
            at slide_up_delay_1

        imagebutton:
            idle "train_idle.png"
            hover "train_hover.png"
            action Jump("train")
            at slide_up_delay_2

transform slide_up_delay_1:
    yoffset 100
    alpha 0.0
    pause 0.2
    linear 0.3 yoffset 0 alpha 1.0

transform slide_up_delay_2:
    yoffset 100
    alpha 0.0
    pause 0.5
    linear 0.3 yoffset 0 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
