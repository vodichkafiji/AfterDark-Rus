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

screen bedroomnight_screen(g=bedroomnight_girls):
    add "bedroomnight_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at bedroomnight_button_animation
            action i.action
    imagebutton:
        idle "arrowback_idle.png"
        hover "arrowback_hover.png"
        action If(junepolice == 1, Jump("livingroomnightjune_example"), Jump("livingroomnight_example"))
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
        action Jump("bedroomnight_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5
    imagebutton:
        idle "images/point and click room/Bedroomnight/bedroomnight_computer.webp"
        hover "images/point and click room/Bedroomnight/bedroomnight_computer.webp"
        action Jump("bedroomnight_computer")
        xpos 5
        ypos 1150
        at bedroomnight_button_animation
    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform bedroomnight_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

define bedroomnight_bg = class_click("bedroomnight_bg", "bedroomnight_bg", None, (0, 0))
define bedroomnight_skelly = class_click("Skelly", "bedroomnight_skelly", Jump("bedroomnight_skelly"), (1190, 190))
define bedroomnight_kitsune = class_click("Kitsune", "bedroomnight_kitsune", Jump("bedroomnight_kitsune"), (2150, 190))
define bedroomnight_bed = class_click("Bed", "bedroomnight_bed", Jump("bedroomnight_bed"), (839,972))


define bedroomnight_girls = class_handler(
    [
        bedroomnight_bg,
        bedroomnight_skelly, bedroomnight_kitsune,  bedroomnight_bed,
    ]
    )

label bedroomnight_example:
    $ computer = 0
    play music "audio/Music/Nights.mp3"
    call screen bedroomnight_screen

label bedroomnight_skelly:
    scene bedroomnight_bg
    "Подпишись на @skelly.uwu в Instagram за их потрясающие навыки создания карт!"
    "Хэштег не спонсирован."
    jump bedroomnight_example
label bedroomnight_kitsune:
    if pushupintro == 0:
        jump pushupintro
    elif pushupintro == 1 and main.strength >= 5 and intro_2 == 1 and intro3 == 1 and intro_jordyn == 1 and intro_brooklyn == 1 and intro_june == 1 and intro_mei == 1 and intro_nora == 1 and intro_yuki == 1 and intro_yejin == 1 and firstfight ==0:
        jump first_fight
    elif firstfight == 1 and kyraalleyevent >= 1 and firstdream == 0:
        jump thefirstdream
    elif pillowtrain == 1 and yejin_train == 1 and chromarkwarehouse == 0:
        scene bedroomnight_bg
        jump warehouse_investigation
    else:
        scene bedroomnight_bg
        k "Ну так что, мы будем тренироваться? Или ты так и будешь весь вечер сопли на кулак наматывать?"
        mc "Я тебе чуть позже отвечу."
        jump bedroomnight_example

label bedroomnight_bed:
    scene bedroomnight_bg
    call screen bed_options
    jump bedroomnight_example

label bedroomnight_computer:
    scene black
    scene computer_night with fade
    $ computer = 4
    "Ты подходишь к компьютеру."
    play sound "audio/sound/pcon.mp3"
    jump computerscreen

label bedroomnight_exitcomputer:
    scene computer_night with fade
    "Ты решаешь, что на сегодня экранного времени достаточно."
    $ computer = 0
    jump bedroomnight_example




label pushupintro:
    scene bedroomnight_bg
    show mc_thinking at right
    show kitsune_smug at left
    with dissolve

    mc "Так, ладно... Когда начинаем?"

    hide kitsune_smug
    show kitsune_neutral at left
    with dissolve
    k "А ты шустрый, а? Никогда. Не сейчас."
    k "Сначала заложим базу. Тебе нужно познакомиться со своими одноклассниками."
    k "Имена, лица, немного доверия — вот твои первые баффы."

    hide mc_thinking
    show mc_confused at right
    with dissolve
    mc "То есть… прокачивать социалку перед боевыми навыками?"

    hide kitsune_neutral
    show kitsune_cheerful at left
    with dissolve
    k "Именно!"
    k "Но пока ты этим занимаешься, мы тренируемся. Тело и ауру."
    k "Будем гонять тебя, подтянем концентрацию, чтобы ты не размазался лицом по полу прямо посреди драки."

    hide mc_confused
    show mc_sigh at right
    with dissolve
    mc "Безжалостно честно, ничего не скажешь."

    hide kitsune_neutral
    show kitsune_neutral at left
    with dissolve
    k "Считай это выживанием. Заведи союзников в классе, а потом приходи ко мне на тренировки."
    k "Сделаешь и то, и другое — откроем Первую Миссию. Забьёшь — откроешь меню «больничной кашки»."

    hide mc_sigh
    show mc_armedcross at right
    with dissolve
    mc "Ладно. Познакомиться со всеми, потом тренировка. А когда закончу?"

    hide kitsune_neutral
    show kitsune_happy at left
    with dissolve
    k "Просто поболтай со мной здесь, дуралей!"
    k "Если всё сделал и отпахал своё, пойдём дальше."

    hide mc_armedcross
    show mc_thinking at right
    with dissolve
    mc "Круто. Время побыть обаятельным и потным. Именно в таком порядке."

    hide kitsune_happy
    show kitsune_smug at left
    with dissolve
    k "Ха! Ну иди давай, герой. Не заставляй свой будущий гарем ждать."

    hide kitsune_smug
    show kitsune_cheerful at left
    with dissolve
    k "А начать мы можем с отжиманий! Вперёд, за дело!"
    $ main.quest = "Увеличь силу до 5.\n\nПознакомься с одноклассниками.\n\nЗатем поговори с Кицунэ ночью."
    $ pushupintro += 1
    jump train
return