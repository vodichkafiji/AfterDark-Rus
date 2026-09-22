label parker_intro:
    scene parkerintro (1) with fade

    "Ты успеваешь сделать всего два шага из класса, прежде чем голос Оттум разрезает тишину."
    show autumnschool_idle (1) at left with dissolve
    show mcschool_sigh at right with dissolve
    mc "Что на этот раз?"

    a "Раз уж ты наконец начал почаще выползать из своей пещеры..."
    a "...можешь заняться чем-то полезным."
    hide mcschool_sigh with dissolve
    show mcschool (10) at right with dissolve
    mc "Звучит подозрительно так, будто ты собираешься повесить на меня какую-то поручение."
    hide autumnschool_idle (1) with dissolve
    show autumnschool_armcrossed (1) at left with dissolve
    a "Бинго. Ты идешь за продуктами. Сегодня. Поздравляю, тебя повысили до мальчика на побегушках."
    a "Купи молоко, яйца и только не всякую странную хрень, которую ты обычно жрешь."
    hide mcschool (10) with dissolve
    show mcschool_armedcross at right with dissolve
    mc "Мне хотя бы положен список покупок, или это проверка моих экстрасенсорных способностей?"
    hide autumnschool_armcrossed (1) with dissolve
    show autumnschool_armcrossed (2) at left with dissolve
    a "Выживешь. Ты знаешь, где магазин."
    a "Главное, не сворачивай, чтобы поныть под мостом или чем ты там обычно занимаешься, когда исчезаешь."
    hide mcschool_armedcross with dissolve
    show mcschool_sigh at right with dissolve
    mc "Я вообще-то просто пытался выйти из класса."
    hide autumnschool_armcrossed (2) with dissolve
    show autumnschool_armcrossed (3) at left with dissolve
    a "Ага, а теперь ты уходишь с целью. Не за что."
    hide autumnschool_armcrossed (3) with moveoutleft
    hide mcschool_sigh with dissolve

    show mcschool (9) with dissolve
    mc "...Похоже, теперь я выполняю квесты «подай-принеси»."
    hide mcschool (9) with dissolve
    show mcschool_tired (2) with dissolve
    mc "Ну, не то чтобы у меня были другие планы на сегодня."

    scene black with fade
    "Город гудит жизнью, но ничто из этого не кажется особо интересным."

    "Люди несутся мимо, словно все опаздывают на что-то очень важное. Машины сигналят. Кто-то орет про хот-доги через квартал. И все же, каким-то образом, всё это... скучно."
    scene parkerintro (2) with dissolve
    mc "(Так, нам просто нужны яйца, молоко и хлеб.)"

    mc "(Яйца, молоко и хлеб. Яйца, молоко и хлеб. Яйца, молоко и хлеб.)"


    scene parkerintro (3) with dissolve
    mc "(Мяйца, лолоко и хлеб.)"

    mc "(...Что-то не то.)"

    mc "(Что я вообще должен был сделать?)"
    scene parkerintro (4) with dissolve
    stop music fadeout 2.0
    mc "(Кажется, от запаха выхлопных газов у меня кружится голова.)"
    play ambient "audio/Ambient/running.mp3"

    mc "(Внезапно быть хреновым сычом-домоседом кажется не такой уж и плохой идеей.)"

    scene parkerintro (5) with dissolve
    "Ты настолько погружен в свои мысли, что даже не замечаешь громких и быстрых шагов позади себя."
    scene parkerintro (6) with dissolve
    mc "(Хм?)"
    stop ambient 
    mc "(Кто-то только что положил руку мне на плечо?)"
    scene parkerintro (7) with dissolve

    mc "(И кто бы это мог... {nw})"
    play sound "audio/Sound/swoosh.mp3"
    scene parkerintro (8) with hpunch
    mc "(...БЫТЬ?!)"

    "Ты поднимаешь глаза и видишь, что кто-то использует твое плечо, чтобы встать на руки."
    play music "audio/Music/cooltune.mp3"
    scene parkerintro (9) with dissolve

    "Прежде чем ты успеваешь среагировать, незнакомец уже перелетает через твою голову."


    "Воздух над тобой рассекается. Стремительная тень проносится в считанных сантиметрах от твоего лица."

    scene parkerintro (10) with dissolve

    "Девушка приземляется на тротуар перед тобой, идеально удерживая равновесие, будто делает подобное каждый день."

    mc "(Что за... колонна?)"
    scene parkerintro (11) with dissolve

    "Она продолжает бежать, едва удоставив тебя взглядом — пока не разворачивается прямо на ходу и не бросает салют двумя пальцами."
    scene parkerintro (12) with hpunch
    mc "Эй! Какого хера?!"
    mc "Нельзя просто так перепрыгнуть через человека и ничего не сказать!"

    scene parkerintro (13) with dissolve

    "Девушка игнорирует тебя и продолжает бежать вперед."
    scene parkerintro (13) with hpunch
    mc "ЭЙ, МУДАК! Я ЗНАЮ, ЧТО ТЫ МЕНЯ СЛЫШИШЬ!"
    scene parkerintro (13) with hpunch
    mc "ТЫ ХОТЯ БЫ ИЗВИНИТЬСЯ НЕ ХОЧЕШЬ?!"

    scene parkerintro (14) with dissolve
    window hide dissolve
    $ renpy.pause(1, hard=True)
    scene parkerintro (15) with hpunch
    window hide dissolve
    "Вместо ответа девчонка просто показывает тебе средний палец."
    scene parkerintro (16) with dissolve
    mc "(Да что с ней вообще не так?!)"
    mc "(Клянусь, некоторых людей в детстве вообще не учили манерам.)"
    scene parkerintro (17) with dissolve
    mc "(Ну и ладно. В конце концов, она никоим образом не навредила мне, кроме как испугала.)"

    mc "(Надо просто вернуться к списку покупок. Может, стоит записать где-то... {nw})"

    mc "(Постойте-ка...)"

    play sound "audio/Sound/bong.mp3"
    scene parkerintro (18) with hpunch
    mc "(ГДЕ МОЙ КОШЕЛЕК?!)"

    "Тебе требуется ровно две наносекунды, чтобы понять, почему девчонка не сбавляла скорость."
    scene parkerintro (19) with hpunch
    "Ты срываешься на бег, не сводя с нее глаз, пока она спринтует впереди."

    mc "ВЕРНИСЬ, ВОРОВКА!!"

    scene black with fade
    window hide dissolve 
    pause 2.0
    scene parkerintro (20) with dissolve
    show parker_run at right with moveinright

    "Ты заворачиваешь за угол на полной скорости. Она все еще впереди — едва-едва — петляя по узкому переулку, будто хозяйка этих мест."

    show mcschool_run (2) at left with moveinright

    "Она оглядывается один раз, замечает тебя и ухмыляется из-под маски."

    u "А ты соображаешь быстрее большинства! Теперь попробуй удержаться на хвосте!"
    hide parker_run with moveoutleft
    "После этого девчонка прибавляет ходу со сбивающей с толку скоростью."
    mc "(Ей что, НРАВИТСЯ всё это?!)"
    hide mcschool_run (2)
    show mcschool_run (1) at left
    mc "Я верну свой кошелек!"
    mc "Там же целых 9 долларов и купон в Коала Кафе!"
    hide mcschool_run (1) with moveoutleft

    "Ты бежишь еще быстрее, проносясь мимо чела с кофе. Он что-то кричит тебе вслед, но ты уже далеко."



    scene utamiintro (6) with dissolve

    "Мусорные баки. Пожарные лестницы. Кирпичные стены пролетают мимо."

    "Она хватается за край мусорного контейнера и перелетает через него так, будто репетировала это сотню раз."

    "Ты неуклюже следуешь за ней, едва не споткнувшись о выброшенный велосипед, но удерживаешь темп."

    mc "(Черт! Такое ощущение, что она знает этот город как свои пять пальцев!)"

    "Затем девчонка исчезает в открытом окне."

    "Не оставляя тебе иного выбора, кроме как проследовать за ней."

    scene parkerintro (21) with dissolve

    mc "Да *ладно* вам."

    mc "(Я же ненавижу *лестницы*.)"

    "Ты влетаешь в здание — какой-то старый жилой дом — взлетая по тесному лестничному пролету через две ступеньки."

    "Третий этаж. Четвертый. И затем—"

    scene parkerintro (22) with hpunch

    "Ты вырываешься на крышу, легкие горят, сердце колотится как бешеное."

    "Город раскинулся внизу, звуки машин теперь где-то далеко."

    show parker_smug at right with moveinleft

    "И вот она."

    "Стоит у самого края, поджидая, пока ты ее догонишь."
    show mcschool_tired (3) at left with moveinright

    mc "Так.. {w}*хах*... {w}теперь некуда... {w}*хах*... {w}бежать..."
    hide mcschool_tired (3)
    show mcschool_tired (2) at left
    mc "(Оу, чувак, я вообще не в форме.)"

    "Она даже не вздрагивает. Вместо этого просто склоняет голову набок."
    hide parker_idle (2)
    show parker_idle (2) at right

    u "А ты неплох. Я думала, ты сдашься еще на полпути."

    hide mcschool_tired (2)
    show mcschool_tired (1) at left

    mc "Ну да, люди имеют тенденцию проявлять настойчивость, когда у них что-то воруют."

    "Ты видишь, как под ее маской расплывается ухмылка, прежде чем она начинает разворачиваться."

    hide parker_idle (2)
    show parker_idle (1) at right


    u "Мило. Но тебе стоит знать, что это еще не конец."
    hide parker_idle (2)
    show parker_run at right

    hide parker_run with moveoutleft
    u "Посмотрим, сможешь ли ты свалить за мной!"

    "Прежде чем ты успеваешь шевельнуться, она разгоняется прямо к краю крыши."
    scene parkerintro (23) with dissolve

    mc "(Без шансов. Ни за что на свете.)"

    "Она прыгает с крыши."

    scene parkerintro (24) with dissolve

    "Ты в панике бросаешься к краю — но она уже благополучно приземлилась на крышу напротив."

    mc "Ты, должно быть, шутишь."
    scene parkerintro (25) with dissolve
    u "Что ж, похоже, твоя удача закончилась, здоровяк."

    u "Если только тебе не все равно на падение с шести метров прямо в переулок."

    scene parkerintro (26) with dissolve

    "Это далеко. Слишком далеко."

    "Ветер усиливается вокруг тебя, трепля одежду."

    mc "(Она реально прыгнула?)"

    mc "(Боже... Я зашел слишком далеко.)"

    u "В чем дело? Зассал лететь?"

    mc "(...)"

    mc "Да к черту... Я зашел уже так далеко."

    scene parkerintro (27) with dissolve

    "Ты медленно отходишь на другую сторону крыши."


    u "Так ты убегаешь? Умный выбор."

    u "Ни за что какой-то придурок без подготовки не перепрыгнет этот разрыв— {nw}"
    stop music fadeout 1.0

    "Ты не даешь себе времени подумать о том, что произойдет дальше."
    play ambient "audio/Ambient/running.mp3"
    scene parkerintro (28) with dissolve

    "Ты просто начинаешь бежать."
    scene parkerintro (29) with dissolve

    "Каждый шаг отдается в ушах. Ты достигаешь края. Прыжок."
    stop ambient 
    scene parkerintro (30) with dissolve
    window hide dissolve
    pause 2.0
    scene parkerintro (31) with dissolve
    window hide dissolve
    pause 2.0
    scene parkerintro (32) with dissolve


    "Время растягивается."

    "Ты в воздухе."

    "Кажется, будто весь мир вокруг замер на пару секунд."

    scene parkerintro (33) with dissolve

    "Крыша становится все ближе и ближе. Кажется, ты уже в считанных сантиметрах от края."

    mc "(Я сделаю это!)"

    mc "(Я долечу!)"

    scene parkerintro (34) with hpunch

    "А затем — падение."

    mc "(Я не долечу!)"

    mc "(Слишком далеко. Слишком—!)"

    "Край крыши стремительно несётся тебе навстречу, как пощечина."

    mc "(Неужели я реально вот так сдохну?!)"

    mc "(После всего, что я сделал, чтобы стать лучше?!)"

    mc "(Это не может так закончиться! Мне еще столько всего нужно сделать!)"

    mc "(Не может быть...)"

    mc "(...)"
    scene black with dissolve
    "Ты закрываешь глаза, готовясь к удару."

    mc "(Не может...)"

    mc "(...)"

    mc "(Прости, Кицунэ.)"

    mc "(Прости, Оттум.)"

    mc "(Простите меня, все.)"

    mc "(Но, кажется, для меня все кончено.)"

    mc "(Я просто... {w}хотел бы, чтобы вы гордились мной.)"
    scene parkerintro (35) with dissolve
    window hide dissolve
    pause 2
    play sound "audio/Sound/eyes.wav"
    image white = "#ffffff"
    scene white with quickerflash
    scene parkerintro (36) with quickerflash

    mc "Нет..."

    scene parkerintro (37) with dissolve
    window hide dissolve
    pause 2

    "Знакомый гул просыпается в твоей груди — словно разряд статического электричества в венах."
    play sound "audio/Sound/powerup.mp3"
    scene parkerintro (64) with quickerflash
    scene parkerintro (39) with quickerflash
    scene parkerintro (38) with quickerflash
    scene parkerintro (64) with quickerflash
    scene parkerintro (39) with quickerflash
    scene parkerintro (38) with quickerflash
    scene parkerintro (64) with quickerflash
    scene parkerintro (39) with quickerflash
    scene parkerintro (64) with quickerflash
    scene parkerintro (39) with quickerflash
    scene parkerintro (64) with quickerflash
    scene parkerintro (39) with quickerflash
    scene parkerintro (64) with quickerflash
    scene parkerintro (38) with quickerflash
    "Твоя нога начинает накапливать силу."

    play sound "audio/Sound/possesion.mp3"
    scene parkerintro (40) with quickerflash
    scene parkerintro (65) with quickerflash
    scene parkerintro (41) with quickerflash
    "Импульс энергии взрывается под твоими ногами."

    play sound "audio/Sound/thud.mp3"
    scene parkerintro (42) with hpunch

    "Ты врезаешься в край соседнего здания, пальцы судорожно цепляются за выступ."

    mc "(Епать—!)"

    mc "(Я жив!? Как, черт возьми?!)"

    scene parkerintro (43) with dissolve

    "У тебя нет времени думать."

    scene parkerintro (44) with dissolve

    "Ты соскальзываешь. Пальцы царапают кирпич."

    "Ты так близко к краю, но долго не продержишься."

    scene parkerintro (45) with dissolve
    window hide dissolve
    pause 2

    play sound "audio/Sound/armgrab.mp3"
    scene parkerintro (46) with hpunch
    window hide dissolve
    "Рука хватает тебя за запястье."
    scene parkerintro (48) with dissolve
    u "Что ты, черт возьми, творишь!?"

    u "Это было... *НЕВЕРОЯТНО* тупо."

    scene parkerintro (49) with dissolve

    "Она вытягивает тебя наверх с поразительной силой."
    play sound "audio/Sound/hoodie.wav"
    scene black with fade

    "Ты валишься на крышу, сердце колотится как безумный барабан."

    scene parkerintro (51) with dissolve


    mc "*Хах*... Я в норме."

    u "Ты, блядь, прыгнул с крыши и чуть не разбился!"

    u "Я имею в виду, кто вообще {i}в здравом уме{/i} так делает?!"

    mc "...."

    mc "Ты буквально сделала только что ровно то же самое!"

    scene parkerintro (50) with dissolve
    u "Ну вообще-то да, но {i}я{/i} крутая."

    u "И я делала это столько раз, что это стало моей второй натурой."

    scene parkerintro (51) with dissolve

    u "Ты {i}едва{/i} в норме."

    mc "У меня все было под контролем."

    u "Ты падал."

    mc "Ну, иногда приходится рисковать, когда сумасшедшая цирковая девка ворует твой кошелек."

    u "Эй! Вообще-то это не очень вежливо!"

    mc "ВОРОВАТЬ КОШЕЛЬКИ ТОЖЕ НЕ ОЧЕНЬ ВЕЖЛИВО!!"
    scene parkerintro (50) with dissolve

    u "...{w}справедливо."

    mc "Вот и договорились. А теперь сними маску, чтобы я мог заявить на тебя в полицию."

    scene parkerintro (52) with dissolve

    "Она вздыхает и качает головой, с трудом сдерживая смешок."

    u "Ну, можешь попытаться, у них и так со мной полно хлопот."

    scene parkerintro (53) with dissolve
    window hide dissolve
    pause 2.0
    play music "audio/Music/parker.mp3" volume 0.75 fadein 1.0
    scene parkerintro (54) with dissolve
    "Девушка снимает маску, открывая довольно симпатичное лицо."
    scene parkerintro (56) with dissolve
    u "Теперь ты доволен, психованный?"

    "Ты бы сделал ей комплимент, если бы не тот факт, что в данный момент у нее твои деньги на продукты."

    scene parkerintro (55) with dissolve


    u "Меня зовут Паркер."

    mc "Замечательно. Паркер. Воровка. Сорвиголова. Ещё и карманница по совместительству?"

    scene parkerintro (61) with dissolve
    pa "Прямо в яблочко!"

    "Ты вытягиваешь руку в ожидательном жесте."

    mc "Кстати, о кошельках…"

    scene parkerintro (56) with dissolve

    "Паркер изогнула бровь. Прежде чем осознать, что бежать ей больше некуда."
    scene parkerintro (57) with dissolve

    pa "Оу... {w}точно. Полагаю, ты его заслужил, да."

    scene parkerintro (62) with dissolve

    "Со вздохом она шарит по своим карманам, прежде чем найти его."

    scene parkerintro (63) with dissolve

    pa "Вот, держи! Клянусь, из него ничего не пропало!"

    pa "Так что технически я его даже не воровала, а просто одолжила без спроса."

    scene parkerintro (60) with dissolve

    "Она бросает его тебе, и ты ловишь кошелек, раскрывая его. Все на месте."

    mc "(Даже мой студенческий... Впечатляющая сдержанность.)"

    scene parkerintro (61) with dissolve

    pa "Я не краду чужие личности, я просто обычный воришка."

    "Ты уставился на нее. Она улыбается."

    scene parkerintro (60) with dissolve

    pa "Не думала, что ты удержишься за мной. Большинство отсеивается."

    mc "Ну да... Я не привык легко сдаваться."

    scene parkerintro (55) with dissolve

    pa "Это заметно. А та фишка с ускорением? Выглядело довольно круто."

    mc "Э-э-э, ты о чем?"

    scene parkerintro (56) with dissolve

    pa "..."

    scene parkerintro (57) with dissolve

    pa "Хм... да неважно. Наверное, показалось."

    scene parkerintro (61) with dissolve

    pa "В общем, давай потусим в следующий раз, когда будешь в центре."

    scene parkerintro (55) with dissolve

    mc "Ты шутишь?! С чего бы мне тусоваться с кем-то, кто пытался меня ограбить?!"

    pa "Я думала, мы сошлись на том, что я просто {i}одолжила{/i} у тебя вещь."

    pa "И вообще, ты что, гулял по городу один в понедельник днем?"
    scene parkerintro (60) with dissolve

    pa "Пф-ф-хах, тебе определенно нужны друзья."

    mc "Эй!{w} Это не... {nw}"

    scene parkerintro (61) with dissolve

    pa "Но это норма! Потому что у меня тоже особо нет друзей!"

    pa "Так что мы можем быть одиночками вместе!"

    "Ты почти поражен тем, как она вообще не видит ничего безумного в том, что предлагает."

    scene parkerintro (60) with dissolve
    mc "И как именно я должен это сделать? Ты же даже не дала мне свой номер."
    scene parkerintro (56) with dissolve
    pause

    pa "..."

    scene parkerintro (59) with dissolve

    pa "Ты что, подкатываешь ко мне?"

    scene parkerintro (59) with hpunch

    mc "Что? Нет! Какого... *абсолютно нет*."

    scene parkerintro (61) with dissolve

    "Она хихикает, явно наслаждаясь этим."

    scene parkerintro (60) with dissolve

    pa "Расслабься. Я сама найду тебя, когда надо будет..."

    mc "Ладно... {w}Вообще ни разу не жутко."

    mc "(Да что *не так* с этой девчонкой?)"

    scene parkerintro (53) with dissolve

    "Она отступает назад, снова надевая маску."

    scene parkerintro (51) with dissolve

    pa "Увидимся, [mcname]"

    mc "Ну, допустим, увидимся."

    scene parkerintro (51) with hpunch

    mc "Погоди! Я же не говорил тебе своего имени?!"

    scene parkerintro (52) with dissolve

    pa "Я сказала, что я не {i}ворую{/i} личности."

    pa "Но я никогда не говорила, что не подглядывала в твой документ."

    scene parkerintro (51) with dissolve

    pa "Кстати, у тебя читательский билет скоро просрочится."

    scene black with fade

    "Паркер исчезает в соседнем переулке, испаряясь так же быстро, как и появилась."

    mc "(…Ну, это было мощно.)"

    stop music fadeout 1.0

    "Ты возвращаешься домой, где у дверей тебя встречает Оттум."

    mc "Офигеть, ты не поверишь, какой у меня был денек!"

    a "Я тоже!"

    a "Мы с Изрой обедали, и она пролила ванильный йогурт прямо мне на футболку!"

    a "Так что весь день это выглядело так, будто... {nw}"

    mc "Ты knew, что в городе есть воры-паркуристы?"

    a "..."

    a "Ладно, твоя история звучит интереснее."

    a "Расскажешь, пока разбираем продукты."

    mc "..."

    a "..."

    mc "..."

    a "Ты забыл купить продукты, не так ли..."
    $ unlock_event(Parker, "Gimme my wallet!", "parker_intro")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ intro_parker += 1
        $ Parker.affection += 1

        $ Parker.quest = "Навести Паркер в городе в понедельник."
        play sound "audio/Sound/affection.mp3" volume 0.5

        "{i}Теперь вы можете навещать Паркер в городе по понедельникам.{/i}"

        jump weekday_evening



