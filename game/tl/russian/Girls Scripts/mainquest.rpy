label brighttalk:
    play music "audio/music/kitsune.mp3"
    show mc_armedcross at right
    with dissolve
    mc "Так... и куда мы двинемся отсюда?"

    hide mc_armedcross
    show mc_sigh at right
    with dissolve
    mc "Ты просто мечешься по моей комнате последние десять минут."

    show kitsune_think at left
    with dissolve

    k "Честно говоря, я думала о твоих силах."

    k "И знаешь правду?"

    hide kitsune_think
    show kitsune_worried at left
    with dissolve
    k "Я не до конца их понимаю."

    hide mc_sigh
    show mc_shocked at right
    with hpunch
    mc "Что!?"

    hide kitsune_worried
    show kitsune_confused at left
    with dissolve
    k "Ты не вписываешься в привычные рамки."

    k "Но вне зависимости от того, кто ты такой, одно можно сказать наверняка: тебе нужно тренироваться."

    hide kitsune_confused
    show kitsune_dissapointed at left
    with dissolve
    hide mc_shocked
    show mc_angry at right
    with hpunch
    mc "Да ну, блядь, правда, что ли, Кицунэ? Я чуть не сдох в прошлый раз."

    k "Мы всё ещё не знаем точно, какой ты «Яркий»."

    k "Ты аномалия. Но единственный способ понять, как работает движок — это погазовать."

    k "Тебе нужно научиться выплёскивать силу по своему желанию."

    k "Хватит ждать смертельной паники или пистолета у виска, чтобы включить реакцию."

    hide mc_angry
    show mc_thinking at right
    with dissolve
    mc "…В подворотне, когда тот чувак приставил пушку к моей голове… это была не просто паника."

    mc "Я почувствовал, как что-то в моей голове приказало мне выплеснуть это. Будто голос, который не был голосом."

    hide kitsune_dissapointed
    show kitsune_smile at left
    with dissolve
    k "Это твой разум говорил твоему телу стравить накопленную энергию, пока она не сжгла тебя изнутри. Это аварийный клапан."

    k "Так работает большинство Заклинателей."
    k "Они собирают, хранят, а потом дают ей вырваться."
    k "Раз уж ты фонишь каким-то светом, как прожектор, я полагаю, ты относишься к этой категории."

    hide mc_thinking
    show mc_armedcross at right
    with dissolve
    mc "Заклинатель? То есть… я типа как маг или вроде того?"

    mc "Но почему тогда моя аура не была синей?"

    hide kitsune_smile
    show kitsune_ugh at left
    with dissolve
    k "Слушай, у меня нет ответов на все вопросы..."

    hide mc_armedcross
    show mc_sluggish at right
    with dissolve
    mc "Это буквально твоя единственная работа."

    hide kitsune_ugh
    show kitsune_dissapointed at left
    with dissolve
    k "Я буду тренировать тебя, как заклинателя, для начала.."

    k "Если башмак не подойдёт, подберем другую пару позже."

    mc "Ладно…{w} и что это значит?"

    mc "Какой вообще приём я должен выучить в своей спальне?"
    hide kitsune_dissapointed
    show kitsune_smug at left
    with dissolve

    hide mc_sluggish
    show mc_armedcross at right
    with dissolve


    mc "..."

    k "..."

    mc "Даже не смей пошутить."

    hide kitsune_smug
    show kitsune_cheerful at left
    with dissolve
    k "Я ничего и не говорила~"

    hide kitsune_cheerful
    show kitsune_smile at left
    with dissolve
    k "Думаю, наш лучший вариант — попробовать начать с малого."

    k "Простой луч света, вылетающий из кончика твоё пальца."

    mc "..."

    hide mc_armedcross
    show mc_thinking at right
    with dissolve
    mc "Типа пальца-пистолета?"

    k "Если хочешь это так назвать."

    mc "Звучит как-то... неэффективно?"

    hide kitsune_smile
    show kitsune_dissapointed at left
    with dissolve
    k "А ты надеялся сразу пулять огромными шарами энергии?"
    play sound "audio/sound/bong.mp3"
    hide mc_thinking
    show mc_embarrased at right
    with hpunch
    mc "Н-НЕТ!"

    hide mc_embarrased
    show mc_sorry at right
    with dissolve

    mc "Но...{w} может, что-то менее..."

    mc "Лажовое?"

    "Кицунэ ухмыляется с раздражающей степенью самодовольства."

    hide kitsune_dissapointed
    show kitsune_smug at left
    with dissolve
    k "Давай опробуем и посмотрим, будешь ли ты всё ещё считать это лажовым после этого."


    scene black with dissolve
    "Она подлетает, подхватывает одну из твоих запасных подушек и прислоняет её к дальней стене."
    k "Так, а теперь я хочу, чтобы ты нашёл это давление. Испутай то самое чувство, которое у тебя было в переулке."
    k "Собери его в груди, протолкни по руке и спусти курок."
    scene pillowshoot (2) with dissolve

    mc "То есть мне просто стоять вот так?"

    k "Плюс-минус да."
    scene pillowshoot (1) with dissolve
    mc "(Вау. Капец как помогла.)"
    mc "Ладно. Глубокий вдох."
    $ renpy.music.set_volume(0)
    scene pillowshoot (3) with dissolve
    "Ты пытаешься вспомнить переулок.{w} Страх.{w} Злость."
    "Ты напрягаешь руку."
    "И..."
    mc "..."
    scene pillowshoot (4) with dissolve
    mc "Бабах."
    $ renpy.pause (2, hard= True)
    play sound "audio/sound/bop2.mp3"
    scene pillowshoot (5)
    $ renpy.pause (2, hard= True)
    "..."
    play sound "audio/sound/Stupid Mistake 4.wav"
    scene pillowshoot (6)
    "Ничего не происходит. Ни единой искры."
    k "Бабах? Серьёзно?"
    play sound "audio/sound/bong.mp3"
    $ renpy.music.set_volume(1)
    scene pillowshoot (7) with hpunch
    mc "Я-Я не знаю! Я думал, надо что-то сказать!"
    k "Вау. Опустошительно. Подушка просто в ужасе."

    mc "Заткнись, я пытаюсь."
    scene pillowshoot (1) with dissolve
    "Ты встряхиваешь кистью и пробуешь снова."
    scene pillowshoot (8) with dissolve
    "Ты сильно щуришься, сжимая челюсть."

    mc "Я смогу."

    "Ты сможешь."
    $ renpy.music.set_volume(0)
    mc "..."
    scene pillowshoot (9) with dissolve
    mc "Пиф-паф."
    $ renpy.pause (2, hard= True)
    play sound "audio/sound/Stupid Mistake.wav"
    $ renpy.music.set_volume(1)
    scene pillowshoot (10) with hpunch
    k "Это было ещё хуже!"
    mc "Это тупо!"
    scene pillowshoot (11) with dissolve
    mc "Ничего не работает. У меня получилось прошлый раз только потому, что я буквально сдыхал!"

    k "Ты форсируешь. Ты пытаешься воссоздать паническую атаку."
    k "Помнишь, как нам пришлось чинить половицу в твоей комнате?"
    scene pillowshoot (12) with dissolve
    mc "Э-э... ну да?"

    k "Так вот, это произошло не потому, что ты умирал, а потому, что тебя захлестнули эмоции."

    scene pillowshoot (16) with dissolve
    k "Переключи мышление. Не думай о страхе смерти. Думай о {i}выплеске{/i}."
    scene pillowshoot (17) with dissolve
    k "Думай о том, как срывает аварийный клапан."

    k "Позволь энергии сделать всё самой, не пытайся контролировать каждую мелочь."
    stop music fadeout 1.0
    scene pillowshoot (20) with dissolve

    "Ты снова поднимаешь руку."
    "На этот раз ты не напрягаешься."
    "Ты просто даёшь ей течь."
    play sound "audio/Sound/powerup.mp3" loop
    scene pillowshoot (21) with dissolve
    "Внезапная резкая вспышка жара загорается прямо на кончике твоего пальца."
    play music "audio/music/pianorise.mp3" 
    mc "Так."
    scene pillowshoot (22) with dissolve
    mc "Успокойся, [mcname]."
    scene pillowshoot (23) with dissolve

    "Энергия на твоем пальце начинает разрастаться, пока не достигает размеров теннисного мяча."
    scene pillowshoot (24) with dissolve
    mc "Ого..."

    k "Вот она! Теперь выталкивай!"
    scene pillowshoot (26) with quickdissolve
    $ renpy.pause (0.02, hard= True)
    scene pillowshoot (27) with quickflash
    $ renpy.pause (0.02, hard= True)
    scene pillowshoot (26) with quickdissolve
    $ renpy.pause (0.02, hard= True)
    scene pillowshoot (27) with quickflash
    $ renpy.pause (0.02, hard= True)


    play sound "audio/Sound/beam2.mp3"
    scene white with flash
    $ renpy.pause (0.2, hard= True)
    scene pillowshoot (28) with dissolve

    "Ослепительная вспышка сине-белого света вырывается из кончиков твоих пальцев."
    "Отдача отбрасывает тебя на шаг назад."
    "Луч бьёт по подушке во всю силу."
    play sound "audio/Sound/magicexplode.mp3"
    scene pillowshoot (30) with hpunch
    $ renpy.pause (0.02, hard= True)
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)
    scene pillowshoot (30) with quickflash
    $ renpy.pause (0.002, hard= True)
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)

    scene pillowshoot (31) with hpunch

    "Подушка наконец разрывается, из-за чего туча перьев разлетается по всей твоей комнате."

    "Ты моргаешь, прогоняя пятна перед глазами."
    stop music fadeout 1.0
    scene pillowshoot (32) with dissolve
    mc "Я сделал это..."
    mc "Охренеть..."
    scene pillowshoot (33) with dissolve
    mc "У меня получилось! Кицунэ, ты видела?!"
    play music "audio/music/kitsune.mp3"
    scene pillowshoot (34) with dissolve
    "Ты смотришь на неё. Она сдувает застрявшее перо со своего плеча, выглядя впечатлённой, но осторожной."
    k "Получилось..."
    k "Я видела. Неплохо для новичка."
    k "У тебя определённо есть.. чистая мощь Заклинателя."

    scene pillowshoot (35) with dissolve

    k "Но... нам нужно будет поработать над твоим контролем."
    k "Помнишь, я говорила о том, что нужно действовать без летального исхода?"
    scene pillowshoot (37) with dissolve
    k "Вот это был смертельный выстрел, [mcname]."
    k "Если бы ты попал в обычного человека, ты бы не просто оглушил его. Ты бы прожёг дыру прямо у него в груди."
    scene pillowshoot (35) with dissolve
    k "Судя по тому, что ты мне говорил, ты бы не хотел никого убивать, так что тебе нужно научиться немного сбавлять обороты."

    "Ты смотришь на свою руку. Кончики твоих пальцев всё ещё слегка дымятся."
    "Восторг угасает, сменяясь холодным осознанием того, на что ты на самом деле способен."

    mc "Понял."
    mc "Сбавить обороты. Принято."
    scene black with dissolve

    "Ты подходишь к кровати, берешь ещё одну запасную подушку и прислоняешь её к стене прямо рядом с новым опалённым следом."
    "Отступив назад в стойку, ты делаешь глубокий вдох и снова поднимаешь руку."
    "На этот раз ты не ищешь взрыва."

    "Ты пытаешься представить более маленький клапан — просто выпускаешь маленький свист пара вместо того, чтобы срывать всю крышку."

    mc "Просто лёгкий толчок..."
    play sound "audio/Sound/beam.mp3"
    scene pillowshoot (38) with flash


    "Ты фокусируешься на жаре в кончиках пальцев, активно натягивая поводья, заставляя энергию подчиниться тебе."

    mc "Ха!"


    "Куда более маленькая искра сине-белого света вспыхивает на твоей руке, ударяя точно в центр подушки."
    play sound "audio/Sound/burn.mp3"
    scene pillowshoot (39) with dissolve

    "В этот раз она не разлетается облаком перьев."

    "Вместо этого в ткани обугливается рваная дыра, из которой лениво вился густой серый дым."

    mc "Круто! Я реально смог её сконтролировать!"

    "Торжествующая ухмылка расплывается на твоем лице. Ты поворачиваешься, чтобы отпраздновать—"

    play sound "audio/Sound/thud.mp3"
    scene pillowshoot (40) with vpunch

    "Но в тот момент, когда ты переносишь вес, внезапная дикая волна истощения бьёт по тебе, как физическая стена."
    "Прежде чем ты успеваешь сообразить, что происходит, твои ноги полностью подкашиваются."
    "Ты тяжело падаешь на колени, жадно глотая воздух и уставившись в половицы, прижимая руку к животу, чтобы тебя не вырвало."

    mc "Что... что за херня...?"

    scene pillowshoot (16) with dissolve

    k "Полегче. Не пытайся вставать прямо сейчас."
    k "Выброс такого количества энергии забирает огромные силы у тела, которое к этому не подготовлено. Ты полностью истощил свои резервы."

    "Ты сильно зажмуриваешься, ожидая, пока комната перестанет кружиться."
    mc "То есть у меня есть всего два или три выстрела этой силой, прежде чем я стану полностью бесполезным."

    scene pillowshoot (12) with dissolve

    k "Именно. Прямо сейчас ты как чувак с пистолетом, в котором всего пара пуль. Ты не можешь просто ходить и палить во всё подряд."
    k "А пока тебе придётся полагаться на боевые искусства Йеджин, чтобы постоять за себя, пока ты учишься основам своей энергии."

    "Ты делаешь медленный глубокий вдох, слегка кивая, когда тошнота начинает отступать."
    "Это досадное ограничение, но она права. Тебе нужна базовая защита, которая не оставляет тебя беспомощным через тридцать секунд."

    scene pillowshoot (15) with dissolve

    k "Не выгляди таким несчастным. Ты адаптируешься невероятно быстро."
    k "Продолжай тренироваться в том же духе, и очень скоро ты будешь готов исследовать тот склад."
    scene black with dissolve
    stop music fadeout 1.0
    mc "Ладно... теперь черед Йеджин."
    $ pillowtrain += 1
    if yejinpatrol == 1:
        $ main.quest = "Потренируйся с Йеджин, затем поговори с Кицунэ"
    else:
        $ main.quest = "Продолжи историю Йеджин, затем потренируйся с ней."

    if day == 6 or day == 7:
        jump bedroomnight_example
    else:
        jump weekdaybedroomnight_example




























