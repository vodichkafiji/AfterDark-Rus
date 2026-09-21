init python:

    class meieventclass_click:
        def __init__(self, name, image, action, pos):
            self.name = name
            self.image = image
            self.action = action
            self.pos = pos

    class meieventclass_handler:
        def __init__(self,clicks):
            self.clicks = clicks

screen meieventclass_screen(g=meieventclass_girls):
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at meieventclass_button_animation
            action i.action


transform meieventclass_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default meieventclass_bg = meieventclass_click("meieventclass_bg", "meieventclass_bg", None, (0, 0))
default meieventclass_june = meieventclass_click("June", "meieventclass_june", Jump("meieventclass_june"), (553, 401))
default meieventclass_tamara_riley = meieventclass_click("Tamara Riley", "meieventclass_tamara_riley", Jump("meieventclass_tamara_riley"), (1934, 698))
default meieventclass_brooklyn = meieventclass_click("Brooklyn", "meieventclass_brooklyn", Jump("meieventclass_brooklyn"), (2506, 492))
default meieventclass_yuki = meieventclass_click("Yuki", "meieventclass_yuki", Jump("meieventclass_yuki"), (2994, 773))
default meieventclass_jordyn = meieventclass_click("Jordyn", "meieventclass_jordyn", Jump("meieventclass_jordyn"), (3617, 430))
default meieventclass_yejin = meieventclass_click("Yejin", "meieventclass_yejin", Jump("meieventclass_yejin"), (2455, 601))
default meieventclass_trio = meieventclass_click("Trio", "meieventclass_trio", Jump("meieventclass_trio"), (778, 568))
default meieventclass_nora = meieventclass_click("Nora", "meieventclass_nora", Jump("meieventclass_nora"), (23, 664))

default meieventclass_girls = meieventclass_handler(
    [
        meieventclass_bg,
        meieventclass_june, meieventclass_tamara_riley, meieventclass_brooklyn, meieventclass_yuki, meieventclass_jordyn,
        meieventclass_yejin, meieventclass_trio, meieventclass_nora,
    ]
    )

label meieventclass_example:
    call screen meieventclass_screen


label meieventclass_june:
    if intro_june == 0:

        jump june_intro
    else:
        jump june_lass
label meieventclass_tamara_riley:
    if intro_2 == 0:
        jump tamara_riley_intro
    else:
        jump tamara_riley_class
label meieventclass_brooklyn:
    if intro_brooklyn == 0:
        jump brooklyn_intro
    else:
        jump brooklyn_class
label meieventclass_yuki:
    if intro_yuki == 0:
        jump yuki_intro
    else:
        jump ella_class
label meieventclass_jordyn:
    if intro_jordyn == 0:
        jump jordyn_intro
    else:
        jump jordyn_class


label meieventclass_yejin:
    if intro_yejin == 0:
        jump yejin_intro
    else:
        jump yejin_class
label meieventclass_trio:
    if intro3 == 0:
        jump trio_intro
    else:
        jump trio_class
label meieventclass_nora:
    if not intro_nora:

        jump nora_intro
    else:
        jump nora_class
    jump meieventclass_example
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
