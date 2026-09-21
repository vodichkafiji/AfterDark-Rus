label utami_intro:
    play sound "audio/Sound/bell.wav" volume 1.0
    stop ambient fadeout 2
    scene intro 0 with fade
    "Занятие заканчивается привычным скрежетом стульев и шумом уставших учеников."

    scene utamiintro (34) with dissolve

    n "Уф-ф-ф~! С уроками *покончено*~ Я во-о-обще не создана для того, чтобы так долго сидеть на месте, честно."

    mc "Ага, должно быть, это был ад — не проверять телефон дольше 30 миллисекунд."

    scene utamiintro (35) with dissolve

    "Нора, не обращая внимания на твою ехидную реплику, продолжает вещать со своим обычным жизнерадостным настроем."

    n "Короче, у меня свободный денек, а мои корни просто *кричат* о помощи. Погнали в салон~!"

    "Ты ошарашен таким предложением. Очевидно, вы с Норой стали лучше знать друг друга, но теперь она зовет тебя потусоваться после школы?"

    "С другой стороны, ты понимаешь, что это, скорее всего, просто уловка, чтобы ты снова поработал её шестеркой на побегушках."

    mc "А у меня есть выбор, или—?"
    scene utamiintro (36) with dissolve

    n "Не-а! А теперь живо, сначала надо забрать Зару. У неё уроки как раз сейчас заканчиваются."

    mc "Серьезно? Зара тоже идет?"

    scene utamiintro (1) with dissolve

    n "А что? У вас какой-то секретный терк между собой?"

    mc "Нет! Ничего такого, клянусь!"

    mc "(В смысле, не думаю, что я ей так уж нравлюсь, но это к делу не относится.)"

    mc "Я просто удивлен, что она согласилась провести день в салоне с тобой."

    scene utamiintro (36) with dissolve

    n "Хе-хе, ну так в этом и вся соль — она пока не знает."

    n "И тебе выпала честь увидеть, как я применю магию своего величия, чтобы убедить её."

    mc "Магию чего?"

    n "Погнали! Если поторопимся, сможем застроить её до того, как она свалит домой!"

    scene black with dissolve

    "Прогулявшись по зданию, вы замечаете Зару, выходящую из класса. Выражение её лица непостижимо, как и всегда."

    scene utamiintro (37) with dissolve

    z "Хм, кажется, здесь тише, чем обычно."

    z "Интересно, почему—"

    scene utamiintro (39) with dissolve

    n "За-а-ара-а-а~!"
    scene utamiintro (38) with dissolve

    z "Оу.{w} Ну разумеется."

    scene utamiintro (4) with dissolve

    n "Мы идем в салон красоты! Ты с нами?"

    z "...Зачем?"

    scene utamiintro (3) with dissolve

    mc "Судя по всему, Норе нужна компания по дороге туда."

    "Зара поднимает на тебя взгляд, будто только что осознала, что ты тоже здесь стоишь."

    z "Хм. Не думала, что ты из тех, кто укладывает волосы в салоне. Хотя, учитывая твое сомнительное окрашивание, это логично."

    mc "Очень смешно. Ты идешь или нет?"

    scene utamiintro (5) with dissolve

    z "С чего бы это?"
    n "Ну-у-у~ Для моральной поддержки! И выглядит так, будто ты все равно ничем больше не занята!."

    scene utamiintro (3) with dissolve

    z "...Мне за это заплатят?"

    n "Ха-ха! Не-а! Но тебе заплатят обнимашками и поцелуйчиками~."

    scene utamiintro (5) with dissolve

    z "Угх, я пойду с условием, что ты {i}не{/i} будешь меня обласкивать."

    n "Потрясающе!! Тогда погнали-и-и~!"

    scene black with fade
    scene utamiintro (6) with dissolve

    "Вы втроем неспешно шагаете по тротуару, солнце лениво печет сверху, пока вокруг гудит послешкольный трафик."


    show noraschool_excited1 at right_nora with moveinleft
    n "О боже, погода просто... *идеальная-а-а*~"

    n "Если пойдет дождь до того, как мы доберемся, я засужу эти облака."

    show mcschool_armedcross at left_mc with moveinleft
    mc "Ты не можешь засудить облака."
    show zaraschool_angry1 at left_zara with moveinleft
    z "Она однажды подала в суд на торговый автомат. Не думаю, что логика её остановит."

    hide noraschool_excited1 with dissolve
    show noraschool_annoyed1 at right_nora with dissolve
    n "Этот автомат *сожрал* мои деньги и выдал просроченный Покки! Моральный вред, детка!"

    hide zaraschool_angry1 with dissolve
    show zaraschool_sigh at left_zara with dissolve
    z "Ты сама — моральный вред."

    hide mcschool_armedcross with dissolve
    show mcschool_sigh at left_mc with dissolve
    mc "Начинаю думать, что я здесь эмоциональный заложник."

    hide noraschool_annoyed1 with dissolve
    show noraschool_carefree2 at right_nora with dissolve
    n "Оу-у~ тебе же нравится~ Признай, ты кайфуешь, тусуясь с двумя милашками типа меня и Зары~"
    hide mcschool_sigh with dissolve
    show mcschool (10) at left_mc with dissolve
    mc "...Одна из вас только что угрожала судом атмосферным явлениям."

    hide zaraschool_sigh with dissolve
    show zaraschool_eyeroll1 at left_zara with dissolve
    z "А вторая думает о том, чтобы шагнуть под колеса."

    hide noraschool_carefree2 with dissolve
    show noraschool_idle2 at right_nora with dissolve
    n "Хе-хе~ Ты такая цундере, Зара-чи~"

    hide zaraschool_eyeroll1 with dissolve
    show zaraschool_suspicious1 at left_zara with dissolve
    z "Как ты меня только что назвала?"
    hide noraschool_idle2 with dissolve
    show noraschool_idle1 at right_nora with dissolve

    hide zaraschool_suspicious1 with dissolve
    show zaraschool_suspicious2 at left_zara with dissolve

    hide mcschool (10) with dissolve
    show mcschool_idle at left_mc with dissolve

    mc "Цундере. Это типа девчонка, которая ведет себя стервозно по отношению к парню, который ей нравится, но просто скрывает свои настоящие чувства."


    hide mcschool_idle with dissolve
    show mcschool (10) at left_mc with dissolve
    z "..."


    n "..."

    hide mcschool (10) with dissolve
    show mcschool_embarrased at left_mc with dissolve

    mc "Ну, или я так слышал."

    hide zaraschool_suspicious2 with dissolve
    show zaraschool_sigh at left_zara with dissolve
    z "Что ж, поверь мне, мои настоящие чувства сейчас как на ладони."

    z "И выражаются они так: \"Хоть бы я сейчас занималась чем угодно другим.\""

    hide noraschool_idle1 with dissolve
    show noraschool_carefree3 at right_nora with dissolve
    n "Оу-у-у, ты такая милая за всей этой своей покерфейсной миной."

    hide zaraschool_sigh with dissolve
    show zaraschool_confused at left_zara with dissolve
    z "Угх-х-х-х, вы оба невыносимы. Зачем я вообще согласилась пойти?"
    hide mcschool_embarrased with dissolve
    show mcschool_pissed1 at left_mc with dissolve
    z "Я понимаю, почему этот зомби-мозг тут плетется, но при чем здесь я?"

    mc "Если я зомби, то поздравляю: ты — первый человек, которого я бы *не стал* есть."

    hide zaraschool_confused with dissolve
    show zaraschool_pissed3 at left_zara with dissolve

    hide noraschool_carefree3 with dissolve
    show noraschool_idle1 at right_nora with dissolve

    z "Эй! Что это значит?!"

    hide mcschool_pissed1 with dissolve
    show mcschool_pissed2 at left_mc with dissolve

    mc "Учитывая, насколько ты ко всему кислая, спорю, вкус у тебя ужасный."

    hide zaraschool_pissed3 with dissolve
    show zaraschool_pissed5 at left_zara with dissolve
    "Глаза Зары наливаются злостью. Кажется, она вот-вот взорвется."

    z "Повтори, зомби.{w} Ну давай, попробуй."
    hide mcschool_pissed2 with dissolve
    show mcschool_pissed3 at left_mc with dissolve
    mc "А то что? Ожог цитрусовыми мне устроишь?"

    hide noraschool_idle1
    show noraschool_carefree1 at right_nora with hpunch

    hide zaraschool_pissed5
    show zaraschool_suspicious1 at left_zara

    hide mcschool_pissed3
    show mcschool_pissed4 at left_mc
    n "ХА-ХА-ХА-ХА-ХА-ХА!"
    n "Вы двое цапаетесь как старая супружеская пара!"
    hide zaraschool_suspicious1 with dissolve
    show zaraschool_blush2 at left_zara with dissolve

    hide mcschool_pissed4 with dissolve
    show mcschool_blush1 at left_mc with dissolve

    window hide dissolve
    pause 1.0
    hide mcschool_blush1
    show mcschool_blush3 at left_mc

    hide zaraschool_blush2
    show zaraschool_blush1 at left_zara
    window hide dissolve
    pause 1.0
    hide mcschool_blush3
    show mcschool_blush2 at left_mc

    hide zaraschool_blush1
    show zaraschool_blush3 at left_zara

    "Вы с Зарой переглядываетесь, а затем быстро отводите взгляды."
    z "Забей, Зомби."

    mc "Унылое личико."

    hide noraschool_carefree1 with dissolve
    show noraschool_idle2 at right_nora with dissolve
    n "Ха-ха! Обожаю смотреть, как мои лучшие школьные друзья подкалывают друг друга~!"

    hide zaraschool_blush3 with dissolve
    show zaraschool_sigh at left_zara with dissolve
    z "...Это не подколы. Это вы двое болтаете, а я пытаюсь выжить."
    hide noraschool_idle2 with dissolve
    show noraschool_annoyed2 at right_nora with dissolve

    n "Хм-м~ Ну, *Я* в восторге! Давно не была у Утами. Она всегда делает из меня такую красотку~"

    hide zaraschool_sigh with dissolve
    show zaraschool_angry2 at left_zara with dissolve
    z "Ты говоришь так, будто тебе нужна помощь."

    hide mcschool_blush2
    show mcschool_realise at left_mc with hpunch
    hide noraschool_annoyed2
    show noraschool_idle1 at right_nora with hpunch


    n "..."
    mc "..."
    z "..."

    hide mcschool_realise with dissolve
    show mcschool_idle at left_mc with dissolve
    hide zaraschool_angry2
    show zaraschool_blush1 at left_zara with dissolve
    mc "Вау, это был комплимент?"

    hide noraschool_idle1 with dissolve
    show noraschool_excited2 at right_nora with dissolve
    "Лицо Норы озаряется радостью, даже ты удивлен."

    hide zaraschool_blush1
    show zaraschool_blush2 at left_zara with dissolve
    z "Что? Нет? Я не имела в виду—"

    hide zaraschool_blush2
    show zaraschool_blush3 at left_zara with hpunch
    z "Угх-х-х-х, я ненавижу вас обоих!"

    hide noraschool_excited2 with dissolve
    show noraschool_carefree3 at right_nora with dissolve
    n "За-а-ара-а-а~ Я знала, что ты ко мне оттаиваешь!"

    hide zaraschool_blush3 with dissolve
    show zaraschool_confused at left_zara with dissolve
    z "Давайте уже просто дойдем до этого чертова салона!"

    scene utamiintro (7) with dissolve
    stop music fadeout 1.0
    "Вы втроем подходите к яркой, современной парикмахерской, изнутри которой гремит поп-музыка."

    mc "(Ну, меня это ни капли не удивляет.)"
    mc "(Надеюсь, у меня не разболится голова от всей этой химии.)"

    scene black with fade
    play sound "audio/Sound/doorbell.mp3"
    "Как только вы переступаете порог, вас уже кто-то ждет с той стороны."
    play music "audio/Music/utami.mp3"
    scene utamiintro (8) with dissolve
    ut "Но-о-ора-а-а! Божечки, приве-е-ет, девочка~!"
    scene utamiintro (9) with dissolve
    ut "Выглядишь миленько, как обычно~ Что за угрюмый дуэт с тобой?"

    "Парикмахерша выглядит не сильно старше вас и одета так, будто она пробежалась сквозь фабрику по производству радуги."
    "Идеальный человек, чтобы заниматься волосами Норы."

    scene utamiintro (12) with dissolve

    n "Привет, Ми-Ми-и-и-и~"

    n "Это мой фотограф и лучшая подруга Зара~"

    z "Нора, в последний раз говорю, я не твоя лучш—{nw}"
    n "А этот парень, Мими, это *ТОТ САМЫЙ*~"

    mc "(Тот самый? О чем она вообще говорит?)"

    scene utamiintro (11) with dissolve

    "Парикмахерша уставилась на тебя, ее взгляд скользит вверх и вниз."

    "Ты не совсем уверен, оценивает она тебя или просто разглядывает."

    ut "А-а-а, так ты тот самый пресловутый [mcname]!"

    ut "Меня зовут Утами! Офигеть как приятно познакомиться~!"

    mc "Э-э, спасибо, но что значит {i}\"пресловутый\"{/i}?"

    ut "Ой, да ничего такого, просто Нора мне кучу всего про тебя рассказала, загадочный мальчик~."

    mc "(Нора рассказывает обо мне своим друзьям!? С каких пор!?)"

    "Чувство смущения вперемешку с удивлением и капелькой гордости накрывает тебя."

    "Если бы ты знал, что сегодня тебе придется производить первое впечатление, ты бы постарался причесаться поаккуратнее."

    mc "О-о, ну, надеюсь, ты слышала только хорошее!"

    ut "М-м-м-м, я никогда не раскрываю, о чем мы сплетничаем~"

    "Теперь ты напрягся еще сильнее, думая о том, что эти две болтают у тебя за спиной."

    scene utamiintro (10) with dissolve

    n "Отстань от него, Мими~ Давай лучше к делу!"

    ut "Конечно, красотка! Поболтаем о нем, [mcname], позже~"

    mc "(Пожалуйста.{w} Не надо.{w})"

    ut "Так каково наше настроение сегодня, королевишна? Только корни?"

    scene utamiintro (12) with dissolve

    n "За это я тебя и люблю, подружка! Ты всегда знаешь, чего я хочу~"

    mc "(Вау... они же буквально зеркальные копии друг друга! Неудивительно, что они так ладят.)"

    scene black with fade

    "Утами жестом приглашает Нору сесть, пока ты и Зара неловко отходите в сторону."

    scene utamiintro (16) with dissolve

    z "Угх, я знала, что это будет скучно."

    mc "Зара, мы тут всего 5 минут."

    z "Ага.{w} 5 скучных минут."

    scene utamiintro (13) with dissolve

    ut "Эй, Зара, не думала немного подравнять кончики? Просто легкую стрижку, может, каскад?"

    scene utamiintro (16) with dissolve

    z "...Нет."

    ut "Ну дава-а-ай~ У меня весь день свободен, я могу тебя втиснуть?"

    z "..."

    z "Я ношу хиджаб."

    ut "Да без проблем! Мы можем с этим подсобить—{nw}"

    scene utamiintro (18) with dissolve

    z "Я ношу его по определенной причине, идиотка."

    scene utamiintro (20) with dissolve

    ut "О-ой! Поняла, извини."

    scene utamiintro (17) with dissolve

    z "Пофиг..."

    ut "Ну а ты, [mcname]? Я и мужские стрижки делаю~."

    scene utamiintro (25) with dissolve

    mc "Я, пожалуй, пасс на сегодня. Но как-нибудь в другой раз."

    scene utamiintro (19) with dissolve

    ut "Вау, Нора, в следующий раз, когда приведет двух людей в мой салон, убедись, что они хотя бы платят."

    z "Мы можем подождать снаружи, если хочешь?"

    n "О нет, я знаю, вы сбежите, как только окажетесь за дверью!"

    "Утами тихо хихикает, пока Зара выглядит явно недовольной этой колкостью."
    scene utamiintro (19) with dissolve

    ut "Ну, я полагаю, ваше присутствие хотя бы создает вид, что салон забит."

    mc "Здесь обычно так пусто?"
    scene utamiintro (14) with dissolve

    ut "Только по средам, в остальные дни у нас обычно биток."

    scene utamiintro (15) with dissolve

    ut "Так что если захотите прийти потусоваться — среда идеальный день~"

    "Хотя Утами говорит это игриво, Нора, кажется, напрягается от этого предложения."

    scene utamiintro (22) with dissolve

    n "Эй, зай, ты стричь-то будешь или как? Мне надо кое-какие сплетни вывалить."

    scene utamiintro (21) with dissolve

    ut "Хе-хе~ Конечно, Нора. С удовольствием послушаю про {i}некоторых{/i} людей."

    mc "(Если работа этой девчонки — постоянно держать меня в напряжении, она отлично с ней справляется.)"

    scene black with fade

    "Нора громко сплетничает, пока Утами подстригает ее волосы словно проводит священный ритуал."

    "Ты слушаешь вполуха, витая в облаках. Учитывая, что в основном они говорят о брендах одежды и косметики."

    scene utamiintro (24) with dissolve

    mc "Ты хоть понимаешь, о чем они болтают?"

    z "Для меня они будто на совершенно другом языке говорят."

    scene utamiintro (23) with dissolve
    n "—И потом она *расплакалась*, когда у нее нарощенные пряди отвалились в бассейне~ Типа, подруга, этот хлор вообще не преданный~"
    scene utamiintro (24) with dissolve
    z "...Как я вообще попадаю в такие ситуации?"
    scene utamiintro (25) with dissolve
    mc "Я перестал задаваться этим вопросом. Так проще."

    scene black with fade
    "После сушки феном, спрея с блестками и мини-фотосессии от Утами, Нора выглядит так, будто только что сошла с обложки журнала."
    scene utamiintro (29) with dissolve
    n "Ну? Что думаешь, [mcname]? Мими сотворила волшебство, да?"

    menu:
        "Выглядит круто, Нора!":

            scene utamiintro (28) with dissolve
            ut "Ну естественно! Ее же подстригли в лучшем салоне мира."
            n "И все же, я рада, что у тебя есть настоящий вкус. Может, ты еще не безнадежен."
        "Ты выглядишь... точно так же.":


            scene utamiintro (27) with dissolve
            "Утами и Нора сдерживают смешок, прежде чем вернуть серьезный вид."
            n "Оу, [mcname]."
            n " Милый, наивный [mcname]."
            n "Тебе еще столько предстоит узнать о моде~."
            mc "....{w}Не уверен, что хочу узнавать больше."

    scene utamiintro (31) with dissolve
    n "Ладно, мы погнали! На связи, Мими! На днях надо перекусить вместе!"
    ut "Еще увидимся~ И вы, ребята, заходите в любое время!"
    z "Угх, слава богу, мы наконец уходим. Нора, по дороге ты ведешь меня в магазин фототехники."
    n "Ладно! Если это значит, что ты будешь фоткать меня получше. Погнали, [mcname]!"
    mc "Прямо за тобой..."

    scene utamiintro (32) with dissolve
    "Утами улыбается тебе, когда ты направляешься к выходу."
    ut "Помни, я свободна по средам. Ну, если тебе вдруг понадобится стрижка~"

    mc "Может, я просто зайду составить тебе компанию."
    scene utamiintro (33) with dissolve
    ut "Ну, может, мне бы это понравилось!"

    z "[mcname]! Шевели булками уже."

    mc "Ладно-ладно, Господи."
    scene black with fade
    stop music fadeout 1.0
    "Ты возвращаешься в школу, как раз вовремя, чтобы пойти домой вместе с Оттум."
    $ unlock_event(Utami, "Rainbow hair", "utami_intro")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ Utami.affection += 1
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i} Теперь вы можете навещать Утами по средам после уроков.{/i}"
        $ intro_utami += 1
        $ Utami.affection += 1
        stop music fadeout 1.0
        $ Utami.quest = "Навести Утами после уроков в среду."
        jump weekday_evening