label warehouse_investigation:

    mc "(Мои инстинкты стали острее. Я реально могу прочитать удар до того, как он прилетит.)"
    mc "(Сейчас или никогда.)"

    play sound "audio/sound/flash.wav"
    show kitsune_smug at left with flash

    k "Посмотрите на него. Всё ещё дышит."
    k "Я почти думала, что Йеджин сломает тебя окончательно."

    hide mc_determined
    show mc_armedcross at right
    mc "Я выжил. Выдержал вас обоих."

    mc "Думаю, я теперь знаю достаточно, чтобы дать сдачи, если возникнут проблемы."
    mc "Я готов, Кицунэ."

    mc "Хватит тянуть — нам нужно проверить тот склад."

    hide kitsune_smug
    show kitsune_neutral at left
    with dissolve
    k "А мы самоуверенны, да?"
    mc "Уверен так сильно, как только могу."
    scene black with dissolve

    k "Ладно...{w} тогда хватит тянуть резину."

    k "Собираемся и выдвигаемся."
    play ambient "audio/ambient/city.mp3"
    play music "audio/music/mysterious.mp3" fadein 1.0
    "Указания Кицунэ в лучшем случае туманны, но после долгих скитаний по разным районам."
    scene warehouse1 (2) with dissolve
    "Вы оказываетесь в запущенном районе на окраине города."

    k "Что ж, если бы у меня была какая-то база операций, думаю, где-то здесь было бы отличное начало."

    "Улицы завалены мусором и ломом, вокруг, похоже, вообще никого."

    mc "Разве тут не должно быть типа...{w} Охраны или чего-то такого?"

    k "..."
    stop ambient fadeout 1.0
    scene warehouse1 (1) with dissolve
    "Вы приходите к тому, что выглядит как тот самый склад."

    "И действительно, ты видишь грубые контуры логотипа с той карточки, всё ещё висящего над дверью."

    mc "Что бы тут ни происходило, похоже, всё закончилось уже давно."

    mc "Чёрт возьми."

    k "Ты надеялся ввязаться в драку?"

    mc "Не знаю... может быть?"

    mc "По крайней мере, тогда мы бы знали, есть ли тут что-то, что стоит защищать."

    k "Ну, нет причин не заглянуть внутрь, там могли остаться улики."


    mc "Или я могу подхватить столбняк."

    k "Не драматизируй, пошли."
    play sound "audio/sound/metaldoor.mp3"
    scene warehouse1 (3) with dissolve
    mc "Место — руины. Посмотрим, осталось ли что-то по углам."

    $ explored_left = False
    $ explored_right = False

