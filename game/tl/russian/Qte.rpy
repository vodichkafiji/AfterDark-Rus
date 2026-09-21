screen quicktime_button():
    default time_left = 2.0
    timer 0.05 repeat True action SetScreenVariable("time_left", time_left - 0.05)


    if time_left <= 0:
        timer 0.1 action Return(False)

    vbox:
        align (0.5, 0.5)
        spacing 15




        imagebutton:
            idle "gui/qte1button_idle.png"
            hover "gui/qte1button_hover.png"
            xpos 0.5
            ypos 0.5
            anchor (0.5, 0.5)
            action Return(True)
            activate_sound "audio/sound/select.mp3"

    bar value time_left range 2.0 xmaximum 1050 ymaximum 150 xpos 0.365 ypos 0.6

screen quicktime2_button():
    default time_left = 2.0
    timer 0.05 repeat True action SetScreenVariable("time_left", time_left - 0.05)


    if time_left <= 0:
        timer 0.1 action Return(False)

    vbox:
        align (0.5, 0.5)
        spacing 15




        imagebutton:
            idle "gui/qte2button_idle.png"
            hover "gui/qte2button_hover.png"
            xpos 0.5
            ypos 0.5
            anchor (0.5, 0.5)
            action Return(True)
            activate_sound "audio/sound/select.mp3"

    bar value time_left range 2.0 xmaximum 1050 ymaximum 150 xpos 0.365 ypos 0.6


screen retry:
    imagebutton:
        idle "gui/retry_idle.png"
        hover "gui/retry_hover.png"
        xpos 0.4
        ypos 0.5
        action Jump("retry")
        activate_sound "audio/sound/select.mp3"

screen retry2:
    imagebutton:
        idle "gui/retry_idle.png"
        hover "gui/retry_hover.png"
        xpos 0.4
        ypos 0.5
        action Jump("retry2")
        activate_sound "audio/sound/select.mp3"

screen quicktime3_button():
    default time_left = 2.0
    timer 0.05 repeat True action SetScreenVariable("time_left", time_left - 0.05)


    if time_left <= 0:
        timer 0.1 action Return(False)

    vbox:
        align (0.5, 0.5)
        spacing 15




        imagebutton:
            idle "gui/qte3button_idle.png"
            hover "gui/qte3button_hover.png"
            xpos 0.5
            ypos 0.5
            anchor (0.5, 0.5)
            action Return(True)
            activate_sound "audio/sound/select.mp3"

    bar value time_left range 2.0 xmaximum 1050 ymaximum 150 xpos 0.365 ypos 0.6


screen quicktime4_button():
    default time_left = 2.0
    timer 0.05 repeat True action SetScreenVariable("time_left", time_left - 0.05)


    if time_left <= 0:
        timer 0.1 action Return(False)

    vbox:
        align (0.5, 0.5)
        spacing 15




        imagebutton:
            idle "gui/qte4button_idle.png"
            hover "gui/qte4button_hover.png"
            xpos 0.5
            ypos 0.5
            anchor (0.5, 0.5)
            action Return(True)
            activate_sound "audio/sound/select.mp3"

    bar value time_left range 2.0 xmaximum 1050 ymaximum 150 xpos 0.365 ypos 0.6