label utami_hair_intro:


    mc "(Утами сказала, что я могу заскочить после уроков... Почему бы и нет. Все лучше, чем заниматься абсолютно ничем.)"

    scene black with fade
    play sound "audio/Sound/doorbell.mp3"
    play music "audio/Music/utami.mp3"
    "Звоночек звякает, когда ты толкаешь дверь. В салоне пахнет фруктовым лаком для волос, краской и капелькой хаоса."

    scene utamihairintro (1) with dissolve

    ut "О-о-ой~ Кого это ветром придуло~ Заблудился или уже соскучился?"

    mc "Честно говоря, я пришел ради кондиционера."

    scene utamihairintro (2) with dissolve

    ut "Грубиян~ А я-то думала, я нравлюсь тебе за мозг *и* за мои шикарные пряди~"

    mc "Я не говорил, что это не так."

    scene utamihairintro (3) with dissolve

    ut "М-м-м~ Лесть не выбьет тебе бесплатный шампунь, детка."

    scene utamihairintro (4) with dissolve


    ut "Короче, я как раз закрываюсь. Если ты не секретный пылесос, у меня не так много времени тебя развлекать~"

    mc "Я могу подмести, знаешь ли. Я не полностью бесполезен."

    scene utamihairintro (5) with dissolve

    ut "А? Ты бы сделал это для меня?"
    mc "Да без проблем, все равно нечем заняться этим днем."


    scene utamihairintro (6) with dissolve

    ut "Ха-ха-ха~ Ладно, ладно, давай. Метла у задней двери. Вперед, Дворник-кун~"

    scene black with fade
    "Ты берешь метлу и начинаешь подметать пол. Обрезки волос, кусочки фольги и блестки каким-то образом оказываются в твоем совке."
    scene utamihairintro (7) with dissolve

    "Утами напевает себе под нос, сидя за столом и время от времени бросая на тебя взгляды через плечо."

    ut "Неплохо~ Уверен, что не подрабатываешь тут тайком?"
    scene utamihairintro (8) with dissolve

    mc "Я подрабатываю ответственным человеком по средам. Никому не говори."

    ut "Поздно~ Я уже пишу Норе."

    mc "Я верну эту метлу с применением насилия."

    scene utamihairintro (9) with dissolve

    ut "И-и-и~ Ты такой забавный, когда понарошку злишься~"

    "Несколько минут проходят в непринужденном ритме — мести, протирать, подкалывать, повторить."
    scene black with dissolve

    "Ты заканчиваешь подметать как раз в тот момент, когда она переворачивает табличку на двери на «ЗАКРЫТО»."

    scene utamihairintro (1) with dissolve

    ut "Так-с~ Салон снова выглядит круто благодаря тебе, красотун~"

    mc "Можешь смело рассказывать всем своим клиентам. Принимаю оплату комплиментами и перекусом."

    scene utamihairintro (2) with dissolve

    ut "Хм-м-м~ Я дам тебе одно из этого сейчас, а второе, мо-о-ожет быть, в следующий раз."

    scene utamihairintro (5) with dissolve
    ut "Спасибо за помощь. Я серьезно."

    mc "...Воу. Это что, искренность сейчас прозвучала?"
    scene utamihairintro (3) with dissolve

    ut "Тссс! Ты испортишь мой имидж~"

    mc "Не волнуйся. Я скажу всем, что ты заставила меня работать под угрозой распыления лака для волос."
    scene utamihairintro (4) with dissolve

    ut "Хе-хе~ Отлично. А теперь выметайся отсюда, пока я не сделала тебе полный макияж."

    mc "Это мой намек уходить."
    $ unlock_event(Utami, "Fruit-Scented", "utami_hair_intro")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ utamihairintro += 1
        $ Utami.affection += 1
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i}Привязанность Утами увеличена.{/i}"
        $ Utami.quest = "Навести Утами в салоне"

        jump weekday_evening