menu warehouse_explore:
    "Исследовать левое крыло" if not explored_left:
        $ explored_left = True
        scene warehouse1 (4) with dissolve
        "Ты направляешься к куче обрушившихся стеллажей. Ты тратишь десять минут, откидывая ржавый металл и сгнивший картон."
        mc "Ничего, кроме старых накладных на промышленные растворители. И все давнишние."
        jump warehouse_explore

    "Исследовать правое крыло" if not explored_right:
        $ explored_right = True
        scene warehouse1 (5) with dissolve
        "Правая сторона склада завалена металлоломом и кучами обугленного гипсокартона."
        mc "Тут тупик. Кто бы ни зачищал это место, они даже скрепку после себя не оставили."
        jump warehouse_explore

    "Проверить заднюю защитную дверь" if explored_left and explored_right:
        jump warehouse_door_scene

label warehouse_door_scene:
    scene black with dissolve
    "Закончив с остальным помещением, ты направляешься к тяжелой стальной двери, вмонтированной в заднюю бетонную стену."
    scene warehouse1 (6) with dissolve
    "Ты хватаешься за ручку и тянешь. Она даже не дёргается. Ощущение, будто её вварили в раму."

    mc "Заперто. И она тяжелая. Скорее всего, армированная сталь."

    show kitsune_neutral at left with dissolve
    k "Зачем тратить силы и тянуть её? У тебя же теперь есть оружие, [mcname]."

    k "Используй свой пальцевый бласт, чтобы уничтожить дверь."

    mc "..."

    mc "Мы не будем это так называть."

    k "Эх, с названием разберёмся позже."

    k "Выдай всё, что у тебя есть. Выжги засов."
    play sound "audio/Sound/powerup.mp3" 
    "Ты делаешь вдох и целишься пальцем в замочную скважину, фокусируясь на жаре в груди."
    mc "(Ни о чём не думай...{w} а потом выплёскивай!)"
    play sound "audio/Sound/beam.mp3"
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)
    scene warehouse1 (7) with quickflash
    $ renpy.pause (0.002, hard= True)
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)
    scene warehouse1 (7) with quickflash
    $ renpy.pause (0.002, hard= True)


    "Луч палящего белого света вырывается из твоих пальцев. Но вместо того чтобы расплавить замок, энергия бьёт в дверь и—"

    play sound "audio/Sound/ricochet.mp3"
    scene warehouse1 (8) with hpunch
    "Луч отскакивает от стали с высоким визгом, рикошетя в бетонную стену в паре дюймов от твоей головы."

    mc "Бля—!"

    k "Что? Он должен был прорезать её насквозь!"
    scene warehouse1 (9) with dissolve
    "Кицунэ подлетает ближе, выглядя искренне озадаченной. Она протягивает призрачную руку, чтобы коснуться ручки, изучая поверхность."

    play sound "audio/Sound/burn.mp3"
    scene warehouse1 (10) with hpunch
    k "Агх! Чёрт!"

    mc "Кицунэ! Ты в порядке?"

    "Она отдёргивает руку, её призрачная форма мерцает по краям. Она смотрит на дверь со смесью страха и раздражения."
    scene warehouse1 (12) with dissolve
    k "УГХ! Ебучий бред, уебанство!"


    k "Тут...{w} барьер."

    k "Какое-то гасило энергии, настроенное специально против частот «Ярких»."
    scene warehouse1 (13) with dissolve
    k "Вот почему твой выстрел срикошетил. Дверь не просто остановила удар; она его отвергла."

    mc "И...{w} что теперь? Если я не могу её взорвать, а ты не можешь коснуться, мы застряли."
    scene warehouse1 (14) with dissolve
    k "Мы застряли *пока что*. Для такого барьера нужна конкретная контр-частота."
    k "Или просто до хрена больше мощи, чем ты можешь выдать прямо сейчас."
    scene warehouse1 (15) with dissolve
    mc "Ну, это капец как бесполезно."

    k "Не совсем. Теперь мы знаем, что они не просто свалили."

    k "Они оставили здесь что-то, что всё ещё защищают."
    scene warehouse1 (16) with dissolve
    k "Пошли отсюда."

    k "Нам нужно стать сильнее, прежде чем мы снова попробуем постучаться в эту дверь."
    play sound "audio/sound/metaldoor.mp3"
    scene black with dissolve

    "Ты отступаешь к входу на склад, потирая болящее плечо."

    scene warehousefight (1) with dissolve
    mc "Барьер? Серьёзно? Тебе надо объяснить мне это поподробнее."
    k "Эта дверь не просто защищает от людей — она создана, чтобы не пускать «Ярких»."

    k "Думаю, наш лучший вариант — списать убытки на данный момент."

    k "Может, нам стоит сосредоточиться на том, чтобы стать сильнее и узнать больше об этих чуваках со Зрачком."
    scene warehousefight (2) with dissolve
    mc "..."

    mc "Ладно..."
    scene warehousefight (3) with dissolve
    "Ты должен признать, что слегка разочарован ситуацией."
    "Упереться в тупик так рано — довольно прискорбно."

    k "Выше нос, чемпион, никто не говорил, что будет легко."

    k "Важно то, как мы будем двигаться дальше."
    scene warehousefight (4) with dissolve
    mc "Пожалуйста, перестань говорить так, будто ты тренер из детского кино девяностых."

    k "Радуйся, что я не знаю, что это значит, и не могу обидеться."

    mc "Но...{w} я всё равно не понимаю."

    mc "Если там было что-то настолько важное, что потребовало барьера..."

    mc "Разве тут не должно быть больше людей для охраны—"
    play sound "audio/sound/metalpunch.wav"
    stop music fadeout 1.0
    scene warehousefight (5) with hpunch
    "Тяжелый металлический *лязг* раздаётся со стороны входа на склад. Ты замираешь."
    scene warehousefight (6) with dissolve
    mc "Ты слышала—?"
    play music "audio/music/chromark.mp3"
    scene warehouse2 with dissolve
    "Из теней ржавых стеллажей выходят три фигуры."
    scene warehousefight (7) with dissolve
    "Их лица скрыты грубыми белыми масками с нарисованным по центру единым глазом."


    u "Вам не разрешено находиться на этой территории. Это частная собственность."
    scene warehousefight (8) with dissolve
    mc "Частная? На табличке снаружи написано 'Аварийное здание'."

    mc "Кто владеет этой собственностью?"

    mc "И что за культистские маски?"
    scene warehousefight (9) with dissolve
    mc "(Постой, этот символ глаза...{w})"

    mc "(Бля, это те самые чуваки, которых я искал?)"

    chrmk "Один из мужчин указывает прямо на Кицунэ."
    scene warehousefight (11) with hpunch
    chrmk "Смотрите, у него одно из этих существ."

    mc "Существ?"

    mc "Чёрт...{w} в смысле, э-э-э—"
    scene warehousefight (12) with dissolve
    mc "Вы правы! Ага, нам, пожалуй, пора идти."

    mc "Никогда не видели классный косплей? Я имею в виду, поразительно, что можно сделать с помощью кабелей."
    scene warehousefight (13) with dissolve
    "Мужчина в центре не смеётся."
    "Он делает шаг вперёд, взмахом открывая стандартный складной нож. Сталь тускло блестит в рассеянном свете."

    chrmk "Если у тебя находится одно из существ, ты идентифицирован как угроза."
    scene warehousefight (14) with dissolve
    chrmk "Ты должен проследовать с нами для допроса."

    chrmk "Не сопротивляйся.{w} Это сделает процесс изъятия куда более грязным для всех участников."

    "Ты собираешь волю в кулак. Запугивание на этих чуваков не сработает."

    mc "(Как же мне не хочется снова драться три против одного.)"

    k "[mcname], будь осторожен. Что-то не так."

    k "Они смотрят не на тебя... они смотрят на *меня*."
    scene warehousefight (10) with dissolve
    mc "..."

    mc "(Ну, хотя бы в этот раз без пушек.)"

    mc "(За моими плечами теперь есть навыки самообороны, и я могу хотя бы по желанию юзать одну из своих абилок.)"

    mc "Слушайте, вы трое. Не хочу хвастаться, но..."

    mc "Вам понадобится нечто большее, чем складной ножик, чтобы—"
    play sound "audio/Sound/powerup.mp3"
    scene warehousefight (15) with dissolve
    "Главный сжимает ножик. Внезапно воздух вокруг лезвия начинает искажаться."

    "Болезненное, яркое **жёлтое свечение** просачивается в металл, удлиняя кромку ножа на несколько дюймов."

    mc "Что за—?"

    k "[mcname], УВЕРНИСЬ!"
    play sound "audio/Sound/magicslash.mp3"
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)
    scene warehousefight (16) with quickflash
    $ renpy.pause (0.002, hard= True)
    scene white with quickflash
    $ renpy.pause (0.002, hard= True)
    scene warehousefight (16) with quickflash
    $ renpy.pause (0.002, hard= True)
    scene warehousefight (16) with hpunch

    "Мужчина рубит с молниеносной скоростью."
    play sound "audio/sound/buildingexplode.mp3"
    scene warehousefight (17) with hpunch
    "Ты ныряешь влево, жёлтое лезвие со свистом рассекает воздух там, где секунду назад была твоя голова."

    "Удар приходится в бетонную колонну позади тебя, выбивая глубокую светящуюся борозду в камне, будто это было мягкое масло."
    scene warehousefight (18) with dissolve
    mc "Складной нож так сделал?! Это невозможно!"
    play sound "audio/sound/flash.wav"
    scene warehousefight (20) with flash
    k "Это не просто нож!"

    k "Жёлтая энергия...{w} он **Усилитель**!"

    mc "Усилитель? Что означает..."
    scene warehousefight (21) with hpunch
    mc "Они Яркие?!"

    k "Как минимум один из них, но мы не можем исключать остальных двух."
    scene warehousefight (22) with dissolve
    k "Чёрт...{w}[mcname], нам нужно выкручиваться из этого."
    scene warehousefight (23) with dissolve
    u "Не знаю, кто ты такой, но раз у тебя одно из этих существ, верхушка Доминиона захочет на тебя взглянуть."
    scene warehousefight (24) with dissolve
    mc "..."
    scene warehousefight (25) with dissolve
    mc "(Похоже, отсюда не выбраться без драки.)"

    mc "Блядь, почему противников всегда больше."
    play sound "audio/sound/jump2.mp3"
    scene warehousefight (32) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (33) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (34) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (35) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (36) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (37) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (36) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (37) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (38) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (39) with dissolve
    $ renpy.pause (0.02, hard= True)
    scene warehousefight (40) with dissolve
    $ renpy.pause (0.02, hard= True)
    stop sound
    stop music fadeout 1.0
    scene warehousefight (41) with dissolve
    "Ты начинаешь успокаивать нервы, понимая, что в этот раз ты подготовлен лучше."
    scene warehousefight (42) with dissolve
    mc "Так... Спокойно..."
    scene warehousefight (43) with dissolve
    mc "Я смогу..."
    play sound "audio/Sound/flash2.mp3"
    scene warehousefight (44) with flash
    mc "Время задать им жару."

