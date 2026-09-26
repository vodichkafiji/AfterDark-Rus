screen computerhome:
    imagebutton:
        idle "images/computer/fanartdesktop_idle.png"
        hover "images/computer/fanartdesktop_hover.png"
        action Jump("computerscreenfan")
        xpos 0.05
        ypos 0.05
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/cheatsdesktop_idle.png"
        hover "images/computer/cheatsdesktop_hover.png"
        action Jump("ask_patreon_code")
        xpos 0.125
        ypos 0.05
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/patreondesktop_idle.png"
        hover "images/computer/patreondesktop_hover.png"
        action Jump("computerscreenpatreon")
        xpos 0.2
        ypos 0.05
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/quitdesktop_idle.png"
        hover im.MatrixColor("images/computer/quitdesktop_idle.png", im.matrix.brightness(0.12))
        action Jump("computerquit")
        xpos 0.03
        ypos 0.815
        activate_sound "audio/sound/pcoff.mp3"

    imagebutton:
        idle "images/computer/homeworkdesktop_idle.png"
        hover im.MatrixColor("images/computer/homeworkdesktop_idle.png", im.matrix.brightness(0.12))
        action Jump("ask_patreon_code2")
        xpos 0.27
        ypos 0.05
        activate_sound "audio/sound/mouse.mp3"