label utamipaintevents:

label utamihillevents:


label city_noonutami:
    play ambient "audio/ambient/Mall.mp3" volume 0.5
    scene city2 with fade
    "Ты выходишь в город."

    scene utamiintro (7) with fade
    "Гудение фенов и болтовня манят тебя к салону Утами."
    scene black with fade

label utami_menu:
    play music "audio/Music/utami.mp3" fadein 1.0
    scene UtamiWeekend with dissolve
    "Утами занята протиркой кресла, но она с ухмылкой смотрит на тебя, когда ты заходишь."
    call screen Utamiaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump utami_menu

label mall_eveninghangutami:
    ut "Тч. Мне бы не помешала пара лишних рук. Ты как, нормально с метлой справляешься?"
    "Ты берешь метлу, которую она тебе бросает, и помогаешь подмести состриженные волосы и привести в порядок стойку."

    scene utamihairintro (8) with fade
    "Утами напевает под какую-то веселую музыку, пока вы уборкой занимаетесь бок о бок."

    ut "Ты получше большинства пустышек, которые сюда приходят. Так держать, зомби-бой."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Привязанность Утами увеличена.{/i}"
    $ Utami.affection += 1
    jump weekday_evening

label mall_eveningwaitutami:
    "Ты чиллишь в салоне, пока Утами заканчивает закрывать заведение."
    jump weekday_evening