label retry2:

    play music "audio/music/fightalley.mp3"    
    play sound "audio/ambient/running.mp3" 
    scene warehouseqte (1) with hpunch
    "Ты мгновенно бросаешься на нападающих, пытаясь сократить дистанцию."

    "Однако их движения ничуть не уступают в скорости."
    play sound "audio/Sound/kick.mp3"
    scene warehouseqte (2) with hpunch
    "Ты решаешь прописать верхний удар ногой чуваку слева."

    "Он едва успевает заблокировать его и делает выпад в твоем направлении.."

    scene warehouseqte (3) with dissolve
    "Маскированный мужчина с жёлто-светящимся лезвием снова делает выпад, его движения рваные и ненормально быстрые."

    "Двое других заходят с боков, пытаясь зажать тебя."
    scene warehouseqte (4) with dissolve
    mc "(Шаг вперёд... перенаправить энергию...)"


    label qte_fight_1:
        play sound "audio/Sound/glitchy.mp3"
        scene blockqte1 (1) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (2) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (3) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (4) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (5) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (3) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (1) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene blockqte1 (5) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        stop sound
        $ result = renpy.call_screen("quicktime3_button")

        if result:
            jump fight_success_1
        else:
            play sound "audio/Sound/punch.mp3"
            scene warehouseqte1fail with hpunch
            "Ты недостаточно быстр, чтобы заблокировать удар."

            "Кулак охранника достигает цели, заставляя тебя отшатнуться назад."
            jump warehousefightcont




    label fight_success_1:
        play ambient "audio/Sound/block.mp3" noloop
        scene warehouseqte (5) with hpunch
        mc "(Пальмок Макги!)"
        "Ты выбрасываешь предплечье, встречая его запястье чётким, выверенным блоком."

        "Удар отдаётся вибрирующей болью по всей руке, но его кулак отлетает в сторону."
        play sound "audio/Sound/punch.mp3"
        scene warehouseqte (6) with hpunch
        "Прямо как на тренировках Йеджин, ты проворачиваешься и вбиваешь удар ладонью ему в грудь."

        chrmk "Гх-а!"
        play sound "audio/Sound/punch.mp3"
        scene warehouseqte (8) with hpunch
        "Он отшатывается назад, жадно глотая воздух."

        mc "(Сработало! Голос Йеджин буквально орёт у меня в голове прямо сейчас...)"

        "Ты добавляешь быстрый джеб ему в маску, чувствуя хруст под костяшками"
        play sound "audio/Sound/powerup.mp3"

    label warehousefightcont:

        scene warehouseqte (7) with dissolve
        "Главарь с жёлтым лезвием уже меняет траекторию своего замаха."


        mc "(Я не смогу это заблокировать...{w} энергия прорежет меня насквозь. Надо уходить!)"


        label qte_fight_2:
            play sound "audio/Sound/glitchy.mp3"
            scene duckqte1 (1) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (2) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (3) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (4) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (5) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (3) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (1) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene duckqte1 (5) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            stop sound
            $ result = renpy.call_screen("quicktime2_button")

            if result:
                jump fight_success_2
            else:

                stop music
                stop ambient
                play sound "audio/Sound/magicslash.mp3"
                scene warehousegameover1 (1) with flash
                scene warehousegameover1 (5) with dissolve
                $ renpy.pause (2, hard= True)
                play ambient "<from 1>audio/Sound/gameover.mp3" noloop
                scene warehousegameover1 (4) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover1 (3) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover1 (4) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover1 (2) with quickdissolve
                $ renpy.pause (2, hard= True)
                call screen retry2

    label fight_success_2:
        play sound "audio/Sound/magicslash.mp3"
        scene warehouseqte (10) with vpunch
        "Ты приседаешь низко, чувствуя жар жёлтого лезвия, пролетающего в миллиметре над твоей шеей."


        "Перекатываясь, ты находишь окно для атаки."
        play sound "audio/Sound/jump.mp3"
        scene warehouseqte (11) with hpunch
        mc "(Вот мой шанс.)"

        "Твоё тело инстинктивно вкладывает всю силу в кулак."
        play sound "audio/Sound/punch.mp3"
        scene warehouseqte (12) with hpunch
        "Ты впечатываешь мощный апперкот охраннику изо всех сил."

        "Однако ощущение такое, будто ты только что ввалил по кирпичной стене."
        scene warehouseqte (13) with hpunch
        "Ты отдёргиваешь руку от боли, пока чувак начинает ржать."

        mc "А-А-АГХ! КАКОГО ХЕРА?!"

        scene warehouseqte (14) with dissolve
        "Грудь мужчины тускло светится жёлтым там, куда пришёлся удар."

        mc "(Чёрт возьми, он может укреплять даже свою одежду!?)"
        scene warehouseqte (15) with hpunch
        "Он замахивается для удара, давая тебе доли секунды на реакцию."
        label qte_fight_3:
            play sound "audio/Sound/glitchy.mp3"
            scene dodgeqte1 (1) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene dodgeqte1 (2) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene dodgeqte1 (3) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene dodgeqte1 (4) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene warehouseqte (15) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene dodgeqte1 (1) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene dodgeqte1 (4) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene warehouseqte (15) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            stop sound
            $ result = renpy.call_screen("quicktime4_button")

            if result:
                jump fight_success_3
            else:
                stop music
                stop ambient
                play sound "audio/Sound/magicslash.mp3"
                scene warehousegameover2 (1) with flash
                scene warehousegameover2 (5) with dissolve
                $ renpy.pause (2, hard= True)
                play ambient "<from 1>audio/Sound/gameover.mp3" noloop
                scene warehousegameover2 (4) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover2 (3) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover2 (4) with quickdissolve
                $ renpy.pause (0.001, hard= True)
                scene warehousegameover2 (2) with quickdissolve
                $ renpy.pause (2, hard= True)
                call screen retry2


    label fight_success_3:
        play sound "audio/Sound/magicslash.mp3"

        scene warehouseqte (16) with hpunch

        "Ты отпрыгиваешь в сторону, едва избегая широкого замаха усиленного лезвия.."

        mc "(Он открылся! Пора!)"
        scene warehouseqte (17) with dissolve
        "Всё ещё находясь в воздухе после уклонения, ты готовишься."
        "Ты быстро вскидываешь руку наводя палец-пистолет прямо в грудь главарю."
        mc "(Я должен сделать этот выстрел точным!)"
        scene warehouseqte (19) with dissolve
        $ renpy.pause (0.3, hard= True)
        play sound "audio/Sound/flasback.mp3"
        scene warehouseqte (17) with dissolve

        mc "(Думай, [mcname], ты уже делал это, ты знаешь, что нужно делать!)"
        play sound "audio/Sound/powerup.mp3"
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (18) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (18) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (18) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (21) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (21) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (19) with quickflash
        $ renpy.pause (0.01, hard= True)
        scene warehouseqte (21) with quickdissolve
        $ renpy.pause (0.01, hard= True)
        stop sound
        stop music
        play ambient "audio/Sound/Shootglitch.mp3" noloop
        scene warehouseqte (20)
        $ renpy.pause (1.07, hard= True)
        play music "audio/Sound/buildup.mp3" noloop 
        scene eyes
        $ renpy.pause (3, hard= True)
        play sound "audio/Sound/beam2.mp3"
        scene white with quickflash
        scene warehouseqte (22) with flash
        $ renpy.pause (2, hard= True)