label parkercityintro:
    scene parkercityintro (1)
    with dissolve
    "Утро понедельника, и каким-то образом тебя снова впрягли идти за продуктами."

    "Ты срезаешь путь через узкий переулок, чтобы сэкономить время, бубня себе под нос цены на яйца, как выживший из ума пенсионер."
    scene parkercityintro (2)
    with dissolve
    mc "(Честно говоря, я даже не злюсь — я просто поражен способностью Оттум заставить меня чувствовать вину и подтолкнуть к черновой работе.)"

    mc "(С другой стороны, она всегда была неоправданно хороша в подобных вещах.)"
    scene parkercityintro (3)
    with dissolve
    mc "(Или, может, мне просто нужно наконец отрастить хребет.)"
    stop music fadeout 2.0
    scene parkercityintro (4)
    with dissolve

    "Две руки внезапно закрывают мне глаза."
    stop music fadeout 2.0

    pa "Угадай, кто-о-о~"

    mc "Ну... не думаю, что грабители или насильники обычно раскрывают свою личность, так что я скажу Паркер?"

    scene parkercityintro (5)
    with dissolve
    play music "audio/Music/parker.mp3" volume 0.75 fadein 1.0

    pa "Дин-дин-дин! У нас есть победитель, народ!"

    scene parkercityintro (6)
    with dissolve

    "Она медленно кружит вокруг меня, как самодовольная акула с СДВГ."
    scene parkercityintro (7)
    with dissolve

    pa "А у тебя хорошие инстинкты. Я *реально* висела на той пожарной лестнице, как летучая мышь, поджидающая момента для броска."

    scene parkercityintro (8)
    with dissolve

    mc "Ты реально относишься к городу как к своей личной детской площадке, да?"

    scene parkercityintro (9)
    with dissolve

    pa "Что я могу сказать? У нас с гравитацией свободные отношения."
    scene parkercityintro (10)
    with dissolve

    pa "Но эй, пока ты все равно обратил на меня внимание..."

    pa "Хочешь попробовать кое-что крутое?"
    scene parkercityintro (11)
    with dissolve

    mc "Уточни определение «крутого». Потому что если это связано с кражей шмоток, я, пожалуй, пасс…."
    scene parkercityintro (12)
    with dissolve

    pa "Не-е-ет, я думала скорее научить тебя пару движениям из паркура."

    scene parkercityintro (14)
    with dissolve

    mc "Если ты забыла, в прошлый раз, когда мы занимались чем-то похожим на паркур, я чуть не свалился со здания."

    scene parkercityintro (15)
    with dissolve

    pa "Пфф. Все с тобой было нормально. А ну давай, я научу тебя делать сальто от стены."

    mc "Сальто от стены. В смысле, ты забегаешь на стену и делаешь сальто назад."
    scene parkercityintro (14)
    with dissolve
    pa "Агась."

    mc "..."

    mc "Я точно грохнусь на жопу."
    scene parkercityintro (13)
    with dissolve

    pa "Да ладно тебе, я покажу первой, чтобы ты понял, что делать."
    scene parkercityintro (15)
    with dissolve

    pa "Это просто. Смотри внимательно."


    scene parkercityintro (16)
    with dissolve
    "Паркер закрывает глаза и делает глубокий вдох."
    pause(1)
    scene parkercityintro (17)
    with dissolve
    "Она срывается с места со скоростью гепарда."
    pause(0.4)
    scene parkercityintro (18)
    with dissolve
    "Забегает на стену…"
    pause(0.4)
    scene parkercityintro (20)
    with dissolve
    pause(0.4)
    scene parkercityintro (19)
    with dissolve
    pause(0.4)
    scene parkercityintro (21)
    with hpunch

    "И крутит сальто назад, будто она профессиональный каскадер в боевике."

    scene parkercityintro (22)
    with dissolve

    pa "Видишь? Что я тебе говорила? Легко же, правда?"
    $ renpy.music.set_volume(0.01)
    play sound "audio/Sound/bop.mp3"
    scene parkercityintro (23)
    window hide dissolve
    pause 2.0 
    scene parkercityintro (24) with dissolve
    window hide dissolve
    pause 2.0 
    $ renpy.music.set_volume(1.)

    mc "Ну да, так что, пожалуй, я пасс."
    scene parkercityintro (25) with dissolve

    pa "Да ну тебе, я знаю, ты сможешь, [mcname]."

    mc "Ты сумасшедшая."
    scene parkercityintro (26) with dissolve

    pa "Ты просто струсил."

    mc "Потому что мне нравится, когда мои позвонки находятся в ровном положении? Абсолютно."

    pa "Ну дава-а-ай. Я тебя подстрахую."
    scene parkercityintro (27) with dissolve

    pa "Значит так: тебе нужно подбежать к ней на средней скорости — не спринтуй, если не хочешь влететь лицом в стену."

    pa "Подбегая к стене, толкнись толчковой ногой и поставь другую ногу на стену."


    pa "Затем ТОЛКНИСЬ от нее и отклони плечи назад, будто падаешь навзничь."
    scene parkercityintro (28) with dissolve

    mc "Я ненавижу каждое слово в этом предложении."
    scene parkercityintro (27) with dissolve

    pa "Ты используешь этот толчок, чтобы закрутиться. Так что, когда окажешься в воздухе, ГРУППИРУЙСЯ — подтяни колени к груди и доделай сальто."
    scene parkercityintro (29) with dissolve

    pa "Раскрывайся, когда увидишь землю, и приземляйся на обе ноги. *Не* приземляйся на прямые — согни колени, чтобы амортизировать удар."

    pa "И бум! Ты самый крутой чувак в этом переулке!"

    scene parkercityintro (30) with dissolve
    "Ты тяжело вздыхаешь. У Паркер это звучит настолько просто, что ты почти убеждаешь себя в том, что это реально."

    scene parkercityintro (31) with dissolve

    mc "...Ладно. К черту. Если я умру, я буду являться тебе в кошмарах."

    pa "Идет."

    scene parkercityintro (32)
    with dissolve
    pause(0.4)
    scene parkercityintro (33)
    with dissolve

    "Ты делаешь глубокий вдох, разгоняешься на стену, и на долю секунды… Тебе кажется, что у тебя получается."

    scene parkercityintro (34)
    with dissolve
    pause(0.4)
    "А потом ты вспоминаешь, что гравитация расписку не подписывала."
    play sound "audio/Sound/thud.mp3"
    scene black
    with hpunch

    "Ты грохаешься плашмя на жопу, как мешок с разочарованием."

    scene parkercityintro (35)
    with dissolve

    pa "Уф. 10/10 за старание, 2/10 за исполнение."

    mc "Ты соврала. Это было нифига не легко."

    scene parkercityintro (36)
    with dissolve

    pa "Ну да... На самом деле я просто хотела посмотреть, как ты шлепнешься на задницу."

    scene parkercityintro (35)
    with dissolve

    pa "Но эй, ты не умер! Так что... прогресс!"

    mc "Кажется, я отбил себе селезенку."


    scene parkercityintro (36)
    with dissolve

    pa "В следующий раз добавим винт!"

    mc "В следующий раз я принесу шлем."
    $ unlock_event(Parker, "Hardcore Parkour", "parkercityintro")
    if _in_replay:
        $ renpy.end_replay()
    else:
        $ parkercityintro += 1
        $ Parker.affection += 1

        $ Parker.quest = "На этом пока всё."
        play sound "audio/Sound/affection.mp3" volume 0.5

        "{i}Привязанность Паркер увеличена.{/i}"

        jump weekday_evening