label utami_beach_one:
    play music "audio/Music/utami.mp3" fadein 1.0
    scene utamiintro (7) with fade
    "Гудение фенов и болтовня манят тебя к салону Утами."
    "Снова пришел убираться? Типа, я жаловаться не буду."
    "Ты берешь метлу, которую она тебе бросает, и помогаешь подмести состриженные волосы и привести в порядок стойку."

    scene utamihairintro (8) with dissolve
    "Утами напевает под какую-то веселую музыку, пока вы уборкой занимаетесь бок о бок."

    scene surfbeach1 (1) with dissolve
    ut "Ну так… {w} как там делишки у Норы и Зары в последнее время?"

    ut "Эти две все так же страдают своими обычными делами?"

    mc "В целом да. Нора таскает меня по магазинам одежды."

    mc "И под этим я имею в виду, что она закупится, пока я таскаю пакеты."

    mc "Зара просто зыркает на меня так, будто я лично оскорбил факт ее существования."
    scene surfbeach1 (2) with dissolve
    ut "Ха-ха! Классика. С Норой непросто, но она безобидная."
    scene surfbeach1 (3) with dissolve
    ut "А вот Зара… {w} у этой девчонки лицо хронической убийцы."

    ut "Мне это даже нравится."
    scene surfbeach1 (4) with dissolve
    "Утами тихо смеется и смотрит через плечо."

    ut "Знаешь, когда Нора впервые привела тебя сюда, я подумала: «Бедный парень, он даже не представляет, во что вляпался»."

    ut "Но ты справляешься с ними получше, чем большинство людей."

    mc "Я не уверен, комплимент это или ты намекаешь, что я просто привыкаю к моральному ущербу."
    scene surfbeach1 (5) with dissolve
    ut "И то, и другое~ В тебе есть этакая тихая стойкость. Это мило."

    "Ты вскидываешь бровь и ухмыляешься ей."

    mc "Мило? От девчонки, которая обвешана блестками и радугой, я это приму."
    scene surfbeach1 (10) with hpunch
    ut "Эй! Блестки — это жизненный выбор, спасибо большое. Они делают мир ярче."
    scene surfbeach1 (6) with dissolve
    ut "Когда доживешь до моих лет, будешь хвататься за любой гламур, какой сможешь найти."

    mc "Ты так говоришь, будто ты старая карга."
    scene surfbeach1 (7) with dissolve
    ut "Угх-х-х, я увядаю, [mcname], скоро вы, молодежь, обойдете меня."

    ut "И все, чем я буду известна — это ископаемое, которое умеет делать дикую химию."
    scene surfbeach1 (8) with dissolve
    mc "Пфф, хорош драматизировать, ты бы никогда не позволила себе выглядеть старо."

    ut "Тут ты меня подловил, детка~ Вот почему нужно увлажнять кожу каждый день!"
    scene surfbeach1 (9) with dissolve
    ut "Ты наносишь солнцезащитный крем каждое утро после пробуждения?"

    mc "Э-э... нет?"
    scene surfbeach1 (10) with hpunch
    ut "А надо бы!"

    ut "Если только не хочешь выглядеть как соленый чернослив в среднем возрасте!"

    mc "(Такая серьезная... Похоже, она реально заморачивается уходом за кожей.)"
    scene surfbeach1 (11) with dissolve
    "Внезапно Утами встает со своего места."
    ut "Угх-х-х~ Сегодня на улице {b}слишком{/b} жарко! Я буквально умираю здесь."

    "Утами драматично обмахивается одной рукой, отклоняясь назад, отчего ее цветное худи-кроп слегка задирается."

    ut "Мои корни потеют, моя кожа кричит… Я {i}так{/i} готова быть на пляже прямо сейчас."

    mc "На пляже?"
    scene surfbeach1 (12) with dissolve
    ut "Типа, реально. Я сгораю от желания поехать!"

    "Волны наверняка звали меня весь день~ "

    ut "Эй… ты свободен сейчас? Тебе стоит поехать со мной~"

    mc "Смотря как. В какие неприятности ты пытаешься меня втянуть на этот раз?"
    scene surfbeach1 (13) with dissolve
    ut " Волны наверняка идеальные, солнце кричит «иди поиграй»~"

    ut "И я {i}так{/i} устала сидеть в четырех стенах."
    scene surfbeach1 (14) with dissolve
    ut "Я могла бы научить тебя серфингу, если это хорошая мотивация~"
    mc "Серфинг, хм?"

    mc "Не думал, что под всем этим блеском и дерзостью скрывается спортивный тип."
    scene surfbeach1 (17) with dissolve

    "Она накреняется через стойку к тебе, ее яркие волосы падают вперед."

    ut "Типа, реально обожаю это!"

    ut "Нет ничего лучше, чем выплыть, поймать волну и просто почувствовать себя живой, понимаешь?"
    scene surfbeach1 (18) with dissolve
    ut "Я бы с супер-охотой сгоняла на пляж с тобой. Что скажешь, красивый? Поехали со мной?"

    mc "Звучит круто, конечно, но у меня нет с собой плавок."
    scene surfbeach1 (19) with dissolve
    ut "Пфф, говно вопрос! Можешь одолжить плавки моего бывшего."

    ut "Он бросил кучу своего барахла у меня дома и так и не вернулся за ним."
    scene surfbeach1 (20) with dissolve
    mc "Фу, гадость, я не буду носить плавки твоего бывшего!"
    scene surfbeach1 (21) with dissolve
    ut "Ой, не будь ребенком, я постирала их с тех пор, как он свалил."

    mc "Все равно, это как-то странно."
    scene surfbeach1 (22) with dissolve
    ut "Это не странно, если ты сам не делаешь это странным, красотун."
    scene surfbeach1 (23) with dissolve
    ut "Ну да ладно, не хочешь — не надо."

    scene surfbeach1 (24) with dissolve
    ut "Но просто знай, что я буду в своем купальнике."
    scene surfbeach1 (25) with dissolve
    ut "В о-о-очень тесном бикини, которое врезается прямо мне в задницу~"

    mc "..."

    mc "Я могу надеть боксеры снизу."
    scene surfbeach1 (26) with dissolve

    mc "И все же… до пляжа довольно долго идти отсюда. В такую жару это займет вечность."

    ut "А кто сказал, что мы идем пешком? Мы поедем на моей тачке. Она припаркована сзади."

    mc "На твоей тачке? У тебя есть машина?"
    scene surfbeach1 (27) with dissolve
    "Утами выдает гордую ухмылочку, высунув язычок."

    ut "Агась! Погнали, покажу."
    scene surfbeach1 (28) with dissolve
    mc "(Я вечно забываю, что у людей в этом городе реально есть свои машины… Я хожу везде пешком как идиот.)"
    scene black with dissolve
    "Вы оба быстро заканчиваете последние приготовления к уборке. Утами переворачивает табличку «Закрыто» и запечатывает входную дверь с веселым мурлыканьем."



    "Минуту спустя вы выходите через задний ход на небольшую служебную парковку."
    scene surfbeach1 (32) with dissolve
    "Там припаркован большой, приподнятый пикап, в кузове которого уже закреплены доски для серфинга."

    "Он брутальный, практичный… и абсолютно не такой, каким его ожидаешь увидеть от человека, похожего на ходячий радужный взрыв."

    mc "…Пикап? Серьезно?"
    scene surfbeach1 (33) with dissolve
    ut "А что? Ты ожидал миленький розовый кабриолет или типа того?"

    "Она звонко смеется и опирается на дверцу водителя, скрестив руки под грудью."

    ut "Я могу выглядеть фифой и пустышкой, но не позволяй радужным волосам и блесткам обмануть тебя, детка."

    scene surfbeach1 (30) with dissolve

    ut "Карета подана, серфер-бой. Прыгай, пока я не передумала и не заставила тебя идти пешком."

    mc "И не подумал бы заставлять тебя ехать одной."
    scene surfbeach1 (29) with dissolve
    ut "Умный выбор. Я быстро устаю от скуки… а когда мне скучно, я склонна делать опасные вещи."
    scene surfbeach1 (30) with dissolve
    ut "Например, врубать музыку слишком громко или заставлять пассажира петь караоке со мной."

    scene black with dissolve
    "Ты забираешься в удивидельно чистую кабину. В ней слабо пахнет кокосовым кремом от загара и ее фруктовыми духами."

    ut "Пристегнись! Сначала быстро заскочим ко мне, чтобы ты забрал те плавки… а потом сразу на пляж."

    ut "Лучше приготовься промокнуть и повеселиться, потому что я не позволю тебе просто сидеть на песке как скучный кусок бревна."

    mc "Я уже начинаю жалеть об этом."

    ut "Врешь~ Ты улыбаешься. Я же вижу."
    play sound "audio/Sound/car.mp3" volume 1
    "Она заводит двигатель с приятным басовитым рокотом и ухмыляется тебе, вечернее солнце подсвечивает ее яркие волосы."

    ut "Готов к приключениям, [mcname]?"

    mc "…Готов, насколько это вообще возможно."

    ut "Вот это настрой! Погнали ловить волны, красотун~"

    scene black with fade
    "После быстрой остановки у Утами дома, чтобы переодеться и забрать плавки, вы наконец приезжаете на пляж."
    stop sound fadeout 1.0
    play ambient "audio/ambient/beachday.mp3" volume 0.6
    scene surfbeach1 (34) with dissolve
    "Солнце яркое и теплое, волны накатывают с хорошей ровной скоростью, а на пляже не слишком людно."

    "Утами выглядит абсолютно в своей стихии в обтягивающем ярком бикини, которое оставляет очень мало места воображению."

    "Она тащит свою доску под мышкой, буквально подпрыгивая от восторга."
    scene surfbeach1 (35) with dissolve
    ut "Наконец-то! Это именно то, чего я жаждала весь день~"
    scene surfbeach1 (37) with dissolve
    ut "Так, новичок, время для твоего первого урока серфинга."

    ut "Готов?"

    mc "Готов, насколько вообще могу быть…"
    mc "..."
    mc "То есть не особо."

    scene surfbeach1 (36) with dissolve
    ut "Не паришься, я тебя всему научу."
    ut "Просто слушай меня и постарайся не наесться песка слишком много раз, ок?"
    scene black with dissolve
    "Вы оба заходите в прохладную воду, пока она не доходит примерно до пояса. Утами встает рядом с тобой."
    scene surfbeach1 (38) with dissolve
    ut "Так, сначала база. Когда идет волна, ты гребешь изо всех сил на животе."

    ut "Затем, когда она приподнимает доску, ты быстро вскакиваешь."
    scene surfbeach1 (39) with dissolve
    ut "Колени согнуты, ноги на ширине плеч, держись низко и по центру."

    ut "Не вставай прямо, как в армии, все должно быть расслабленно."
    scene surfbeach1 (38) with dissolve
    mc "Понял… вроде как."
    scene surfbeach1 (44) with dissolve
    "Ты пробуешь. Волна толкает доску вперед, и ты пытаешься подпрыгнуть…"
    play sound "audio/sound/Watersplash.mp3"
    scene black with hpunch
    "Чтобы тут же потерять равновесие и вспахать лицом воду."
    scene surfbeach1 (42) with dissolve
    "Ты выныриваешь, кашляя и плюясь соленой водой."

    mc "Так… это было вообще не круто."
    scene surfbeach1 (38) with dissolve
    ut "Ха-ха! Неплохо для первой попытки."

    ut "Ты был слишком зажат. Расслабь тело немного."

    ut "Согни колени сильнее. Держи вес по центру доски. Чувствуй волну, а не борись с ней."
    scene surfbeach1 (43) with dissolve
    ut "Когда я скажу «вставай», ты подпрыгиваешь быстро, но плавно."
    scene surfbeach1 (44) with dissolve
    "Быстро приближается еще одна волна, Утами подбирает момент."
    ut "Готов? Вот идет одна."

    "Утами дает тебе легкий толчок в поясницу для нужного момента."

    ut "Греби! Греби! …Вскакивай!"
    scene surfbeach1 (45) with hpunch
    "Тебе удается подняться наполовину..."
    play sound "audio/sound/Watersplash.mp3"
    scene black with hpunch
    "Прежде чем доска заваливается, и ты снова летишь в воду с большим всплеском."
    scene surfbeach1 (40) with dissolve
    mc "Это куда сложнее, чем кажется!"

    ut "У тебя нормально получается~"
    ut "Большинство людей падает раз десять, прежде чем продержаться хотя бы две секунды."

    "Она звонко смеется и игриво брызгает на тебя водой."
    scene surfbeach1 (42) with dissolve
    ut "На, попробуй еще раз. Я буду прямо здесь и подскажу."
    scene surfbeach1 (44) with dissolve
    "Утами остается рядом, давая постоянные советы, пока ты делаешь еще несколько попыток."

    ut "Плечи расслабь… смотри вперед, а не вниз… о! Вот это было получше!"
    scene surfbeach1 (45) with dissolve
    ut "Ты почти удержался. Просто доделай рывок. Не сомневайся."
    scene surfbeach1 (46) with vpunch
    "Тебе наконец удается простоять пару секунд на доске!"

    ut "А-а-а-а! У-у-у-у!"

    ut "Краса-а-авчик~"

    ut "[mcname]! [mcname]! [mcname]!"

    play sound "audio/sound/Watersplash.mp3"
    scene black with hpunch
    "Прежде чем потерять равновесие и снова завалиться вбок."
    scene surfbeach1 (47) with dissolve
    mc "Я сделал это!"

    mc "…Типа того."

    ut "Да! Видишь?"

    ut "Ты уже вникаешь~"

    "Она радостно хлопает в ладоши."

    ut "Продолжай! Я не позволю тебе сдаться, пока ты не проедешься хотя бы на одной волне нормально. Приказ тренера Утами."

    mc "Тебе слишком нравится смотреть, как я фейлю."
    scene surfbeach1 (43) with dissolve
    ut "Ну естественно~ Смотреть, как симпатичные парни падают — это половина веселья."

    ut "Но я обещаю, что сделаю из тебя серфера, красотун."

    "Она подмигивает и готовится помочь тебе с следующей волной, явно кайфуя от происходящего."
    scene black with fade
    "Вы оба заканчиваете на сегодня."
    scene surfbeach1 (36) with dissolve
    ut "Это было так весело~"

    ut "Мы должны делать это постоянно!"

    mc "Звучит здорово, но в следующий раз я принесу свои шорты."

    mc "Эти мне постоянно натирают, по-моему, они немного маловаты."
    scene surfbeach1 (37) with dissolve
    "Утами выдает хитрую ухмылочку."

    ut "Значит, у тебя член побольше, чем у него..."

    mc "..."
    scene surfbeach1 (35) with dissolve
    ut "Так! Давай поторапливаться и отвезем тебя назад!"
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene black with dissolve
    "Вы переодеваетесь, и Утами везет тебя обратно к школе."

    $ unlock_event(Utami, "Surf Lesson", "utami_beach_one")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ utamisurf += 1
        $ Utami.affection += 1
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i}Привязанность Утами увеличена.{/i}"
        $ Utami.quest = "Навести Утами снова в ее салоне."

    jump weekday_evening