label fight_final_win:
    scene warehouseqte (23) with hpunch
    "Сфокусированный луч чистой белой энергии взрывается на кончике твоего пальца."

    "Он врезается в грудь главаря, энергия моментально разносит его жёлтый барьер в щепки."
    play ambient "audio/Sound/crateexplode.mp3" noloop 
    scene warehouseqte (24) with hpunch


    "Ударная волна отправляет его в полёт назад, впечатывая в штабель ящиков, которые обрушиваются прямо на него."
    scene warehousebeatup (1) with dissolve

    mc "ХА! Ну и как тебе—"
    play ambient "audio/sound/heartbeat.mp3"
    play sound "audio/sound/static.wav"

    scene warehousebeatup (2) with hpunch

    mc "Нгхх!"

    "Твоё тело мгновенно слабеет, сила уже полностью испарилась из тебя."

    "Ты даже не успеваешь восстановиться, как остальные двое уже снова идут в атаку."
    play sound "audio/sound/kick.mp3"
    scene warehousebeatup (3) with hpunch
    "Тяжёлое колено влетает тебе прямо в рёбра, выбивая воздух из лёгких."

    mc "Аргх, бля—"
    play sound "audio/sound/thud.mp3"
    scene warehousebeatup (4) with hpunch
    "Ты валишься на бок, задыхаясь."
    scene warehousebeatup (5) with hpunch
    play sound "audio/sound/kicks.mp3"
    "Ещё один пинок, на этот раз в живот."

    "Ты сгибаешься пополам, мир перед глазами плывёт в оттенках серого и красного."

    chrmk "Сила у тебя есть, а вот дисциплины — ноль."

    chrmk "Ты просто батарейка, которая ждёт, пока её разрядят."

    scene black with hpunch
    play sound "audio/sound/punch.mp3"
    "Кулак влетает тебе в челюсть. Потом ещё один."

    "Звук ударов их ботинок по твоему телу превращается в глухой, ритмичный тук."
    play sound "audio/Sound/thud.mp3"
    scene warehousedefeat (1) with hpunch
    "Ты прижат к холодному полу склада."

    "Главарь встаёт на колено рядом с тобой, жёлтое свечение его ножа отражается в его мёртвой, разрисованной маске."

    chrmk "Смотрите не покалечьте его слишком сильно, на верху его хотят видеть целым."

    mc "(После всех этих тренировок... Я всё равно ни хрена не могу?)"
    scene warehousedefeat (2) with hpunch
    mc "(Какая же это ебучая херня!)"

    scene warehousedefeat (3) with dissolve
    "Вкус меди заполняет твой рот, пока ты смотришь снизу вверх на главаря, жёлтое свечение его лезвия гудит с тошнотворной, хищной энергией."
    scene warehousedefeat (18) with dissolve
    "Твоё зрение начинает расплываться, а три фигуры перед тобой становятся всё менее и менее чёткими."
    scene warehousedefeat (26) with dissolve
    chrmk "Пора забирать тебя."
    stop ambient fadeout 1.0
    scene warehousedefeat (4) with dissolve
    $ renpy.pause (2, hard= True)
    stop music 
    play sound "audio/sound/wind.mp3" fadein 1.0 
    scene warehousedefeat (5) with dissolve
    "Внезапно воздух на складе буквально взрывается диким воплем."
    scene warehousedefeat (6) with dissolve
    "Яростный локальный шквал проносится по помещению, швыряя тяжелые ящики в стены, будто они сделаны из фанеры."
    scene warehousedefeat (8) with dissolve
    u "Так-с..."
    scene warehousedefeat (9) with dissolve
    u "Полетели."
    play sound "audio/sound/windmagic.mp3"
    scene warehousedefeat (7) with vpunch
    "Троих маскированных мужчин сбивает с ног и подбрасывает стеной спрессованного воздуха."
    play ambient "audio/Sound/thud.mp3" noloop
    scene black with hpunch
    "Их швыряет вверх, и они с тошнотворным хрустом врезаются в гофрированные стальные стены."
    "Ты получаешь второй укол адреналина, пытаясь двигать затуманенным телом, чтобы понять, что происходит."

    scene warehousedefeat (10) with dissolve
    play music "audio/music/chromark.mp3" fadein 2.0

    "Женщина стоит в центре обломков."

    "Она одета в облегающий тёмный тактический костюм, её лицо скрыто за изящной маской Оцелота."

    u "Приветики."

    mc "Э-э...{w}Привет?"

    "Женщина игнорирует вырубленных бандитов и переключает всё внимание на тебя."
    play sound "audio/sound/wallhit.mp3"
    scene warehousedefeat (12) with hpunch
    "Когда ты пытаешься подняться, ты чувствуешь, как тебя прижимает к стене."
    "Вспышка движения, и она уже через всю комнату подлетает к тебе. Она хватает тебя за воротник и впечатывает в несущую колонну."

    scene warehousedefeat (13) with dissolve
    u "Так... кто ты вообще такой?"

    mc "Я...{w} Я не...{w}"
    play sound "audio/sound/wallhit.mp3"
    scene warehousedefeat (12) with hpunch
    "Ты пытаешься сохранять спокойствие, хотя твои рёбра словно сжали в тисках."

    "Ты смотришь в холодные узкие прорези маски оцелота."

    u "Не строй из себя дурачка. Ты явно один из нас."

    mc "Из нас? Ты имеешь в виду Яр-"
    play sound "audio/sound/wallhit.mp3"
    scene warehousedefeat (12) with hpunch
    u "Кто тебя подослал? Ты скаут Доминиона, который сбежал?"
    play sound "audio/sound/wallhit.mp3"
    scene warehousedefeat (14) with hpunch
    mc "Нгхх! АУ!"
    scene warehousedefeat (15) with dissolve
    mc "Чувиха, поработай над своими навыками общения!"
    scene warehousedefeat (17) with dissolve
    mc "Я без понятия, о чём ты говоришь!"

    mc "Я даже не знаю, что такое этот ебучий Доминион!"

    "Она смотрит на тебя долгую паузу, её хватка сжимается, а потом она резко отпускает тебя."
    scene warehousedefeat (13) with dissolve
    u "Твой пульс слишком скачет для профессионала."
    u "Что означает..."

    "Женщина бубнит что-то себе под нос."
    "Ты не совсем слышишь её слова, но готов поклясться, это было что-то вроде «О Боже..»"

    scene warehousedefeat (13) with dissolve
    u "Вопреки здравому смыслу, я тебе верю."

    u "Не говоря уже о том, что будь ты нормально обучен, ты бы не слился базовой шестёрке Доминиона."
    scene warehousedefeat (12) with dissolve
    u "Послушай меня: если ты один из нас, тебе лучше сидеть тихо и не отсвечивать."

    u "Это не игрушки."
    scene warehousedefeat (16) with dissolve
    "(Судя по тому, сколько раз я едва не сдох, я склонен согласиться с этим утверждением.)"
    play sound "audio/sound/hoodie.wav"
    scene warehousedefeat (20) with hpunch

    u "Не стой у меня на пути и не попадайся Хромарку на глаза."
    scene warehousedefeat (21) with dissolve
    mc "Постой! Спасибо...{w} за помощь."

    mc "Но мне нужно знать, кто ты. Что вообще всё это такое?"

    scene warehousedefeat (22) with dissolve
    u "..."
    u "Ты не хочешь этого знать."

    u "В той жизни, к которой ты примкнул, знание убивает."

    mc "И всё же...{w} спасибо. Я бы уже был мёртв, если бы не ты."

    u "Нет...{w}смерть — это последнее, что они бы с тобой сделали."
    "Женщина замирает у выхода, её голова слегка наклоняется, будто она прислушивается к ветру."

    u "Я бы не была так уверена, что ты хочешь меня благодарить."

    mc "Что это значит—"
    stop music
    play ambient "audio/sound/windmagic.mp3" noloop
    scene warehousedefeat (23) with hpunch

    "Прежде чем ты успеваешь среагировать, она будто испаряется."

    mc "Че—"
    play sound "audio/sound/punch.mp3"
    scene black with hpunch
    $ renpy.pause (0.003, hard= True)
    scene warehousedefeat (23) with hpunch
    "Чёткий, точный удар ребром ладони прилетает тебе в боковину шеи, попадая по нерву с хирургической точностью."
    scene warehousedefeat (24) with dissolve
    mc "(Я...{w} реально...)"
    scene warehousedefeat (25) with dissolve
    mc "(Ненавижу...{w} сегодняшний день...)"
    play sound "audio/sound/thud.mp3"
    scene black with hpunch
    $ renpy.pause (4, hard= True)
    "..."


    "Интересно."

    "Ты не добился ничего, кроме полного провала."

    "Получив то, что многие назвали бы воплощением фантазии."

    "Возможность трахать столько тел, сколько захочешь, с лучшим оправданием, о котором только можно просить."

    "И никакой ответственности за их чувства."
    scene hero (1) with dissolve
    $ renpy.pause (3, hard= True)
    "Ты ведь герой в этой истории...{w}Правда?"

    "Каждый удар, который ты принял, каждая пытка, которую твой разум устроил тебе."

    "Всё это служит этой самой цели."

    "Вот почему тебе позволено это делать."

    "Поздравляем. Ты можешь играть чужими жизнями во имя высшего блага."
    scene hero (2) with dissolve
    $ renpy.pause (3, hard= True)
    "..."

    "Почему ты чувствуешь вину?"

    "Это синдром самозванца? Ты думаешь, что не заслуживаешь этого в отличие от других."

    "Нет?"

    "Тогда почему ты чувствуешь вину?"

    "Ты ведь герой."


    "Ты думаешь, что ты плохой человек?"
    menu badperson:
        "Да":

            "..."
        "Да":

            "..."
    "Ты думаешь, что ты хуже отброса?"
    menu scum:
        "Да":

            "..."
        "Да":

            "..."

    "Ты всё равно продолжишь идти вперёд?"

    menu forward:
        "Да":

            "..."
        "Да":

            "..."

    "Правильно. Ты будешь идти вперёд."

    "Потому что ты — герой этой истории."

    "Ты — герой."
    scene hero (3) with dissolve
    $ renpy.pause (3, hard= True)

    "Ты — герой."
    "Ты — герой."
    "Ты — герой."
    "Ты — герой."

    "Именно ты."

    u "[mcname]!"

    play sound "audio/sound/hoodie.wav"
    scene mina (1) with hpunch
    "Ты резко подрываешься, резкий судорожный вдох вырывается из твоего пересохшего горла."
    "Твоя грудь тяжело вздымается, словно ты только что вынырнул с глубины тёмной воды."
    scene mina (2) with dissolve
    "Ты оглядываешься по сторонам, полностью дезориентированный. Жестокая геометрия склада, запах горелого бетона, вспышки белого света — исчезли. Всё исчезло."

    "Воздух здесь совершенно другой. Он тёплый, слегка пахнет лавандой и стиральным порошком."

    "Здесь чисто, уютно... и абсолютно незнакомо."
    scene mina (3) with dissolve
    "Когда ты пытаешься спустить ноги с матраса, прохладный воздух бьёт по коже. Внезапная волна незащищенности накрывает тебя."

    "Ты полностью голый, если не считать трусов. В комнате, которую ты в жизни не видел."

    mc "(Что за херня... Что это за место? Где моя одежда?)"

    "Ты прижимаешь руку к лбу, ожидая ощутить липкую теплоту крови или мучительную боль от треснувшей челюсти после берцев."

    "Но ничего нет. Ни крови. Ни опухоли."
    "Твои мышцы ноют от глубокого, фантомного истощения, но физические повреждения после драки полностью отсутствуют."
    mc "(Я был так готов драться, так гордился тем, что тренировки Йеджин реально сработали на секунду... а потом со мной разделались как с ребёнком. Я вообще не тяну этот уровень.)"

    "Психологический груз давит на тебя, заставляя сердце колотиться о рёбра. Ты изолирован, незащищён и абсолютно беззащитен."


    mc "(Это сделала та женщина в маске Оцелота?)"

    mc "(Нет... она вырубила меня, или... что-то вроде того...)"

    mc "(Она не выглядела как тип, заботливо отправляющий посылочки.)"

    mc "(Это было странно... технически я спал, но...)"

    mc "(Нет... Это было что-то другое.)"

    mc "(Будто я находился в каком-то туманном состоянии разума.)"

    mc "..."


    mc "Что, блядь, со мной происходит?"
    play sound "audio/sound/unlockingdoor.mp3"
    scene mina (5) with hpunch
    "Резкий механический щелчок разрывает тишину. Снаружи комнаты кто-то поворачивает дверную ручку."

    scene mina (4) with hpunch
    "Ты спрыгиваешь с кровати и встаешь в отчаянную боевую стойку."

    mc "(Ч-чёрт! Я не готов к этому!)"

    mc "(Кто бы или что бы ни было за этой дверью, это точно тот человек, который меня похитил.)"

    mc "(Но у меня тут не так много вариантов...)"

    "Твои костяшки побелели, колени согнуты. Ты готовишься увидеть культиста в маске, чувака в костюме или кого-то злобного на вид."
    play ambient "audio/sound/dooropen.wav" noloop
    scene mina (6) with dissolve
    "Дверь распахивается, но вместо врага до боли знакомое лицо хлопает глазами, глядя на тебя из дверного проёма."

    scene mina (7) with dissolve


    mi "О! Ты проснулся!"

    mi "Я так волновалась из-за—"
    play sound "audio/sound/bong.mp3"
    scene mina (8) with hpunch

    mi "..."

    mi "Э-э..."
    play music "audio/music/acting.mp3"
    scene mina (9) with hpunch
    mc "Мина?! Что происходит? Как я сюда попал?!"

    "Мина тут же отводит взгляд, её лицо заливается густым, ярким румянцем, пока она закрывает лицо руками."

    mi "Я—я нашла тебя без сознания возле моей улицы!"
    scene mina (11) with dissolve
    mi "Ты был в каком-то странном костюме и лежал полностью вырубленный в грязи!"
    mi "Честно говоря, я сначала подумала, что ты какой-то эксцентричный, опасный бездомный..."

    mi "Но потом я сняла маску и увидела твоё лицо."
    scene mina (12) with dissolve
    mi "Я не могла просто бросить тебя там! Тем более я была у тебя в долгу."
    scene mina (13) with dissolve
    mi "Так что я притащила тебя внутрь, а ты, должно быть...{w}"

    mi "Разделся до трусов в какой-то момент ночью."
    mc "(Костюм?)"

    mc "(О чёрт, мой костюм!)"

    mc "Я...{w} э-э, занимался косплеем! Ага! Для крупного фестиваля неподалёку."
    scene mina (10) with dissolve
    mc "Это подпольная нишевая тема."

    mc "Поразительно, что сейчас можно сделать из ткани, евы и реквизита, ха-ха..."

    "Мина выглядит слегка озадаченной, но у неё нет причин не верить твоей лжи."
    scene mina (9) with dissolve
    mi "О...{w}ладно, я вроде слышала о чём-то таком на днях."
    scene mina (14) with dissolve
    mi "Но как ты тут оказался?"
    "Ты вспоминаешь произошедшее, пытаясь найти способ складно соврать."

    scene mina (11) with dissolve
    mc "Постой, Мина, это реально важно."

    mc "Ты видела кого-нибудь ещё там?"

    mc "Типа...{w} леди в тёмном тактическом костюме? В маске ягуара или оцелота?"

    scene mina (9) with dissolve

    mi "Леди в маске...{w} ягуара? Нет?"
    scene mina (10) with dissolve
    mi "Это что, какая-то БДСМ тема?"
    scene mina (10) with hpunch
    mc "Что?{w} Нет!!{w} Просто, был ли кто-то ещё со мной?"

    scene mina (14) with dissolve
    mi "Никого не было."
    scene mina (11) with dissolve
    mi "Ты буквально притащился по тротуару возле моего квартала и отключился прямо на бетоне в одиночку."

    mc "(В одиночку? Это невозможно.)"

    mc "(Как я мог прийти сюда сам после того нападения? Моё тело двигалось само по себе?)"

    scene mina (15) with dissolve
    "Мина громко прокашливается, всё ещё упорно глядя в стену, чтобы не смотреть на тебя."

    mi "Эм, слушай... Я правда рада, что ты не умер и у тебя нет травмы мозга, но..."
    scene mina (16) with dissolve
    mi "Не мог бы ты *пожалуйста* что-нибудь надеть?"

    mi "Так очень трудно вести диалог."


    "Таинственная миссия в твоей голове резко разбивается о смущающую реальность."


    mc "Оу... Точно..."
    scene black with fade
    "Мина дрожащим пальцем указывает на небольшую стопку вещей, оставленных на стуле неподалёку."

    mi "Это вещи моего брата. Они должны... более-менее подойти."

    "Ты быстро подбегаешь и натягиваешь одежду, привыкая к слегка мешковатому, неловкому сидению футболки и спорток."

    "Пока ты застёгиваешься, твои мысли бешено крутятся."

    "Ты неуклюже выдумываешь дикую, закрученную историю о бурной афтерпати после косплея."

    "Плохая реакция на энергетик и гопники, которые отжали кошелёк, чтобы хоть как-то объяснить абсурдность ситуации."

    "Ты не можешь понять, верит ли она хотя бы единому слову или просто думает, что у тебя очень странная тайная жизнь."

    scene mina (23) with dissolve
    "Ты садишься с Миной за столик у кровати."

    mi "Ну, какое бы там ни было у тебя странное хобби..."
    scene mina (18) with dissolve
    mi "Я просто рада, что нашла тебя раньше, чем кто-то другой."
    scene mina (20) with dissolve
    mi "Ты выглядел довольно беспомощным там."
    mc "Спасибо, Мина. Серьёзно, я твой должник за это."
    scene mina (22) with dissolve
    mc "Но... мне правда пора идти."
    mc "Оттум, наверное, уже с ума сходит от волнения."
    scene mina (24) with dissolve
    mi "Ну, теперь мы в расчёте, наверное. Только, пожалуйста, соберись и доберись до дома без приключений!"
    "Твой разум всё ещё гудит от безумия этой ночи."

    "Запечатанная дверь, шестёрки Хромарка, Усилитель и таинственная повелительница ветра."

    scene mina (21) with dissolve

    mc "Эй, Мина? Мы могли бы... оставить всё это строго между нами?"

    mc "Если кто-то узнает, что я очнулся в таком виде, мне этого до конца жизни не забудут."

    scene mina (25) with dissolve
    "Мина издаёт тихий, забавный смешок, напряжение наконец покидает её плечи."

    mi "Не волнуйся, твой секрет в полной безопасности со мной."
    scene mina (26) with dissolve
    mi "Просто... постарайся не вводить в привычку вырубаться в случайных районах, ладно?"

    mc "По рукам. Ещё раз спасибо, Мина."

    scene black with dissolve
    "Тебе удаётся вернуться в свою квартиру, не привлекая ничьего внимания."
    $ chromarkwarehouse += 1
    $ main.quest =  "На этом пока всё!"
    jump day_cycle


label fight_fail:
return