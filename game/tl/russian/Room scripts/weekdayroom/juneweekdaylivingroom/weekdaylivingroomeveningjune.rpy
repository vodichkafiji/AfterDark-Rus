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

screen weekdaylivingroomeveningjune_screen(g=weekdaylivingroomeveningjune_girls):
    add "weekdaylivingroomeveningjune_bg"
    for i in g.clicks:
        button:
            focus_mask True pos i.pos
            add i.image
            at weekdaylivingroomeveningjune_button_animation
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
        action Jump("weekdaylivingroomnightjune_example")
        xpos 0.8
        ypos 0.13
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_3
    imagebutton:
        idle "evening_idle.png"
        hover "evening_idle.png"
        action Jump("livingroommeveningjune_example")
        xpos 0.999999
        ypos 0.23
        xanchor 1.0
        yanchor 1.0
        at slide_in_delay_5

    imagebutton:
        idle "images/point and click room/weekdaylivingroomeveningjune/eveningjune.png"
        hover "images/point and click room/weekdaylivingroomeveningjune/eveningjune.png"
        action Jump("junelivingroom")
        xpos 280
        ypos 335
        at weekdaylivingroomeveningjune_button_animation

    imagebutton:
        idle "images/point and click room/weekdaylivingroomeveningjune/eveningjuneautumn.png"
        hover "images/point and click room/weekdaylivingroomeveningjune/eveningjuneautumn.png"
        action Jump("weekdaylivingroomeveningjune_autumn")
        xpos 2225
        ypos 690
        at weekdaylivingroomeveningjune_button_animation


    text "День [totaldays]" size 130 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" align (0.98, 0.01) outlines [(4, "#000000", 1, 1)] at slide_in_delay_5




transform weekdaylivingroomeveningjune_button_animation:
    on idle:
        ease .1 yoffset 0 additive 0
    on hover:
        ease .1 yoffset -10 additive .2

default weekdaylivingroomeveningjune_bg = class_click("weekdaylivingroomeveningjune_bg", "weekdaylivingroomeveningjune_bg", None, (0, 0))




default weekdaylivingroomeveningjune_girls = class_handler(
    [
        weekdaylivingroomeveningjune_bg, 
  
    ]
    )

label weekdaylivingroomeveningjune_example:
    call screen weekdaylivingroomeveningjune_screen

label weekdaylivingroomeveningjune_autumn:
    if intro3 == 1:
        jump autumntvevents
    else:
        scene weekdaylivingroomeveningjune_bg
        "Сначала тебе нужно поговорить с Отэм в классе."
        jump weekdaylivingroomeveningjune_example



label junelivingroom:
    scene weekdaylivingroomeveningjune_bg
    scene black with dissolve
    "Ты подходишь к Джун, стоящей у кухни."
    "Похоже, она без спроса угощается вашим с Отэм мороженым."
    scene junelivingroom (1) with dissolve
    mc "Смотрю, ты уже неплохо тут освоилась."

    j "Эй, здорово хотя бы раз иметь собственное пространство, где можно спокойно походить, ясно?"

    a "Тебе вообще-то не разрешали вот так просто разгуливать."

    a "И перестань сжирать всё наше мороженое!"
    scene junelivingroom (2) with dissolve

    j "Эй, я делаю это, чтобы избавиться от своих вредных привычек."
    scene junelivingroom (4) with dissolve
    j "Вы не разрешаете мне курить в доме, так что мне нужно в чём-то топить стресс."

    a "Я даже [mcname] не разрешаю курить в доме, с чего бы мне разрешать тебе?"

    mc "А ведь она права, Джун."
    scene junelivingroom (5) with dissolve
    j "Эх."
    scene junelivingroom (3) with dissolve
    j "И что это вообще за вкус такой?"

    j "«The Tonight Dough с Джимми Фэллоном»?"

    j "Из всего, что можно было выбрать, вы взяли *это*??"

    mc "..."
    scene junelivingroom (7) with dissolve
    mc "Слушай, а правда, Отэм, почему мы выбрали именно его?"

    a "Да потому что это, блядь, смешно."

    mc "..."

    mc "Думаю, вот тебе и ответ."
    scene junelivingroom (5) with dissolve
    mc "В любом случае, мы с Отэм обычно смотрим «Во все тяжкие» по вечерам, если хочешь — присоединяйся."

    scene junelivingroom (6) with dissolve
    j "Э-э, нет, спасибо."

    j "Я пыталась смотреть это с ней, но взбесилась после того, как та горячая гот-девка сдохла от передоза."
    scene junelivingroom (4) with dissolve
    j "Я лучше пойду прошвырнусь на улицу, раз уж мне нужно найти *хоть какое-то* место, чтобы выкурить сигарету."

    a "Ой, поплачь мне тут ещё."
    scene junelivingroom (7) with dissolve
    a "И штаны уже надень наконец."
    a "Ни я, ни [mcname] не хотим смотреть, как ты разгуливаешь в одной футболке."
    scene junelivingroom (8) with dissolve
    "Пока Отэм возвращается к просмотру телевизора, Джун спокойно держит ложку во рту."
    scene junelivingroom (9) with dissolve
    "Затем она поворачивается спиной и задирает футболку, оголяя ровно столько задницы, чтобы донести свою мысль."

    j "Извини, [mcname], это что, неподобающий наряд для дома?"

    mc "Я, э-э..."
    scene junelivingroom (10) with dissolve
    j "То-то же."
    scene weekdaylivingroomeveningjune_bg
    jump weekdaylivingroomeveningjune_example
return