label utami_beach_two:
    scene utamiintro (7) with fade
    "Гудение фенов и болтовня манят тебя к салону Утами."
    scene black with dissolve
    play sound "audio/sound/dooropen.mp3"
    play music "audio/Music/utami.mp3" fadein 1.0
    "Ты толкаешь дверь салона еще одним жарким днем среды."

    "Знакомый фруктовый аромат лака для волос и шампуня бьет тебя в нос мгновенно."

    "Утами за стойкой, мурлычет себе под нос, расставляя кое-какие баночки."

    "Она поднимает взгляд, как только ты заходишь, и ее лицо проясняется."
    scene surfbeach2 (1) with dissolve
    ut "Ну надо же~ Смотрите, кто снова решил появиться!"

    ut "Мой любимый почти-серфер."

    mc "Почти-серфер? Мне казалось, в прошлый раз у меня вполне нормально получилось."
    scene surfbeach2 (2) with dissolve
    ut "Ха-ха! Ты простоял целых три секунды."

    ut "Я бы сказала, это уверенно ставит тебя в категорию «Почти серфер»."

    ut "Но это прогресс! Я горжусь тобой."

    "Она опирается на стойку, положив подбородок на ладони и даря тебе игривую улыбку."
    scene surfbeach2 (3) with dissolve
    ut "Так что… скажи честно..."

    ut "Тебе было весело на пляже в прошлый раз? Даже со всеми падениями лицом в воду?"

    mc "Да, на самом деле было довольно весело."

    mc "Даже если я выпил половину морской воды."

    "(К тому же, не думаю, что мое бледное тело создано для такого количества солнца.)"
    scene surfbeach2 (4) with dissolve
    ut "Видишь? Я знала, что тебе понравится. Океан умеет завлекать людей."

    "Утами бросает взгляд в окно на яркий солнечный свет, затем возвращается к тебе с лукавым огоньком в глазах."
    scene surfbeach2 (5) with dissolve
    ut "Кстати говоря… сегодня снова тупо жаркий день."

    ut "Снова идеальная погода для пляжа~"

    "Она смотрит на тебя с кривой ухмылкой."

    ut "Я тут подумала… не хочешь снова сгонять на пляж со мной?"

    ut "Типа прямо после того, как я закроюсь?"
    scene surfbeach2 (3) with dissolve
    ut "Мы можем пропустить всю эту тему с «обучением новичка» на этот раз и просто кайфануть.~"

    mc "Снова?"

    mc "Ты реально не можешь без волн, да?"
    scene surfbeach2 (9) with dissolve
    ut "Виновна~ Серфинг — моя терапия. К тому же…"

    "Она мило наклоняет голову и бросает на тебя дразнящий взгляд."
    scene surfbeach2 (10) with dissolve
    ut "Мне было очень весело с тобой в прошлый раз."

    ut "Смотреть, как ты падаешь, было мило, но в этот раз я хочу покататься как следует."

    ut "Может, переймешь у меня пару навыков из первых рук~"
    scene surfbeach2 (11) with dissolve
    mc "Ты просто хочешь еще посмеяться надо мной, когда я буду падать."

    ut "Может, капельку. Но в основном мне нужна компания."

    ut "Пляж всегда веселее, когда ты с кем-то~."

    "Ты скрещиваешь руки на груди и ухмыляешься ей."
    scene surfbeach2 (13) with dissolve
    mc "А что, если я скажу нет?"

    ut "Тогда я буду супер-грустной и мне придется ехать одной…"
    scene surfbeach2 (14) with dissolve
    ut "В том крошечном бикини, которое тебе так понравилось в прошлый раз."

    "Она подмигивает и делает игривый круговорот за стойкой."

    mc "...Ты вообще не умеешь быть тонкой, да?"
    scene surfbeach2 (12) with dissolve
    ut "Тонкость — это скучно. Так что скажешь, красотун? Пляж, раунд два?"

    mc "Ладно, ладно. Я в теме."
    scene surfbeach2 (13) with dissolve
    ut "Е-е-е! Вот это я понимаю подход."

    "Утами радостно хлопает в ладоши, ее яркие волосы подпрыгивают."

    ut "Дай мне минут двадцать, чтобы закончить закрытие, и можем ехать."
    ut "Уговор тот же, что и в прошлый раз, лучше приготовь плавки!"

    play ambient "audio/ambient/beachday.mp3" volume 0.6
    scene black with dissolve
    "Волны сегодня немного больше, но после прошлого урока ты держишься вполне достойно."

    "Тебе удается встать на нескольких небольших волнах и даже проехать на одной приличное расстояние. Утами подбадривает тебя каждый раз."
    scene surfbeach2 (16) with dissolve
    ut "Да! Это было куда лучше, чем вчера! У тебя реально получается, серфер-бой~"

    mc "Не сглазь. Я все еще чувствую, что я в одном неверном движении от того, чтобы снова наесться песка."
    scene surfbeach2 (15) with dissolve
    "Утами звонко смеется, гребя рядом с тобой на своей доске в том же самом крошечном цветном бикини."

    ut "Ты отлично держишься! Просто держи вес по центру и—"
    stop music fadeout 1.0
    scene surfbeach2 (17) with dissolve
    "Ее слова прерываются, когда позади вас обоих поднимается огромная волна."

    ut "Воу— большая идет! Спокойно!"
    play sound "audio/sound/Watersplash.mp3"
    scene surfbeach2 (18) with hpunch

    "Твоя доска сильно заваливается. Ты теряешь равновесие, падаешь вбок и врезаешься прямо в Утами."
    "Удар отправляет вас обоих под воду в хаотичную кучу-малу из конечностей, пены и досок."
    scene black with vpunch
    "Когда ты выныриваешь, кашляя и жадно хватая воздух, ты тут же замечаешь, что что-то очень не так."
    ut "Фух, нам повезло. Ну и дичь была, а?"
    scene surfbeach2 (19) with dissolve
    mc "...."

    mc "(Прекрати пялиться.)"

    mc "(Посмотри на чайку.)"
    mc "(Посмотри на солнце и сожги себе сетчатку.)"

    mc "..."

    mc "(Звуки подключающегося модема.)"

    ut "Блин, тут что, похолодало или—"
    scene surfbeach2 (20) with hpunch
    "Она смотрит вниз, осознает, что произошло, и ее лицо мгновенно заплывает густым румянцем."

    ut "Ой, бля—! Куда делся мой верх?!"
    scene surfbeach2 (21) with dissolve
    "Она быстро прикрывает обнаженную грудь обеими руками, выглядя смущенной впервые с тех пор, как ты ее знаешь."

    ut "Типа, нам нужно срочно найти укрытие!"

    ut "Я НЕ позволю кому-то еще смотреть на них бесплатно."
    scene surfbeach2 (22) with dissolve
    "Ты пытаешься осмотреть территорию в поисках чего-то, что можно использовать как укрытие."

    mc "…Э-э."

    "Ты, к сожалению, ограничен в возможностях из-за того обстоятельств, что вы находитесь в чертовом океане."

    "В нескольких метрах от вас ты замечаешь ее яркий верх от бикини, плавающий возле камней."
    scene surfbeach2 (23) with dissolve
    mc "Вон там! Возле скал. Поплыли туда, пока никто не увидел."
    stop ambient fadeout 1.0
    scene black with dissolve
    "Вы оба быстро плывете к кучке скал, торчащих из воды и закрывающих вас от основного пляжа."
    scene surfbeach2 (24) with dissolve
    "Оказавшись за скалами и скрывшись из виду, Утами издает раздраженный вздох, все еще прикрываясь."

    ut "Угх, как же это бесит… Мне так нравился этот верх. Глупая волна."

    "Сейчас она скорее раздражена, чем смущена, осматривая воду вокруг."
    play music "audio/Music/Jazzy.mp3" volume 0.75 fadein 1.0
    scene surfbeach2 (25) with dissolve
    "Ее грудь пышная, упругая и блестит от морской воды на ярком солнце."
    scene surfbeach2 (25) with hpunch
    mc "(ЧАЙКИ! СОЛНЦЕ! ДАВАЙ, [mcname!u]!)"

    "Утами замечает это почти мгновенно."
    scene surfbeach2 (26) with dissolve
    ut "…Эй. Вообще-то мои глаза выше."

    mc "Извини— я не хотел—"
    scene surfbeach2 (27) with dissolve
    ut "Не хотел? Ты уставился на мою сиську и смотришь уже секунд двадцать подряд."
    scene surfbeach2 (28) with dissolve
    "Она слегка сдвигает руки, выставляя грудь напоказ, и наклоняет голову с игривым огоньком в глазах."

    ut "В чем дело, [mcname]?"

    ut "Никогда не видел девчонку без верха~"

    ut "Или мои просто выглядят настолько хорошо, когда они мокрые и упругие?"
    mc "..."

    mc "(Думаю, мне больше не нужно смотреть на чаек.)"
    "Ты тяжело сглатываешь, не в силах выдать разумный ответ."
    scene surfbeach2 (29) with dissolve
    ut "Хе-хе~ Посмотрите на него. Весь раскраснелся."

    ut "Это даже мило~"

    "Она подплывает чуть ближе в воде, ее голос снижается до томительного шёпота."

    ut "Раз уж ты и так смотришь во все глаза… может, хочешь взглянуть поближе?"

    mc "П-погоди секунду, это как-то слишком прямолинейно, нет?"

    ut "Пфф, мы же взрослые люди—"
    scene surfbeach2 (30) with dissolve
    ut "К тому же, я уверена, Нора не будет против... Если она не узнает, конечно."

    mc "Не уверен, что это хорошая идея—"
    scene surfbeach2 (29) with dissolve
    ut "Ну, а вот он говорит обратное."

    "Твое сердце колотится. Она замечает твое явное возбуждение, и ее улыбка становится только шире."

    ut "М-м-м… кто-то взбудоражился.~"

    ut "Знаешь… мы тут отлично скрыты за скалами, нас никто не увидит~"
    scene black with dissolve
    "Она подбирается еще ближе, прижимаясь обнаженной грудью к тебе, ее голос становится томящим."

    ut "Хочешь, чтобы я позаботилась об этом?"

    ut "Вот этими~?"

    "Не дожидаясь окончательного ответа, Утами запускает руки под твои плавки и высвобождает твой твердеющий член."
    "Она делает пару медленных поглаживаний под водой, прежде чем направить его между своих мягких, мокрых сисечек."

    ut "Вот так~ Просто расслабься и дай мне со всем разобраться."

    "Она сжимает груди вокруг твоей плоти, создавая тесный, теплый тоннель."
    "Ощущения невероятные — мягко, скользко от морской воды и очень приятно."

    scene utamiboob with dissolve

    "Утами начинает двигать бюстом вверх и вниз, скользя по твоему члену между сисек плавными, размеренными движениями."

    ut "М-м-м… чувствуешь, какие они мягкие? Ты так смотрел… Я подумала, тебе это понравится."

    "Она смотрит на тебя с шаловливой улыбкой, вода капает с ее ярких волос."

    ut "Давай, ты можешь трогать их, пока я это делаю. Сжимай их… играй с моими сосками, если хочешь."

    "Ты опускаешь руки и ласкаешь ее грудь, пока она продолжает ласкать тебя, ее мягкая плоть полностью обволакивает тебя."

    "Утами ускоряет темп, сжимая сиськи еще сильнее и время от времени облизывая головку твоего члена, когда она выскакивает между ними."

    ut "Ах-х~ Ты становишься еще тверже… Тебе приятно, красотун?"

    ut "Можешь кончать, когда захочешь. Просто залей мне всю грудь, если хочешь~ Я не против испачкаться."

    "Сочетание ее дразнящих слов, теплого давления ее груди и рискованной обстановки быстро доводит тебя до грани."

    mc "Утами… я уже близко—"

    ut "Тогда сделай это. Кончи для меня~"
    play sound "audio/Sound/cum.wav" 
    scene surfbeach2 (31) with flash

    "Со стоном ты толчком входишь между ее сисек в последний раз и разряжаешься, густые струи семени брызгают на ее грудь и шею."

    "Утами издает довольный тихий стон, выдавливая последние капли своей грудью."
    scene surfbeach2 (32) with dissolve
    ut "М-м-м… ну вот и все. Посмотри, какой беспорядок ты навел~"

    "Она смотрит вниз на свою измазанную грудь с игривой ухмылкой, затем снова на тебя."
    scene surfbeach2 (33) with dissolve
    ut "Похоже, мне придется еще раз искупаться, чтобы отмыться… или, может, я просто позволю тебе поглазеть еще немного."
    scene black with dissolve
    "Она подмигивает тебе и мягко целует в щеку."

    ut "Это было весело. Нам стоит устроить такие «случайности» почаще."

    mc "Ага. Да."

    mc "..."

    mc "Вау."


    $ unlock_event(Utami, "Beachjob", "utami_beach_two")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ Utami.affection += 5
        $ Utami.lust += 3
        $ utamibeachbj += 1
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i}Привязанность и похоть Утами увеличены.{/i}"
        $ Utami.quest = "На этом пока всё!"
        jump weekday_evening
return