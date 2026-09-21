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

screen class_screen(g=class_girls):
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at class_button_animation
            action i.action
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (1.0, 0.0) outlines [(4, "#000000", 1, 1)]



transform class_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default class_bg = class_click("class_bg", "class_bg", None, (0, 0))
default class_june = class_click("June", "class_june", Jump("class_june"), (553, 401))
default class_tamara_riley = class_click("Tamara Riley", "class_tamara_riley", Jump("class_tamara_riley"), (1934, 698))
default class_brooklyn = class_click("Brooklyn", "class_brooklyn", Jump("class_brooklyn"), (2506, 492))
default class_yuki = class_click("Yuki", "class_yuki", Jump("class_yuki"), (2994, 773))
default class_jordyn = class_click("Jordyn", "class_jordyn", Jump("class_jordyn"), (3617, 430))
default class_mei = class_click("Mei", "class_mei", Jump("class_mei"), (3271, 608))
default class_yejin = class_click("Yejin", "class_yejin", Jump("class_yejin"), (2455, 601))
default class_trio = class_click("Trio", "class_trio", Jump("class_trio"), (778, 568))
default class_nora = class_click("Nora", "class_nora", Jump("class_nora"), (23, 664))

default class_girls = class_handler(
    [
        class_bg,
        class_june, class_tamara_riley, class_brooklyn, class_yuki, class_jordyn,
        class_mei, class_yejin, class_trio, class_nora,
    ]
    )

label class_example:
    call screen class_screen


label class_june:
    if intro_june == 0:
        jump june_intro
    elif juneskatepark == 1 and junebrotherintro == 0:
        scene black with fade
        "Ты пытаешься подойти к Джун."
        scene junefsoff (1) with dissolve
        j "Отвали от меня, [mcname]."
        mc "Джун, пожалуйста, я-"
        scene junefsoff (2) with hpunch
        j "Отвали, блядь, пока я не заорала!"
        scene junefsoff (3) with dissolve
        j "Иди пялься на какую-нибудь другую девчонку."
        mc "Блин, вот же чёрт..."
        $ June.quest = "Джун явно тебя избегает. Дай ей немного времени и пространства."
        $ junetalkto = 1
        jump class_example
    else:
        jump june_class
label class_tamara_riley:
    if intro_2 == 0:
        jump tamara_riley_intro
    else:
        jump tamara_riley_class
label class_brooklyn:
    if intro_brooklyn == 0:
        jump brooklyn_intro
    else:
        jump brooklyn_class
label class_yuki:
    if intro_yuki == 0:
        jump yuki_intro
    else:
        jump ella_class
label class_jordyn:
    if intro_jordyn == 0:
        jump jordyn_intro
    else:
        jump jordyn_class

label class_mei:
    if intro_mei == 0:
        jump mei_intro
    else:
        jump mei_class
label class_yejin:
    if intro_yejin == 0:
        jump yejin_intro
    else:
        jump yejin_class
    jump class_example
label class_trio:
    if intro3 == 0:
        jump trio_intro
    else:
        jump trio_class
label class_nora:
    if not intro_nora:

        jump nora_intro
    else:
        jump nora_class
    jump class_example
return