label parkerhillevents:

transform fast_moveoutleft:
    linear 0.2 xalign -1.0


label mondaycity_eveningparker:
    play ambient "audio/ambient/City.mp3" volume 0.5
    scene city2 with fade
    "Ты срезаешь путь по переулку по дороге домой."

    scene black with fade
    "С крыши над тобой раздается знакомый голос, окликающий тебя."

play music "audio/Music/Parker.mp3" fadein 1.0
label parker_menu:
    scene ParkerWeekend with dissolve
    "Паркер приземляется рядом с тобой на корточки и выдает безумную ухмылку."
    call screen Parkeraction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump parker_menu

label city_eveninghangparker:
    pa "Спорим, ты не сможешь удержаться за мной вокруг квартала? Готов принять вызов?"
    "Ты колеблешься, но она уже трусит задом наперед, заманивая тебя."

    scene parkercityintro (37) with fade
    "Ты плетешься за ней по переулкам и перилам, сердце колотится, а ты изо всех сил пытаешься не упасть."

    pa "Ты не умер. Это победа. По крайней мере, для тебя."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Привязанность Паркер увеличена.{/i}"
    $ Parker.affection += 1
    jump weekday_evening

label city_eveningwaitparker:
    "Ты зависаешь на пожарной лестнице с Паркер, наблюдая за огнями внизу."
    jump weekday_evening
return