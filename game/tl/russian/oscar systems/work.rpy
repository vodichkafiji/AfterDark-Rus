



default oscar_tamara_work_has_started = False
default oscar_tamara_work_greeting_index = 0
default oscar_tamara_work_earnings = 0
default oscar_tamara_work_last_total_day = -1

define oscar_tamara_work_entry_render = ad_tamara_work_greeting_01
define oscar_tamara_work_followup_renders = (
    ad_tamara_work_greeting_02,
    ad_tamara_work_greeting_03,
    ad_tamara_work_greeting_04,
    ad_tamara_work_greeting_05,
)

label tamara_work:
    if day == 6 or day == 7:
        mc "Не-а... Выходные — не время для работы."
        jump tamara_menu

    if oscar_tamara_work_last_total_day == totaldays:
        mc "Я уже отработал свою смену сегодня вечером."
        jump tamara_menu

    $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 4)
    scene expression oscar_tamara_work_entry_render with dissolve

    if not oscar_tamara_work_has_started:
        mc "Привет, мистер Кабана."

        c "[mcname]! Всегда рад тебя видеть!"

        c "Тамара вон там, если хочешь начать—"
        scene cabanawork (3) with dissolve
        mc "Вообще-то, я хотел с вами поговорить."

        mc "Вы...{w}случайно не ищете сейчас работников?"

        mc "Я трудолюбивый...{w} и мне бы не помешали деньги."
        scene cabanawork (2) with dissolve
        "Кабана отводит взгляд, словно ему неловко."

        c "Не знаю, парень, сейчас у нас туго с деньгами..."

        c "Мне едва хватает денег даже на зарплату собственной дочери."
        scene cabanawork (3) with dissolve
        mc "Много платить не придётся, да и лишняя пара рук не помешает."
        scene cabanawork (5) with dissolve
        "Он тяжело вздыхает, наконец уступая."

        c "Ещё один человек, который будет разносить еду, нам пригодится."


        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Возьми форму из подсобки, и я покажу, что нужно делать."
        mc "Отлично. Спасибо, сэр!"
        $ oscar_tamara_work_has_started = True
    elif oscar_tamara_work_greeting_index == 0:
        mc "Я снова здесь, мистер Кабана. Помочь чем-нибудь?"
        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Всегда рад, амиго. Бери форму и за работу."
    elif oscar_tamara_work_greeting_index == 1:
        mc "Привет, Кабана. Я пришёл помочь."
        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Ты вовремя. Сегодня бару не помешает помощь."
    elif oscar_tamara_work_greeting_index == 2:
        mc "Вам сегодня вечером нужен ещё один работник?"
        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Я надеялся, что ты спросишь. Давай начнём."
    elif oscar_tamara_work_greeting_index == 3:
        mc "Я готов к ещё одной смене, мистер Кабана."
        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Хорошо. Переоденься и приходи ко мне."
    else:
        mc "Привет, мистер Кабана. ¿Puedo ayudar?"
        $ oscar_tamara_work_greeting_index = renpy.random.randint(0, 3)
        scene expression oscar_tamara_work_followup_renders[oscar_tamara_work_greeting_index] with dissolve
        c "Да...{w} но тебе стоит подтянуть испанский, если хочешь, чтобы тебя здесь воспринимали всерьёз."
        c "Может, Тамара научит тебя паре фраз, пока вы вместе занимаетесь."

    scene expression ad_tamara_work_shift with dissolve
    $ oscar_tamara_work_earnings = renpy.random.randint(3, 7)
    $ ad_add_money(oscar_tamara_work_earnings)
    $ oscar_tamara_work_last_total_day = totaldays
    "Ты проработал в «Кабанасе» несколько часов и заработал $[oscar_tamara_work_earnings]."

    scene black with dissolve
    "Попрощавшись с Кабаной и Тамарой, ты отправляешься домой."
    if day == 6 or day == 7:
        jump day_cycle
    else:
        jump day_cycle
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