screen computerscreen_fanart:
    imagebutton:
        idle "images/computer/fanart/exit.png"
        hover im.MatrixColor("images/computer/fanart/exit.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.9
        ypos 0.08
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanart1.png"
        hover im.MatrixColor("images/computer/fanart/fanart1.png", im.matrix.brightness(0.12))
        action Jump("fanart1")
        xpos 0.05
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanart2.png"
        hover im.MatrixColor("images/computer/fanart/fanart2.png", im.matrix.brightness(0.12))
        action Jump("fanart2")
        xpos 0.16
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanart3.png"
        hover im.MatrixColor("images/computer/fanart/fanart3.png", im.matrix.brightness(0.12))
        action Jump("fanart3")
        xpos 0.28
        ypos 0.14
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart4.png"
        hover im.MatrixColor("images/computer/fanart/fanart4.png", im.matrix.brightness(0.12))
        action Jump("fanart4")
        xpos 0.48
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart5.png"
        hover im.MatrixColor("images/computer/fanart/fanart5.png", im.matrix.brightness(0.12))
        action Jump("fanart5")
        xpos 0.59
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart6.png"
        hover im.MatrixColor("images/computer/fanart/fanart6.png", im.matrix.brightness(0.12))
        action Jump("fanart6")
        xpos 0.703
        ypos 0.14
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart7.png"
        hover im.MatrixColor("images/computer/fanart/fanart7.png", im.matrix.brightness(0.12))
        action Jump("fanart7")
        xpos 0.05
        ypos 0.488
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart8.png"
        hover im.MatrixColor("images/computer/fanart/fanart8.png", im.matrix.brightness(0.12))
        action Jump("fanart8")
        xpos 0.17
        ypos 0.488
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart9.png"
        hover im.MatrixColor("images/computer/fanart/fanart9.png", im.matrix.brightness(0.12))
        action Jump("fanart9")
        xpos 0.29
        ypos 0.41
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart10.png"
        hover im.MatrixColor("images/computer/fanart/fanart10.png", im.matrix.brightness(0.12))
        action Jump("fanart10")
        xpos 0.405
        ypos 0.41
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart11.png"
        hover im.MatrixColor("images/computer/fanart/fanart11.png", im.matrix.brightness(0.12))
        action Jump("fanart11")
        xpos 0.525
        ypos 0.488
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart12.png"
        hover im.MatrixColor("images/computer/fanart/fanart12.png", im.matrix.brightness(0.12))
        action Jump("fanart12")
        xpos 0.652
        ypos 0.41
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart13.png"
        hover im.MatrixColor("images/computer/fanart/fanart13.png", im.matrix.brightness(0.12))
        action Jump("fanart13")
        xpos 0.762
        ypos 0.41
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart14.png"
        hover im.MatrixColor("images/computer/fanart/fanart14.png", im.matrix.brightness(0.12))
        action Jump("fanart14")
        xpos 0.152
        ypos 0.71
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart15.png"
        hover im.MatrixColor("images/computer/fanart/fanart15.png", im.matrix.brightness(0.12))
        action Jump("fanart15")
        xpos 0.352
        ypos 0.71
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart16.png"
        hover im.MatrixColor("images/computer/fanart/fanart16.png", im.matrix.brightness(0.12))
        action Jump("fanart16")
        xpos 0.472
        ypos 0.71
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart17.png"
        hover im.MatrixColor("images/computer/fanart/fanart17.png", im.matrix.brightness(0.12))
        action Jump("fanart17")
        xpos 0.6
        ypos 0.71
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"


    imagebutton:
        idle "images/computer/fanart/fanartarrow.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.05
        ypos 0.8
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanartarrow2.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow2.png", im.matrix.brightness(0.12))
        action Jump("computerscreenfan2")
        xpos 0.9
        ypos 0.8
        activate_sound "audio/sound/mouse.mp3"






screen computerscreen_fanart2:
    imagebutton:
        idle "images/computer/fanart/exit.png"
        hover im.MatrixColor("images/computer/fanart/exit.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.9
        ypos 0.08
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart18.png"
        hover im.MatrixColor("images/computer/fanart/fanart18.png", im.matrix.brightness(0.12))
        action Jump("fanart18")
        xpos 0.05
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart19.png"
        hover im.MatrixColor("images/computer/fanart/fanart19.png", im.matrix.brightness(0.12))
        action Jump("fanart19")
        xpos 0.165
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart20.png"
        hover im.MatrixColor("images/computer/fanart/fanart20.png", im.matrix.brightness(0.12))
        action Jump("fanart20")
        xpos 0.27
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart21.png"
        hover im.MatrixColor("images/computer/fanart/fanart21.png", im.matrix.brightness(0.12))
        action Jump("fanart21")
        xpos 0.375
        ypos 0.15
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"

    imagebutton:
        idle "images/computer/fanart/fanart22.png"
        hover im.MatrixColor("images/computer/fanart/fanart22.png", im.matrix.brightness(0.12))
        action Jump("fanart22")
        xpos 0.49
        ypos 0.1
        style "fanart_thumb"
        activate_sound "audio/sound/mouse.mp3"


    imagebutton:
        idle "images/computer/fanart/fanartarrow.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow.png", im.matrix.brightness(0.12))
        action Jump("computerscreenfan")
        xpos 0.05
        ypos 0.8
        activate_sound "audio/sound/mouse.mp3"










screen computerscreen_cheats:
    imagebutton:
        idle "images/computer/cheats/affection.png"
        hover im.MatrixColor("images/computer/cheats/affection.png", im.matrix.brightness(0.12))
        action Jump("affectioncheat")
        xpos 0.05
        ypos 0.1
    imagebutton:
        idle "images/computer/cheats/totaldays.png"
        hover im.MatrixColor("images/computer/cheats/totaldays.png", im.matrix.brightness(0.12))
        action Jump("totaldayscheat")
        xpos 0.23
        ypos 0.1
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/cheats/strength.png"
        hover im.MatrixColor("images/computer/cheats/strength.png", im.matrix.brightness(0.12))
        action Jump("strengthcheat")
        xpos 0.41
        ypos 0.1
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanartarrow.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.05
        ypos 0.8
        activate_sound "audio/sound/mouse.mp3"

screen computerscreen_patreon:
    imagebutton:
        idle "images/computer/fanart/exit.png"
        hover im.MatrixColor("images/computer/fanart/exit.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.9
        ypos 0.08
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanartarrow.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.05
        ypos 0.1
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanartarrow2.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow2.png", im.matrix.brightness(0.12))
        action Jump("computerscreenpatreon2")
        xpos 0.8
        ypos 0.14
        activate_sound "audio/sound/mouse.mp3"


screen computerscreen_patreon2:
    imagebutton:
        idle "images/computer/fanart/exit.png"
        hover im.MatrixColor("images/computer/fanart/exit.png", im.matrix.brightness(0.12))
        action Jump("computerscreen")
        xpos 0.9
        ypos 0.08
        activate_sound "audio/sound/mouse.mp3"
    imagebutton:
        idle "images/computer/fanart/fanartarrow.png"
        hover im.MatrixColor("images/computer/fanart/fanartarrow.png", im.matrix.brightness(0.12))
        action Jump("computerscreenpatreon")
        xpos 0.05
        ypos 0.1
        activate_sound "audio/sound/mouse.mp3"






label computerscreen:
    scene computerscreen_home
    call screen computerhome


label computerscreenfan:
    scene computerscreen_fanart with dissolve
    call screen computerscreen_fanart

label computerscreenfan2:
    scene computerscreen_fanart with dissolve
    call screen computerscreen_fanart2

label cheatmenu:
    scene computerscreen_cheats
    call screen computerscreen_cheats

label computerscreenpatreon:
    scene computerscreen_patreon with dissolve
    call screen computerscreen_patreon


label computerscreenpatreon2:
    scene computerscreen_patreon2 with dissolve
    call screen computerscreen_patreon2

label computerscreenpatreonrenders:
    scene patreonrenders with dissolve
    jump render1



label ask_patreon_code:

    if persistent.patreon_unlocked:
        scene passwordcorrect
        "Пароль подтвержден!"
        jump cheatmenu
    else:
        scene passwordrequired with hpunch
        "Нужен пароль?"
        mc "Ах да, я установил пароль на это приложение, чтобы Отэм не смогла в него зайти."
        mc "Так...{w} какой он там был?"
        "От автора русификатора: для вас я выдал пароль к чит-кодам :)"
        "Пароль будет: {w}fiji"
        $ code_try = renpy.input("Введите свой код с Patreon:", length=64).strip()
        if code_try == "fiji":

            $ persistent.patreon_unlocked = True
            $ renpy.save_persistent()
            play sound "audio/sound/affection.mp3"
            scene passwordcorrect
            "Пароль верный!"
            mc "Да! Получилось!"
            "Чит-коды разблокированы! Теперь ты можешь открывать чит-меню."
            jump cheatmenu
        else:
            scene passwordincorrect with vpunch
            play sound "audio/sound/wrong.mp3"
            "Пароль, который ты ввел, оказался неверным."
            mc "Черт, на языке же вертится...{w} Какой он был?"
            jump computerscreen



label ask_patreon_code2:

    if persistent.patreon_unlocked2:
        scene passwordcorrect
        "Пароль верный!"
        jump computerscreenpatreonrenders
    else:
        scene passwordrequired with hpunch
        "Нужен пароль?"
        mc "Бля, у меня еще был один пароль?"
        mc "Так...{w} какой он там был?"
        "От автора русификатора: для вас я выдал пароль к рендерам :)"
        "Пароль будет: {w}fiji"
        $ code_try = renpy.input("Введите свой код с Patreon:", length=64).strip()
        if code_try == "fiji":

            $ persistent.patreon_unlocked2 = True
            $ renpy.save_persistent()
            play sound "audio/sound/affection.mp3"
            scene passwordcorrect
            "Пароль верный!"
            mc "Да! Получилось!"
            "Рендеры разблокированы! Теперь у тебя есть доступ к рендерам с Patreon."
            jump computerscreenpatreonrenders
        else:
            scene passwordincorrect with vpunch
            play sound "audio/sound/wrong.mp3"
            "Пароль, который ты ввел, оказался неверным."
            mc "Черт, на языке же вертится...{w} Какой он был?"
            jump computerscreen



label computerquit:
    if computer == 1:
        jump bedroommorning_exitcomputer
    elif computer == 2:
        jump bedroomnoon_exitcomputer
    elif computer == 3:
        jump bedroomevening_exitcomputer
    elif computer == 4:
        jump bedroomnight_exitcomputer
    elif computer == 5:
        jump weekdaybedroomevening_exitcomputer
    elif computer == 6:
        jump weekdaybedroomnoon_exitcomputer
    elif computer == 7:
        jump weekdaybedroomnight_exitcomputer
    else:
        jump computerhome






































label affectioncheat:
    "ПРЕДУПРЕЖДЕНИЕ: After Dark задумывалась как песочница, где уровень привязанности нужно поднимать естественным путем."
    "Использование читов на привязанность может привести к багам или багам логики."
    menu:
        "Сколько привязанности ты хочешь добавить?"
        "Добавить +1":
            jump one_affection
        "Добавить +5":
            jump five_affection
        "Отмена":
            jump cheatmenu

label totaldayscheat:
    menu:
        "Сколько дней ты хочешь добавить?"
        "Добавить +1":
            "Количество дней увеличено"
            $ totaldays += 1
            jump totaldayscheat
        "Добавить +5":
            "Количество дней увеличено"
            $ totaldays += 5
            jump totaldayscheat
        "Отмена":
            jump cheatmenu

label strengthcheat:
    menu:
        "Сколько силы ты хочешь добавить?"
        "Добавить +1":
            "Сила увеличена"
            $ main.strength += 1
            jump strengthcheat
        "Добавить +5":
            "Сила увеличена"
            $ main.strength += 5
            jump strengthcheat
        "Отмена":
            jump cheatmenu

label one_affection:
    menu(screen="two_col_choice"):
        "Кому ты хочешь добавить привязанности?"
        "Отэм":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Отэм увеличена.{/i}"
            $ Autumn.affection += 1
            jump one_affection
        "Бруклин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Бруклин увеличена.{/i}"
            $ Brooklyn.affection += 1
            jump one_affection
        "Грейс":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Грейс увеличена.{/i}"
            $ Grace.affection += 1
            jump one_affection
        "Изра":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Изры увеличена.{/i}"
            $ Izra.affection += 1
            jump one_affection
        "Джордин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Джордин увеличена.{/i}"
            $ Jordyn.affection += 1
            jump one_affection
        "Джун":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Джун увеличена.{/i}"
            $ June.affection += 1
            jump one_affection
        "Мэй":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Мэй увеличена.{/i}"
            $ Mei.affection += 1
            jump one_affection
        "Нора":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Норы увеличена.{/i}"
            $ Nora.affection += 1
            jump one_affection
        "Кайра":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Кайры увеличена.{/i}"
            $ Kyra.affection += 1
            jump one_affection
        "Лили":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Лили увеличена.{/i}"
            $ Lily.affection += 1
            jump one_affection
        "Паркер":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Паркер увеличена.{/i}"
            $ Parker.affection += 1
            jump one_affection
        "Райли":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Райли увеличена.{/i}"
            $ Riley.affection += 1
            jump one_affection
        "Тамара":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Тамары увеличена.{/i}"
            $ Tamara.affection += 1
            jump one_affection
        "Ютами":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Ютами увеличена.{/i}"
            $ Utami.affection += 1
            jump one_affection
        "Йеджин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Йеджин увеличена.{/i}"
            $ Yejin.affection += 1
            jump one_affection
        "Юки":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Юки увеличена.{/i}"
            $ Yuki.affection += 1
            jump one_affection
        "Зара":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Зары увеличена.{/i}"
            $ Zara.affection += 1
            jump one_affection
        "Отмена":
            jump cheatmenu



label five_affection:
    menu(screen="two_col_choice"):
        "Кому ты хочешь добавить привязанности?"
        "Отэм":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Отэм увеличена.{/i}"
            $ Autumn.affection += 5
            jump one_affection
        "Бруклин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Бруклин увеличена.{/i}"
            $ Brooklyn.affection += 5
            jump one_affection
        "Грейс":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Грейс увеличена.{/i}"
            $ Grace.affection += 5
            jump one_affection
        "Изра":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Изры увеличена.{/i}"
            $ Izra.affection += 5
            jump one_affection
        "Джордин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Джордин увеличена.{/i}"
            $ Jordyn.affection += 5
            jump one_affection
        "Джун":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Джун увеличена.{/i}"
            $ June.affection += 5
            jump one_affection
        "Мэй":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Мэй увеличена.{/i}"
            $ Mei.affection += 5
            jump one_affection
        "Нора":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Норы увеличена.{/i}"
            $ Nora.affection += 5
            jump one_affection
        "Кайра":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Кайры увеличена.{/i}"
            $ Kyra.affection += 5
            jump one_affection
        "Лили":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Лили увеличена.{/i}"
            $ Lily.affection += 5
            jump one_affection
        "Паркер":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Паркер увеличена.{/i}"
            $ Parker.affection += 5
            jump one_affection
        "Райли":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Райли увеличена.{/i}"
            $ Riley.affection += 5
            jump one_affection
        "Тамара":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Тамары увеличена.{/i}"
            $ Tamara.affection += 5
            jump one_affection
        "Ютами":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Ютами увеличена.{/i}"
            $ Utami.affection += 5
            jump one_affection
        "Йеджин":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Йеджин увеличена.{/i}"
            $ Yejin.affection += 5
            jump one_affection
        "Юки":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Юки увеличена.{/i}"
            $ Yuki.affection += 5
            jump one_affection
        "Зара":
            play sound "audio/Sound/affection.mp3" volume 0.5
            "{i}Привязанность Зары увеличена.{/i}"
            $ Zara.affection += 5
            jump one_affection
        "Отмена":
            jump cheatmenu
return