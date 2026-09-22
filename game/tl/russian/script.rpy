init 1 python:
    if persistent.language == "russian" or _preferences.language == "russian":
        persistent.pref_text_font = "Fonts/NotoSansDisplay-ExtraBold.ttf"

define gui.interface_text_outlines = [ (9, "#00000080", 2, 2) ]
define gui.dialogue_text_outlines = [ (9, "#000000ff", 2, 2) ]
define gui.name_text_outlines = [ (9, "#000000ff", 2, 2) ]

define config.developer = False

define b = Character("Бруклин", color="#8013f9")
define j = Character ("Джун", color="#8bb9d5")
define J = Character ("Джордин", color="#475bf5")
define n = Character ("Нора", color="#ff00f7")
define m = Character ("Мэй", color="#05ebb4")
define y = Character ("Юки", color="#2962bc")
define t = Character ("Тамара", color="#2a9362")
define K = Character ("Кайра", color="#00ff11")
define r_name = "{color=#FF0000}Рай{/color}{color=#0000FF}ли{/color}"
define r = DynamicCharacter("r_name", what_color="#FFFFFF", substitute=False)
define z = Character ("Зара", color="#eaf976")
define g = Character ("Грейс", color="#d1cd4a")
define u = Character("???", color="#808080")
define a = Character("Отэм", color="#6495ED")
define mc = Character("[mcname]", color="#FFFFFF")
define l = Character("Логан", color="#FF8300")
define pe = Character("Пьер", color="#740F35")
define pa = Character("Паркер", color="#FFFF00")
define q = Character("Куинн", color="#c0c596")
define L = Character("Лили", color="#FF69B4")
define I = Character("Изра", color="#EEE8AA")
define k = Character("Кицунэ", color="#FF4500")
define h = Character ("Харриет", color= "#7FF5C3")
define mi = Character ("Мина", color="#4fa08d")
define ye = Character ("Йеджин", color= "#000053")
define ut = Character ("Утами", color= "#89CFF0")


define H = Character ("Хинэ" , color = "#ca5836")
define M = Character ("Минни" , color = "#ca5836")
define B = Character ("Банни", color = "#9F2B9A")
define Shi = Character ("Шиори", color = "#7c548f")



define bro = Character ("Броги", color = "#61CF25")
define har = Character ("Хару", color = "#7FB3E3")



define c = Character ("Кабана", color="#ffcb3d")
define ca = Character ("Карли", color = "#8013f9")
define isa = Character ("Айзая", color = "#9F2B9A")
define ti = Character ("Тецуя", color = "#cdf570")
define ren = Character ("Ренджи", color = "#1c8d1c")


define guy1 = Character ("Хулиган", color = "#c5ac67")
define guy2 = Character ("Хулиган", color = "#f1413b")
define guy3 = Character ("Хулиган", color = "#dbc715")
define guy4 = Character ("Хулиган", color = "#ff87f5")
define ga = Character ("Девушка А", color = "#D1ECF4")
define gb = Character ("Девушка Б", color = "#9F2B9A")
define pg = Character ("Дедушка", color = "#1c8d1c")
define g1 = Character ("Софи", color = "#ca5836")
define g2 = Character ("Сидни", color = "#d6cd77")
define young_mc = Character ("Маленький [mcname]", color="#FFFFFF")
define girl_harassed = Character ("Девушка", color="#00992e")
define mcj = Character ("{color=#FFFFFF}[mcname]{/color} и {color=#8bb9d5}Джун{/color}")
define dol = Character ("Мистер Долдрам", color = "#003113")
define thg1 = Character ("Бандит 1", color = "#6d0303")
define tg2 = Character ("Бандит 2", color = "#2b00a1")
define tg3 = Character ("Бандит 3", color = "#002e19")
define G = Character ("Джианна", color = "#912900")
define rh = Character ("Рона", color = "#ac0000")
define ja = Character ("Янус", color = "#8a8272")
define po = Character ("Полиция", color = "#280a7c")




define host = Character ("Фудзинами", color = "#ac0000")
define dunkle = Character ("ДанклФанкл", color = "#2b00a1")
define chrmk = Character ("Охранник", color = "#FFFFFF")
define cthug = Character ("Участник Crbs", color ="#0BFF00")

define S = Character ("Сэми", color = "#9F2B9A")
define ser = Character ("Офицер", color = "#280a7c")



define s = Character ("Стример", color="#9F2B9A")


define centered = Character(None, what_xalign=0.5, window_xalign=0.5, window_yalign=0.4, what_text_align=0.5, window_background=None)


image movie_background = Movie(size = (3840,2160), channnel="movie", play="images/trippy.webm")
image Chapter_1 = Movie(size = (3840,2160), channnel="movie", play="images/Transitions/Learning-to-Love.ogv")
image Flowerscene1 = Movie(size = (3840,2160), channnel="movie", play="images/video/flowersscene1.mp4")
image Flowerscene2 = Movie(size = (3840,2160), channnel="movie", play="images/video/flowersscene2.mp4")
image Flowerscene3 = Movie(size = (3840,2160), channnel="movie", play="images/video/flowersscene3.mp4")


image Izra30date = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra30Event.webm")
image 20minutes = Movie(size = (3840,2160), channnel="movie", play="images/video/20minuteslater.webm")
image quest = Movie(size = (3840,2160), channnel="movie", play="images/video/quest.webm")


image Alleysex1 = Movie(size = (3840,2160), channnel="movie", play="images/video/alleysex1.mp4")
image Alleysex2 = Movie(size = (3840,2160), channnel="movie", play="images/video/alleysex2.mp4")
image Alleysex3 = Movie(size = (3840,2160), channnel="movie", play="images/video/alleysex3.webm")


image Izrasex1 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra/Izrasex1.webm")
image Izrasex2 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra/Izrasex2.webm")
image Izrasex3 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra/Izrasex3.webm")
image Izrasex4 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra/Izrasex4.webm")


image lilygoof1 = Movie(size = (3840,2160), channnel="movie", play="images/video/lilygoof/lilygoof1.webm")
image lilygoof2 = Movie(size = (3840,2160), channnel="movie", play="images/video/lilygoof/lilygoof2.webm")


image tvstatic = Movie(size = (3840,2160), channnel="movie", play="images/video/tvstatic.mp4")

image citysit = Movie(size = (3840,2160), channnel="movie", play="images/video/City.mp4")

image drink = Movie(size = (3840,2160), channnel="movie", play="images/video/drink.webm")

image eyes = Movie(size = (3840,2160), channnel="movie", play="images/video/eye6.webm")

image bunnyscissor1 = Movie(size = (3840,2160), channnel="movie", play="images/video/Bunny/bunnyscissor1.webm")
image bunnyscissor2 = Movie(size = (3840,2160), channnel="movie", play="images/video/Bunny/bunnyscissor2.webm")
image bunnyscissor3 = Movie(size = (3840,2160), channnel="movie", play="images/video/Bunny/bunnyscissor3.webm")

image grass1 = Movie(size = (3840,2160), channnel="movie", play="images/video/Grass6.mp4")
image grass2 = Movie(size = (3840,2160), channnel="movie", play="images/video/Grass5.mp4")
image question2 = Movie(size = (3840,2160), channnel="movie", play="images/video/question2.mp4")
image alone2 = Movie(size = (3840,2160), channnel="movie", play="images/video/alone2.mp4")

image Izrabj1 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_bj_1_pov.webm")
image Izrabj2 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_bj_1_3rd.webm")
image Izrabj3 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_bj_climax.webm")

image Izrahj1 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_hj_1_pov.webm")
image Izrahj2 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_hj_1_3rd.webm")
image Izrahj3 = Movie(size = (3840,2160), channnel="movie", play="images/video/Izra2/izra_hj_climax.webm")





image autumntv1 = Movie(size = (3840,2160), channnel="movie", play="images/video/autumn/fucksake.webm")
image autumntv2 = Movie(size = (3840,2160), channnel="movie", play="images/video/autumn/autumnmast3.webm")
image autumntv3 = Movie(size = (3840,2160), channnel="movie", play="images/video/autumn/autumnmast4.webm")
image autumntv4 = Movie(size = (3840,2160), channnel="movie", play="images/video/autumn/autumnmast5.webm")


image rileyroom1 = Movie(size = (3840,2160), channnel="movie", play="images/video/riley/rileymast5.webm")
image rileyroom2 = Movie(size = (3840,2160), channnel="movie", play="images/video/riley/rileymast3.webm")
image rileyroom3 = Movie(size = (3840,2160), channnel="movie", play="images/video/riley/rileymast4.webm")
image rileyroom4 = Movie(size = (3840,2160), channnel="movie", play="images/video/riley/rileymast6.webm")
image rileyroom5 = Movie(size = (3840,2160), channnel="movie", play="images/video/riley/rileymast7.webm")

image utamiboob = Movie(size = (3840,2160), channnel="movie", play="images/video/Utami/utamiboob.webm")

image junesex1 = Movie(size = (3840,2160), channnel="movie", play="images/video/june/junesex1.webm")
image junesex2 = Movie(size = (3840,2160), channnel="movie", play="images/video/june/junesex2.webm")
image junesex3 = Movie(size = (3840,2160), channnel="movie", play="images/video/june/junesex3.webm")

image AutumnWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Autumnweekend.webm")
image BrooklynWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Brooklynweekend.webm")
image GraceWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Graceweekend.webm")
image IzraWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Izraweekend.webm")
image JuneWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Juneweekend.webm")
image JordynWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Jordynweekend.webm")
image LilyWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Lilyweekend.webm")
image MeiWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Meiweekend.webm")
image NoraWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Noraweekend.webm")
image ParkerWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Parkerweekend.webm")
image RileyWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Rileyweekend.webm")
image TamaraWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Tamaraweekend.webm")
image UtamiWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Utamiweekend.webm")
image YejinWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Yejinweekend.webm")
image YukiWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Yukiweekend.webm")
image ZaraWeekend = Movie(size = (3840,2160), channnel="movie", play="images/Weekendgirls/Zaraweekend.webm")






define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define ahhflash = Fade(0.05, 0.0, 0.05, color="#fff")
define dissolve2 = Dissolve(2.0)
define dissolve3 = Dissolve(3.0)
define dissolve4 = Dissolve(4.0)
define dissolve5 = Dissolve(5.0)
define dissolve10 = Dissolve(10.0)
define dissolve15 = Dissolve(15.0)
define pixellatex = Pixellate(2.0)
define quickflash = Fade(0.05, 0.0, 0.05, color="#fff")
define sexfade = Fade(0.5, 0.0, 0.05, color="#fff")
define cumflash = Fade(0.2, 0.0, 0.2, color="#fff")
define quickdissolve = Dissolve(0.05)


define dissolvepat = Dissolve(0.5)
define quickerflash = Fade(0.05, 0.0, 0.005, color="#fff")

default option1 = False
default option2 = False
default option3 = False
default option4 = False
default option5 = False
default option6 = False
default option7 = False
default option8 = False
default option9 = False


default cerbergang = False
default kyragoon = False
default cerberhine = False


default intro_nora = 0
default intro_june = 0
default intro_brooklyn = 0
default intro_yuki = 0
default intro_mei = 0
default intro_jordyn = 0
default intro_2 = 0
default intro3 = 0
default intro_grace = 0
default intro_zara = 0
default intro_kyra = 0
default intro_parker = 0

default computer = 0

transform bigger:
    zoom 1.5






init:
    $ renpy.music.register_channel("ambient","sfx",True,tight=True)

    $ left = Position(xpos= 0.25, xanchor='left')
    $ right = Position(xpos= 0.75, xanchor='right')
    $ preferences.transitions = 2

    $ day = 0
    $ totaldays = 0
    $ dorm = 0




    $ affection_cabana = 0

    $ damian = 0


    $ izraballetintro = 0
    $ izraskateintro = 0
    $ izra5event = 0
    $ izra10event = 0
    $ izra15event = 0
    $ izra20event = 0
    $ izra25event = 0
    $ izrainbetweenevent = 0
    $ izra30event = 0
    $ izraclimaxevent = 0
    $ izrabj = 0


    $ autumntvintro = 0
    $ autumnskateintro = 0
    $ autumnmovie = 0



    $ gracemallintro = 0
    $ graceinvest = 0
    $ graceinterrogate = 0


    $ tamarabarintro = 0
    $ tamaradrinkoff = 0
    $ Cabana_respect = 0
    $ kiss_event = 0
    $ tamara_liquor_walk = 0



    $ rileyarcadeintro = 0
    $ rileylibraryintro = 0
    $ rileyroom = 0
    $ rileyconfront = 0
    $ rileyroom2 = 0



    $ brooklynhallintro = 0
    $ brooklyncafeintro = 0
    $ brooklyntalent1 = 0
    $ brooklyntalent2 = 0
    $ brooklyntalent_signup = 0


    $ lilyzoointro = 0
    $ lilyroofintro = 0
    $ lilyflowerroof = 0
    $ lilyzooshed = 0

    $ zaraskateintro = 0
    $ zaraskateeventone = 0


    $ noragymintro = 0
    $ noramallintro = 0
    $ nora5event = 0



    $ jordyntrackintro = 0
    $ jordynparkintro = 0
    $ jordyndogevent = 0


    $ parkercityintro = 0

    $ utamihairintro = 0
    $ utamisurf = 0
    $ utamibeachbj = 0


    $ yejinclassintro = 0
    $ yejindojointro = 0
    $ yejinbully = 0
    $ yejinblackmail = 0
    $ yejinpatrol = 0

    $ yukilibraryintro = 0
    $ yukiconintro = 0
    $ yuki5event = 0
    $ yuki10event = 0
    $ yukibook2event = 0
    $ yukikitsunebook = 0
    $ yukiladder = 0


    $ meipaintintro = 0
    $ meihillintro = 0
    $ meievent5prelude = 0
    $ mei5event = 0
    $ meisketch = 0



    $ junesmokeintro = 0
    $ junealleyintro = 0
    $ june5event = 0
    $ june10event = 0
    $ june15event1 = 0
    $ junelilyzoo = 0
    $ june15event2 = 0
    $ junehallway1 = 0
    $ juneskatepark = 0
    $ junetalkto = 0
    $ junebrotherintro = 0
    $ junehelp = 0
    $ junepanick = 0
    $ junepolice = 0


    $ kyraalleyevent = 0
    $ kyra_recruitment = 0
    $ kyragangevent = 0



    $ pushupintro = 0
    $ firstfight = 0
    $ firstdream = 0
    $ storydream1 = 0
    $ storydream2 = 0
    $ yejin_train = 0
    $ pillowtrain = 0
    $ chromarkwarehouse = 0

    $ intro_utami = 0
    $ intro_yejin = 0
    $ intro_nora = 0
    $ intro_june = 0
    $ intro_brooklyn = 0
    $ intro_yuki = 0
    $ intro_mei = 0
    $ intro_jordyn = 0
    $ intro_2 = 0
    $ intro3 = 0
    $ intro_grace = 0
    $ intro_zara = 0
    $ intro_kyra = 0
    $ intro_parker = 0


    $ riley_favor_owed = 0

image splash = "splash.jpg"

label splashscreen:
    play sound "splash.mp3"
    $ renpy.movie_cutscene('splash.mp4')
    stop sound
    pause 1.0
    show splash with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0

    return


label start:

    stop music




    scene intro 0






    $ renpy.pause(2, hard=True)





label intro:
    $ persistent.patreon_unlocked = True
    scene intro 0
    with fade
    $ renpy.pause(2, hard=True)
    pause 2.0

    if persistent.damian_triggered:
        jump stoplooking
    else:
        jump starting

label starting:
    $ main.quest = "Продвинуться по сюжету."

    play music "audio/Music/Calm_Music.mp3" volume 1.0
    centered "{size=160}{cps=10}Привет{/cps}"
    centered "{size=160}{cps=10}Как ты?{/cps}"
    centered "{size=160}{cps=10}Странный вопрос, я знаю, но мне любопытно.{/cps}"
    centered "{size=160}{cps=10}Прямо сейчас, в этот момент — что ты чувствуешь?{/cps}"
    centered "{size=160}{cps=10}Как прошёл твой день? Надеюсь, ты не слишком себя загонял.{/cps}"
    centered "{size=160}{cps=10}Я надеюсь, у тебя всё хорошо. Надеюсь, тебе спокойно.{/cps}"
    centered "{size=160}{cps=10}Честно говоря, я не могу знать наверняка.{/cps}"
    centered "{size=160}{cps=10}Я мог бы дать тебе выбор ответить «да» или «нет», но не думаю, что это действительно нужно.{/cps}"
    centered "{size=160}{cps=10}Скорее, мне не так уж это и важно.{/cps}"
    centered "{size=160}{cps=10}И у меня есть чувство, что тебе тоже не так уж важно.{/cps}"
    centered "{size=160}{cps=10}Не удивлюсь, если ты сейчас просто проматываешь этот текст.{/cps}"
    centered "{size=160}{cps=10}Пытаешься побыстрее добраться до самой истории, до желанных моментов.{/cps}"
    centered "{size=160}{cps=10}Куда спешить? Игра никуда не денется."
    centered "{size=160}{cps=10}Если идти по жизни, вцепившись в одну цель...{/cps}"
    centered "{size=160}{cps=10}Ты упустишь всю красоту, что приходит с неспешным путём.{/cps}"
    centered "{size=160}{cps=10}Людей, которых ты встретил, места, где ты побывал, воспоминания, которыми дорожишь.{/cps}"
    centered "{size=160}{cps=10}Представь, если бы всё это ничего не значило для тебя только потому, что ты был слишком сосредоточен на том, что впереди, а не на том, что здесь и сейчас.{/cps}"
    centered "{size=160}{cps=10}И посмотри, где ты теперь!{/cps}"
    centered "{size=160}{cps=10}Смотришь на чёрный экран порно-игры в одиночестве, пока кто-то отчитывает тебя за нетерпеливость.{/cps}"
    centered "{size=160}{cps=10}Я так тобой горжусь.{/cps}"
    centered "{size=160}{cps=10}….{/cps}"
    centered "{size=160}{cps=10}…..{/cps}"
    centered "{size=160}{cps=10}Кстати, я серьёзно.{/cps}"
    centered "{size=160}{cps=10}Я горжусь тобой.{/cps}"
    centered "{size=160}{cps=10}Даже если мы никогда не встречались.{/cps}"
    centered "{size=160}{cps=10} Даже если мы на разных концах света."
    centered "{size=160}{cps=10} Даже если я не знаю ни твоего имени, ни возраста, ни пола, ни того, через что ты проходишь.{/cps}"
    centered "{size=160}{cps=10}Я горжусь тобой.{/cps}"
    centered "{size=160}{cps=10}Тебе не обязательно мне верить, может, тебе кажется, что это невозможно.{/cps}"
    centered "{size=160}{cps=10}Может, ты сам собой не гордишься.{/cps}"
    centered "{size=160}{cps=10}Может, другие тобой не гордятся.{/cps}"
    centered "{size=160}{cps=10}Но я горжусь.{/cps}"
    centered "{size=160}{cps=10}Надеюсь, тебе стало немного легче, если было не по себе.{/cps}"
    centered "{size=160}{cps=10}А если нет — тоже ничего страшного…..{/cps}"
    centered "{size=160}{cps=10}Ладно, кажется, я и так задержал тебя надолго.{/cps}"
    centered "{size=160}{cps=10}Пора начинать твою историю.{/cps}"
    window hide 
    scene movie_background with fade
    centered "{size=160}{cps=10}Чтобы ты мог стать тем, кем хочешь быть.{/cps}"
    centered "{size=160}{cps=10}Чтобы ты мог испытать то, что хочешь испытать.{/cps}"
    centered "{size=160}{cps=10}Чтобы ты мог гордиться тем, кем станешь.{/cps}"
    centered "{size=160}{cps=10}Это ты.{/cps}"
    centered "{size=160}{cps=10}Поздравляю.{/cps}"
    centered "{size=160}{cps=10}Но кто ты без имени?{/cps}"
    centered "{size=160}{cps=10}Говорят, знание чьего-то имени даёт над ним власть.{/cps}"
    centered "{size=160}{cps=10}Но что, если даже ты сам не знаешь своего?{/cps}"
    centered "{size=160}{cps=10}Тебе дана полная свобода решить это самому.{/cps}"
    centered "{size=160}{cps=10}Немногим выпадает такая привилегия.{/cps}"
    centered "{size=160}{cps=10}Но тебе я подарю это удовольствие.{/cps}"
    centered "{size=160}{cps=10}Так скажи мне.{/cps}"
    centered "{size=160}{cps=10}Как тебя зовут?{/cps}"
    stop music
    play sound "audio/Sound/Glitch1.wav" volume 1.0
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy8 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy9 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy7 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy6 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy8 with quickdissolve
    $ renpy.pause(0.01, hard=True)
    scene scawy9 with quickdissolve
    scene intro 0 with quickdissolve
    pause 1.0


    $ mcname = renpy.input ("Придумай себе имя. (оставь пустым для Маилз.)", length =32)
    $ mcname = mcname.strip()
    if mcname.lower() == "damian":
        $ persistent.damian_triggered = True
        centered "{size=160}{cps=10} Не стоило выбирать это имя..."
        $ renpy.quit()
    if mcname == "":
        $ mcname = "Маилз"
    centered "{size=160}{cps=10}А, значит тебя зовут [mcname]."
    centered "{size=160}{cps=10}Это действительно прекрасное имя.{/cps}"
    centered "{size=160}{cps=10}Да... Правда прекрасное.{/cps}"
    centered "{size=160}{cps=10}Желаю тебе всего наилучшего в этой истории, [mcname].{/cps}"
    centered "{size=160}{cps=10}Теперь я отпущу тебя.{/cps}"
    centered "{size=160}{cps=10}Но прежде чем уйти.{/cps}"
    centered "{size=160}{cps=10}У меня есть ещё один вопрос к тебе, [mcname].{/cps}"
    centered "{size=160}{cps=10}Это займёт всего мгновение.{/cps}"
    centered "{size=160}{cps=10}Но мне любопытно.{/cps}"

    stop music
    centered "{size=160}{cps=10} Приходилось ли тебе в жизни переживать травму?{/cps}"

    menu trauma:
        "Да":




            centered "{size=160}{cps=10}Понятно.{/cps}"
            centered "{size=160}{cps=10}Мне жаль это слышать.{/cps}"
            centered "{size=160}{cps=10}Как ты справился с этой травмой? Как переживал горе?{/cps}"
            centered "{size=160}{cps=10}Тебе становится грустно, когда думаешь об этом? Или злишься?{/cps}"
            centered "{size=160}{cps=10}Может, кажется, что можно было это предотвратить.{/cps}"
            centered "{size=160}{cps=10}хмм{/cps}"
            centered "{size=160}{cps=10}Меня завораживает, как по-разному мы все переживаем горе.{/cps}"
            centered "{size=160}{cps=10}Ни у кого нет одинакового опыта.{/cps}"
            centered "{size=160}{cps=10}Никто не сталкивается с теми же трудностями.{/cps}"
            centered "{size=160}{cps=10}Никто не горюет одинаково.{/cps}"
            centered "{size=160}{cps=10}Как думаешь, как бы ты отреагировал, если бы в один день потерял всё?{/cps}"
            centered "{size=160}{cps=10}Как бы ты переживал это?{/cps}"
            centered "{size=160}{cps=10}Может, ты уже потерял.{/cps}"
            centered "{size=160}{cps=10}Может, поэтому ты здесь….{/cps}"
            centered "{size=160}{cps=10}Извини, я разболтался.{/cps}"
            centered "{size=160}{cps=10}Наверное, я просто немного устал.{/cps}"
            centered "{size=160}{cps=10}Надеюсь, тебе понравится твой опыт здесь.{/cps}"
            $ renpy.pause(3, hard=True)
            play sound "audio/Sound/static.mp3" volume 0.75
            scene black with quickflash
            stop sound
            scene intro 0 with fade
            scene intro 13 with fade
            pause 2.0
            scene intro 0 with fade
            $ renpy.pause(1, hard=True)
            window hide
            pause 1.0
            call screen start_choice
            jump actualintro
        "Нет":



            centered "{size=160}{cps=10}Правда?{/cps}"
            centered "{size=160}{cps=10}Что ж, это хорошо.{/cps}"
            centered "{size=160}{cps=10}Хмммм...{/cps}"
            centered "{size=160}{cps=10}Да... Полагаю, это действительно хорошо.{/cps}"
            centered "{size=160}{cps=10}Я даже немного тебе завидую.{/cps}"
            centered "{size=160}{cps=10}Потому что ты такой...{/cps}"
            centered "{size=160}{cps=10}Такой...{/cps}"
            play sound "audio/Sound/static.mp3" volume 0.75
            scene lucky with quickflash
            stop sound
            play music "audio/Music/lucky1.mp3" volume 1
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            play sound "audio/Sound/static.mp3" volume 1
            scene lucky2 with quickflash
            stop sound
            play music "audio/Music/lucky2.mp3" volume 1
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            play sound "audio/Sound/static.mp3" volume 1
            scene lucky3 with quickflash
            stop sound
            play music "audio/Music/lucky4.mp3" volume 1
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            centered "{size=160}{cps=10}ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИКВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК ВЕЗУНЧИК{/cps}"
            play sound "audio/Sound/static.mp3" volume 1
            scene lucky4 with quickflash
            stop sound
            play music "audio/Music/lucky3.mp3" volume 1
            $ renpy.pause(2, hard=True)
            play sound "audio/Sound/static.mp3" volume 0.75
            stop music
label intromonologue:
    play sound "audio/Sound/static.mp3" volume 0.75
    scene black with quickflash
    scene black with quickflash
    stop sound
    play sound "audio/Sound/scarykitsune.mp3" volume 0.4
    show scarykit with quickdissolve
    "{cps=*100}Жкхкинцб рнце фуй цчехас йхкзус,Ьбн иреме, пеп ширн уцктбг, иухдч—Чеп нмдюкт, чеп фхузухкт, скъ чеп ьнцч,{w=0.1}{nw}{/cps}"
    "{cps=*100}Йнчд пузехцчзе н ънчхуцчн, тк йужхе.Ча шзнйнэб рефа киу, цчурб еппшхечтак,Четышгюнк чнъу фу ужсетш.{w=0.1}{nw}{/cps}"
    "{cps=*100}Ут цпрутнч иурузш н уцпернч шъсарпш—Ту тк фшцпео ршпезуиу зтшчхб.Зкйб рнца иузухдч жехъечтас чутус,{w=0.1}{nw}{/cps}"
    "{cps=*100}Фуршфхезйа н рлн, уччуькттуо йу жркцпе.Утн уьехшгч чкжд жеопуо-йхшиуо,Е фуцрк цпхугчцд ц чзунс пуэкрбпус н жеэсепус.{w=0.1}{nw}{/cps}"
    "{cps=*100}Хеццпелшч жеопн у ркцтаъ ыехдъ, У йхкзтнъ пухутеъ н эёфучк чеот,Хеццпелшч фху цуз, фхуйезэнъ цзун сацрн,{w=0.1}{nw}{/cps}"
    "{cps=*100}У цйкрпеъ, мепргьёттаъ цхкйб мефшчеттаъ чхуф.«У, нйёс», — цпелкч ут, — «рнэб ме фурдтш—Чес кцчб зурэкжцчзу, ийк скхпткч ршттао цзкч.{w=0.1}{nw}{/cps}"
    "{cps=*100}Ту тк нйн фу рнцбксш цркйш,Ут зкйёч п хшнтес, итнрн н цчктетндс.Зкйб цчунч фкхкцкьб чктнцчао узхеи,{w=0.1}{nw}{/cps}"
    "{cps=*100}Ийк рнца тефхезрдгч эеин ргйко,Ча теойёэб цзуё нсд, цзуо хемшс—Зкйб рнца чухишгч ткуфхкйкрёттуцчбг.{w=0.1}{nw}{/cps}"
    "{cps=*100}Ут шражтёчцд н цпелкч: «Вчу зцё эшчпе!»,Пхейд чкс зхкскткс чеота нм ихшйн чзуко.Н чурбпу теьтёэб ча футнсечб,{w=0.1}{nw}{/cps}"
    "{cps=*100}Пеп ут шлк з йкцдчн эеиеъ, тецскэрнзу цзужуйкт.Утн фнхшгч йузкхнкс, фбгч цустктнкс,Зазухеьнзегч фхезйш, ьчу ча ъхетнр.{w=0.1}{nw}{/cps}"
    "{cps=*100}Рнц, фшцчб н пхецнз, тнпуийе тк йхши—Ут чпёч теьере, ьчу путьегчцд путыус.Чеп тк йузкхдо рнцш ц иремесн фресктн,{w=0.1}{nw}{/cps}"
    "{cps=*100}Тн прапецчуо чзехн з ужёхчпк нсктн.Нъ снх — тепрутёт, нъ црузу — шрузпе—Нъ фхезйе — жусже ц ьецузас скъетнмсус.{w=0.1}{nw}{/cps}"
    play sound "audio/Sound/scarykitsune2.mp3" volume 0.4
    "{cps=*100}Н кцрн ча шзнйнэб киу те фурдтк,Фуйснитёч н цпхукчцд з чктн—Фхуцчу учзкхтнцб. Фхнчзухнцб цркфас.{w=0.1}{nw}{/cps}"
    "{cps=*100}Рнц тнпуийе тк йеркпу фумейн.{w=0.01}{nw}{/cps}"

    hide scarykit
    show scarykit2 with quickdissolve
    hide scarykit2
    show scarykit3 with quickdissolve
    hide scarykit3
    show scarykit4 with quickdissolve
    hide scarykit4
    show scarykit5 with quickdissolve
    hide scarykit5
    show scarykit6 with quickdissolve
    $ renpy.pause(3, hard=True)
    play sound "audio/Sound/static.mp3" volume 0.75
    scene black with quickflash
    stop sound
    scene intro 0 with fade
    scene intro 13 with fade
    pause 2.0
    scene intro 0 with fade
    $ renpy.pause(1, hard=True)
    window hide
    pause 1.0
    call screen start_choice
label actualintro:
    scene intro 0 with fade
    $ renpy.pause(1, hard=True)
    window hide
    pause 1.0

    play music "audio/Music/Ambient.mp3" volume 1.0

    mc "Что бы ты назвал идеальной жизнью?"
    mc "Не думаю, что многие назвали бы мою жизнь идеальной."
    mc "Моя семья жила достаточно комфортно, мы почти ни в чём не нуждались."
    mc "Не сказать, что жизнь была идеальной, но, помнится, она была счастливой."
    mc "Насколько я помню, я был счастлив."
    mc "Хотя, если подумать, я мало что помню из детства."
    mc "Я почти не помню родителей, да и сестру тоже."

    scene intro 2
    with fade

    mc "Я не помню, чтобы считал маму самым добрым человеком на свете."
    mc "Но помню, что она всегда следила, чтобы у нас с сестрой было всё необходимое, и ставила нас на первое место."
    mc "Матери такие, что уж тут скажешь."
    mc "Если твоя мама всё ещё рядом, обязательно позвони ей как-нибудь и напомни, как много она для тебя значит."
    mc "Помню, ей это очень нравилось."
    mc "Я почти не помню её лица, но её улыбку я забыть не смог бы никогда."

    scene intro 3
    with fade

    mc "Мы с сестрой были близки, когда у неё случались проблемы, она всегда шла сначала ко мне."
    mc "А когда проблемы случались у меня, она узнавала первой."
    mc "Хоть она и была отчаянной, но именно мне всегда приходилось нас вытаскивать, когда она что-то натворит."
    mc "Хотя я и не жаловался — для этого и нужны старшие братья."
    mc "По крайней мере, я так думаю..."

    scene intro 4
    with fade

    mc "Мой отец..."
    mc "..."
    mc "Я......"
    mc "Он......"

    scene intro 1
    with fade

    mc "Впрочем, это уже не важно."

    scene intro 5


    mc "Теперь их всех нет."
    mc "Мертвы или пропали — точно не знаю."
    mc "Я даже не помню, как это случилось."
    mc "Однажды я просто проснулся в приюте, растерянный и плачущий..."
    mc "Проснулся, ага...."
    mc "......Я не.....{w}произносил этих слов....{w}уже очень давно...."
    mc "......."
    mc "......."
    mc "Воспитательница сказала, что меня нашли у порога — видимо, кто-то меня туда подкинул."

    scene intro 6 with fade

    mc "Меня бросили одного в 9 лет."
    mc "4 года я провёл в этом приюте."
    mc "Я даже не пытался сблизиться с воспитателями или другими детьми."
    mc "Слишком боялся снова кого-то потерять."
    mc "Слишком боялся, что однажды проснусь и снова буду один."
    mc ".....{w}Проснусь.....{w}хмм....."
    mc "........"
    scene intro 7 with fade

    mc "В конце концов, каким-то чудом меня удочерила... усыновила одинокая женщина."
    mc "Зачем ей понадобилось взваливать на себя стресс ещё одного ребёнка — этого не понять никому."
    mc "Особенно такого, как я."
    mc "Но я был благодарен."
    mc "Невероятно благодарен."

    scene intro 8 with fade

    mc "Но с тех пор, как я потерял свою настоящую семью."
    mc "Со мной что-то не так."
    mc "Что-то, о чём я никому не рассказывал."
    mc "Что-то.......что меня пугает."
    mc "К...{w}ошмар....{w}от которого я не могу.....{w}проснуться....{w}"
    mc "Проснись...Проснись..."
    mc "Я не могу.....{w}проснуться...{w}"
    mc "Я....{w}не могу проснуться...{w}потому что....{w}я не...{w}спал...."
    mc "Я...{w}не...{w}спал..."
    mc "Я......{w}не......{w}спал..."
    stop music
    play sound "audio/Sound/static.mp3" volume 0.75
    scene intro 10 with quickdissolve
    scene intro 11 with quickdissolve
    scene intro 12 with quickdissolve
    scene intro 10 with quickdissolve
    scene intro 11 with quickdissolve
    scene intro 12 with quickdissolve
    scene intro 10 with quickdissolve
    scene intro 11 with quickdissolve
    scene intro 12 with quickdissolve

    scene intro 9 with quickdissolve
    play sound "audio/Sound/Whisper.wav" volume 0.75


    window hide dissolve
    pause 2

    $ renpy.pause(4, hard=True)

    scene black with fade
    $ renpy.pause(2, hard=True)
    stop sound

    label scene_1:


        window hide dissolve
        pause 1.0


        play music "audio/Music/Nights.mp3" volume 1.0 fadein 1

        mc "В последнее время я сам на себя не похож."

        mc "Когда наступает день, мне ничего не хочется делать, а когда он заканчивается…"

        mc "Обычно я так ничего и не сделал, просто зря потратил время."

        mc "Не сказать, что у меня есть какие-то цели или амбиции, но даже если бы были..."

        mc "Не думаю, что смог бы заставить себя хоть одну из них воплотить."

        scene 1scene with fade

        mc "(Прошло уже десять лет с тех пор.)"
        mc "(Десять лет с тех пор, как я потерял семью.)"
        mc "(Десять лет с тех пор, как я потерял способность спать.)"
        mc "(Теперь мне 19 лет.)"

        scene 1scene (1) with dissolve

        mc "(Мы с приёмной сестрой только что переехали в собственную квартиру, подальше от мамы, на наш последний учебный год.)"
        mc "(Наверное, я должен от этого чувствовать воодушевление, да? Новый старт, своё собственное место. Но ощущается всё совсем не так.)"
        mc "(Ощущается просто как ещё одно пространство, в котором можно чахнуть впустую.)"
        scene 1scene (6) with dissolve

        mc "(Несмотря на то, что мне повезло получить второй шанс с новой семьёй, у меня так и не вышло по-настоящему сблизиться с людьми.)"
        mc "(По крайней мере, не по-настоящему. Люди считают меня отстранённым. Может, они и правы.)"

        scene 1scene (2) with dissolve

        mc "(У меня есть пара друзей, но не сказать, что я сам ищу их компании.)"
        mc "(Они скорее... знакомые, которых я терплю.)"
        scene 1scene (3) with dissolve
        mc "(Наверное, мне никогда не хотелось расспрашивать их о жизни или увлечениях. Проще держать их на расстоянии.)"
        mc "(И не дай бог им узнать что-то обо мне.)"

        scene 1scene (4) with dissolve
        mc "(Я не силён в спорте, не особо умный, и уж точно не тусовщик."
        mc "(Для них я, наверное, просто какой-то мрачный саркастичный придурок, который так и не вырос из своей готической фазы.)"

        scene 1scene (5) with dissolve
        mc "(И может, так даже лучше. Проще играть роль, которую они мне уже назначили, чем пытаться объяснить правду.)"
        mc "(Люди любят простые истории. Им не нужна сложность. Они не хотят знать, что на самом деле творится у тебя в голове.)"
        scene 1scene (7) with dissolve
        mc "(В этом году мы выпускаемся, так что налаживать связи, наверное, всё равно уже поздно.)"
        mc "(Да и не то чтобы я смог бы, даже если бы захотел.)"
        mc "(Чёрт, я даже из этой комнаты выходить не хочу, не то что идти в школу.)"

        scene 1scene (8) with dissolve

        mc "(С того самого дня... дня, когда я проснулся в последний раз... того дня, когда я очнулся в приюте 10 лет назад, я никогда по-настоящему ни с кем не был близок.)"
        mc "(Помню, как лежал на том холодном, жёстком матрасе, глядя в потолок, гадая, как я вообще там оказался.)"
        scene 1scene (9) with dissolve
        mc "(Воспоминания о семье были размытыми — как сон, от которого только что очнулся и никак не можешь собрать по кусочкам.)"

        mc "(Мне было всего девять, но я уже понимал достаточно, чтобы осознать: я один.)"
        scene 1scene (10) with dissolve
        mc "(И вот теперь я здесь, но никогда ещё не был так одинок.)"
        scene 1scene (11) with dissolve
        mc "(Забавно, впрочем. Разве не странно осознавать, сколько версий тебя существует в головах других людей?)"
        mc "(Кто-то может видеть в тебе замкнутого человека, который почти не говорит, а кто-то — того, кто не умолкает ни на секунду.)"
        scene 1scene (12) with dissolve
        mc "(Кто-то может считать тебя добрым и заботливым, а кто-то — холодным и отстранённым. А кто-то — вовсе робким.)"
        mc "(Правда в том, что тот «ты», которого воспринимают люди — иллюзия, сконструированная из воспитания, влияния окружения, страха, жадности и других эгоистичных факторов.)"
        scene 1scene (14) with dissolve
        mc "(Настоящий ты существует за пределами всех этих восприятий, просто наблюдая.)"
        mc "(Это истинное «я» неотделимо от всех остальных, потому что никакой изначальной отделённости не существует.)"
        scene 1scene (12) with dissolve
        mc "(Мы все взаимосвязаны, как листья одного дерева.)"
        mc "(Ирония в том, что не найти одного и того же человека дважды, даже в одном и том же человеке.)"
        mc "(Но даже зная это, я всё равно не могу вырваться из стен, которые сам вокруг себя выстроил.)"
        scene 1scene (15) with dissolve
        mc "(Страх отвержения, страх быть непонятым — вот что держит меня взаперти.)"
        mc "(И может, это нормально. Может, так безопаснее.)"
        mc "(Потому что каждый раз, впуская кого-то, я в итоге получал только боль.)"

        scene 1scene (16) with dissolve

        mc "(Не понимаю, почему все вокруг такие осуждающие.)"
        mc "(Я понимаю, почему Отэм такая. Наверное, потому что ей не всё равно... отчасти.)"
        mc "(А отчасти, наверное, ещё и потому, что все остальные смотрят на неё так, мол: «Эй, а твой брат просто бездельник».)"
        mc "(«[mcname] такой», «[mcname] сякой».)"
        mc "Что ж, [mcname] — это я. Почему бы тебе не принять, каким я хочу быть."

        play sound "audio/Sound/dooropen.wav" volume 0.75

        scene 1scene (17) with dissolve
        window hide dissolve
        pause 2
        scene 1scene (20) with dissolve
        a "Так, всё, хватит. Я не дам тебе сидеть в этом подземелье и разводить философскую хрень ещё хоть секунду."
        mc "(Прежде чем я успеваю уйти в мысли ещё глубже, дверь распахивается настежь. Без стука. Без предупреждения. Как всегда, Отэм.)"
        scene 1scene (18) with dissolve
        mc "(Поначалу я ей не доверял. С чего бы? Все, кто был мне дорог, исчезли. Почему с ней должно быть иначе?)"
        mc "(Но она не сдалась на мне, даже когда я давал ей все поводы это сделать.)"
        mc "Отэм, я не в настроении. Просто... оставь меня в покое, ладно?"

        scene 1scene (21) with dissolve
        a "Ну уж нет. Этому не бывать. Ты вообще себя слышишь? Ты не выходил отсюда с тех пор, как мы приехали, [mcname]."

        mc "(Ух. У меня нет сил на это.)"
        scene 1scene (25) with dissolve
        mc "И к чему ты клонишь? Со мной всё нормально."

        a "Нет, не нормально. И ты сам это знаешь."
        scene 1scene (24) with dissolve
        "Её голос режет тебя острее, чем ты ожидал. Хотя она даже не кричит."
        "Она даже не злится. Она просто... устала. И почему-то от этого только хуже."
        scene 1scene (29) with dissolve
        a "Думаешь, я не замечаю? То, как ты почти не ешь? То, как ты ни с кем не разговариваешь — даже со мной?"

        "Ты молчишь. Хочешь, чтобы она перестала говорить, но сил заставить её уйти тоже нет."

        a "Слушай, я понимаю. Тебе пришлось пройти через... многое. Больше, чем должен переживать любой человек."
        scene 1scene (27) with dissolve
        mc "Слушай, Отэм, просто... хватит, ладно."

        a "Нет, я не остановлюсь."
        a "Вот так закрываться от всех? Это тебе не помогает. Это никому не помогает."
        scene 1scene (26) with dissolve
        mc "И что, по-твоему, я должен с этим делать, а?"
        mc "Притворяться кем-то другим? Натянуть улыбку и стать тем, кого ты себе придумала?"
        mc "Потому что я не такой, Отэм. И если ты ждёшь именно этого, тебе лучше просто оставить меня в покое."
        scene 1scene (33) with dissolve
        a "Нет! Я не прошу тебя притворяться. Я прошу тебя попробовать. Сходи в школу. Хотя бы один день. Это всё, о чём я прошу."
        scene 1scene (34) with dissolve
        mc "(Я смотрю на неё, и впервые она не смотрит на меня тем обычным взглядом «командирши-старшей-сестры», который всегда выглядел на ней нелепо.)"
        mc "(Она просто выглядит... взволнованной.)"
        mc "Почему тебе вообще так не всё равно?"
        scene 1scene (35) with dissolve
        a "Потому что ты моя семья, идиот. И мне невыносимо видеть тебя таким. Мне невыносимо чувствовать, что я тебя теряю."
        "Её голос срывается в конце, и мне приходится отвести взгляд."
        mc "(Я не могу выдержать то, как она сейчас на меня смотрит.)"
        mc "Ты меня не теряешь, Отэм. Я просто... застрял."
        a "Тогда дай мне помочь. Пожалуйста. Сходи завтра в школу. Один день. Просто посмотрим, что будет."
        scene 1scene (36) with dissolve
        mc " (Часть меня хочет сказать «нет». Велеть ей выйти и оставить меня одного.)"
        mc "(Но другая часть меня... та, что помнит, как сильно она старалась, как она всегда была рядом... та часть не может сказать «нет».)"
        scene 1scene (37) with dissolve
        mc "Ладно, твоя взяла. Завтра. Я пойду в школу."
        scene 1scene (38) with dissolve
        a "Спасибо. Это всё, чего я хотела."

        "Ты закатываешь глаза, но не можешь сдержать едва заметную улыбку."

        a "Так, а теперь ложись, тебе нужно отдохнуть перед завтрашним важным днём."
        scene 1scene (39) with dissolve

        mc "Погоди, ты что, здесь спишь?"

        a "Ну да, мне надо убедиться, что ты уснёшь."

        mc "(Много ей от этого будет пользы...)"

        mc "Уф, ладно, подвинься."

        scene 1scene (40) with dissolve

        a "Ого, мы так не делали с самого детства!"

        a "Помнишь, как я пробиралась к тебе в комнату, когда не могла уснуть?"

        mc "Как я мог забыть? Ты была такой плаксой."

        a "Пффф, можно подумать, мистер «Чёрный парад» тут не такой же."
        scene 1scene (43) with dissolve

        "Вы лежите в тишине какое-то время, тяжесть комнаты давит на тебя."
        mc "Не то чтобы я хотел признавать твою правоту насчёт «Чёрного парада», но ты никогда не задумывалась, насколько всё это... бессмысленно?"
        mc "Как будто что ни делай, ничего по-настоящему не меняется?"
        scene 1scene (42) with dissolve
        a "Иногда. Но, думаю, это просто часть того, каково быть человеком, братишка. Весь фокус в том, чтобы найти то, ради чего стоит стараться."
        a "Ну знаешь, всякое такое — семья, друзья, повторы «Своей игры»."
        mc "(Я горько усмехаюсь, качая головой.)"
        mc "Ага? Ну, ты — единственная семья, что у меня есть. А с друзьями у меня как-то не очень."
        scene 1scene (42) with dissolve
        mc "А если у тебя ничего такого нет? Если всё, что у тебя есть — это ты сам?"

        a "Тогда ты позволяешь кому-то помочь тебе это найти. Вот зачем я здесь, знаешь ли. Я не дам тебе проходить через это в одиночку."

        mc "Ты говоришь так, будто это легко."

        a "Это не легко. Но оно того стоит. Как и ты."
        scene 1scene (43) with dissolve
        mc "Наверное, просто сейчас я чувствую себя потерянным."

        mc "Я сам себя не понимаю."
        scene 1scene (44) with dissolve

        "Я хочу поступать правильно. Но не поступаю."
        scene 1scene (49) with dissolve

        mc "Вместо этого я делаю то, что ненавижу."
        scene 1scene (50) with dissolve
        mc "Наверное, я просто был ленивым. И, чёрт возьми, может, я и есть такой."
        mc "Но может быть... может, я просто устал притворяться, будто меня всё устраивает."
        scene 1scene (51) with dissolve
        mc "У всех остальных, кажется, есть причина вставать по утрам. У меня даже нет причины ложиться спать."
        mc "Я даже не хочу, чтобы меня спасали. Я хочу найти причину, ради которой стоило бы спасать себя самому."
        scene 1scene (52) with dissolve
        mc "Понимаешь, о чём я?"

        mc "....."
        scene 1scene (53) with dissolve

        mc "Отэм?"

        scene 1scene (56) with dissolve
        window hide
        pause 2.0

        scene 1scene (55) with dissolve

        mc "Ну конечно."

        scene 1scene (57) with dissolve

        mc "(Что ж, хотя бы она немного отдохнёт.)"

        mc "(Видимо, я скучнее, чем сам думал.)"


        scene 1scene (60) with dissolve
        "Ты сидишь так до самого рассвета, совершенно неподвижно, будто изображая сон."

        "Но ты не спишь."
        stop music
        play sound "audio/Sound/static.mp3" volume 0.75
        scene 1scene (61) with quickdissolve
        scene 1scene (60) with quickdissolve
        scene 1scene (61) with quickdissolve
        scene 1scene (60) with quickdissolve
        scene 1scene (61) with quickdissolve
        stop sound
        scene 1scene (60) with quickdissolve

        "Ты никогда не спишь."




    label scene_2:

        scene intro 0
        with fade
        window hide dissolve
        pause 1.0

        scene 2scene (1)
        with dissolve
        play music "audio/Music/Acting.mp3" volume 1.0

        "Ты надеваешь форму, которую должен был носить последние две недели."

        "К счастью, раз она ни разу не была в деле, она такая же чистая и отглаженная, как в день покупки."

        scene 2scene (2) with dissolve

        mc "(Мне правда не хочется идти сегодня. Но выбора особо нет.)"
        scene 2scene (3) with dissolve

        mc "(Может, если я начну ходить хотя бы раза два в неделю, Отэм отстанет от меня.)"

        mc "(К тому же...)"
        scene 2scene (4) with dissolve

        mc "(Может, всё будет не так уж плохо...)"
        mc "(...А может, будет. Кого я обманываю?)"
        scene 2scene (3) with dissolve
        mc "(Не то чтобы эта дурацкая форма что-то меняла. Под ней всё тот же я.)"

        scene 2scene (2) with dissolve
        mc "(И всё же... если я продолжу прятаться, я знаю, чем это кончится. Ещё одна лекция от Отэм.)"
        mc "(Эта девчонка умеет вызывать чувство вины лучше, чем кто-либо ещё.)"
        mc "(Может, она права, что подталкивает меня. Не то чтобы у меня было много других дел.)"

        scene 2scene (4) with dissolve
        mc "(Но даже если я пойду, не то чтобы люди вдруг начали меня замечать. Я просто... есть.)"
        mc "(Для большинства я просто её странный приёмный брат. Чёрт, я даже не уверен, что кто-то заметил бы, если б меня не стало.)"
        scene 2scene (5) with dissolve
        mc "(А если и заметили бы, то, скорее всего, потому что им что-то от меня нужно.)"
        mc "(Кто-то сказал бы, что это делает меня полезным для других...)"
        mc "(А по-моему, это делает меня скорее обузой.)"


        scene 2scene (6) with dissolve
        mc "(Неважно, я знаю одно: если смогу пережить сегодняшний день... думаю, всё будет нормально.)"
        scene 2scene (8) with dissolve
        mc "(Никогда не видел Отэм счастливее, чем когда я реально стараюсь. Так что, может, это пойдёт ей на пользу.)"
        mc "(И может...)"
        scene 2scene (9) with dissolve
        mc "(Просто может быть...)"
        scene 2scene (10) with dissolve
        window hide dissolve
        pause 1.0
        scene 2scene (7) with dissolve
        mc "(Этого хватит и для меня тоже.)"
        scene black with fade
        play music "audio/Music/School.mp3" volume 1.0
        scene 2scene (11) with dissolve
        "Вы с Отэм идёте в школу. Ветер гонит листья."
        mc "Ты сегодня явно хорошо выспалась."
        a "А кого это удивляет? Я всегда сплю как убитая!"
        mc "(Хоть у кого-то из нас так.)"
        "Отэм потягивается, закинув руки за голову, пока вы идёте, прохладный утренний воздух заставляет листья хрустеть под ногами."
        scene 2scene (12) with dissolve
        a "Знаешь, у меня хорошее предчувствие насчёт сегодня."

        mc "Да ну? Что, звёзды сошлись? Какое-то божественное послание от вселенной?"

        a "Не, просто интуиция. В смысле, статистически же возможен хороший день, разве нет?"
        scene 2scene (13) with dissolve
        mc "Статистически — конечно. Но я бы сказал, вероятность резко падает в тот момент, когда мы ступаем на территорию школы."

        a "Ого, вот это оптимизм. Тебе бы вести мастер-класс на тему «как ожидать худшего»."

        mc "Я предпочитаю думать об этом как о «реалистичной готовности к разочарованию»."

        a "Или просто модный способ сказать «пессимист»."
        scene 2scene (16) with dissolve
        mc "Слушай, я просто хочу сказать: если сегодня случится что-то нелепое, типа..."

        mc "Не знаю, внезапная контрольная? Я буду морально готов, а вот ты запаникуешь."

        a "Пфф, как будто. Я расцветаю под давлением."

        mc "Это говорит человек, который на прошлой неделе под давлением забыл, как пишется слово «ресторан»."

        a "Эй! Это был глюк мозга, а не паника!"
        scene 2scene (26) with dissolve

        mc "Глюк мозга, значит? Новое слово для «тупости», которого я раньше не слышал."

        mc "Глюк мозга, значит? Новое слово для «тупости», которого я раньше не слышал."

        a "Знаешь что? Ты просто завидуешь моей позитивной энергии. Вот в чём дело."

        mc "Ну да, точно в этом. Я просто раздавлен тем, что не просыпаюсь каждое утро, источая бредовый оптимизм."
        scene 2scene (46) with dissolve

        a "Ты вообще не источаешь оптимизм. Ты источаешь запах человека, который забывает мыть голову в душе."

        mc "Ну да, а ты источаешь запах человека, который вообще не моется."

        a "Эй! Так с женщиной не разговаривают!"
        scene 2scene (25) with dissolve

        mc "Ты права, дай знать, когда я буду разговаривать с одной."

        a "Да пошёл ты, чел!"

        "Отэм изображает возмущение, но её ухмылка выдаёт, насколько ей это нравится."

        scene 2scene (21) with dissolve
        a "Я скучала по этому, знаешь?"
        mc "По чему? По тому, как я над тобой издеваюсь?"

        a "Нет, дурак, по тому, что мы с тобой куда-то ходим вместе."

        a "Мы раньше каждый день вместе ходили в школу. Что случилось?"

        scene 2scene (20) with dissolve

        mc "(Я не могу ответить, потому что, если честно, сам не знаю.)"
        mc "(Не секрет, что раньше мы были ближе, но я не помню, из-за чего мы отдалились.)"
        scene 2scene (16) with dissolve

        a "Ну что ж, первый день после перерыва. Волнуешься?"

        mc "О да, аж дух захватывает от предвкушения образовательных подвигов."

        a "Да ладно тебе, не может быть всё так плохо."

        mc "Ага, ну а что вообще может пойти не так, правда?"
        scene 2scene (17) with dissolve

        mc "О, погоди, у меня есть список."

        mc "Учитель рассаживает всех по местам, и я застреваю рядом с тем, кого ты терпеть не можешь."

        mc "Меня вызывают, чтобы я «наверстал» или представился классу."
        scene 2scene (18) with dissolve

        mc "Случайно назвать учителя «мамой»."
        mc "Пришлось бы зубрить кучу дерьма за те две недели, что я пропустил."
        mc "Случайно назвать учителя «папой»."
        scene 2scene (19) with dissolve
        a "Ладно, я поняла, господи."
        scene 2scene (20) with dissolve
        a "Если тебе от этого станет легче, я могу помочь тебе наверстать всё, что ты пропустил."
        scene 2scene (22) with dissolve
        mc "Ты предлагаешь мне репетиторство?"

        a "О боже, вот оно, начинается.."

        mc "Мисс «тройка тоже оценка» тут у нас? Ты кто такая и что ты сделала с моей Отэм?"
        scene 2scene (14) with dissolve
        a "Эй, не смейся, я в этом году правда стараюсь изо всех сил."
        a "Всё становится серьёзно, [mcname]. Как бы я ни ненавидела учёбу, в этом году мы будем подавать документы в колледж."
        a "И мне бы правда хотелось иметь выбор, куда поступать."
        a "И тебе я того же желаю. Так что если у тебя проблемы — дай знать."
        scene 2scene (15) with dissolve

        a "{size=-17}Плюс это значит, что я буду проводить с тобой больше времени...{/size}"
        mc "А? Что ты сказала, Отэм?"

        scene 2scene (23) with hpunch
        stop music

        u "Эй!! Мешки под глазами!!"

        scene 2scene (24)

        mc "О боже."
        mc "Есть только один человек на свете, кто меня так называет."
        play ambient "audio/ambient/running.mp3"

        scene 2scene (47)

        u "Иду"

        scene 2scene (48)

        u "К"

        scene 2scene (49)

        u "ТЕБЕ!"
        stop ambient
        play sound "audio/Sound/thud.mp3"
        scene intro 0
        with hpunch
        pause 2.0
        play music "audio/Music/Friends.mp3" volume 1.0
        play sound "audio/Sound/deathbell.mp3"

        scene 2scene (27) with hpunch
        "Прежде чем ты успеваешь хоть как-то осознать происходящее, тебя уже держат в захвате за шею, и ты с трудом дышишь."
        l "Чё это ты тут раскис!?"
        scene 2scene (27) with hpunch
        l "Сто лет тебя не видел!"
        scene 2scene (29) with dissolve

        I "Ну надо же, какая приятная встреча."


        scene 2scene (30) with dissolve
        I "Извини, [mcname], он сорвался с поводка."

        I "И, судя по всему, это всё равно бы не помогло."

        pe "К тому же, когда он начинает бежать, ты знаешь — его уже не поймаешь."

        a "Ну, мы обе знаем, что ты бы не рискнула сломать каблук, пытаясь это сделать."
        scene 2scene (31) with dissolve

        I "Осторожнее, Отэм, ты бы не узнала элегантность, даже если бы она впорхнула прямо в тебя."

        a "Да? А я вот сегодня утром об элегантность споткнулась и велела ей убраться с дороги."

        I "Манеры, {i}mon ami{/i}. Однажды я научу тебя делать реверанс."

        pe "Если вы, дамы, не против, я бы хотел перекинуться парой слов с братом Отэм."

        a "Он весь твой, но не думаю, что он сейчас способен говорить."
        mc "(Как ты, наверное, уже понял, это люди, которых я хорошо знаю.)"

        scene 2scene (28) with dissolve
        mc "(Высокий, который прямо сейчас душит меня до полусмерти — это Логан.)"
        scene 2scene with dissolve
        mc "(Невысокий, с серьгой — это Пьер.)"
        scene 2scene (31) with dissolve
        mc "(Как я уже говорил, я не так уж много о них знаю, несмотря на то что мы друзья.)"
        mc "(Единственное, что я знаю — стоит им во что-то влипнуть...)"
        mc "(...меня почему-то всегда тоже туда втягивают, хочу я того или нет.)"

        scene 2scene (28) with dissolve
        mc "(С Логаном всё довольно просто.)"
        mc "(Я бы не назвал его тупым, он просто...)"
        mc "(....)"
        mc "(Ладно, да, я бы назвал его тупым.)"
        mc "(Хотя он это компенсирует своей пугающей силой.)"

        scene 2scene with dissolve

        mc "(Пьер — полная противоположность Логана.)"
        mc "(Он брат лучшей подруги Отэм, Изры. Так что я его неплохо знаю.)"
        mc "(Чего ему не хватает в мускулах, он с лихвой компенсирует мозгами.)"
        mc "(А ОСОБЕННО — обаянием.)"
        mc "(Но это не мешает ему использовать это обаяние, чтобы выпутываться из неприятностей.)"
        mc "(Я никогда не видел, чтобы кто-то умел выкручиваться из ситуаций так же ловко, как он.)"

        scene 2scene (32) with dissolve
        pe "Что ж, приятно видеть тебя на ногах. Я уж на секунду подумал, что Отэм тебя прикончила и спрятала тело."
        l "А я ставил на то, что кто-то наконец-то тебя проэкзорцировал!"

        scene 2scene (33) with hpunch

        mc "А ну слезьте с меня!"
        mc "(Они говорят, что переживали за меня, но так и не решили меня проведать.)"
        mc "(Ни звонка, ни даже сообщения ни от кого. Вот так я и понимаю, что для них не так уж важен.)"

        scene 2scene (35) with dissolve

        "Пьер кладёт руку тебе на плечо и что-то шепчет на ухо."
        pe "Слушай, теперь, когда ты вернулся..."
        pe "Мой верный наперсник, мой недооценённый гений… мне нужны твои услуги."
        mc "Ты...{w} серьёзно?"
        pe "У меня есть пара укурков, которые думают, что я продам им «органическую и импортную» дурь. Мне нужна твоя помощь."

        scene 2scene (36) with dissolve

        mc "Ты... хочешь, чтобы я помог тебе продавать наркотики?"
        pe "Что? Нет, конечно нет. Это просто сушёные чайные листья и орегано, но им об этом знать не обязательно."
        pe "В любом случае, это только первый шаг моего плана стать супербогатым миллиардером."
        pe "У меня всё расписано вот здесь."
        play sound "audio/Sound/Paper.wav"
        show paper with dissolve

        "Пьер протягивает тебе листок бумаги, испещрённый недодуманными идеями, каракулями долларовых знаков и рисунком Пьера в солнечных очках."
        pe "Так что... может, пойдём на урок и начнём этим заниматься?"

        hide paper with dissolve

        l "Годный план, кстати, мне ещё надо, чтобы ты сделал за меня домашку."
        mc "(Похоже, они соскучились по мне только потому, что им от меня что-то нужно.)"

        scene 2scene (34) with dissolve
        pe "Что ж, полагаю, пора браться за дело! Увидимся с вами, девчонки, позже на уроке."
        mc "Эй, погодите-ка! Я вообще ни на что не соглашался из того, что вы тут наговорили!"
        pe "Не опаздывай!"
        mc "Богом клянусь, вы бы лучше отпустили меня, или я—"

        scene 2scene (38) with dissolve
        "Твой голос становится всё тише — тебя утаскивают Логан и Пьер."
        I "{i}Mon Dieu{/i}, до чего же тупые эти парни."
        a "Эй, вообще-то это про мою семью ты сейчас говоришь."
        scene 2scene (39) with dissolve
        I "Уф, не напоминай. Хотя бы у тебя с ним общих генов нет."
        I "Знаешь, на днях я видела, как он делал листовки — искал людей, готовых нарядиться в него, чтобы он мог сбежать с урока?"
        scene 2scene (41) with dissolve
        I "В смысле, ну как можно быть таким тупым? Не то чтобы он найдёт кого-то достаточно низкого, чтобы кого-то обмануть."
        I "Он даже меня попросил это сделать, раз уж мы близнецы! Видимо, до него не дошло, что мы совсем не похожи."
        stop music fadeout 1.0
        scene 2scene (42) with dissolve
        I "В смысле, не могли же мы правда быть генетически родственниками, да? Может, его усыновили, а нам просто не сказали."
        I "Ты как думаешь, Отэм?"
        I "Отэм?"
        scene 2scene (44) with dissolve

        I "Отэм, солнышко? Всё в порядке?"
        a "А— эм, да, всё хорошо. Просто задумалась."

        scene 2scene (45) with dissolve

        a "Ну же, не хватало нам ещё опоздать на урок!"


        scene intro 0 with fade
        pause 2.0


    label scene_3:
        play music "audio/Music/School.mp3" volume 1.0
        scene 3scene (1) with fade
        pe "Ого, ты ведь впервые видишь новый класс, да, [mcname]?"
        mc "Ну, наверное... По-моему, выглядит так же, как и прошлый."
        l "Ну да, но это твой последний год, ты впервые заходишь в один из этих кабинетов."
        mc "Нееет, я аж убит горем от этого."
        l "Эй, ничего страшного, зато в этом году мы хотя бы все сидим вместе!"
        mc "Я вообще-то сарказм—"
        pe "Эй, народ, а почему эти две девчонки сидят за нашей партой?"
        scene 3scene (2) with dissolve
        mc "Не знаю, вы их раньше видели?"
        l "Они точно не из нашего класса."
        scene 3scene (4) with dissolve
        "Ты подходишь к двум девушкам, болтающим друг с другом."
        mc "Эм... п-привет, вы сидите на нашем месте. Не могли бы вы пересесть?"
        scene 3scene (5) with dissolve
        mc "Алло? Я же попросил вас—"
        mc "Вы меня вообще слушаете?"
        mc "..."
        scene 3scene (6) with dissolve
        mc "Что ж, какая увлекательная беседа выходит у меня с самим собой."
        mc "Ладно, Пьер, я передаю ход тебе."
        scene 3scene (9) with dissolve
        pe "Эй, дамоч—"
        scene 3scene (9) with hpunch
        g2 "Ой, привет, Пьер, как дела?~"
        scene 3scene (10) with dissolve
        g2 "Ой, прости, это ваше место? Мы сейчас же пересядем!"
        g1 "Слушай, раз уж мы тут. Как думаешь, мы с тобой могли бы как-нибудь сходить в кино?"
        scene 3scene (12) with dissolve
        g2 "Эй, я как раз хотела это спросить!"
        mc "(Характер Пьера — как будто в видеоигре он вложил все очки умений в харизму."
        mc "(Он определённо был бы самым популярным ловеласом, если бы не тот факт, что... ну...)"

        scene 3scene (13) with dissolve
        pe "Нет, спасибо, я гей."
        mc "(Ага, вот именно.)"
        scene 3scene (14) with dissolve
        g1 "А, ясно... а ты как, Логан?"

        l "Ох, спасибо, но мне запрещено появляться в этом кинотеатре после того, как я прыгнул сквозь один из их проекционных экранов."

        scene 3scene (16) with dissolve
        g1 "Уф, мы никогда не найдём нормального парня в этой школе."
        scene 3scene (19) with dissolve
        g2 "Может, стоит присмотреться к байкерам из «Цербера» у входа?"
        g1 "Ага, конечно, я прямо мечтаю, чтобы меня похитила банда. Думай головой, пожалуйста."
        scene 3scene (18) with dissolve

        pe "Что ж, пора начинать!"
        play sound "audio/Sound/bell.wav" volume 2
        scene intro 0 with fade
        pause 2.0
        scene 3scene (20) with fade
        "Ты проводишь утро, помогая Пьеру и Логану."
        scene 3scene (20) with hpunch
        l "КАК, ЧЁРТ ВОЗЬМИ, ТЫ ТАК БЫСТРО ПОНИМАЕШЬ ЭТУ ЧУШЬ!?"
        l "ТЫ ЧТО, КАКОЙ-ТО СУПЕРГЕНИЙ!?"
        mc "Логан, это базовое умножение."
        mc "Мы это в детском саду проходили..."

        scene 3scene (21) with dissolve

        mc "Но, наверное, для тебя гением станет любой, у кого в голове не кирпич, да?"
        l "З-заткнись, мешки под глазами."

        scene 3scene (22) with dissolve

        pe "Так, [mcname], что у тебя нового?"

        scene 3scene (23) with dissolve
        pe "Читал новые книги или смотрел какие-нибудь сериалы в последнее время?"

        pe "Пробовал новые места поесть в городе?"

        pe "Может, завёл новое хобби или типа того?"
        scene 3scene (24) with dissolve

        pe "Или... может, у тебя появился кто-то особенный?"

        scene 3scene (26) with dissolve
        mc "Пшшш, ну да, нет. В тот день, когда это случится, ты будешь куда больше сосредоточен на новостях."

        scene 3scene (27) with dissolve

        mc "Потому что там будут сообщать о летающих в небе свиньях."

        mc "(Ну и потом, быть рядом с незнакомцами так долго звучит утомительно.)"
        scene 3scene (28) with dissolve

        mc "(Не то чтобы я никогда не хотел девушку, это было бы неплохо, но, наверное, я никогда особо и не старался.)"

        scene 3scene (29) with dissolve

        mc "(Плюс ко всему, физический контакт и общение — это вообще не моё.)"

        scene 3scene (30) with dissolve

        l "Хех, а кому вообще нужны девушки или парни? Я уже женат."

        pe "...."

        mc "...."

        pe "Что?"

        scene 3scene (31) with dissolve

        l "На ком я женюсь?"

        l "Как хорошо, что ты спросил, Пьер…"

        pe "Но я вообще-то не—"

        scene 3scene (32) with dissolve

        l "Я женат..."

        scene 3scene (33)
        with hpunch
        window hide dissolve
        pause 1.0
        scene 3scene (34)
        with hpunch
        window hide dissolve
        pause 1.0
        scene 3scene (35)
        with dissolve
        window hide dissolve
        pause 1.0
        scene 3scene (36)
        with dissolve

        play sound "audio/Sound/Swoosh.mp3" volume 0.75

        scene 3scene (37)
        with hpunch

        l "НА СПРАВЕДЛИВОСТИ!"

        scene 3scene (41) with dissolve
        mc "...."

        pe "...."

        scene 3scene (42) with dissolve
        pause 2.0

        scene 3scene (38) with dissolve

        mc "Ну да, только слепой женился бы на тебе {i}добровольно{/i}."

        l "ЭТА ШУТКА ДАЖЕ НЕ ОРИГИНАЛЬНАЯ, ЗАДНИЦА!"

        play sound "audio/Sound/Slam.wav" volume 1.0

        scene 3scene (39)
        with hpunch

        stop music

        narrator "*Бабах*"

        u "ЧЁЁЁРТ!"

        scene 3scene (40)
        with dissolve

        u "*Пыхтение* *Пыхтение*"

        scene 3scene (43)
        with dissolve

        play music "audio/Music/LilyTheme.mp3" volume 1.0

        u "Да блин!! Я успела вовремя!!"

        scene 3scene (44)
        with dissolve

        u "А?"

        scene 3scene (45)
        with dissolve
        window hide dissolve
        pause 1.0
        pause 3
        play sound "audio/Sound/bong.mp3" volume 1.0
        scene 3scene (46)
        with dissolve

        u "Эээ...."

        scene 3scene (47)
        with dissolve

        u "П-привет всем, меня зовут Лили."

        scene 3scene (48)
        with dissolve

        L "И-извините за такую сцену, хаха."

        scene 3scene (49)
        with dissolve

        a "Приятно познакомиться, Лили, я Отэм."

        a "Поздравляю, что не опоздала."

        a "Можешь сесть с нами с Изрой, если хочешь."

        I "Ты точно умеешь делать эффектный выход."

        scene 3scene (50)
        with dissolve

        L "Спасибо большое, Отэм!"

        L "Ну да, эффектное появление — это моя фишка."

        scene 3scene (51)
        with dissolve

        mc "(Лили, значит... Она очень симпатичная.)"


        narrator "Ты не можешь понять, в чём дело. Но невысокая блондинка, стоящая перед тобой, кажется очень знакомой."

        scene 3scene (50) with dissolve

        narrator "Почти как если бы..."
        scene 3scene (54) with dissolve
        narrator "Ты уже встречал её раньше..."
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene 3scene (52) with quickflash
        stop sound
        L "А?"
        "Взгляд Лили встречается с твоим напрямую. Будто она почувствовала, что ты смотришь на неё краем глаза."
        scene 3scene (53) with dissolve
        mc "(ЧЁРТ)."


        mc "(Она заметила, что я на неё пялился?)"

        mc "(Теперь я, наверное, выгляжу как конченый извращенец.)"

        scene 3scene (52) with dissolve

        pause 1.0

        scene 3scene (54) with dissolve

        mc "Погоди, она мне улыбается в ответ?"

        mc "...."

        mc "Да ладно..."
        scene 3scene (25) with dissolve
        mc "Наверное, она просто вежливая..."




    label scene_4:

        stop music

        scene intro 0
        with fade

        scene 4scene (1)
        with fade

        play music "audio/Music/School.mp3" volume 1.0

        window hide dissolve
        pause 1.0

        "Урок заканчивается. Ты спешишь, чтобы выйти отсюда первым."

        "Ты идёшь по тихим коридорам, приглушённый гул голосов доносится из-за дверей кабинетов."

        mc "(Откуда я знаю эту девушку...)"

        mc "(Клянусь, это было прямо как встретить старого друга после долгой разлуки.)"

        "Ты на секунду задумываешься об этом, но не зацикливаешься. Смысла нет."

        scene 4scene (2) with dissolve

        mc "(Эх, не так уж это и важно. Может, она просто похожа на какую-то актрису из фильма.)"

        mc "(К тому же у меня есть дела поважнее. Например, мне нужно больше сигарет.)"

        mc "(Наверное, придётся зайти в магазин сегодня после обеда. Надо спросить у Отэм, не нужно ли ей чего.)"



        scene 4scene (3) with dissolve
        narrator "Твои мысли прерывает громкий смех, доносящийся из-за поворота у шоссе."
        "Тебе даже не нужно смотреть, чтобы понять, чей это смех."

        mc "(Лёгок на помине.)"

        scene 4scene (6) with dissolve

        "Ты сворачиваешь за угол как раз вовремя, чтобы увидеть, как Отэм смеётся так сильно, что чуть не падает. Лили ухмыляется, как ребёнок утром на Рождество."
        a "ПАХАХАХА!"
        a "Да не может быть, чтобы ты правда так ей и сказала!"
        L "Хехе, ага, она была в бешенстве! Лицо стало ярко-красным — я думала, она сейчас взорвётся!"

        scene 4scene (7) with dissolve

        mc "Что вы тут, девчонки, затеяли?"
        a "О, привет, [mcname]!"

        a "Лили как раз рассказывала мне одну нелепую историю из своей старой школы."

        a "Мы вообще-то как раз собирались идти в торговый центр."

        scene 4scene (4) with dissolve

        L "Отэм много о тебе рассказывала, [mcname]."

        mc "Надеюсь, только хорошее."

        "Ты бросаешь на Отэм встревоженный взгляд. Но она лишь улыбается, явно забавляясь твоим смущением."

        a "Не переживай так, чел. Я так и не собралась упомянуть твою винтажную коллекцию порнухи."

        mc "Ахахахахахах, какая смешная {i}шутка{/i}, Отэм."

        mc "Вечно у тебя эти забавные {i}шутки{/i}, которые просто {i}шутки{/i} и совсем-совсем не правда."


        scene 4scene (5) with dissolve

        L "Эй, не переживай. Скорее всего, ей и в подмётки не годится моя коллекция."

        mc "Эм.."
        scene 4scene (4) with dissolve
        L "Я тоже просто шучу!"

        L "Или нет?"
        scene 4scene (5) with dissolve

        L "Ты никогда не узнаешь."

        scene 4scene (4) with dissolve

        L "В общем, тебе стоит поехать с нами в торговый центр!"

        scene 4scene (8) with dissolve

        L "Но сразу предупреждаю, не думаю, что там есть Hot Topic."

        "Она бросает на тебя лукавую ухмылку, явно собой довольная."

        scene 4scene (9) with dissolve

        a "О, точно! Мы так давно с тобой не ходили по магазинам."
        a "Пойдём, проведём немного времени вместе, и я вас как следует познакомлю?"

        scene 4scene (10) with dissolve

        mc "Причина, по которой я никогда не хожу с тобой по магазинам, в том, что обычно платить за всё приходится мне."
        mc "(Клянусь, если бы я пару лет назад не устроился на летнюю подработку, она бы уже начала везде ходить голой.)"
        mc "И, боюсь, придётся отказаться. У меня после школы есть планы."

        scene 4scene (11) with dissolve

        narrator "Не колеблясь ни секунды, Лили бросается к тебе бежать. Явно не считывая обстановку."

        L "Ой, да ладно тебе, хватит быть таким занудой! Будет весело, обещаю!"

        a "Эмм, Лили, п-погоди секунду."

        scene 4scene (15) with hpunch

        window hide dissolve
        pause 1.0

        scene 4scene (12) with dissolve

        L "Было бы неплохо услышать мужское мнение кое о чём."
        L "Ты мог бы помочь мне примерить симпатичные новые наряды."

        a "СТОЙ, НЕТ, ЛИЛИ, ХВАТИТ!"

        stop music

        scene 4scene (13) with dissolve
        window hide dissolve
        pause 1.0
        play sound "audio/Sound/uhohglitch.mp3" volume 1.0
        scene 4scene (14) with quickflash
        window hide dissolve
        pause 1.0
        scene 4scene (15) with dissolve
        window hide dissolve
        pause 1.0
        play sound "audio/Sound/uhohglitch2.mp3" volume 1.0
        scene 4scene (16) with quickflash
        window hide dissolve
        pause 1.0
        play music "audio/Music/scawr.mp3" volume 1.0
        u "ХВАТИТ, БЛЯДЬ, ДЁРГАТЬСЯ, ЗАСРАНЕЦ!"

        scene 4scene (17) with dissolve

        u "ЧЕМ БОЛЬШЕ ТЫ УПИРАЕШЬСЯ, ТЕМ БОЛЬШЕ КОЖИ Я С ТЕБЯ СПОЗЖЕ СОДЕРУ!"

        scene 4scene (18)
        with dissolve

        mc "ОТПУСТИ МЕНЯ!"


        mc "Где она..."

        scene 4scene (19) with hpunch

        mc "ГДЕ МОЯ СЕСТРА?!"
        stop music
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene 4scene (23) with quickdissolve
        scene 4scene (19) with quickdissolve
        scene 4scene (24) with quickdissolve
        scene 4scene (25) with quickdissolve
        stop sound
        play sound "audio/Sound/uhohglitch3.mp3" volume 1.0
        $ renpy.pause(4, hard=True)
        stop sound
        scene black
        $ renpy.pause(1, hard=True)
        play ambient "audio/ambient/tv.mp3" volume 1.0
        scene scareroom (1)
        $ renpy.pause(1, hard=True)
        scene scareroom (2)
        $ renpy.pause(1, hard=True)
        scene scareroom (1)
        $ renpy.pause(1, hard=True)
        scene scareroom (3)
        $ renpy.pause(1, hard=True)
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene black with quickflash
        scene black with quickflash
        scene scareroom (4) with quickflash
        stop sound
        $ renpy.pause(1, hard=True)
        scene scareroom (5)
        $ renpy.pause(1, hard=True)
        scene scareroom (4)
        $ renpy.pause(1, hard=True)
        scene scareroom (6)
        $ renpy.pause(1, hard=True)
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene lilyyoung1 with quickflash
        $ renpy.pause(0.2, hard=True)
        scene lilyyoung2 with quickflash
        $ renpy.pause(0.2, hard=True)
        scene scareroom (7) with quickflash
        stop sound
        $ renpy.pause(1, hard=True)
        scene scareroom (8)
        $ renpy.pause(1, hard=True)
        scene scareroom (7)
        $ renpy.pause(1, hard=True)
        play sound "audio/Sound/besttostayclose.mp3" volume 0.2
        $ renpy.pause(6, hard=True)
        play sound "audio/Sound/lightswitch.mp3" volume 1.0
        scene scareroom (9)
        $ renpy.pause(4, hard=True)
        play sound "audio/Sound/uhohglitch4.mp3" volume 0.75
        scene scareroom (10) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (11) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (12) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (10) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (11) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (12) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (10) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (11) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (12) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (10) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (11) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (12) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (10) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (11) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (12) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (13) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene scareroom (14) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        stop sound
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene 4scene (22) with quickdissolve
        scene 4scene (24) with quickdissolve
        scene 4scene (23) with quickdissolve
        scene 4scene (27) with quickflash
        stop sound
        stop ambient


        L "Ч-что это было?"
        L "[mcname]?"

        scene 4scene (28) with dissolve

        L "[mcname], ты в поряд-"

        scene 4scene (29) with hpunch

        mc "КАКОГО ЧЁРТА ЭТО БЫЛО!?"

        mc "ДА КТО ТЫ ВООБЩЕ ТАКАЯ?!"

        scene 4scene (30) with dissolve

        L "Я-я не знаю, я-"

        scene 4scene (29) with hpunch
        mc "НЕ ВРИ МНЕ, ТЫ ЗНАЛА, ЧТО ЭТО БЫЛО."

        mc "ПОЧЕМУ Я БЫЛ ТАМ, И К КОМУ Я ОБРАЩАЛСЯ?!"

        scene 4scene (30) with dissolve

        L "Чт-нет-мне жаль я-"

        scene 4scene (31) with dissolve

        L "Пожалуйста, п-перестань, ты делаешь мне больно!"
        scene 4scene (32) with dissolve

        a "БОЖЕ МОЙ! [mcname!u], ОТПУСТИ ЕЁ!"
        scene 4scene (33)
        with dissolve
        window hide dissolve
        pause 1.0
        play sound "audio/Sound/uhohglitch.mp3" volume 1.0
        scene 4scene (34)
        with quickflash
        window hide dissolve
        pause 1.0
        mc "Какого хрена?"
        scene 4scene (35)
        with dissolve
        window hide dissolve
        pause 1.0

        scene 4scene (36) with dissolve

        mc "Ч-чёрт, Лили. Мне так жаль, я—."
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene 4scene (20) with quickflash
        scene 4scene (37) with quickflash
        scene 4scene (20) with quickflash
        scene 4scene (37) with quickflash
        scene 4scene (38) with quickflash
        stop sound
        mc "Аргх, да что за хрень—"
        play sound "audio/Sound/Static.mp3" volume 1.0
        scene 4scene (20) with quickflash
        scene 4scene (39) with quickflash
        scene 4scene (20) with quickflash
        scene 4scene (39) with quickflash
        scene 4scene (44) with hpunch
        stop sound
        mc "Аргххх!!"
        "Острая боль пронзает твою голову."
        "Твой сбитый с толку разум заполняют образы, которые ты не в силах понять."
        scene 4scene (45) with dissolve
        mc "Прости, мне... мне нужно идти."

        scene 4scene (42) with dissolve
        "Ты бежишь так быстро, как только можешь, всё ещё сжимая голову от боли."
        scene 4scene (43) with dissolve
        a "Т-ты в порядке?"

        L "Эм, да, конечно. Наверное, я его как-то ущипнула, или типа того."

        a "Ну, это неприемлемо! Клянусь, я с ним поговорю."

        a "Не могу поверить, что он на такое способен! Распускать руки — это совсем на него не похоже."
        scene 4scene (40) with dissolve

        L "О-Отэм, всё нормально. Уверена, он просто немного испугался."
        L "Так, ну что, идём за покупками или нет?"
        a "Ты точно готова?"
        L "Не спрашивала бы, если бы не была готова."

        scene 4scene (41) with dissolve
        L "(К тому же меня не так уж потрясло то, что сделал [mcname]. Думаю, любой бы так среагировал, если...)"
        L "(Я до сих пор не понимаю, что увидела.)"
        L "(Но я точно знаю, что это было что-то, чего мне видеть не полагалось.)"

        scene 4scene (46) with dissolve
        window hide dissolve
        pause 1.0

        u "Понятно."
        u "Значит, вот когда ты пробудил [mcname]..."

        scene 4scene (47) with dissolve

        window hide dissolve
        pause 1.0

        u "Кекекеке"

        u "Что ж... полагаю, вот здесь и начинается моя работа."

        scene black with fade
        window hide dissolve
        pause 1.0
        play music "audio/Music/Acting.mp3" volume 1.0 fadein 1.0
        play ambient "audio/ambient/convenience.wav" volume 1.0

        scene 5scene (1) with fade

        "Ты оказываешься в магазине у дома. Голова уже не болит, но ты всё ещё в замешательстве от того, что произошло."

        mc "(Я всё ещё не понимаю... Я не помню, чтобы что-то из этого происходило. И что я увидел, когда та девушка Лили ко мне прикоснулась?)"

        scene 5scene (2) with dissolve
        mc "(Уф, мне нужны сигареты.)"

        scene 5scene (4) with dissolve

        u "Ха! Да ладно тебе, детка, дай нам чего-нибудь!"

        "Твои мысли прерывает звук смеха с другого конца магазина."

        scene 5scene (5) with dissolve

        "Там собралась компания парней из твоей школы, и не нужно много времени, чтобы понять почему."

        "В центре компании стоит светловолосый ученик, слишком близко склонившись к явно смущённой девушке."

        "Его окружают приспешники, смеющиеся над каждым его словом, каким бы отвратительным оно ни было."

        mc "(Я слышал об этом парне. Кажется, его зовут Куинн.)"
        mc "(Капитан команды по регби, отличник, сын какого-то важного адвоката. И абсолютный кусок дерьма.)"

        "Девушка пытается отойти, но Куинн преграждает ей путь с самодовольной ухмылкой."
        scene 5scene (6) with dissolve

        q "Ой, да ладно тебе, детка. Не стесняйся. Мы же знаем, тебе нравится это внимание."

        scene 5scene (7) with dissolve

        girl_harassed "Пожалуйста, просто оставь меня в покое."

        q "Зачем бы мне это делать? Ты — лучшая часть моего дня. К тому же, с таким телом, тебе стоило бы меня благодарить."

        "Его приспешники разражаются хохотом, один хлопает его по спине."

        scene 5scene (8) with dissolve

        mc "(Чёрт, надо бы что-то сказать, но я знаю, чем это для меня обычно кончается.)"

        "Часть тебя хочет просто уйти. Связываться с Куинном и его компанией никогда добром не кончалось. Но тут он заходит ещё дальше."

        scene 5scene (9) with hpunch
        "Куинн притягивает её ближе, пока она пытается вырваться. Ясно, что добром это не кончится."

        scene 5scene (10) with dissolve

        girl_harassed "Я-я сказала, хватит!"

        q "Что? Не хочешь меня? Я знаю, что это неправда. Может, тебе просто нужно немного подбодрить."

        scene 5scene (11) with dissolve
        stop music fadeout 1.0

        mc "(Всё, хватит. Я не могу просто стоять здесь.)"

        scene 5scene (12) with dissolve

        mc "Э-эй, она же явно сказала нет."
        "Твой голос звучит строго, но в нём явно не хватает уверенности."

        scene 5scene (13) with dissolve
        "Смех стихает, все взгляды обращаются к тебе. Куинн медленно поворачивается, его самодовольная ухмылка становится шире."

        q "Так-так, гляньте-ка, у нас тут комплекс героя."

        q "Слушай, чел, вижу, что ты никогда не был с женщиной, но мне ни одна девчонка не отказывает."
        scene 5scene (14) with dissolve

        q "Хотя, если подумать, если бы девчонка увидела твою уродливую рожу на улице ночью, она бы, наверное, тоже решила, что ты насильник."

        mc "(Его слова для меня ничего не значат. Я и похуже про себя говорил.)"

        mc "Просто оставь её в покое, чел."

        scene 5scene (15) with dissolve
        "Один из прихвостней Куинна, тощий парень с гадкой ухмылкой, встревает."

        guy1 "Эй, это разве не младший братец Отэм?"

        guy2 "О, точно, это та горячая цыпочка с синими прядями в волосах, да?"

        scene 5scene (16) with dissolve

        guy1 "Блин, она вечно прячет самое лучшее. А я бы содрал с неё эти чулки не глядя."
        scene 5scene (17) with dissolve

        guy2 "Ага, и как тебе такое, шишка? Отэм вообще легко даёт?"

        guy1 "Готов поспорить, её ноги сами бы раздвинулись, стоило бы ей с нами заговорить."

        guy1 "Единственные другие парни, с которыми она тусуется — это вот этот неудачник и мелкий неудачник Пьер."

        "Твоя челюсть напрягается, руки сжимаются в кулаки."

        mc "Заткни свою чёртову пасть."

        scene 5scene (18) with dissolve

        "Другой парень смеётся, его голос режет слух."

        guy3 "Ого, вот это задело за живое. А как насчёт её подружки Изры? Такое подтянутое тело, вау!"

        guy3 "У неё эти танцовщицкие ноги, что тянутся бесконечно. А задница? Готов поспорить, она знает толк в мужском теле."

        guy3 "Знаешь, может, завтра наш друг тут нас с ними познакомит."

        guy3 "Уверен, они не откажу-"

        scene 5scene (19) with hpunch

        play sound "audio/Sound/punch.mp3" volume 1.0

        scene 5scene (20) with dissolve
        window hide dissolve
        pause 2.0
        "Без предупреждения ты наносишь удар исподтишка и смотришь, как его тело валится на пол."
        play sound "audio/Sound/Thud.mp3" volume 1.0
        scene 5scene (21) with hpunch
        "Ты сам удивлён — поднять на кого-то руку абсолютно не в твоём характере."
        "Тишина заполняет помещение, пока до всех доходит, что ты только что сделал."
        play music "audio/Music/Fight.mp3" volume 1.0 fadein 1.0
        play sound "audio/Sound/Hoodie.wav" volume 1.0
        scene 5scene (22) with hpunch
        q "Большая ошибка, дебил."

        "Прежде чем ты успеваешь среагировать, его плечо врезается тебе в грудь, зажимая в полный нельсон..."

        guy2 "Ты об этом пожалеешь, засранец!"

        play sound "audio/Sound/punch.mp3" volume 1.0
        scene 5scene (23) with hpunch
        pause 2.0
        "Боль взрывается по всему лицу. Ты чертыхаешься, пытаясь сопротивляться, но бесполезно."
        play sound "audio/Sound/punches.mp3" volume 1.0
        scene 5scene (24) with hpunch
        pause 2.0
        scene 5scene (25) with dissolve
        guy2 "Что, уже не такой крутой?"
        guy2 "Сказать нечего? А!?"
        guy1 "Хахаха! Ого! Давай ещё, это станет вирусным!"
        scene 5scene (26) with dissolve
        play sound "audio/Sound/Thud.mp3" volume 1.0
        "Куинн наконец даёт тебе упасть на пол. Ты пытаешься встать, пока мир начинает расплываться."
        scene 5scene (27) with hpunch
        guy4 "МЫ ЕЩЁ НЕ ЗАКОНЧИЛИ, СУКА!"
        play sound "audio/Sound/Glassbreak.mp3" volume 1.0
        scene black with hpunch

        "Один из парней впечатывает твою голову в холодильник, разбивая стекло и оставляя на голове ещё больше крови."
        play sound "audio/Sound/Kicks.mp3" volume 1.0
        scene 5scene (28) with hpunch
        guy4 "ТЕБЕ ХАНА. СЛЫШИШЬ МЕНЯ! ХАНА! СДОХНИ НАХРЕН!"
        "Твоё зрение начинает расплываться, пока компания хулиганов топчет и пинает тебя по лицу."
        scene 5scene (29) with dissolve
        "Девушка кричит, а кассир что-то бормочет про вызов полиции. Наконец они отступают."
        stop sound fadeout 1.0
        q "В следующий раз не лезь не в своё дело."

        "Он смеётся, пока они с компанией вразвалочку выходят из магазина."

        stop music fadeout 1.0

        scene 5scene (30) with dissolve
        "Ты едва в сознании, пока начинаешь осознавать, что случилось."
        "Боль жгучая, но, на удивление, терпимее, чем ты ожидал."
        scene 5scene (31) with dissolve

        girl_harassed "Боже мой, ты в порядке? Я-я не хотела, чтобы—"
        scene 5scene (32) with dissolve

        mc "Я в норме...{w} Это ерунда..."

        scene 5scene (33) with dissolve

        mc "Ты в порядке?"

        girl_harassed "Я-{w}да, я в порядке, но тебе нужно в больни-{nw=2}"
        scene 5scene (34) with dissolve

        mc "Я сказал, что в норме. Если больше ничего, я иду домой."

        scene 5scene (35) with dissolve

        girl_harassed "Пожалуйста... просто подожди, тебе нужна помощь."

        mc "Если честно...{w} мне не так уж и больно."
        mc "Видимо, их удары были такими же хилыми, как и их эго."
        scene 5scene (36) with dissolve

        girl_harassed "Я-."
        girl_harassed "...."
        girl_harassed "Я...{w} Ладно, если ты думаешь, что с тобой всё будет в порядке."
        girl_harassed "Просто, пожалуйста, скажи кому-нибудь, если у тебя сотрясение."

        scene 5scene (38) with dissolve

        mc "Обязательно посчитаю алфавит в обратном порядке или типа того, когда доберусь домой."

        "Она тихонько усмехается твоей шутке."

        girl_harassed "Это для пьяных, а не для людей с сотрясением."

        mc "Хм... значит, может, у меня и правда повреждение мозга."

        mc "В любом случае... рад, что ты в порядке."

        mc "Увидимся."

        scene 5scene (39) with dissolve

        girl_harassed "..."

        girl_harassed "Погоди секунду."

        play sound "audio/Sound/kiss.mp3" volume 1.0

        scene 5scene (40) with dissolve

        "Прежде чем ты успеваешь среагировать, она притягивает тебя и коротко целует в щёку."

        scene 5scene (41) with dissolve

        mi "Эмм... {w}Меня зовут Мина... Спасибо тебе, типа... что спас меня и всё такое."

        scene 5scene (42) with dissolve

        mi "Если увидишь меня в школе, не стесняйся поздороваться."

        mc "Я...{w}буду иметь в виду."

        stop ambient fadeout 1.0

        scene black with fade


        "По иронии судьбы, несмотря на всю боль в голове, именно поцелуй девушки заставляет твой разум опустеть."

        "Ты возвращаешься в квартиру. После всего, что случилось сегодня, тебе просто хочется скрыться в своей комнате и побыть одному."

        mc "Да что вообще на меня нашло?"



    label scene_5:

        scene intro 0
        with fade

        "Позже той же ночью."

        play music "audio/Music/Nights.mp3" volume 1.0

        scene 6scene (1) with fade

        mc "(Чёрт, может, я пострадал сильнее, чем думал.)"

        mc "(Та девушка, наверное, была права... может, мне и правда нужен врач.)"

        scene 6scene (2) with dissolve

        mc "(Хотя я ей не соврал — учитывая, что они со мной сделали, мне должно было быть куда больнее.)"

        mc "(И вообще, какого чёрта я вмешался? Обычно я бы просто дал им самим разбираться.)"
        scene 6scene (3) with dissolve

        mc "(Реалистично, они, наверное, не стали бы её сильно калечить… Куинну есть что терять.)"

        mc "(Так почему же... неужели просто потому, что так было правильно?)"


        scene 6scene (4) with dissolve
        pause 1.0
        mc "(….)"
        mc "(Что бы я сегодня ни увидел… {w}с тех пор я веду себя странно.)"
        mc "Да что со мной не так?"
        mc "Что за хрень я увидел, когда Лили меня схватила?"
        mc "Почему я не мог уснуть уже 10 лет?"
        "Столько вопросов, а толку — как будто я кричу в кирпичную стену."
        "Ничего в моей жизни не имеет смысла, всё — лабиринт, который приходится проходить без единой подсказки."
        "Шутка без панча,"
        "Головоломка без решения."
        "Игра без приза."

        mc "Почему я просто не могу быть нормальным?"

        play sound "audio/Sound/Flash.wav" volume 0.75

        play music "audio/Music/reveal.mp3" volume 1.0
        scene 6scene (5) with flash

        u "ПОТОМУ ЧТО ТЫ НЕ НОРМАЛЬНЫЙ, [mcname!u]."

        scene 6scene (6) with dissolve


        mc "Что за—"

        scene 6scene (7) with dissolve
        "Внезапной вспышкой луч света заполняет твою комнату."
        "Прежде чем ты успеваешь хоть немного осознать происходящее, свет начинает говорить."
        u "НЕ БОЙСЯ, [mcname!u], Я — СОСУД, ЗДЕСЬ, ЧТОБЫ ТЕБЕ ПОМОЧЬ."

        scene 6scene (8) with dissolve
        narrator "Оно правда только что сказало {i}«Не бойся»{/i}?? В такой ситуации довольно сложно не бояться."
        mc "К-кто ты, чёрт возьми, такая!?"
        mc "Какого хрена тебе надо!?"

        scene 6scene (7) with dissolve

        u "ТЕБЕ ДАРОВАНЫ СПОСОБНОСТИ, КОТОРЫЕ ТЫ ДАЖЕ НАЧАТЬ ПОНИМАТЬ НЕ В СОСТОЯНИИ."
        u "МИР, КАКИМ ТЫ ЕГО ВИДИШЬ — ЛИШЬ ЧАСТЬ КАРТИНЫ, И Я БУДУ ТВОИМ ПРОВОДНИКОМ, ЧТОБЫ ЕЁ РАЗГАДАТЬ."
        narrator "Ничего из этого не имеет смысла. Я что, сплю? Нет, я бы заметил, если бы засыпал."
        mc "Хватит говорить загадками и покажи мне, кто ты, чёрт возьми, такая!!"
        narrator "Погоди... С чего это я тут требования выдвигаю? Мне правда хочется разозлить эту штуку?"
        narrator "Думаю, терять мне и правда нечего. Оно ведь сказало, что здесь, чтобы «помочь мне», в конце концов."
        u "ЕСЛИ РАСКРЫТИЕ МОЕЙ ИСТИННОЙ ФОРМЫ СДЕЛАЕТ ТЕБЯ БОЛЕЕ СПОКОЙНЫМ, Я ПОЙДУ НАВСТРЕЧУ."
        u "ЛИЦЕЗРЕЙ."

        play sound "audio/Sound/Flash.wav" volume 0.75

        scene 6scene (9) with flash
        stop music
        window hide dissolve
        pause 2.0
        scene 6scene (10) with dissolve
        window hide dissolve
        pause 2.0
        scene 6scene (11) with dissolve
        window hide dissolve
        pause 2.0
        scene 6scene (12) with dissolve

        u "Здарова, засранец."

        play music "audio/Music/Kitsune.mp3" volume 1.0

        scene 6scene (14) with dissolve
        mc "...."

        mc "Хех, вот оно наконец и случилось."

        scene 6scene (15) with dissolve

        mc "Я спятил."

        scene 6scene (16) with dissolve

        u "Э, не совсем, хотя это было бы, наверное, проще объяснить."

        mc "Ну, я не знаю, как ещё объяснить странную собачью тётку у меня в комнате."
        scene 6scene (17) with dissolve

        u "Я не собака."

        mc "Ну да, ты собака-{i}тётка.{/i}"

        scene 6scene (18) with dissolve

        u "Боже, ты всё такой же занудный."

        u "Если хочешь знать, я — дух. Дух-{i}ЛИСИЦА{/i}, если точнее."

        scene 6scene (16) with dissolve
        u "Можешь звать меня Кицунэ. Несмотря на твой тон, приятно снова тебя видеть, [mcname]."
        scene 6scene (21) with dissolve
        mc "Эммм, ладно..."

        "Ты пялишься на странную фигуру, непринуждённо стоящую в твоей комнате, будто ей там самое место. Её острая ухмылка ясно даёт понять, что твоя растерянность её забавляет."

        mc "Что ты делаешь в моей комнате, Кицунэ?"

        mc "И вообще, что значит {i}снова{/i}?"

        "Сердце чуть ускорилось. Что-то в ней казалось странно знакомым и в то же время абсолютно чужим?"
        scene 6scene (22) with dissolve

        mc "Погоди, если подумать..."
        scene 6scene (20) with dissolve

        mc "Откуда, чёрт возьми, ты знаешь моё имя?"

        scene 6scene (16) with dissolve

        "Кицунэ тихо посмеивается, её золотые глаза лукаво поблёскивают, почти светясь в тусклом свете комнаты."
        k "Хм-хм, ты и правда любопытный."
        k "Что ж, отвечая на твой вопрос — мы с тобой уже встречались раньше."
        k "Просто чуть дальше в будущем."
        mc "В будущем?"


        scene 6scene (33) with dissolve

        k "Именно."

        scene 6scene (36) with dissolve

        k "Видишь ли, я не просто какой-то дух. Я связана конкретно с тобой."
        k "Думай обо мне как... о твоём фамильяре."
        k "В твоей жизни есть куда больше, чем ты когда-либо осознавал, [mcname]."
        k "Ты нечто очень особенное — «Сияющий»."
        k "Внутри тебя скрыта сила, которую ты даже вообразить не можешь."

        "Её слова тяжело повисли между нами. Я — могущественный? Звучало абсолютно нелепо. Я же просто какое-то случайное ничтожество... разве нет?"

        scene 6scene (26) with dissolve

        k "В будущем тебе суждено столкнуться с неудержимым злом. Силой, достаточно мощной, чтобы угрожать всему миру."

        scene 6scene (32) with dissolve

        k "Но, к сожалению, ты потерпел неудачу — причём, добавлю, весьма эффектную."

        mc "Погоди, что? Типа как в дешёвой сказочке или что-то такое?"

        "Твой желудок скрутило от её прямолинейной честности. Мне сложно поверить хоть чему-то из этого."
        "Впрочем, когда в твоей комнате появляется магическое существо и сообщает тебе о твоём неизбежном поражении, это не особо вселяет уверенность."
        scene 6scene (57) with dissolve

        k "В твои последние мгновения ты умолял меня вернуться назад — тренировать тебя, переписать твою историю."
        k "Честно говоря, поначалу я колебалась. Путешествия во времени — не самое приятное дело, знаешь ли."

        scene 6scene (36) with dissolve

        "Её взгляд впился в твой — твёрдый, но странно успокаивающий."

        k "Но каким-то образом ты убедил меня, что это наш лучший шанс."

        scene 6scene (33) with dissolve

        k "Вот почему я сейчас здесь."

        mc "...."

        mc "Звучит... правда глупо."
        scene 6scene (66) with dissolve
        k "И ЭТО ВСЁ, ЧТО ТЫ МОЖЕШЬ СКАЗАТЬ??"

        scene 6scene (27) with dissolve
        mc "Ладно, подыграю тебе секунду. Учитывая, что я всё равно не могу объяснить, почему ты в моей комнате."


        mc "Гипотетически, если то, что ты говоришь — правда."
        mc "Почему избранный — именно я?"

        scene 6scene (28) with dissolve
        mc "На случай, если ты не заметила, из меня так себе боец."
        mc "Сомневаюсь, что тренировки это исправят, что бы ты ни делала."
        scene 6scene (29) with dissolve
        mc "И почему именно в этот момент? Из всех возможных времён?"

        scene 6scene (37) with dissolve
        k "Что ж, отвечая на последний вопрос — путешествия во времени... {w} штука сложная."
        k "Всё произошло так быстро, что у меня и не было возможности выбрать, в какую именно точку времени я попаду."
        scene 6scene (33) with dissolve
        k "И хотя это правда, что ты не самый одарённый в бою."
        k "К счастью для тебя, твоя сила никак не связана с физическими данными."

        scene 6scene (36) with dissolve
        k "На самом деле твоя сила происходит от количества травм, которые человек пережил за свою жизнь."
        mc "Ладно, просто хочу убедиться, что я не забрёл в чей-то фанфик с Тамблера 2011 года. Ты правда сказала, что травма — моя сила?"

        scene 6scene (33) with dissolve
        k "Именно так."

        scene 6scene (16) with dissolve
        k "Вот кое-что, чего ты, наверное, не знал."

        k "Знаешь ли ты, что у людей с бессонницей, как правило, очень высокий IQ?"

        mc "Нет... но какое это вообще имеет отношение к делу?"

        k "Хотя у бессонницы может быть много причин, чаще всего она связана с травмой."

        scene 6scene (18) with dissolve

        k "На поверхности это выглядит изматывающим, хаотичным, даже раздражающим."
        k "Но под этим слоем боли и истощения скрывается необычайный потенциал для творчества и силы."

        scene 6scene (36) with dissolve

        k "Существам, столкнувшимся с суровыми условиями, даётся два пути."

        k "Приспособиться и эволюционировать — или умереть."
        scene 6scene (33) with dissolve
        k "И ты официально один из первых, кто эволюционировал!"

        scene 6scene (30) with dissolve

        mc "Эмм... повезло мне?"

        mc "То есть ты хочешь сказать, что весь мой эмоциональный багаж — на самом деле моя скрытая суперсила?"
        scene 6scene (31) with dissolve
        k "Именно! Дело не в том, насколько ты силён или искусен физически."
        k "Дело в том, чтобы обуздать глубину своего опыта и превратить эмоциональную стойкость во что-то ощутимое, во что-то могущественное."
        "Я даже не знаю, как это осмыслить. Мир и впрямь холодный и ёбнутый."
        scene 6scene (24) with dissolve
        mc "Отлично, значит, вместо терапии я получаю магические силы. Логично, чего уж там."
        "Кицунэ тихонько смеётся, явно позабавленная твоим сарказмом."

        k "Если тебе от этого станет легче, то, что ты пробудил, куда полезнее современной терапии."



        scene 6scene (16) with dissolve

        k "Ну а теперь..."

        k "Есть ещё вопросы?"





        menu AnyQuestions:
            "И что с того?":




                mc "Ладно, и что с того?"
                mc "Может, я умный и всё такое..."

                mc "Но не думаю, что это поможет мне победить «Абсолютное зло» или как ты его там назвала."

                scene 6scene (17) with dissolve

                k "Что ж, это было бы правдой, если бы это было {i}всё{/i}, на что ты способен."

                k "Но подумай секунду..."

                scene 6scene (19) with dissolve

                k "Когда мы говорим о людях с бессонницей, мы говорим о людях, которым трудно заснуть."

                k "Это довольно легко лечится медикаментами, и даже в тяжёлых случаях все рано или поздно засыпают."

                k "Но ты — нет. Уже 10 лет ты ни разу не спал. По всем законам биологии ты должен быть мёртв."

                k "Однако ты жив. А значит, остаётся ещё один вопрос:"

                scene 6scene (62) with dissolve

                k "Можешь себе представить, на что способен человек, не спавший десять лет?"

                menu Whatamicapableof:
                    "На что я способен?":

                        mc "Ладно... и на что именно я способен?"

                        scene 6scene (32) with dissolve
                        k "Хм... этого я сказать не могу."
                        mc "(Ого. Ну ты и помощница.)"

                        scene 6scene (77) with dissolve

                        k "Твоя будущая версия себя точно не {i}раскрыла{/i} весь свой потенциал."

                        k "Но даже он смог сделать многое из того, что обычный человек не смог бы, после того как я с ним связалась."

                        menu link:
                            "Связалась?":

                                scene 6scene (51) with dissolve

                                mc "Ты сказала, что {i}связалась{/i} с будущей версией меня?"


                                k "Да, чтобы человек раскрыл свои потенциальные силы, он должен быть духовно связан со своим фамильяром."


                                mc "Ладно, и... как мне это сделать?"

                                scene 6scene (57)
                                with dissolve

                                k "Это не так просто."

                                k "Это должно быть нечто, чему твоя душа полностью себя посвятит. Только тогда ты сможешь связаться со мной."

                                mc "(Звучит зловеще...)"

                                jump AnyQuestions
            "Травма?":



                scene 6scene (17) with dissolve

                mc "Ты постоянно говоришь про травму..."

                mc "Но я не помню, чтобы со мной случалось что-то плохое..."

                mc "Я знаю, что мои родители и сестра погибли, но...{w}я даже не знаю, что случилось..."


                scene 6scene (19) with dissolve

                k "Хмм, будущая версия тебя тоже не знала."

                k "Я предполагаю, что ты мысленно похоронил то, что с ними случилось, чтобы не переживать горе."

                menu:
                    "ПОХОРОНИЛ?!":

                        scene 6scene (19) with hpunch

                        mc "Похоронил!?"


                        mc "Похоронил!?"


                        mc "То есть ты говоришь, что с ними могло случиться что-то плохое, и я заставил себя это забыть?!"

                        scene 6scene (18) with dissolve

                        k "Это вполне возможно..."

                        k "Ты сумел подсознательно не давать себе спать целых 10 лет."

                        scene 6scene (33) with dissolve

                        k "Но не переживай, если дело в этом…"

                        k "По мере того как ты будешь становиться сильнее, ты, возможно, сможешь вспомнить, что случилось."

                        jump AnyQuestions
            "Не-а.":

                jump scene_5p2












    label scene_5p2:

        scene 6scene (27) with dissolve

        mc "Ну, может, ещё один."
        scene 6scene (28) with dissolve

        mc "Как именно ты собираешься меня тренировать?"

        scene 6scene (35) with dissolve

        k "Кекекекеке."

        mc "Ты над чем вообще смеёшься?"

        scene 6scene (36) with dissolve

        k "Ну, технически, тренировать себя будешь ты сам."

        k "Твоя травма уже тщательно отполирована."

        scene 6scene (16) with dissolve

        k "Так что единственное, что осталось — укрепить твою связь с людьми."
        mc "Что значит «моя связь с людьми»?"

        scene 6scene (35) with dissolve
        k "Кекекекеке."

        scene 6scene (60)
        with hpunch

        mc "Может, хватит уже, блин, ржать, и просто скажешь?"

        scene 6scene (62) with dissolve

        k "Господи, ладно, ладно..."

        k "Ну, если попроще для тебя:"

        k "Твоя травма сама по себе сильна... Но ты можешь стать ещё сильнее, укрепляя связи с людьми."

        scene 6scene (53) with dissolve

        k "Видишь ли, почти у каждого человека есть своё горе."

        k "Хоть оно и разнится по тяжести, почти каждый человек в истории сталкивался с той или иной травмой в своей жизни."

        scene 6scene (54) with dissolve
        k "Когда ты формируешь связь с кем-то другим, вы по сути обмениваетесь частичкой своих переживаний и горя друг с другом."

        scene 6scene (55) with dissolve

        k "В итоге это делает вас обоих сильнее."


        k "И если связь достаточно сильна, ты можешь даже раскрыть потенциал тех, кто связан с тобой. Сделав их такими же сильными, как ты сам."

        scene 6scene (20) with dissolve

        mc "Звучит ещё тупее."

        scene 6scene (39) with dissolve


        k "Это порно-игра, не жди пикового художественного текста."

        scene 6scene (40) with dissolve

        mc "Ты с кем вообще разговариваешь?"

        scene 6scene (41) with dissolve

        k "Не бери в голову."

        k "В любом случае..."

        scene 6scene (34) with dissolve

        k "Твоя будущая версия так и не смогла построить связи, вот почему он потерпел неудачу."

        scene 6scene (35) with dissolve
        k "Так что я помогу тебе найти партнёрш, чтобы помочь тебе стать сильнее."

        scene 6scene (74) with dissolve

        mc "Ладно, кажется, логично."
        mc "{cps=*10}В смысле, если связь — это ключ к силе, то построение отношений—{w=0.1}{nw}{/cps}"
        pause 0.5
        scene 6scene (75)
        mc "ТАК, СТОП, СЕКУНДУ!"

        scene 6scene (76)
        with hpunch

        mc "ТЫ СКАЗАЛА «ПАРТНЁРШИ»?!"

        scene 6scene (35) with dissolve

        k "Кекекекеке."

        mc "Звучит как что-то из дейтинг-симулятора, а не как духовный план роста!"


        scene 6scene (66) with dissolve
        k "{size=-17}О, ты бы не поверил...{/size}"

        k "Эй, твоя аура на травме не расцветёт, если ты будешь дуться в углу. Тебе нужны *связи*, милый."
        scene 6scene (66) with dissolve

        k "Так что для этого..."
        scene 6scene (35) with dissolve

        k "Мы соберём тебе гарем."

        scene 6scene (48) with dissolve
        "Ты закрываешь глаза, пытаясь осмыслить весь этот абсурд."
        "Ну конечно.{w} Почему бы и нет.{w} Само собой.{w} Добавим «эмоционально заряженный квест на свидания» в список моих проблем."

        "Ты чувствуешь, как дёргается висок, пока до тебя доходит весь смысл сказанного."

        scene 6scene (49) with dissolve

        mc "Хех, гарем, значит..."

        scene 6scene (51) with dissolve

        mc "Слушай, собачья тётка."

        k "Лисья."

        scene 6scene (50) with dissolve

        mc "Без разницы."

        scene 6scene (51) with dissolve

        mc "Если ты думаешь, что я вообще смогу разговаривать с девушками, не говоря уже о том, чтобы собрать гарем — тебе не повезло."

        mc "Даже если от этого зависит весь мир."

        mc "Чёрт, ты бы видела меня сегодня, я запаниковал, когда девушка меня схватила."

        scene 6scene (65) with dissolve

        k "О, я видела, ты знатно облажался, хех."


        scene 6scene (66) with dissolve

        mc "Погоди, и как долго ты за мной шпионишь, извращенка?"

        k "Я на это не обижаюсь. Я, по сути, это ты, так что ты оскорбляешь сама себя."
        scene 6scene (18) with dissolve

        k "И я здесь только сегодня. Но, видимо, этого хватило, чтобы увидеть, как ты сам себя опозорил."

        "Твоё лицо краснеет от досады."

        mc "Эй, да пошла ты!"

        mc "Если ты это видела, зачем вообще со мной разговаривать... Ты же должна понимать, я безнадёжен."

        scene 6scene (37) with dissolve

        k "Господи, хватит уже устраивать вечеринку жалости к себе..."

        k "Что бы ты ни думал, ты довольно привлекательный парень."

        scene 6scene (32) with dissolve

        k "В своём таком...{w} жалко-неудачном стиле."
        mc "Ого. Спасибо."

        scene 6scene (36) with dissolve

        k "Нам просто нужно укрепить твою уверенность. Сделать так, чтобы тебе было комфортнее рядом с людьми."

        k "Другими словами..."

        scene 6scene (33) with dissolve

        k "Сделать так, чтобы ты не был мразью."

        scene 6scene (36) with dissolve

        k "К тому же, у тебя есть я и мои силы, чтобы тебе помочь!"

        mc "Магия? Типа какая?"

        k "Ну, дела говорят громче слов, наверное."
        scene 6scene (63) with dissolve

        k "Вот, дай-ка я тебя исцелю."
        "Ты едва успеваешь додумать эту мысль, как она поднимает один палец, и от него исходит сияющий свет."
        scene 6scene (44) with dissolve
        window hide dissolve
        pause 2.0
        play sound "audio/Sound/heal.mp3"
        scene 6scene (45) with flash

        mc "Какого хрена—"

        "Мягкое тепло быстро разливается по всему телу, растворяя каждую боль и синяк, будто их никогда и не было."

        "Вся боль, которую ты чувствовал, исчезла без следа."
        scene 6scene (56) with dissolve

        mc "К-как ты это сделала?"

        k "Ну, легко! Я просто—"

        scene 6scene (57) with dissolve


        k "..."

        k "..."

        scene 6scene (65) with dissolve

        k "Ладно,{w} возможно, я забыла."

        scene 6scene (65) with hpunch

        mc "Что?! Как ты могла забыть?! Ты только что это сделала!"
        scene 6scene (66) with dissolve

        k "Мои воспоминания из будущего, тупица!"

        k "Чем больше я вмешиваюсь в временную линию, тем более размытыми становятся вещи."

        k "А значит, у нас тут время как бы взаймы."

        mc "Отлично... Есть что-то ещё, что тебе стоит мне показать, прежде чем ты окончательно забудешь всё полезное?"

        scene 6scene (62) with dissolve

        k "Хм, ну... Я могу вызывать когнитивную визуализацию стимулов, ориентированных на желания."

        mc "...Что?"

        scene 6scene (64) with hpunch

        k "Это значит, что я могу вот так!"

        "Свет из пальца Кицунэ снова начинает исходить, но на этот раз он куда ярче."

        scene 6scene (58) with dissolve

        mc "{cps=*2}Погоди, что ты дела-{w=0.1}{nw}{/cps}"
        play sound "audio/Sound/possesion.mp3"
        scene 6scene (59) with flash

        mc "иииииииит"
        stop music
        play sound "audio/Sound/Static.mp3"
        scene black with quickflash
        scene 6scene (59) with quickflash
        scene black with quickflash
        scene 6scene (67) with quickflash
        stop sound

        mc "Уф, да что за хрень. Я себя странно чувствую."
        "Ты чувствуешь головокружение, начиная приходить в себя."
        "Ты понимаешь, что лежишь на чём-то вроде цветочной кровати, однако что-то не так."

        mc "Что эта лисья тётка со мной сделала?"
        scene 6scene (68) with dissolve
        mc "И почему у меня ноги так странно себя чувствуют?"
        "Ты заставляешь глаза открыться, моргая от мягкого свечения над тобой."

        mc "....."

        scene 6scene (69) with dissolve

        mc "Погоди..."

        scene 6scene (70) with hpunch
        play music "audio/Music/Jazzy.mp3"

        mc "М-Мина?!"
        "Ты резко просыпаешься окончательно, пока зрение проясняется."

        "Мина сидит сверху на тебе — полностью обнажённая."

        "Твоё сердце замирает. Замешательство, потом возбуждение, потом снова замешательство, нарастая, как волна прилива, обрушивающаяся на твой и без того сбитый с толку мозг."

        mi "Не совсем, но в целом да."

        mc "Что происходит!? Это реально!?"

        mi "Не-а, но ты бы хотел, чтобы было. Именно поэтому это и происходит."

        mc "Погоди, так... это просто моё воображение?"

        scene 6scene (71) with dissolve

        mi "В точку. Но для тебя это ощущается вполне реальным, разве нет?"

        mc "Н-наверное... Пугающе убедительно."
        scene 6scene (70) with dissolve

        mi "Расслабься. Я здесь просто чтобы дать тебе небольшой превью твоих желаний."

        mc "Это... невероятно бесцеремонно, знаешь ли?"

        mi "Ой, да расслабься ты! Это просто твои собственные мысли. Считай это бесплатным пропуском для исследования."

        mc "Ты не особо помогаешь с замешательством..."

        scene 6scene (71) with dissolve

        mi "Эх, ты милый, когда растерян."

        scene 6scene (70) with dissolve

        mi "Ну а теперь..."

        "Мина — или видение, похожее на неё — бросает на тебя лукавую ухмылку."

        mi "Давай разыграем твоё желание, хорошо?"

        scene Flowerscene1 with dissolve

        "Мина медленно начинает двигать бёдрами, нежно вжимаясь в тебя, её тепло полностью окутывает твои чувства."
        "Она издаёт тихий, прерывистый стон, слегка наклоняясь вперёд, задавая размеренный, медленный ритм."

        mi "Ммф... вот так... это так приятно..."

        "Это не ощущается как сон, {i}каждая{/i} часть тебя чувствует {i}всё{/i}."

        "Её движения постепенно ускоряются, дыхание становится тяжелее, а бёдра начинают двигаться более интенсивно."

        mi "Ах... да... вот так... прямо там..."

        scene Flowerscene2 with dissolve

        "Она ускоряется ещё сильнее, теперь двигаясь неистово."
        "Её тело быстро поднимается и опускается на тебе, стоны становятся громче и отчаяннее."

        mi "О боже... да... да... ещё!"

        scene Flowerscene3 with dissolve

        "Её движения становятся лихорадочными, голос наполняется неприкрытой страстью, пока она приближается к пику, бёдра двигаются настойчиво, ногти слегка впиваются в твою кожу."

        mi "Блять! Я сейчас..."

        "Она резко выгибает спину, запрокидывая голову с громким, дрожащим стоном, пока её тело сжимается вокруг тебя, волны удовольствия прокатываются по ней."

        scene 6scene (72) with flash
        pause 0.5
        scene 6scene (72) with flash
        pause 0.5
        scene 6scene (72) with flash
        pause 0.5

        mi "Нгхааа! Нгхааа!"
        stop music
        play sound "audio/Sound/static.mp3"
        scene 6scene (73) with quickdissolve
        scene 6scene (72) with quickdissolve
        scene 6scene (73) with quickdissolve
        scene 6scene (72) with quickdissolve
        scene 6scene (73) with quickdissolve
        play sound "audio/Sound/uhohglitch3.mp3"
        mi "АААААХХХХХХХХХ"

        mi "Уте шражтёчцд мшжесн црнэпус уцчхасн, меиузухнч црузесн црнэпус црейпнсн, н фуужкюекч зкюн, ьчу тнпуийе тк жарн кё, ьчужа йехнчб. Ьчу жа ча тн йкрер… тк йузкхдо рнцш."
        play sound "audio/Sound/static.mp3" 
        scene black with quickflash
        scene 6scene (73) with quickflash
        scene black with quickflash
        scene 6scene (73) with quickflash
        scene black with quickflash
        scene 6scene (73) with quickflash
        stop sound
        play music "audio/Music/Kitsune.mp3"
        scene 6scene (57) with quickflash

        k "Упс! Прости, немного увлеклась."
        scene 6scene (62) with hpunch

        mc "Да что за хрень?!"
        scene 6scene (62) with hpunch

        mc "Ч-что это было?!"

        k "Что было?"

        mc "Ты о чём—"

        mc "О, да ёб твою мать."

        scene 6scene (33) with dissolve

        k "Расслабься, расслабься. Я шучу."

        scene 6scene (35) with dissolve

        k "Обещаю, этот конкретный навык должен закрепиться!"

        mc "Отлично... Уверен, что вызывать случайные сексуальные сны точно пригодится, когда мы будем пытаться спасти мир."

        k "Эй, это всё равно полезнее того, чего ты добился сегодня."

        scene 6scene (38) with dissolve

        k "Ты умудрился травмировать свою новую подругу, а потом получил взбучку от четырёх парней."

        k "Не сказать, что ты показал свою лучшую игру, да?"

        mc "Именно! Может, тебе стоит выбрать кого-то другого в избранные герои. Я явно не подхожу."
        scene 6scene (66) with dissolve

        k "Если бы это так работало, я бы не застряла с тобой, гений."

        k "Я — часть тебя. Я вообще-то не выбираю, чьим фамильяром становлюсь."

        mc "У меня вообще есть выбор в этом бардаке?"
        scene 6scene (33) with dissolve

        k "Конечно!"

        k "Ты можешь либо собраться и спасти мир..."

        k "Либо..."

        k "Ты можешь струсить и смотреть, как ты сам и все, кто тебе дорог, ужасно погибают."

        mc "Восхитительно. Реально заманчивые варианты у тебя тут."

        scene 6scene (34) with dissolve

        k "Господи, хватит быть такой размазнёй. Ты ведёшь себя так, будто уже проиграл, а мы даже не начали."

        mc "Технически мы уже проиграли! Разве не поэтому ты вообще здесь?"

        scene 6scene (19) with dissolve

        k "А, точно..."
        scene 6scene (77) with dissolve

        k "Эх, наверное, всё будет нормально."
        scene 6scene (81) with dissolve

        k "Скорее всего."

        scene 6scene (65) with dissolve

        k "Может, 50 на 50."

        mc "Ты как-то не особо продаёшь мне эту идею с героической судьбой, Кицунэ."

        k "Если честно, думаю, предотвращение конца света само себя неплохо продаёт, дружище."

        scene 6scene (79) with dissolve

        mc "Ага...{w} нет, не особо."

        mc "Ты по сути говоришь, что весь мир зависит от 19-летнего девственника."
        scene 6scene (80) with dissolve

        mc "И его странной духовной собачьей тётки, которая научит его клеить девчонок — и как именно, кстати?"
        play sound "audio/Sound/bong.mp3" volume 1.5
        scene 6scene (82) with hpunch


        k "В ПОСЛЕДНИЙ РАЗ!"

        k "Я НЕ ЁБАНАЯ СОБА-"

        stop music

        play sound "audio/Sound/knock.wav" volume 0.75

        scene 6scene (83)

        a "[mcname]? С кем ты разговариваешь?"

        k "Чёрт..."

        a "Я захожу."

        scene 6scene (84)

        k "Двойной чёрт!"

        scene 6scene (85) with dissolve

        k "Это кто?"

        mc "Эммм, человек, с которым я живу?"

        k "Она не должна знать о моём существовании!"

        mc "В смысле, мне бы даже хотелось, чтобы она тебя увидела, просто чтобы самому убедиться, что я не под наркотой."
        scene 6scene (86) with dissolve

        k "Хватит умничать. Мне нужно превратиться и спрятаться, живо!"

        scene 6scene (88) with dissolve

        play sound "audio/Sound/Flash.wav" volume 0.75

        scene 6scene (89) with flash
        $ renpy.pause (2, hard= True)
        pause 2.0
        scene black with fade

        play music "audio/Music/Nights.mp3" volume 1.0

        scene 6scene (91) with fade
        play sound "audio/Sound/dooropen.wav" volume 1.0

        a "*Зевает*. [mcname], сейчас три часа ночи."
        a "Что происходит? Клянусь, я слышала, как ты с кем-то разговаривал."

        scene 6scene (92) with dissolve

        a "...."
        a "Почему у тебя плюшевая игрушка?"

        scene 6scene (93) with dissolve
        mc "Ох, Отэм. Прости, что разбудил!"
        mc "Извини, наверное, я просто слишком громко включил телек, и я—"

        scene 6scene (95) with dissolve

        mc "Погоди...{w} ты сказала, плюшевая игрушка?"
        scene 6scene (96) with dissolve

        mc "...."

        scene 6scene (97) with dissolve
        window hide dissolve
        pause 2.0
        scene 6scene (98) with dissolve
        mc "Убейте.{w} меня."

        scene 6scene (99) with dissolve
        a "Что ж, раз уж я тут, заодно и поговорим о том, что случилось сегодня."
        "Тишина мучительно растягивается между вами, удушающая и гнетущая. Отэм садится рядом с тобой, в глазах — искренняя тревога и разочарование."

        scene 6scene (102) with dissolve

        a "[mcname], нам нужно поговорить о том, что случилось сегодня с Лили."
        "Сердце грохочет в груди, каждый удар усиливает стыд и досаду."
        a "Я знаю, что в последнее время всё не очень. Богом клянусь, поверь — я вижу это каждый день."

        scene 6scene (101) with dissolve
        a "Но причинять боль кому-то вот так, особенно девушке... это не нормально. Это никогда не нормально."
        "Её голос слегка срывается, и я внутренне вздрагиваю от боли, которую слышу за этими словами."

        scene 6scene (102) with dissolve

        a "Я знаю, тебе тяжело, знаю, ты злишься, но ты не можешь просто продолжать отталкивать всех вот так."
        a "Тебе нужно с кем-то поговорить. Если не со мной, то хоть с кем-то — чёрт, да с кем угодно."

        scene 6scene (104) with dissolve

        "Я кусаю щёку изнутри, пока не чувствую вкус крови."
        "Тяжесть её взгляда невыносима, будто она сдирает слои, которые я годами выстраивал."
        a "Пожалуйста, скажи хоть что-нибудь. Что угодно."

        mc "..."
        scene 6scene (108) with dissolve

        a "[mcname], не закрывайся от меня снова. Я так стараюсь тебе помочь, а ты просто продолжаешь меня отталкивать—"
        stop music
        mc "Хватит."

        scene 6scene (107) with dissolve

        a "Что?"
        "Что-то внутри меня наконец сорвалось, как плотина, не выдержавшая слишком большого давления."

        play music "audio/Music/Run.mp3"
        scene 6scene (105) with hpunch
        mc "Чёрт возьми, Отэм! Я сказал, «хватит!» Я знаю, ты делаешь это только потому, что у тебя в голове есть какой-то идеальный образ меня!"
        mc "Хочешь знать, почему я с тобой не разговариваю? Потому что дерьмо, с которым я разбираюсь — оно моё! Не твоё!"
        "Её глаза расширяются от шока, рот приоткрывается, будто она хочет что-то сказать, но слов не находится."

        scene 6scene (109) with dissolve

        mc "Думаешь, разговоры об этом помогают? Думаешь, мне нравится быть худшим человеком, которого ты знаешь?"
        mc "Новость дня — нет! Каждый долбаный день я чувствую, будто умираю, а ты продолжаешь кидать мне спасательные круги, которые вообще ни хрена не значат."
        mc "Ты понятия не имеешь, насколько я сломан, и, если честно, я не хочу, чтобы ты это знала."
        "Выражение лица Отэм меняется, боль читается в каждой черте. Её голос звучит едва слышным шёпотом, дрожащим и надрывным."
        a "Я... я просто хочу, чтобы с тобой снова всё было хорошо. Я не могу тебя потерять."

        scene 6scene (110) with dissolve

        mc "Ты не помогаешь. Ты...{w} ты не помогаешь."
        mc "Просто...{w} оставь меня в покое."
        "Тишина, что следует за этим, оглушительна, полна недосказанных слов и вновь открывшихся ран."


        scene 6scene (111) with dissolve

        "Отэм сдерживает слёзы. Пытается сохранить самообладание."
        "Ты понимаешь, что это ранило её сильнее всего, что ты когда-либо ей говорил."


        scene 6scene (112) with dissolve

        a "Хорошо. Если ты этого хочешь, я оставлю тебя в покое."
        a "Извини, что я для тебя такая долбаная обуза."


        scene 6scene (113) with dissolve

        "Не говоря больше ни слова, она медленно поворачивается, выходит и тихо закрывает за собой дверь."


        scene 6scene (114) with dissolve

        "Ты выдыхаешь. Ты был слишком резок, но, наверное, весь этот стресс на тебе сказывается."

        stop music fadeout 1.0

        scene 6scene (115) with dissolve

        play sound "audio/Sound/Flash.wav" volume 0.75

        window hide dissolve
        pause 1.0

        scene 6scene (116)
        with flash
        pause 2.0

        k "Уф, я думала, она никогда не уйдёт!"

        scene 6scene (118) with dissolve

        k "Она раздражающая, как ты вообще с этим живёшь?"
        k "Наверное, у неё симпатичное личико, но блин, она вечно лезет в твои дела."

        scene 6scene (123) with dissolve

        "Твои глаза расширяются, ты полностью замираешь от шока. Лицо горит, пока ты пытаешься осмыслить увиденное."
        mc "Эмм."

        scene 6scene (117) with dissolve

        k "Что? Что с тобой не так? Ты выглядишь так, будто увидел—"
        mc "Ты кое-что забыла..."

        scene 6scene (119) with dissolve

        k "...."

        scene 6scene (120) with dissolve

        "Внезапно осознав, что происходит, её уверенное выражение исчезает, сменяясь внезапным румянцем."
        k "О..."

        scene 6scene (124) with dissolve

        mc "Эм... Кицунэ, ты не могла бы магически надеть на себя одежду?"

        scene 6scene (121) with dissolve

        k "Дааа, насчёт этого... я вроде как не помню, как это делать."

        "....."

        mc "(Что за хрень вообще происходит в моей жизни.)"

        scene 6scene (122) with dissolve

        k "Эмм... не могла бы ты принести мне полотенце?"




        scene black
        with fade
        pause 4.0
        play music "audio/Music/sadguitar.mp3" fadein 2.0
        scene autumn6 (1) with dissolve
        window hide 
        pause 2
        scene autumn6 (3) with dissolve
        a "..."
        window hide 
        pause 2
        scene autumn6 (2) with dissolve
        window hide 
        pause 2
        play sound "audio/Sound/flasback.mp3"
        scene autumn6 (4) with flash
        mc "Все рано или поздно отсюда уходят. И мы больше никогда не увидимся. Так что не стоит слишком привыкать к людям."

        a "...Это как-то грустно."

        mc "Грусть — это просто реализм с более паршивым восприятием."

        a "А?"
        scene autumn6 (5) with dissolve
        mc "Не знаю. Просто... люди уходят. Места меняются. Этого не остановить."

        mc "Но я не знаю."
        scene autumn6 (6) with dissolve
        mc "Иногда они что-то после себя оставляют."
        scene autumn6 (7) with dissolve
        a "...Почему ты мне это отдаёшь?"

        mc "Потому что тебе, кажется, холодно. А мне оно особо не нужно."

        mc "Это ведь тоже что-то да значит, разве нет?"
        play sound "audio/Sound/flasback.mp3"
        scene autumn6 (8) with flash

        a "..."
        a "Ты всегда был до жути нигилистичным, да?"
        scene autumn6 (9) with dissolve
        a "Но тогда. Ты хотя бы позволял мне с тобой об этом поговорить."

        a "А теперь это как будто..."
        scene autumn6 (10) with dissolve
        a "Блять."

        a "Я просто хочу, чтобы ты дал мне помочь."
        stop music fadeout 2.0




    label scene_6:




        scene black
        with fade
        pause 4.0

        scene chap1bed with fade

        "Солнечный свет пробивается в твою комнату сквозь полузакрытые жалюзи, будто пытаясь выглядеть артистично."
        "Утро тихое... пугающе тихое."
        "Не той умиротворяющей тишиной. А той, в которой ты просто ждёшь, когда реальность залепит тебе пощёчину."
        "Ты лежишь, глядя в потолок, будто он хранит ответы на все твои тупые поступки."

        show mc_sluggish
        with dissolve

        mc "(Уф... который час?)"
        "Тупая пульсация отдаётся за глазами. Классика."
        "Ты не уверен, устал ли ты, чувствуешь ли вину, эмоционально подавлен, или всё сразу."

        hide mc_sluggish
        show mc_sorry
        with dissolve

        mc "(Отэм...)"
        mc "(Она пыталась быть милой. Поддержать. Что бы то ни было.)"
        mc "(А я, будучи эмоционально недоразвитым идиотом, каким являюсь, фактически откусил ей голову.)"
        mc "(Отличная работа. Прямо блестяще справился с ролью «функционального человека».)"
        "Ты стонешь и проводишь рукой по лицу, будто это как-то отмотает время назад."

        hide mc_sorry
        show mc_sigh
        with dissolve

        mc "(А потом ещё она...)"
        "Ты вспоминаешь голос лисицы. Гладкий. Самодовольный. Пропитанный энергией «я знаю то, чего не знаешь ты»."
        "{i}Твоя аура на травме не расцветёт, если ты будешь дуться в углу.{/i}"
        "{i}Тебе нужны *связи*, милый.{/i}"
        mc "(Ничто так не говорит об эмоциональной стабильности, как нотации от магической лисицы с проблемами в поведении.)"
        mc "(Серьёзно, вся эта затея кажется выдуманной. «Связи»? Будто я какой-то главный герой хентая?)"
        mc "(Следующим делом у меня появятся волосы, закрывающие глаза, и член, закрытый мозаикой цензуры.)"
        "Ты выдыхаешь через нос — где-то между вздохом и смехом."
        mc "(И худшее? Она вообще-то может быть права.)"
        mc "(Не насчёт бредятины с гаремом. Но... может, насчёт всего остального.)"
        hide mc_sigh
        show mc_worried
        with dissolve

        mc "(Похоже, лекарство от моих проблем — формирование глубоких эмоциональных связей. Потому что *это* звучит так просто.)"
        mc "(Никакого давления. Просто судьба всего моего будущего на кону, или типа того.)"
        "Ты слышишь скрип половицы за дверью твоей комнаты."
        "Отлично. Вселенная проснулась. Пора притвориться, что у тебя всё под контролем."

        hide mc_worried
        show mc_thinking
        with dissolve

        mc "(Так что теперь? Пойти в школу и... поговорить с людьми? Постараться не делать всё странным и ужасным?)"
        mc "(Ну да. Потому что *это* у меня в прошлом отлично получалось.)"
        "Ты смотришь на свою форму, будто она принадлежит какому-то незнакомцу. Причём очень скучному."
        "Тишина затягивается. Часы тикают, будто издеваются над тобой."

        hide mc_thinking
        show mc_armedcross
        with dissolve

        mc "(Ладно. Вставай. Извинись перед Отэм. Не будь мудаком. Может, заведи друга-другого. Постарайся не умереть эмоционально.)"
        mc "(Легко.)"
        "Ты не двигаешься."
        "Проходит ещё несколько секунд. Всё ещё не двигаешься."

        hide mc_armedcross
        show mc_sigh
        with dissolve

        mc "....."

        mc "(Это будет ужасно неловко.)"

        hide mc_sigh
        scene black
        with fade


        "Ты наконец вытаскиваешь себя из кровати и принимаешь тот факт, что теперь ты трагичный главный герой малобюджетной инди-драмы."
        "Пол холодный. Свет раздражает. Мозг всё ещё глючит."
        "Но эй, ты стоишь вертикально. Это уже прогресс."

        scene schoolentrance with fade
        pause 2.0

        "Ты приходишь в школу пораньше, наполовину надеясь, что прошлая ночь была стресс-сном от бессонницы и слишком большого количества энергетиков."
        "В глубине души ты уже знаешь правду."
        "А значит, да — самодовольный лисий дух из будущего {i}правда{/i} появился в твоей комнате."
        "И да, она сказала, что твоя душа работает на травме и что тебе нужно собрать гарем, чтобы спасти мир."
        "Естественно, это значит, что твоя и без того проклятая жизнь только что пережила смену жанра."
        "Ты вздыхаешь."
        "Тебе официально не может хоть раз, блин, повезти."




        play music "audio/Music/School.mp3" volume 1.0 fadein 1

        scene 7scene (1) with fade
        window hide
        pause 2.0

        scene 7scene (2) with dissolve
        window hide
        pause 2.0

        scene 7scene (3) with dissolve
        window hide
        pause 2.0

        scene 7scene (4) with dissolve
        window hide
        pause 2.0

        scene 7scene (5) with dissolve

        "Ты заходишь в коридор — и чувствуешь это мгновенно."
        "Взгляды. Десятки взглядов. В основном девчачьи. Все на тебе."
        mc "(Ладно... что за хрень происходит?)"
        mc "(Они пялятся. Шепчутся. Косятся. Это из-за вчерашнего с Лили? Неужели уже так быстро разлетелось?)"

        scene 7scene (6) with dissolve

        mc "(Чёрт. Какой бы социальный статус у меня ни был, он окончательно вылетел в трубу, если они узнали, что я распустил на неё руки.)"
        mc "(Можно попрощаться и с хорошим колледжем. Блин, моя жизнь, считай, кончена.)"

        scene 7scene (7) with dissolve

        "Прежде чем ты успеваешь осознать, насколько ты попал, тебя перехватывают две девушки."

        scene 7scene (9) with dissolve

        "Они выглядят... нервно?"

        g1 "П-привет! Эм, я-я Софи..."
        g2 "А я Сидни! М-мы просто хотели поздороваться..."
        mc "Эм...{w} Привет?"
        mc "(Погодите, разве не эти девчонки вчера полностью игнорировали моё существование?)"
        mc "(Почему они вдруг ведут себя так застенчиво?)"
        mc "(Что за романтическая комедия тут вообще происходит?)"
        g2 "М-мы вот думали, не хочешь ли ты, может... как-нибудь сходить куда-нибудь со мной?"

        scene 7scene (10) with dissolve

        g1 "Ха! Он же имеет в виду *меня*, да? Ты же сначала на меня смотрел!"
        g2 "Что? Да ну нет, я первая заговорила!"

        scene 7scene (11) with dissolve

        "Обе начинают спорить — громко, драматично, будто ты какой-то приз. Ты слишком ошарашен, чтобы шевельнуться."
        mc "(Так, это что-то новенькое... Как вообще реагировать на такую ситуацию?)"
        mc "(У меня ни разу девушка не просила даже карандаш одолжить, не то что не приглашала на свидание!)"
        mc "(Давай, [mcname]. Думай!)"
        mc "(Что бы сделала одна из этих знаменитостей? Они бы выдали крутую цепляющую фразу, да?)"
        "Ты пытаешься вспомнить какие-нибудь из тех фраз-подкатов, что Пьер говорил людям за все эти годы."

        mc "(Ладно, ладно, просто... скажи что-нибудь остроумное. Крутое. Запоминающееся.)"
        scene 7scene (12) with dissolve

        mc "Д-дамы, пожалуйста, успокойтесь."
        mc "Если бы я мог переставить алфавит, я бы поставил тебя и себя рядом."

        scene 7scene (13) with dissolve

        mc "Погодите, не так, я имею в виду мы и...{w} нас?"

        scene 7scene (14) with dissolve

        mc "Я-я имею в виду тебя, меня и... мою кровать?"


        scene 7scene (15) with dissolve
        "..."

        "..."
        scene 7scene (16) with dissolve

        g2 "Можешь его забирать."
        g1 "Нет, он весь твой."

        scene 7scene (17) with dissolve

        g2 "Хочешь просто пойти подсматривать за командой по лёгкой атлетике в душевых?"
        g1 "Больше всего на свете."

        scene 7scene (18) with dissolve

        "Они уходят. На лицах — мгновенное сожаление. Одна из них изображает рвотный позыв."
        mc "...Ага. Логично."
        mc "(Не могу даже нормально поговорить, чтобы не взорвать всю свою социальную репутацию.)"

        scene 7scene (20)
        with flash
        play sound "audio/Sound/Flash.wav" volume 0.75

        scene 7scene (20)
        with hpunch

        k "Это лучшее, что ты смог сделать с усиленным уровнем привлекательности?"
        mc "Ты в моей школе?! Ты спятила?!"

        scene 7scene (22) with dissolve


        k "Расслабься. Я твой фамильяр, помнишь? Я иду туда же, куда и ты."
        k "К тому же мне скучно, а подглядывать за твоей неловкой социальной жизнью — лучшее реалити-шоу, что я видела за века."
        mc "Да как вообще эти девчонки—{w}погоди. Это была *ты*, да?"

        scene 7scene (23) with dissolve


        k "Ммм, может быть. У тебя теперь есть феромоны, милый. Твоё тело излучает достаточно эмоциональной энергии, чтобы привлечь половину женского населения."

        scene 7scene (21) with dissolve


        mc "Было бы неплохо узнать об этом {i}до{/i} того, как я опозорился."
        k "Упс. Наверное, забыла упомянуть, что твоя новообретённая сексуальность идёт в комплекте с нулевыми социальными навыками."

        scene 7scene (23) with dissolve


        k "В любом случае, нам нужно поработать над твоей харизмой, если вся эта затея со спасением мира через гарем должна сработать."
        mc "Никакого «нам». Тебя тут не должны видеть."

        scene 7scene (22) with dissolve



        k "Расслабься. Ещё рано. Никто случайно не завернёт за угол и—"

        scene 7scene (24) with hpunch


        stop music

        u "[mcname]!!"

        scene 7scene (25) with dissolve


        k "...Или, может, кто-то {i}как раз{/i} случайно завернёт за угол и выкрикнет твоё имя."
        mc "Чёрт, она поднимается по лестнице."

        scene 7scene (26) with hpunch

        k "Эй! Что ты делаешь?!"

        mc "Извини, Кицунэ."

        scene 7scene (27) with dissolve

        k "(Приглушённые вопли)"
        "Ты успел спрятать Кицунэ, прежде чем кричавшая твоё имя поднялась по лестнице."

        scene 7scene (28) with hpunch
        "Вот ты где, свинья!"
        "Резкий, знакомый голос прорезает воздух — и у тебя падает сердце."
        play music "audio/Music/Izra.wav" volume 1.0

        scene 7scene (29) with dissolve
        "Передо мной стоит устрашающая фигура со взглядом, который я знаю слишком хорошо."
        mc "О, п-привет, Изра."
        narrator "Изра... сестра Пьера и лучшая подруга Отэм."
        narrator "Как и про остальных, я про неё немного знаю."
        narrator "В основном потому, что она меня слишком сильно пугает."
        I "Даже не смей мне «привет, Изра» говорить, мистер."

        scene 7scene (30) with dissolve
        I "Я слышала о том, что вчера случилось с тобой и Лили."
        I "Если думаешь, что можешь просто ходить и орать на девушек, может, мне стоит преподать тебе урок."

        mc "П-погоди, стой, Изра, кажется, тут какое-то недоразумение."
        mc "Отэм поговорила с Лили, и всё прояснилось! Так что не нужно—"

        scene 7scene (31) with hpunch

        mc "ВАУ!! ЭЙ!!"

        "Прежде чем ты успеваешь хоть как-то среагировать, рука Изры вжимает тебя в стену."
        "Её хватка, что неудивительно, сильная — трудно даже возражать."

        mc "Ва-эм... Изра... ты... д-довольно близко, тебе не кажется?"

        I "Кажется, ты в чём-то ошибаешься, [mcname]."
        I "Ничего не должно было проясняться, потому что вообще ничего не должно было произойти в первую очередь!"
        I "Я не позволю брату моей лучшей подруги доставлять ей проблемы."
        I "И уж тем более не позволю тебе причинять милой Лили какие-либо страдания."

        I "Так что в следующий раз, когда её увидишь, извинишься и как-нибудь загладишь свою вину."
        I "Или, Богом клянусь, я вышвырну твою задницу в это окно, стоит мне до тебя добраться."
        "Странно видеть её такой."
        "Хотя она знакома с Лили всего день, она уже настолько её защищает."
        "Ведёт себя как мать по отношению к ней и к Отэм."
        "Причём очень сильная и страшная мать."
        "Но это уже другой вопрос."

        scene 7scene (32) with dissolve

        k "Нгххх"

        scene 7scene (33) with hpunch


        k "Тц— могла бы предупредить, что собираешься так сделать, придурок!"

        scene 7scene (34) with dissolve

        mc "АГА! Я ТЕБЯ ПОНЯЛ, ЧЁТКО! КРИСТАЛЬНО! ОБЯЗАТЕЛЬНО ТАК И СДЕЛАЮ!"

        scene 7scene (35) with dissolve

        k "(О, ради всего...)"
        k "(Мне что, самой всё делать приходится?)"

        scene 7scene (36) with dissolve


        I "Эм, [mcname], ты в порядке? Ты весь красный."

        scene 7scene (37) with dissolve


        mc "Ч-ЧТО, Я? НЕТ, У МЕНЯ ВСЁ ПРЕКРАСНО!"

        scene 7scene (38) with dissolve


        mc "Я СПОКОЕН! ХОЛОДЕН, КАК ОГУРЕЦ В СНЕГУ!{w} А ТЫ КАК!?"

        scene 7scene (39) with dissolve


        mc "ТАК ЧТО ЭМ, Е-ЕСЛИ БЫ Я МОГ ПЕРЕСТАВИТЬ БУКВЫ В А-АЛФАВИТЕ, Я БЫ-"
        stop music
        play sound "audio/Sound/possesion.mp3" volume 0.6
        scene 7scene (40) with quickflash
        pause 2.0

        scene 7scene (41) with dissolve

        mc "(Погоди—что это бы—)"
        k "(Господи, ты безнадёжен. Дай-ка я порулю секунду.)"
        play music "audio/Music/possesed.mp3"
        scene 7scene (42) with dissolve

        "Внезапно твои нервы исчезают. Тобой овладевает другая энергия."

        scene 7scene (43) with dissolve


        "Одним резким движением ты меняешь расклад."

        scene 7scene (45) with dissolve
        play sound "audio/Sound/thud.mp3" 

        "И теперь уже {i}ты{/i} прижимаешь Изру к стене."

        scene 7scene (46) with dissolve

        I "Ч-что ты, чёрт возьми, делаешь?!"
        mc "Так, погоди-ка секунду, милашка."

        scene 7scene (47) with dissolve
        mc "Теперь, когда меня не давит вес твоей ярости... я смотрю на тебя совсем в другом свете."

        I "Что?! Ну, эм... я, э, эм... Чего-чего?!"

        scene 7scene (48) with dissolve
        mc "Эти острые глаза, этот бескомпромиссный тон, эти милые маленькие пучки на голове..."
        mc "Ты набираешь у меня немало баллов, врать не буду."
        I "Ч-что—{w} я-{w} ты же брат Отэм!"
        mc "Приёмный брат. И расслабься—"
        mc "Я просто ценю то, о чём все остальные слишком боятся сказать вслух."


        scene 7scene (49) with dissolve

        "Ты склоняешь голову набок. Бросаешь ей ухмылку, которая не твоя."
        mc "Ты особенная."
        mc "Эта защитническая жилка. Этот убийственный взгляд. Вся эта энергия «тронешь её — и я тебя закопаю»."
        mc "Это... притягательно."

        scene 7scene (47) with dissolve
        I "Я-я, н-ну, я не"

        "На лице Изры смесь замешательства и смущения."

        mc "Признай это."
        mc "Ты уже думала обо мне раньше."
        mc "Гадала, почему у меня никогда не было девушки."
        mc "Решила, что я слишком странный... или, может, я всегда просто на тебя засматривался?"

        scene 7scene (51) with dissolve
        I "{cps=*2}Ну что ж... я п-польщена, [mcname], но я-{w=0.1}{nw}{/cps}"
        scene 7scene (52) with dissolve
        mc "Шшшшш."
        mc "Больше никаких слов."

        scene 7scene (53) with dissolve
        mc "{cps=*1}Просто позволь этому случиться. Я хочу, чтобы твои губы занялись кое-чем дру-{w=0.1}{nw}{/cps}"

        stop music
        play sound "audio/Sound/bell.wav" 

        scene 7scene (55)
        with hpunch
        window hide dissolve
        pause 2.0

        scene 7scene (54) with dissolve

        mc "Это что за хрень?"
        play sound "audio/Sound/possesion.mp3" volume 0.6

        scene 7scene (55) with flash

        "Вот так вот чары рассеиваются. Тело напрягается. Разум возвращается на место."


        mc "(Какого хрена вообще—что я только что—?)"

        scene 7scene (57) with hpunch
        mc "Ах!"

        mc "Блять! Мне жа- Ах!"

        scene 7scene (58) with hpunch
        mc "М-мне пора! Увидимся позже!"

        "Ты разворачиваешься, будто у тебя ноги горят, и мчишься по коридору."
        "Как будто, если бежать достаточно быстро, она всё забудет."

        scene 7scene (60) with dissolve
        "Изра стоит там же, всё ещё прижатая к стене, моргая."

        I "..."

        scene 7scene (61) with dissolve
        I "Хм."
        scene 7scene (60) with dissolve
        I "..."
        I "(...Мне кажется, или он вдруг стал горячее?)"

        scene 7scene (62) with dissolve
        "..."
        I "Уф.{w} Нет.{w} Абсолютно нет."
        scene 7scene (63) with dissolve
        I "...Наверное."
        I "(Это... был брат Отэм??)"
        I "(Он никогда не говорил со мной так... ни с кем не говорил. Не {i}так{/i}.)"

        scene 7scene (64) with dissolve
        "Изра слегка хмурится, её глаза сужаются — не от злости, а от задумчивости."
        I "(Что бы подумала Отэм, если бы это увидела?)"
        I "(Была бы она рада, что её лучшая подруга встречается с её братом?)"
        I "(А что насчёт Пьера? Они вроде неплохо ладят, он бы поддержал?)"
        scene 7scene (65) with dissolve
        I "(Уф, да что я вообще несу? Я бы никогда с ним не встречалась…)"
        I "(По крайней мере...{w} раньше бы не стала... так что изменилось?)"

        scene 7scene (66) with dissolve

        "Она вдруг смотрит в сторону коридора, по которому ты умчался."
        I "Погоди-ка... разве у нас сейчас не один и тот же урок?"

        I "Да куда он вообще несётся?!"




    label scene_7:

        scene black with fade
        "Ты проводишь весь день, избегая всех."
        play music "audio/Music/Acting.mp3"
        "Ты прячешься по коридорам, ныряешь в пустые классы и даже трижды притворяешься, что завязываешь шнурки, лишь бы уклониться от людей."
        "К моменту финального звонка ты эмоционально опустошён."
        "К моменту финального звонка ты эмоционально опустошён."
        "Но наконец ты находишь местечко перед входом, где можно спрятаться на пару минут."
        scene 8scene (1) with dissolve
        mc "Ладно. Никого рядом."
        mc "Ты выдыхаешь с облегчением, наконец-то можно получить хоть какие-то ответы."

        scene 8scene (2) with dissolve


        "Ты снова оглядываешься и шепчешь себе под нос."


        mc "Кицунэ. Нам нужно поговорить."
        play sound "audio/Sound/Flash.wav"
        scene 8scene (3) with flash

        "Рядом с тобой возникает мерцание."

        "Кицунэ материализуется, будто ждала всё это время."

        k "Долго же ты, гений."

        mc "Что за хрень случилась сегодня утром?!"

        scene 8scene (45) with dissolve

        mc "Почему я—Почему я был—"

        mc "ТЫ ЧТО, ОДЕРЖАЛА МЕНЯ?!"

        k "Дай определение {i}«одержала»{/i}."

        scene 8scene (41) with hpunch

        mc "ТОТ МОМЕНТ, КОГДА ТЫ ЗАЛЕЗЛА МНЕ В УХО!"

        k "Аааа, {i}это{/i}."

        k "Расслабься. Ты тонул хуже дешёвого линкора. Я просто... дала тебе небольшой буст."

        scene 8scene (49) with dissolve

        mc "«Буст»?! Ты угнала моё тело, как краденую машину!"

        k "Технические детали."

        k "Тебе бы спасибо мне сказать. Ты был мёртв в воде. Если бы я не вмешалась, ты бы стал постоянным пятном на ботинке Изры."

        scene 8scene (44) with dissolve

        mc "Я—я прижал её к стене!"

        mc "Я почти—!"

        mc "О боже, я чуть её не поцеловал."

        k "Ага. И ей {i}понравилось{/i}."

        "Твоя душа покидает тело."
        mc "Я умру. Меня убьёт лучшая подруга Отэм и закопает за спортзалом."
        scene 8scene (43) with dissolve

        k "Эй, могло быть и хуже."

        k "По крайней мере, теперь ты знаешь, что способен флиртовать."
        scene 8scene (41) with dissolve

        mc "Я не флиртовал! {i}ТЫ{/i} флиртовала!!"

        k "Семантика."
        scene 8scene (7) with dissolve
        pe "Говорю тебе, чел, Бэтмен с временем на подготовку побеждает всех."
        l "Ладно, а что насчёт Тора? У него нет слабостей, как у Супермена."
        pe "Бэтмен буквально находил способы победить Дарксайда и Брейниака; у Тора нет шансов."
        pe "Он мог бы телепортировать Тора в другое измерение, где вселенная вот-вот закончится, если бы понадобилось."
        l "Ладно, ладно, хорошо... но что насчёт Бэтмена с временем на подготовку..."
        scene 8scene (4) with dissolve
        l "Против другого Бэтмена с временем на подготовку?"
        scene 8scene (6) with dissolve
        pe "..."
        pe "Логан...{w} а это разве не сводит на нет весь смысл сравнения силы?"
        scene 8scene (5) with dissolve
        l "Похоже, ты просто плохой проигрывающий!"
        l "Хотя ничего, Пьер. Моя башковитость иногда даже меня саму пугает."
        scene 8scene (9) with dissolve
        mc "Чёрт—ЧЁРТ!"
        "Ты резко выпрямляешься, глаза широко раскрыты. Ты слышишь, как Пьер и Логан приближаются."

        mc "Только не сейчас. Не сейчас, не сейчас, не—"

        scene 8scene (10) with dissolve

        mc "Кицунэ, СПРЯЧЬСЯ!"

        k "А? Зачем?"

        mc "ПОТОМУ ЧТО Я НЕ ХОЧУ ОБЪЯСНЯТЬ ДРУЗЬЯМ, ПОЧЕМУ Я РАЗГОВАРИВАЮ С СИЯЮЩЕЙ ЖЕНЩИНОЙ-ЛИСОЙ В КОСПЛЕЕ!"

        k "Уф, люди такие драматичные."

        scene 8scene (12) with dissolve
        mc "Может, хватит УЖЕ ГОВОРИТЬ и просто исчезнешь?!"

        k "Ладно, но ты мне должен — снова."
        play sound "audio/Sound/Flash.wav"
        scene 8scene (13) with flash

        "Она взмахивает рукой в воздухе и исчезает в мерцании лисьего огня прямо как—"

        l "Воу, что это была за вспышка?"

        pe "[mcname]?"

        l "Эй, чел! Ты как? Выглядишь так, будто призрака увидел."

        mc "(Чёрт, из всех моментов эти парни выбрали именно сейчас, чтобы меня доставать.)"
        mc "(Надо попытаться сохранить лицо.)"
        scene 8scene (15) with dissolve
        mc "Эм, ага. Просто вышел покурить."
        mc "Вы, наверное, просто вспышку от моей зажигалки увидели, хаха!"
        "Ты внутренне морщишься, издавая один из самых несмешных смешков, что только можно представить."

        scene 8scene (22) with dissolve
        "Похоже, Пьер уловил моё явное смущение. Не то чтобы я хорошо его скрывал."
        pe "[mcname], серьёзно, как ты?"

        l "Ага, чел, ты сегодня прогулял урок."


        mc "Я—эм... ага. Просто нужен был воздух. Ну знаешь, туман в голове. Недосып. Жизнь."

        scene 8scene (19) with dissolve

        pe "Ладно... но ты не просто опоздал. Ты {i}вообще{/i} не появился."

        pe "Я спросил у Отэм, всё ли с тобой в порядке, она выглядела как-то раздражённой. Таким тоном «не спрашивай меня»."

        l "Ага, а я попытался спросить у Изры, и она начала вести себя реально странно. Спотыкалась на словах и всё такое."

        mc "(Наверное, всё ещё отходит от того, что я сказал...)"

        scene 8scene (17) with dissolve

        mc "О, ага, не переживайте, ребят, у меня всё нормально."
        mc "Отэм вечно на меня злится, так что тут ничего нового."
        scene 8scene (16) with dissolve
        mc "Клянусь, со мной ничего необычного не происходит!"
        narrator "Купились они на это?"


        pe "Ага... не куплюсь."
        mc "(Вот же ж хрень.)"
        pe "Слушай, мы, может, не так уж хорошо друг друга знаем, но мне нравится думать, что я неплохо разбираюсь в людях."
        scene 8scene (22) with dissolve
        pe "Так что тебя беспокоит, а? Переживаешь из-за школы? Поругался с Отэм?"
        mc "(Может, в твоей комнате появилась волшебная лисья тётка из будущего?)"
        mc "(Может, эта лисья тётка сказала тебе, что для спасения мира нужно собрать гарем?)"
        mc "(Может, моя сестра ни с того ни с сего начала с тобой флиртовать, хотя раньше едва признавала твоё существование?)"
        mc "(Ого, Пьер, ты правда хорошо разбираешься в людях...)"
        mc "(.....)"
        mc "(Боже, какой же я мудак, он же просто пытается помочь.)"
        mc "(Хотя, не то чтобы я мог рассказать им обоим, что происходит.)"

        scene 8scene (23) with dissolve

        mc "Хех, если бы Отэм со мной поругалась, у меня бы сейчас руки и ноги не хватало."

        mc "Я в порядке, ребят, серьёзно, но спасибо за заботу"

        scene 8scene (24) with dissolve

        mc "Наверное, просто... {w} немного устал-"

        scene 8scene (25) with dissolve

        u "Эй, вы трое!!"

        scene 8scene (26)
        with dissolve

        "Девчонки уже ждут у входа в школу."


        a "Ого, даже не знала, что ты сегодня ещё в школе."

        a "Ты и завтра всех игнорить планируешь, или это было разовое представление?"

        "Её голос лёгкий, но за ним чувствуется острота. Она злится. И не особо это скрывает."

        scene 8scene (27)
        with dissolve

        a "В общем..."

        a "Раз уж ты в последнее время сам по себе, мне просто нужно знать—"

        a "Нормально, если Лили и Изра зайдут сегодня вечером?"

        mc "С-сегодня? Почему? Зачем?"

        a "Ночёвка. Ничего особенного. Просто хочу, чтобы Лили почувствовала себя как дома, и показать Изре новую квартиру."

        scene 8scene (28) with dissolve

        a "Слушай, тебе не обязательно с кем-то разговаривать, мне просто нужно твоё разрешение."


        I "Эм... присоединяйся, если хочешь, однако..."

        "Изра избегает твоего взгляда. Её обычной уверенности как не бывало."

        pe "Блин, так ты сегодня не готовишь? Видимо, буду заказывать еду навынос."

        scene 8scene (29) with dissolve

        mc "(Вот в чём фишка.)"

        mc "(Спросить меня при всех. Я буду выглядеть козлом, если скажу нет. Классический ход Отэм.)"
        mc "(И всё же, сегодня я бы предпочёл провести время с кем угодно, только не с этими тремя.)"

        scene 8scene (30) with dissolve

        mc "(Отэм всё ещё на меня злится, и я её не виню.)"
        scene 8scene (31) with dissolve

        mc "(Изра даже смотреть на меня не может после того, что случилось сегодня утром...)"
        scene 8scene (32) with dissolve
        mc "(А Лили... Ну да. Она теперь меня до смерти боится.)"

        scene 8scene (35)
        with dissolve
        mc "(Бедная девчонка, наверное, травмирована моим присутствием. Удивительно, что она вообще хочет прийти к нам домой.)"
        scene 8scene (37) with dissolve

        "Ты глубоко вздыхаешь — ты планировал сегодня вечером получить больше ответов от Кицунэ. Но не хочешь создавать ещё больше проблем."

        "Наверное, можно подождать, пока они все не уснут."
        scene 8scene (36) with dissolve

        mc "Ладно. Как скажешь."

        mc "Пусть приходят."

        a "...Просто не мешайся сегодня вечером, ладно?"

        scene 8scene (38) with dissolve

        mc "Я и не планировал делать что-то ещё."

        mc "Увидимся завтра, ладно?"


        l "Понял тебя, мешки под глазами!!"

        scene 8scene (39) with dissolve

        I "Вижу, твой брат всё такой же угрюмый, как обычно."

        a "Некоторые вещи никогда не меняются, наверное."

        stop music fadeout 1.0

        scene 8scene (40)
        with dissolve
        window hide dissolve
        pause 3.0
        scene intro 0
        with dissolve
        window hide dissolve
        pause 2

        narrator "Позже той же ночью"
        play music "audio/Music/Sleepover.mp3" volume 1.0 fadein 1



        label scene_8:

        scene 9scene (3) with dissolve

        a "Ну так, что думаете о квартирке?"

        scene 9scene (5) with dissolve
        I "Ты шутишь? Это место потрясающее!"

        L "Д-да... у тебя такая большая комната."

        scene 9scene (4) with dissolve
        a "Хаха, спасибо! Я ещё не всё своё барахло перевезла."

        scene 9scene (6) with dissolve

        I "Хотя времени у тебя явно хватило, чтобы перевезти всё своё скейтерское снаряжение."
        a "Да ладно тебе, Из, ты же знаешь, без него мне никак!"
        L "Оу? Ты катаешься на скейте, Отэм?"
        a "Ещё как! С самого детства."
        a "Мы с Изрой раньше всё время ходили в скейтпарк, когда были маленькими."
        I "Хех, может, нам стоит как-нибудь свозить тебя туда, Лили."
        a "Да, было бы весело! Ты в порядке будешь, после пары разодранных коленок."

        scene 9scene (7) with dissolve

        L "Эммм, может, как-нибудь в другой раз."
        L "В общем?"

        a "Эй, не пытайся сменить тему!"

        scene 9scene (8) with dissolve
        I "Хаха! Удачи с этим, наша малышка Отэм терпеть не может ходить на вечеринки."
        a "Это нечестно! Ты вечно пытаешься подсунуть мне жутких парней на вечеринках!"
        I "Если бы ты поторопилась и завела себе парня, у нас бы не было этой проблемы~"
        scene 9scene (7) with dissolve
        L "Чт-? У тебя никогда не было парня, Отэм?"
        a "Ну, я—эм-"
        scene 9scene (9) with hpunch
        I "Вот именно!? Разве не безумие!?"
        I "Она такая красивая и с ней так весело! Все парни должны за ней бегать!"
        scene 9scene (10) with dissolve
        I "Не говоря уже о том, что у неё огромная грудь!"
        I "Но стоит мне попытаться её с кем-то свести, она их отшивает!"

        scene 9scene (11) with dissolve

        a "Может, хватит уже щипать меня за щёку?"
        I "Ах да, извини."

        scene 9scene (12) with dissolve

        a "Тебе никогда не приходило в голову, что мне, может, нравится быть одной?"
        I "Ой, солнышко... Никому не нравится быть одному."
        L "Изра... разве ты сама не одна?"
        I "Ага, и меня это не радует!"
        scene 9scene (13) with dissolve
        a "К тому же, я отшивала всех тех парней, потому что ни один из них не в моём вкусе..."
        I "Оу? И какой же у тебя вкус тогда, мисс Высокие Запросы?"
        L "Да, мне тоже любопытно."

        scene 9scene (14) with dissolve
        a "Мой вкус?"
        a "Хм... я как-то никогда особо об этом не задумывалась."
        scene 9scene (15) with dissolve
        a "Ну, наверное, мне бы хотелось парня с некоторым классом."
        scene 9scene (16) with dissolve
        a "Ну знаешь, водит на свидания, относится с уважением, всё такое."
        scene 9scene (17) with dissolve
        mc "{i}Эй, дуреха, молоко просрочилось. Сходишь за новым?{/i}"
        scene 9scene (18) with dissolve
        a "Ещё мне бы хотелось парня, который может сам о себе позаботиться."
        a "Кого-то, у кого хорошая гигиена, много хобби, и кто может выглядеть презентабельно."
        scene 9scene (20) with dissolve
        mc "{i} Когда я в последний раз мылся?{/i}"
        scene 9scene (19) with dissolve
        mc "{i}*Нюх* *Нюх*{/i}"
        scene 9scene (21) with dissolve
        mc "{i} Эх, наверное, ещё денёк-другой продержусь.{/i}"
        scene 9scene (22) with dissolve

        a "И, наверное, как бы поверхностно это ни звучало, мне бы хотелось парня с классным телом.."

        scene 9scene (23) with dissolve
        mc "{i}Ээуу! Выйди отсюда, я переодеваюсь!{/i}"

        a "{cps=*1}Красивые белые, мягкие волосы….. .крутые татухи…. Уютные худи….{w=0.1}{nw}{/cps}"
        scene 9scene (24)
        stop music
        I "Отэм?"

        I "Тебе придётся говорить погромче."

        a "……….."
        a "………."
        a "……….."

        I "{cps=*5}...Отэ-{w=0.1}{nw}{/cps}"

        scene 9scene (25) with dissolve

        a "*кхм*"
        a "В общем, как я и говорила, у меня, по сути, нет никакого типа."

        I "{cps=*5}Эй, но ты сказа-{w=0.1}{nw}{/cps}"

        scene 9scene (26) with hpunch

        a "МЫ ИДЁМ ДАЛЬШЕ!"


        scene 9scene (27) with dissolve
        pause 3.0

        scene 9scene (28) with dissolve
        "Лили осторожно поднимает пыльную фоторамку со стола Отэм."

        L "Это... ты и [mcname]?"
        scene 9scene (29) with dissolve

        a "Ага... это было давно."

        "Лили обводит пальцем край рамки, взгляд смягчается."

        L "Вы оба тут выглядите счастливыми. Он даже улыбается."

        "Отэм тихо смеётся, почти с грустью."

        scene 9scene (34) with dissolve

        a "Тогда у него ещё были причины улыбаться."
        scene 9scene (35) with dissolve

        L "Он тогда был другим?"
        scene 9scene (34) with dissolve

        a "Ага. Куда более открытым. Даже игривым. Он раньше рисовал каляки по всей моей домашке, просто чтобы меня позлить."

        a "Теперь он едва разговаривает вообще."
        scene 9scene (34) with dissolve

        "Отэм опускает взгляд, на секунду замолкая."

        a "Мне жаль, что так вышло."

        L "Это не твоя вина—"

        a "Нет. В каком-то смысле моя. Я слишком сильно на него надавила, и он это выместил на тебе."

        scene 9scene (36) with dissolve

        L "Он выглядел окаменевшим, когда я к нему прикоснулась."

        L "Я не ненавижу его, Отэм. Просто... не знаю, как с ним разговаривать."
        a "Если честно? Я тоже не знаю."
        a "Но он не бессердечный, Лили. Он просто... ранен. А раненые люди иногда ранят других."
        a "Я не оправдываю это. Просто объясняю."
        scene 9scene (35) with dissolve
        L "Я понимаю. Бог знает, скольким людям я сама причинила боль..."

        scene 9scene (34) with dissolve
        "Комната на мгновение затихает. Только тихий гул машин за окном заполняет тишину."
        L "Эй, Отэм?"
        a "Да?"
        L "[mcname] когда-нибудь рассказывал тебе, какой у него была жизнь до того, как твоя мама его усыновила?"

        scene 9scene (31) with dissolve

        a "Хмм, не особо…"
        a "Он утверждает, что почти ничего не помнит."
        I "Ему ведь было лет 10? Казалось бы, в таком возрасте он должен многое помнить."
        a "Наверное… он, скорее всего, просто не хочет об этом думать…."

        scene 9scene (33) with dissolve

        a "Он не… любит открываться кому-либо о чём-либо."
        a "С тех пор как я его встретила, это я плакалась ему в плечо о своих проблемах, а он никогда не делал того же для меня…"

        scene 9scene (32) with dissolve
        a "Но я уверена, что рано или поздно он это сделает! Это лишь вопрос времени, пока он откроется, да?"

        scene 9scene (40) with dissolve
        I "Эх, не знаю… Может, ему просто нужно выходить в свет и больше общаться."

        I "Он казался вполне «разговорчивым», когда флиртовал со мной сегодня…"

        scene 9scene (41) with dissolve

        I "…...…"
        a "……..."
        L "......"
        a "Ты что….."

        scene 9scene (42)
        with hpunch

        play music "audio/Music/Argument.mp3" volume 1.0

        a "ЧТО???"

        I "ОЙ ОЙ ОЙ ОЙ ОЙ ОЙ!"

        scene 9scene (43)
        with hpunch

        a "ТЫ ФЛИРТОВАЛА С МОИМ ЁБАНЫМ БРАТОМ?!"
        a "КОГДА???"
        I "Я уже сказала-"

        a "ПОЧЕМУ??"
        a "КАК??"
        a "ПОЧЕМУ??"
        I "Эй, Отэм, успокойся! Это было просто-"

        scene 9scene (42)
        with hpunch

        a "УСПОКОИТЬСЯ?! КАК Я ДОЛЖНА ОСТАВАТЬСЯ СПОКОЙНОЙ В ТАКОЙ СИТУАЦИИ?!"
        a "ТЫ НИКОГДА РАНЬШЕ НЕ ПРОЯВЛЯЛА К НЕМУ ИНТЕРЕСА, ТАК ПОЧЕМУ ИМЕННО СЕЙЧАС?!"

        scene 9scene (44) with dissolve

        I "Это была просто безобидная шутка, клянусь!"

        I "Но признай, разве не круто было бы, если б я стала твоей невесткой?"


        scene 9scene (45)
        with hpunch

        a "НЕТ!!"
        I "ОЙ ОЙ ОЙ ОЙ!!!!"

        scene 9scene (46) with dissolve

        I "Но почему нет-то!?"

        a "ПОТОМУ ЧТО Я ТАК СКАЗАЛА!?"
        I "Да блин, ему всё равно рано или поздно придётся с кем-то встречаться. Почему бы не со мной?"

        scene 9scene (48) with dissolve

        a "Я сама решу, на ком он женится!"

        I "Кто вообще сказал что-то про женитьбу?!"
        I "И ты не можешь так делать! Это его право решать!"

        scene 9scene (49) with dissolve

        a "А моё право как его сестры — убедиться, что он женится на правильной женщине!"

        I "О, значит, я недостаточно хороша для твоего брата?!"
        a "Ты сама это сказала, не я!"

        scene 9scene (50) with dissolve
        L "Эм…."

        scene 9scene (51) with dissolve

        L "Пойду-ка я в ванную…."

        scene 9scene (52) with dissolve
        a "Ладно, по коридору налево."
        I "Кричи, если заблудишься, милая!"

        scene 9scene (53) with dissolve

        a "Так, на чём мы остановились?"
        a "А, точно."

        scene 9scene (54) with dissolve

        a "ЕСЛИ ТЫ ЕЩЁ РАЗ ЗАФЛИРТУЕШЬ С МОИМ БРАТОМ, Я ВСЕМ РАССКАЖУ, ЧТО ТЫ БОИШЬСЯ МАТРЁШЕК!"
        I "ЭЙ, ТЫ ЖЕ ОБЕЩАЛА НИКОМУ НЕ ГОВОРИТЬ!"
        scene 9scene (55) with dissolve
        I "И ЭТО БЫЛО ВСЕГО ОДИН РАЗ, И ОНИ СТАНОВИЛИСЬ ВСЁ БОЛЬШЕ, ЛАДНО?!"

        stop music fadeout 2.0
        scene intro 0
        with fade
        window hide dissolve
        pause 2.
        scene 9scene (58)
        with fade
        window hide dissolve
        pause 2.
        play sound "audio/Sound/dooropen.wav"
        scene 9scene (59)
        with dissolve
        pause 3.0
        narrator "*Приглушённые голоса*"
        scene 9scene (60)
        with dissolve

        L "Хмм?"

        window hide dissolve
        pause 2.0

        scene 9scene (64)
        with dissolve

        L "(Это доносилось из комнаты [mcname].)"
        L "(Почему он до сих пор не спит? И с кем он разговаривает?)"

        scene 9scene (61)
        with dissolve


        L "(Наверное, не стоит вмешиваться....)"
        L "(Но...)"

        L "......."

        scene 9scene (62)
        with dissolve
        window hide dissolve
        pause 2.0
        scene 9scene (63)
        with dissolve
        window hide dissolve
        pause 2.0
        scene intro 0
        with fade
        play music "audio/Music/Kitsune.mp3" volume 1.0 fadein 1

        scene 10scene (1) with dissolve
        k "Пффф—колледж? Ты?"

        scene 10scene (3) with dissolve

        mc "Так, это грубо."

        mc "Просто спрашиваю. Я в итоге {i}поступаю{/i} в твоей версии временной линии?"

        scene 10scene (25) with dissolve

        k "Кажется, помню, как ты поступил. Даже купил переоценённые учебники и всё такое."

        k "А потом вылетел где-то в середине второго курса, потому что — вот это шок — перестал ходить."

        scene 10scene (8) with dissolve

        mc "Хех… Да, похоже на правду."

        mc "Я даже не хотел туда идти. Просто это был «следующий шаг», или что-то такое."

        scene 10scene (13) with dissolve

        mc "А что насчёт Отэм?"

        mc "У неё получилось?"


        k "Я….эм…."

        k "Не помню….."

        scene 10scene (11) with dissolve
        mc "Что? Как ты можешь не помнить?"
        k "Потому что та временная линия начинает переставать существовать, а вместе с ней и мои воспоминания."
        scene 10scene (17) with dissolve
        mc "Ну да, я не куплюсь. Что ты от меня скрываешь?"
        scene 10scene (29) with dissolve
        k "*Вздох* Совет на будущее, [mcname]: не трать столько времени, переживая о будущем."
        k "Сосредоточься на том, что мы делаем {i}прямо сейчас{/i}."
        mc "Легко тебе говорить, ты уже прожила будущее."

        scene 10scene (26) with dissolve

        k "Уже не совсем! Я уверена, что события сегодняшнего дня уже кардинально изменили будущее. Так что теперь я в той же лодке, что и ты."

        mc "Ты можешь в этот раз закончить колледж, или стать стриптизёром! Да кто ж его знает!"
        mc "Фантастика…."

        scene 10scene (14) with dissolve
        mc "........"

        scene 10scene (16) with dissolve
        pause 1.0
        scene 10scene (15) with dissolve

        mc "Слушай, насчёт сегодня… С Изрой..."

        scene 10scene (30) with dissolve

        k "Она милашка, да? Тебе определённо стоит добавить её в гаре—"

        scene 10scene (15) with dissolve

        mc "Не надо. Она никогда раньше со мной так не разговаривала. Она едва на меня смотрела раньше."

        mc "И то, что я сделал — это точно был не я."

        mc "Так что... что ты сделала?"

        scene 10scene (25) with dissolve


        k "Как я уже говорила... ты сходил с ума, и я {i}слегка подтолкнула{/i} процесс."

        k "Тебе нужна была уверенность. И пока ты не научишься находить её сам, я тебе её одолжу."

        scene 10scene (27) with dissolve

        k "Пожалуйста."

        mc "То есть всё это — те слова, то, как я прижал её к стене, назвал горячей—"

        mc "Это была ты?!"

        scene 10scene (22) with dissolve


        narrator "Ты сжимаешь кулаки."

        narrator "Ты не знаешь, отчего у тебя сбивается дыхание — от сигарет или от паники."

        k "Расслабься. Думаешь, я могла бы заставить её покраснеть, если бы там уже чего-то не было?"

        scene 10scene (17) with dissolve


        mc "Не может быть. Не может быть, чтобы кто-то вроде Изры чувствовал такое. Она красивая. Устрашающая. Совсем не моего уровня."

        k "Вот как это работает, гений. Моя аура усиливает то, что уже похоронено внутри. Всё, что я сделала — вытащила это на поверхность."

        scene 10scene (15) with dissolve


        mc "Но я же не {i}выбирал{/i} говорить такое! Я даже не знал, что {i}могу{/i}!"

        mc "Я не тот парень, который флиртует в ответ. Я тот парень, что запинается на словах, и его игнорируют."

        scene 10scene (28) with dissolve


        k "Господи Иисусе, хватит уже устраивать вечеринку жалости к себе! Тебя что, убьёт немного верить в себя?"
        mc "Это… легче сказать, чем сделать."

        scene 10scene (26) with dissolve


        k "Не переживай, как только ты со мной свяжешься, у нас будет полно девчонок, влюблённых в тебя по уши."

        scene 10scene (20) with dissolve


        mc "(Вот ещё одна проблема… связать мой дух с Кицунэ, как я вообще это сделаю?)"
        mc "(Она имела в виду связь {i}физически{/i} или {i}метафорически{/i}? Не знаю, нравится ли мне звучание хоть одного из этих вариантов.)"
        mc "Ты уверена, что я на такое способен? Я знаю, что от этого зависит весь мир, но… я не такой человек…"

        scene 10scene (23) with dissolve


        k "Что ж, на это я скажу…"

        scene 10scene (27) with dissolve


        k "Не повезло!"
        k "Мы сделаем из тебя такого человека."

        scene 10scene (30) with dissolve


        k "И, похоже, твой первый шанс это доказать открывается прямо сейчас — вот эта дверь!"
        mc "А?! Ты о чём вообще?!"

        scene 10scene (27) with dissolve


        k "Увидимся позже!"

        play sound "audio/Sound/Flash.wav" volume 0.75

        scene 10scene (33)
        with flash
        window hide dissolve
        pause 2
        scene 9scene22
        with flash

        mc "(Она что, просто меня бросит????)"

        scene black
        with dissolve

        mc "(Впрочем, неважно. Кто это вышел сюда так поздно ночью?)"


        play sound "audio/Sound/dooropen.wav" volume 0.75
        play music "audio/Music/Thetruedark.mp3" volume 1.0 fadein 1

        scene intro 0
        with fade
        window hide dissolve
        pause 2
        scene 10scene (34) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (35) with dissolve
        L "Эм… Привет."
        mc "Лили?"
        L "…...."

        scene 10scene (36) with dissolve


        L "Можно мне тут немного посидеть?"

        scene 10scene (37) with dissolve

        window hide dissolve
        pause 2
        scene 10scene (38) with dissolve

        window hide dissolve
        pause 2
        scene 10scene (39) with dissolve
        "Ты стряхиваешь сигарету и освобождаешь место для Лили."
        scene 10scene (40) with dissolve
        mc "Прошу, ваше величество."

        scene 10scene (41) with dissolve
        L "Благодарю, мой преданный подданный."
        "Лили тихонько хихикает, чего достаточно, чтобы слегка тебя смутить."

        scene 10scene (42) with dissolve
        mc "О, эм, я не пытался—в смысле, я просто дурачился."

        L "Хаха, всё нормально, расслабься."

        scene 10scene (45) with dissolve

        mc "Где остальные девчонки? Уже от них устала?"
        scene 10scene (47) with dissolve

        L "Хаха, не совсем. Они сейчас немного заняты."
        L "Я подумала, что выйду сюда и составлю тебе компанию."
        scene 10scene (49) with dissolve
        mc "Если ты именно поэтому здесь, можешь с тем же успехом вернуться внутрь."
        L "О-о..."
        scene 10scene (50) with dissolve

        k "Что? Нет! Что ты делаешь??"

        scene 10scene (49) with dissolve

        mc "Из меня не очень хорошая компания, если ты ещё не заметила."
        scene 10scene (45) with dissolve
        L "Ничего страшного. Думаю, свежий воздух в любом случае не помешает."

        scene 10scene (57) with dissolve
        "Ты зажигаешь сигарету дрожащей рукой. Пламя на мгновение колеблется, прежде чем разгореться, будто тоже сомневается в твоём решении."
        window hide dissolve
        pause 2
        scene 10scene (58) with dissolve
        window hide dissolve
        pause 2

        "Лили смотрит на тебя с неловким выражением."

        L "Эти штуки тебя убьют, знаешь ли?"

        scene 10scene (59) with dissolve

        mc "Хех, на это и надеюсь."

        scene 10scene (60) with dissolve

        "Ты сразу понимаешь, насколько жалко это прозвучало."

        mc "Эмм, чёрт, извини, это было реально по-дурацки. Я имел в виду—"

        scene 10scene (61) with dissolve

        L "Пфахаха, всё нормально. Мне показалось забавным."
        L "Ты и правда социально неуклюжий, да."
        mc "Спасибо, что напомнила..."

        scene 10scene (48) with dissolve

        L "Слушай, я хотела извиниться за тот день… Мне стоило спросить, прежде чем распускать руки."
        L "Я себя за это корю. Последнее время я на нервах, и, наверное, поэтому среагировала так странно."
        L "Но это не оправдание, и я искренне извиняюсь за то, что перешла эту черт-"
        mc "Почему это ты извиняешься?"

        scene 10scene (49) with dissolve
        L "Что?"

        mc "Ты не сделала ничего плохого, это я на тебя набросился из-за такой глупости."
        L "Но у тебя явно была причина—"
        mc "Нет, не было..."

        scene 10scene (62) with dissolve
        mc "*Вздох*"
        mc "...…."

        scene 10scene (63) with dissolve

        mc "Я не… Я не тот человек, с которым тебе стоит быть рядом, Лили."

        scene 10scene (64) with dissolve
        mc "Я совсем не как Отэм, она из кожи вон вылезет, чтобы завести новых друзей. А я активно избегаю людей."
        scene 10scene (65) with dissolve
        mc "Тебе было бы лучше держаться от меня подальше."
        scene 10scene (67) with dissolve
        mc "Я эгоист, засранец, и я растрачиваю свой потенциал, гния в кровати большую часть дня."
        scene 10scene (66) with dissolve
        mc "Останься подругой моей сестры, она будет прикрывать твою спину всю оставшуюся жизнь. А я просто тебя разочарую, если ты продолжишь пытаться."

        scene 10scene (51) with dissolve
        k "О боже, этот мир обречён."

        scene 10scene (52) with dissolve

        L "…...."
        L "Отэм рассказала мне о твоём детстве. Могу представить, как тебе было тяжело."
        scene 10scene (48) with dissolve
        L "Но не думаю, что это автоматически делает тебя безнадёжным."
        L "Знаешь… меня тоже усыновили..."
        scene 10scene (49) with dissolve
        mc "Правда? Почему?"
        mc "В смысле—чёрт, прости, это был глупый вопрос."

        scene 10scene (53) with dissolve
        L "Всё нормально, я бы предпочла не вдаваться в подробности… Но в какой-то мере, думаю, я тебя понимаю…"
        L "Тяжело привыкать к новой обстановке после чего-то подобного..."
        L "Это меняет то, как ты видишь мир… как ты видишь окружающих людей."
        scene 10scene (54) with dissolve
        L "В то же время жизнь — это то, что ты из неё делаешь, понимаешь?"
        L "Если ты загоняешь себя в рамки из-за того, как паршиво тебе было в прошлом, ты никогда не вырастешь."
        scene 10scene (52) with dissolve
        L "До Отэм и Изры у меня толком не было друзей. Я… боялась, что люди сблизятся со мной, а потом снова исчезнут."
        L "У тебя хотя бы всегда была Отэм; у меня никогда не было брата или сестры, с кем можно было поговорить, понимаешь?"
        scene 10scene (48) with dissolve
        L "Я ушла из старой школы, потому что дети постоянно надо мной издевались, может, я это заслужила, не знаю."
        scene 10scene (54) with dissolve
        L "Но я хочу дать своей жизни новый старт!"
        L "У нас последний учебный год, я говорю: забудь о прошлом и стремись стать лучшей версией себя."
        mc "......"
        scene 10scene (53) with dissolve
        L "Или что-то в этом роде, хаха..."
        mc "Ты потрясающая."
        scene 10scene (49) with dissolve
        L "А? Откуда это вдруг?"
        mc "От той чертовски потрясающей речи, что ты мне только что толкнула!"
        scene 10scene (53) with dissolve
        L "О… спасибо. Это было ерундой."
        scene 10scene (68) with dissolve
        mc "Так, если тебя усыновили, в каком приюте ты была?"
        L "Я была в том, что на{nw}"
        $ renpy.music.set_volume(0.01)
        scene 10scene (69)
        $ renpy.pause(4, hard=True)
        scene 10scene (70)
        $ renpy.pause(3, hard=True)
        $ renpy.music.set_volume(1.)
        scene 10scene (68)
        mc "Да ладно! Я был в том же самом!"
        L "О ничего себе, серьёзно? Видимо, мы просто разминулись."
        L "Тесен мир, что тут скажешь!"
        mc "Не то слово!"
        scene black with fade
        $ renpy.pause(1, hard=True)
        scene 10scene (44) with dissolve
        with fade
        window hide dissolve
        pause 5
        "Проходят часы, и ты замечаешь, что присутствие Лили нравится тебе всё больше и больше."
        scene 10scene (71) with dissolve
        "Однако становится ясно, что темы для разговора у вас заканчиваются."
        $ renpy.pause(2, hard=True)
        scene 10scene (68) with dissolve

        L "Ого... тут правда холодно…"
        mc "Да... есть такое..."

        scene 10scene (72) with dissolve
        window hide dissolve
        pause 5
        $ renpy.pause(2, hard=True)
        scene 10scene (73) with dissolve
        mc "(Давай уже, обними её за плечи.)"

        scene 10scene (74) with dissolve

        L "(Ну давай уже, обними меня за плечи.)"

        scene 10scene (75) with dissolve

        k "(Ты когда-нибудь замечал, что и бетон, и стекло в основном состоят из песка, а значит, небоскрёбы — это просто очень высокие песочные замки?)"

        scene 10scene (76) with dissolve

        k "(В смысле…)"

        scene 10scene (77)
        with hpunch

        k "Быстро обними её, блин, за плечи!"

        scene 10scene (78)

        play sound "audio/Sound/bong.mp3" volume 1.0

        L "Ты что-то слышал?"

        scene 10scene (79) with dissolve

        L "Готова поклясться, я только что слышала, как кто-то сказал что-то про плечо и руку."

        mc "АХАХА, ДОЛЖНО БЫТЬ, ВЕТЕР ИЛИ ЧТО-ТО ТАКОЕ!"

        scene 10scene (80)
        with hpunch

        mc "ЭМ... ВОТ, МОЖЕШЬ ВЗЯТЬ МОЮ ТОЛСТОВКУ, ЧТОБЫ СОГРЕТЬСЯ!"


        play sound "audio/Sound/Hoodie.wav" volume 1.0

        scene intro 0
        with fade
        window hide dissolve
        pause 2
        pause 2
        "Ты стягиваешь толстовку и протягиваешь её Лили."
        "Она ей до нелепого велика, но от этого выглядит только милее."
        scene 10scene (81) with dissolve
        L "Ой, эм... спасибо, хаха..."
        L ".….."

        scene 10scene (82) with dissolve
        L "Эй, странный вопрос, но…"
        L "Ты когда-нибудь переживаешь из-за будущего?"
        mc "Пффт, да только постоянно? А ты?"
        scene 10scene (84) with dissolve
        L "Да… Я знаю, это неизбежно, но... меня пугает наблюдать, как я взрослею."
        L "Мне почти 19, я больше не могу полагаться на то, что я ребёнок."
        L "Скоро мне придётся идти в колледж или искать работу… Это волнующе, но одновременно и жутко."
        scene 10scene (82) with dissolve
        L "И не приведи господи найти парня, чтобы выйти замуж и завести семью…"
        L "В смысле, кто вообще захочет провести остаток жизни с такой раздражающей, как я."
        scene 10scene (83) with dissolve
        mc "Хаха, ну, у тебя ещё полно времени, чтобы разобраться в себе."
        mc "Я не особо помню свою родную семью, но моя биологическая мама всегда говорила мне и сестре одну вещь…"
        mc "«В конце концов всё будет хорошо. А если не хорошо — значит, это ещё не конец»."
        scene 10scene (82) with dissolve
        L "Хмм, звучит как довольно мудрая женщина."
        mc "Ага…{w} думаю, так и было"
        scene 10scene (83) with dissolve
        mc "И не думаю, что у тебя возникнут проблемы с тем, чтобы найти кого-то, кто захочет на тебе жениться."
        mc "Чёрт, если судить по последним паре часов, я бы не отказался провести остаток жизни с тобой, какой бы раздражающей ты ни была."
        scene 10scene (87) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (86) with dissolve

        L ".....…."
        mc "Лили?"
        L ".....…."
        mc "Всё...{w} в порядке?"
        scene 10scene (85) with dissolve
        L "О-ой, просто я, эмм..."
        scene 10scene (88) with dissolve
        L "Т-ты правда умеешь подбадривать людей!"
        mc "О, спасибо, наверное..."
        scene 10scene (89) with dissolve
        "Почти инстинктивно Лили придвигается к тебе ближе."
        scene 10scene (90) with dissolve
        "Она настолько близко, что ты чувствуешь тепло её дыхания сквозь холодный ветер."
        scene 10scene (91) with dissolve
        L "…...."
        mc "Лили я....."
        "Вы оба достаточно близко, чтобы поцеловаться, и с каждой секундой это становится всё очевиднее."
        "Ты безнадёжно ищешь слова, чтобы разрядить обстановку, прежде чем Лили наконец не находит способ сменить тему."
        scene 10scene (92) with dissolve
        L "Ого, я раньше не замечала, у тебя куча татуировок!"
        scene 10scene (93) with dissolve
        mc "О-эм, да, я их набиваю, сколько себя помню…"
        L "А почему? Они что-то для тебя значат?"
        mc "…...."
        mc "Не, мне в основном просто нравится, как они выглядят…"
        scene 10scene (92) with dissolve
        L "Ты не...{w} против, если я их потрогаю?"
        mc "Ага...{w} Валяй."
        scene 10scene (93) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (94) with dissolve
        $ renpy.music.set_volume(0.0)
        play sound "audio/Sound/static.mp3"
        scene glitch1 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 10scene (94) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch1 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (24) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch1 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (22) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch1 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (23) with quickdissolve
        scene 4scene (22) with quickdissolve
        scene 4scene (24) with quickdissolve
        stop sound
        play ambient "audio/ambient/creatureambien.mp3" volume 0.75
        scene 10scene (95) with quickdissolve
        $ renpy.pause(1.0, hard=True)


        "Ты обнаруживаешь себя сидящим за незнакомым тебе столом."
        "Напротив тебя сидит существо гротескного вида. Тело человеческое, но лицо полностью ненормальное."
        "И всё же ты не чувствуешь страха. Вместо этого ты ощущаешь какое-то тепло, исходящее от её присутствия."
        u "Милый…"
        "Её голос мягкий. Будто она боится тебя напугать."

        scene 10scene (97) with dissolve

        u "Мне сегодня позвонили из школы."
        u "Твоя учительница сказала, что видела, как какие-то мальчишки задирали тебя за спортзалом."
        u "Почему ты мне не сказал?"
        "Ты не говоришь. Не потому что не хочешь. Потому что не можешь. Будто у тебя нет рта."

        scene 10scene (95) with dissolve
        u "Я знаю, это тяжело. Я знаю, это ранит сильнее, чем можно выразить словами."
        u "Но мне нужно, чтобы ты кое-что знал, ладно?"
        u "В тебе нет ничего — *ничего* — плохого."

        scene 10scene (96) with dissolve
        u "Ты добрый. Ты чуткий. Ты глубоко всё чувствуешь. Это не делает тебя слабым. Это делает тебя {i}хорошим{/i}."
        u "Ты носишь так много в своём маленьком сердце, и я просто хочу…"

        scene 10scene (97) with dissolve

        "Её голос срывается."
        u "Я хочу{w} чтобы ты позволил мне нести хоть часть этого вместо тебя."
        "Лицо существа остаётся неизменным, однако его голос и язык тела говорят о том, что оно плачет."

        scene 10scene (95) with dissolve
        u "Ты идеальный маленький мальчик, {chaos}xvyism{/chaos}"
        scene 10scene (96) with dissolve
        u "Однажды кто-то увидит тебя так же, как вижу я."

        u "И останется."

        scene 10scene (98) with dissolve

        u "Дорогой, мне нужна твоя помощь."

        "Из соседней комнаты доносится неузнаваемый голос."

        "Она колеблется, затем отвечает."

        u "Хорошо, милый."
        stop ambient
        play sound "audio/Sound/static.mp3"
        scene glitch2 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 10scene (98) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch2 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 10scene (98) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (24) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch2 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (22) with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene glitch2 with quickdissolve
        $ renpy.pause(0.01, hard=True)
        scene 4scene (23) with quickdissolve
        scene 4scene (22) with quickdissolve
        scene 4scene (24) with quickdissolve
        $ renpy.music.set_volume(1.)
        stop sound
        scene 10scene (99) with quickdissolve
        $ renpy.pause(0.5, hard=True)
        scene 10scene (100) with dissolve
        $ renpy.pause(0.5, hard=True)
        scene 10scene (101) with dissolve
        mc "(Опять видение, значит...)"
        mc "(Что вообще означало это?)"
        scene 10scene (102) with dissolve
        mc "Извини, Лили. Я на секунду отключился-"
        scene 10scene (103) with dissolve
        "Рука Лили всё ещё лежит на твоей руке."
        "Её глаза широко раскрыты… Стеклянные слёзы катятся по щеке."
        mc "Лили? Ты в порядке?"
        L "Ага, а что?"
        scene 10scene (104) with dissolve
        $ renpy.pause(1, hard=True)
        L "О...{w} я даже не заметила, что..."
        scene 10scene (105) with dissolve
        L "Я в порядке, клянусь."
        scene 10scene (106) with dissolve
        L "Наверное, мне стоит вернуться внутрь, не хочу, чтобы остальные девчонки подумали, что у меня проблемы с животом или типа того."
        mc "О, эм..{w} ладно. Ты точно в порядке?"
        scene 10scene (107) with dissolve
        L "В порядке настолько, насколько вообще могу быть. Спасибо, что снова со мной поговорил."
        mc "Да...{w} никаких проблем..."
        scene black with fade
        "Ты желаешь Лили спокойной ночи, прежде чем она уходит внутрь."


        stop music

        stop sound
        play sound "audio/Sound/dooropen.wav" volume 0.75
        scene 10scene (108) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (109) with dissolve
        L "Эй, народ, простите, я заблудилась по пути в-"
        window hide dissolve
        pause 2
        play sound "audio/Sound/bong.mp3" volume 1.0
        scene 10scene (110)

        L "О..."

        scene 10scene (111) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (112) with dissolve

        L "Хм. Видимо, они сами себя вымотали…"

        scene intro 0
        with fade
        window hide dissolve
        pause 2
        play music "audio/Music/Kitsune.mp3" volume 1.0

        scene 10scene (1)
        with hpunch

        k "УХУУУУ!"


        scene 10scene (27) with dissolve

        k "Поверить не могу! У тебя получилось!"
        mc "Получилось что?"
        k "Ты поговорил с девушкой и не был социально неловким!"
        scene 10scene (31) with dissolve

        k "Ты вообще-то был довольно очаровательным, хех."
        k "(Что-то в нём изменилось; это не тот [mcname], которого я знала в своей временной линии.)"
        k "(Подумать только, он смог так вырасти за такое короткое время…)"

        mc "Хм, наверное, и правда получилось... Странно, я даже не задумывался об этом."

        scene 10scene (24) with dissolve

        k "Что ж, может, не думать — это как раз лучший подход к этому делу."


        mc "Да..."
        mc "Да, ты права!!"
        scene 10scene (26) with dissolve
        k "Хехехехе, мне нравится эта новая уверенность. Ты наконец видишь свой истинный потенциал."
        mc "Легко не будет. Но, кажется, у меня и правда может получиться! У нас реально может быть шанс спасти мир!"

        scene 10scene (27) with dissolve

        k "Что ж тогда… Похоже, ты готов сделать это официально!"
        mc "Ты о чём-{nw}"

        play music "audio/Music/reveal.mp3" volume 1.0
        scene 10scene (113) with dissolve

        narrator "Внезапно поведение Кицунэ полностью меняется."
        narrator " Почти так, будто её кто-то одержал."
        k "Твоей божественной силой......"

        play sound "audio/Sound/Beam.mp3" volume 1.0
        scene 10scene (114)
        with flash

        k "Раскрой потенциал этого человека, чтобы он превзошёл свои пределы."
        mc "Погоди, что именно ты делаешь??"
        mc "Это же не будет больно, да?"
        mc "Потому что не на это я подписывал-"

        scene 10scene (115)
        with hpunch

        k "ДА ОБРЕТЁТ ОН ПРИКОСНОВЕНИЕ СИЯНИЯ!"

        stop music
        play sound "audio/Sound/Flash.wav" volume 1.0
        scene 10scene (116)
        with flash
        window hide dissolve
        pause 2
        scene 10scene (117)
        with flash
        window hide dissolve
        pause 2
        scene 10scene (118) with flash
        window hide dissolve
        pause 2
        scene 10scene (119) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (120) with dissolve
        window hide dissolve
        pause 2
        scene 10scene (121) with dissolve

        mc "Что ты со мной сделала?"

        play sound "audio/Sound/burn.mp3" volume 1.0
        scene 10scene (122)
        with hpunch

        mc "Ай! Горячо!"
        scene 10scene (27) with dissolve

        k "Поздравляю, ты официально Сияющий."

        scene 10scene (26) with dissolve

        k "С этого момента тебе суждено сражаться с силами, что противостоят выживанию человечества."
        k "Я, как твой фамильяр, буду помогать тебе на этом пути."
        k "Начнём завтра, так что как следует выспи-"

        scene 10scene (25) with dissolve

        k "Эм….. в смысле."

        scene 10scene (27) with dissolve

        k "Спокойной ночи!"
        play sound "audio/Sound/Flash.wav" volume 1.0
        scene 10scene (33)
        with flash
        window hide dissolve
        pause 2
        scene 9scene120
        with flash
        window hide dissolve
        pause 2
        scene 10scene (124) with dissolve
        mc "Я всё ещё пытаюсь осмыслить то, что произошло за последние пару дней…."
        scene 10scene (123) with dissolve
        mc "Но если вот во что превратилась моя жизнь… Если вот что мне суждено делать……"
        scene 10scene (125) with dissolve
        $ renpy.pause(1, hard=True)
        mc "Тогда будь я проклят, если хотя бы не выжму из этого максимум!"


    label Chapter1Scene1:

        scene intro 0
        with fade
        window hide dissolve
        pause 2
        play sound "audio/Sound/Chapter1.mp3" volume 0.75
        show Chapter_1
        with fade
        pause 5.0
        $ renpy.pause(8, hard=True)
        scene intro 0
        with fade

        $ renpy.pause(3, hard=True)

        scene intro 0 with fade
        pause 1
        stop sound
        play music "audio/Music/jazz.mp3" volume 1.0
        scene chap1bed
        "Свет из окна пронзает твои веки, будто пассивно-агрессивно напоминая, что ты всё ещё жив."
        show mc_dissapointed
        with dissolve
        mc "(Уф...)"

        "Тело ноет. Мысли в тумане. Но больше всего... ты чувствуешь себя странно."

        "Не как «съел что-то странное» странно. Скорее...{w} будто реальность слегка треснула."
        hide mc_dissapointed
        show mc_worried
        with dissolve
        mc "(Та штука с Кицунэ... это правда было, да?)"

        "Ты смотришь вниз на свою руку. Наполовину ожидаешь, что она засветится, или задёргается, или вспыхнет пламенем."

        mc "..."
        hide mc_worried
        show mc_sigh
        with dissolve

        mc "Не-а...{w} всё те же 5 толстых пальцев, что были всегда."

        mc "(Ладно, ну, блин. Наверное, стоит начать с... чем бы там я ни должен заниматься.)"
        scene chap1bed (1) with dissolve

        "Ты подходишь к своему столу, глядя на экран компьютера, всё ещё решая, что спросить."
        scene chap1bed (2) with dissolve

        mc "...."

        "Ты открываешь окно браузера и печатаешь, не задумываясь."
        scene chap1bed (3) with dissolve

        "Ты слегка морщишься от слов на экране, тебя окатывает волна смущения."

        mc "(Ну... может, у Гугла идеи получше, чем у меня на данный момент.)"
        scene chap1bed (4) with dissolve

        "Перерыв все предложения от ИИ и сайты-разводки по саморазвитию, максимум, что ты находишь — общие слова поддержки."

        mc "«{i}Будь собой и будь добрым?{/i}» «{i}Будь открытым и позитивным?{/i}»"
        scene chap1bed (5) with dissolve

        mc "(Ого, это ещё бесполезнее, чем я думал.)"

        "И всё же ты пытаешься через это продраться. Если это должно тебе помочь, надо отнестись серьёзно."
        scene chap1bed (6) with dissolve


        "В одной из статей говорится, что люди, которые чаще улыбаются, кажутся более располагающими."

        mc "(Больше улыбаться, значит...{w}ладно, наверное, стоит над этим поработать.)"

        scene chap1bed (7) with dissolve
        "Ты смотришь на своё отражение через экран компьютера, пытаясь изобразить лучшую улыбку, на какую способен, не выглядя при этом жутко."

        mc "..."
        "У тебя не получается."

        mc "Так, выглядит это жутковато..."
        play sound "audio/Sound/Flash.wav"
        scene chap1bed (8) with flash

        k "Эй, это ты сказал, не я."
        scene chap1bed (8) with hpunch
        mc "Кицунэ?!"

        k "Здарова, засранец."

        scene chap1bed (9) with dissolve
        mc "Господи, тебе надо прекратить меня так пугать."

        k "Может, это {i}тебе{/i} надо перестать быть вечно на нервах."

        k "В любом случае, я бы не стала полагаться на эту технологическую коробку с этим делом."

        k "Если хочешь, чтобы люди тебя реально полюбили, тебе нужен непосредственный опыт."

        mc "....{w}Почему ты назвала это «технологической коробкой»?"

        k "Раздевайся."

        scene chap1bed (10) with hpunch

        mc "...Прости, что?!"

        k "Снимай одежду. Хотя бы верх. Давай, красавчик."
        scene chap1bed (11) with dissolve

        mc "Я—я не буду раздеваться перед тобой! Ты девушка!"
        scene chap1bed (14) with dissolve

        k "О боже, ты кто вообще? Какой-то закомплексованный ребёнок? Я буквально часть тебя."
        scene chap1bed (15) with dissolve

        k "К тому же, ты вчера видел меня голой, так что всё честно."

        scene chap1bed (12) with dissolve

        mc "М-могу я хотя бы узнать, зачем мне раздеваться?"

        k "Потому что твоё тело меняется. Хочешь посмотреть, как ты теперь выглядишь, или как?"
        scene chap1bed (13) with dissolve

        mc "Я в курсе, что такое половое созревание, Кицунэ, мне не нужно демонстрировать волосы на теле или что ты там хочешь увидеть."

        k "Просто сделай это."

        scene black with dissolve

        "Неохотно ты встаёшь и стягиваешь футболку через голову."

        "Ты смотришь на себя."

        scene chap1bed (16) with dissolve

        "Твоё тело выглядит так, будто его отфотошопили для фитнес-журнала."

        "Худощавого телосложения, которое ты знал, больше нет. Вместо него: рельефные мышцы, подтянутая кожа и пресс, которого точно не было 24 часа назад."

        mc "(Какого хрена...)"
        scene chap1bed (17) with dissolve

        k "Говорила же. Твоё тело подстраивается под силу."

        scene chap1bed (19) with dissolve
        k "Если вспомнить твою тощую фигуру меньше 12 часов назад, сразу видно, что процесс идёт бешеными темпами!"

        k "Сейчас это происходит автоматически. Но если хочешь по-настоящему это контролировать, тебе нужно тренироваться."

        scene chap1bed (18) with dissolve

        k "Иначе твоё новенькое симпатичное тело может взорваться, как микроволновка с вилкой внутри."

        mc "...Это же не метафора, да?"

        scene chap1bed (20) with hpunch

        k "Не-а."

        mc "..."

        mc "Пойду приму душ."

        k "Удачи тебе сегодня!"





        scene chap1shower (8) with fade

        "Слабое жужжание старой лампы в ванной смешивается с мягким шипением душа, заполняя воздух тихим гулом."
        "Ты смотришь в зеркало, взгляд прикован к отражению. Капли конденсата стекают по стеклу, размывая контуры лица."
        scene chap1shower (9) with dissolve
        mc "Так, [mcname], сегодня тот самый день. Начало твоей новой жизни... Тебе нужно спасти мир."

        scene chap1shower (6) with dissolve
        mc "Всё, что нужно — это выйти и поговорить с людьми."
        mc "Не так уж и сложно, да?"

        scene chap1shower (5) with dissolve

        mc "Ты справишься!"

        scene chap1shower (10) with dissolve

        mc "Наверное..."

        scene chap1shower (11) with dissolve

        mc "Может быть..."
        mc "..."

        scene chap1shower (12) with hpunch

        mc "Не справлюсь я..."

        scene chap1shower (13) with dissolve

        mc "Нет!"
        mc "Пути назад уже нет..."

        scene chap1shower (14) with dissolve
        mc "*вздох* Глубоко дыши, чел."
        scene chap1shower (16) with dissolve
        pause 1

        scene chap1shower (17) with dissolve
        mc "(Этот шрам... тот, что на шее. Это больше, чем просто отметина. Это напоминание о моей связи с Кицунэ.)"

        scene chap1shower (18) with dissolve
        mc "(Кицунэ... эта напористая, саркастичная и уклончивая заноза в заднице. Как я вообще во всё это вляпался?)"

        scene chap1shower (19) with dissolve
        mc "(Ещё вчера я был обычным парнем, а сегодня у меня загадочный шрам и волшебный лисий дух, называющий меня «Сияющим».)"

        scene chap1shower (2) with dissolve
        mc "(Внутри меня — невообразимая сила. Сила, что рождается из травмы... отлично, как раз то, что мне было нужно.)"

        scene chap1shower (20) with dissolve
        mc "(Она сказала, что мы встретились в будущем, и что я с треском провалился.)"
        mc "(Что в момент моего поражения я попросил её вернуться назад во времени, чтобы тренировать меня. Отличная поддержка уверенности, ничего не скажешь.)"

        scene chap1shower (21) with dissolve
        mc "Но она также сказала, что моя сила исходит от травмы. Чем больше я сближаюсь с людьми, тем сильнее становлюсь."
        mc "Помни, ради чего ты это делаешь. Ради всех, кто тебе дорог. Ради будущего."
        mc "Кицунэ верит в меня, чего бы это ни стоило. Наверное, она видит что-то, чего не вижу я. Может... может, мне тоже стоит попробовать поверить в себя."

        scene chap1shower (3) with dissolve
        mc "Шаг за шагом, [mcname]. Шаг за шагом. Кицунэ на тебя рассчитывает. Мир на тебя рассчитывает."
        mc "Мне нужно как можно скорее начать выстраивать связи с людьми, так что школа — лучшее место для старта."

        scene chap1shower (22) with dissolve

        mc "Может, стоит поговорить с Логаном и Пьером. Они хорошо ладят с людьми, могут помочь мне с разговорами с девчонками."
        mc "Я не справлюсь один. Мне понадобится вся помощь, какую только можно получить."

        scene chap1shower (23) with dissolve

        mc "Я справлюсь."
        mc "Это новый день."
        scene chap1shower (24) with dissolve
        mc "Новое начало"
        mc "Ничто не встанет у меня на пути!"
        $ renpy.music.set_volume(0.01)

        scene chap1shower (25) with dissolve
        window hide dissolve
        pause 1
        scene chap1shower (1) with dissolve
        window hide dissolve
        pause 0.5
        scene chap1shower (26) with dissolve
        window hide dissolve
        pause 1
        play sound "audio/Sound/boowomp.mp3"
        scene chap1shower (27)


        mc "Твою ж мать."
        play sound "audio/Sound/smack.mp3" volume 1

        $ renpy.music.set_volume(1.)

        scene intro 0 with hpunch
        window hide hpunch
        pause 1
        scene chapter1kitchen (4) with dissolve

        L "....."
        I "...."

        scene chapter1kitchen (5) with dissolve

        L "Что не так с лицом [mcname]?"
        I "...Понятия не имею."

        scene chapter1kitchen (2) with dissolve

        a "Новая тату?"
        mc "Ага."

        scene chapter1kitchen (3) with dissolve

        a "Мне нравится."
        a "Тебе идёт."
        mc "Спасибо."

        scene chapter1kitchen (4) with dissolve

        L "....."
        I "...."

        scene chapter1kitchen (6) with dissolve

        L "Так, это неловко."
        L "Так ты скажешь что-то про здоровенный отпечаток ладони у него на лице, или мне сказать?"

        scene chapter1kitchen (7) with dissolve

        I "*Кхм* *Кхм* да заткнись ты *Кхм*"

        scene chapter1kitchen (8) with dissolve

        I "Так, [mcname], когда ты успел набить новую тату?"

        scene chapter1kitchen (9) with dissolve

        mc "О, эм... вчера вечером набил."
        mc "Спонтанное решение."

        scene chapter1kitchen (10) with dissolve

        mc "(В смысле, технически это не ложь, я просто опускаю пару деталей.)"

        scene chapter1kitchen (11) with dissolve

        L "Хм, странно. Я не заметила новую тату, когда мы разговаривали прошлой но-"
        play sound "audio/Sound/prowler.mp3" volume 0.4

        scene chapter1kitchen (14) with fade
        pause 1

        $ renpy.music.set_volume(0.01)

        a "Ты о чём вообще, Лили?"
        I "Ты хочешь сказать, что сбежала с нашей ночёвки, чтобы поговорить с [mcname] прошлой ночью?"
        a "Пожалуйста, расскажи подробнее.."
        I "Да, будь добра."

        scene chapter1kitchen (12) with dissolve

        L "...."

        scene chapter1kitchen (13) with dissolve

        L "Неважно, мне всё это привиделось."

        scene chapter1kitchen (15)
        $ renpy.music.set_volume(1.0)

        a "Отлично! Тогда собираемся в школу!"
        mc "...."
        mc "Что вообще сейчас произошло?"

        scene intro 0 with fade
        window hide fade
        pause 2



        play music "audio/Music/School.mp3" volume 1.0
        scene school with fade
        mc "(После событий этого утра я уже не так уверен во всём этом.)"
        mc "(Надеюсь, Логан и Пьер дадут мне какой-нибудь дельный совет.)"
        mc "...."
        mc "...."
        mc "(Надеюсь, хоть {i}Пьер{/i} даст мне дельный совет.)"
        mc "(Наверное, стоит попытаться их найти до начала урока.)"

        scene chap1school (2) with dissolve
        window hide fade
        pause 1

        pe "....."
        scene chap1school (1) with dissolve

        pe "Так, эм... {w}тихий выдался денёк, да."

        scene chap1school (2) with dissolve
        window hide fade
        pause 1

        pe "....."

        scene chap1school (1) with dissolve

        pe "...Ты слышал, что Smosh, походу, снова воссоединяются?"

        scene chap1school (2) with dissolve
        window hide fade
        pause 1

        pe "....."

        scene chap1school (3) with dissolve

        pe "Да, я не знаю, как к этому относиться."

        scene chap1school (4) with dissolve

        pe "В смысле, ностальгическую часть я понимаю, но это как пытаться заново пережить славные деньки средней школы."
        pe "С тех пор много всего изменилось. И они сами, и их зрители пошли дальше."

        scene chap1school (5) with dissolve

        pe "Попытка Smosh воссоздать свою старую магию может просто выйти натужной и оторванной от реальности."

        scene chap1school (6) with dissolve

        pe "Не знаю, это странно. Я понимаю, что люди в восторге, просто сам как-то не особо, понимаешь?"

        scene chap1school (7) with dissolve

        pe "К тому же, если подумать, их изначальный контент был продуктом своего времени. Интернет, юмор, да и социальные темы — всё изменилось."
        pe "Попытка воспроизвести их старый стиль может сегодня просто не отозваться так же, понимаешь, о чём я?"

        scene chap1school (3) with dissolve

        pe "Типа, зачем нам так зацикливаться на попытках заново пережить кусочки детства, даже когда мы знаем, что они не дотянут до наших сегодняшних стандартов"

        scene chap1school (4) with dissolve

        pe "Мы вообще уверены, что скучаем по самому контенту? Или просто по тому, как этот контент заставлял нас себя чувствовать?"


        scene chap1school (6) with dissolve

        pe "Хотя не знаю, я могу полностью ошибаться, и всё может получиться классно."

        scene chap1school (7) with dissolve

        pe "Просто пытаюсь быть реалистом, наверное."

        scene chap1school (8) with dissolve

        pe "....."

        scene chap1school (9) with dissolve

        l "Да что за хрень такая этот Smosh?"

        scene chap1school (10) with dissolve

        mc "Привет, народ."

        scene chap1school (11) with dissolve

        pe "О, привет, [mcname]. Как оно?"
        l "Йо, мешки под глазами."
        mc "О чём вы тут говорили?"
        l "Ничего важного."

        scene chap1school (12) with dissolve

        pe "Осваиваешься в новом учебном году?"

        scene chap1school (13) with dissolve

        mc "Вообще-то, об этом я и хотел с вами поговорить."

        scene chap1school (14) with dissolve

        mc "У меня небольшие проблемы кое с чем."

        scene chap1school (15) with dissolve

        mc "Думаете... я могу попросить у вас помощи?"

        stop music fadeout 1.0
        scene chap1school (16) with dissolve

        mc "Хм?"
        play sound "audio/Sound/beewel.mp3" volume 0.3
        scene chap1school (17)
        window hide fade
        pause 1

        mc "Эм, ребят?"
        mc "Что с лицами?"

        play music "audio/Music/goof.mp3" volume 1.0
        scene chap1school (20) with hpunch

        l "ЧТО ТЫ СДЕЛАЛ С МЕШКАМИ ПОД ГЛАЗАМИ!?"
        l "НАСТОЯЩИЕ МЕШКИ ПОД ГЛАЗАМИ НИКОГДА БЫ НЕ ПОПРОСИЛИ У НАС ПОМОЩИ!"

        scene chap1school (18) with dissolve

        pe "Погоди, Логан, не будь смешным. [mcname] никто не подменил!"

        scene chap1school (19) with dissolve

        pe "Давай просто сначала его выслушаем. Наверное, что-то по мелочи, типа, узнать, во сколько начинается следующий урок."
        mc "Вообще-то... я тут подумал, не могли бы вы помочь мне получше научиться разговаривать с девчонками-"

        scene chap1school (21) with hpunch

        pe "ЛАДНО, ЧТО ТЫ СДЕЛАЛ С [mcname!u]!?"

        scene chap1school (22) with dissolve

        mc "*вздох*"

        stop music
        play sound "audio/Sound/Smack.mp3" volume 0.75
        scene chap1school (23) with vpunch

        mc "ВЫ ОБА, ХВАТИТ УЖЕ!"

        scene intro 0
        window hide fade
        pause 1
        play music "audio/Music/School.mp3" volume 1.0 fadein 1
        scene chap1school (24) with fade

        mc "Успокоились уже?"
        pe "Хаха, да, всё нормально. Просто удивились, вот и всё."
        l "Извини за такую реакцию, просто мы такого от тебя не ожидали."
        pe "Ага, ты раньше никогда не проявлял интереса к девчонкам."

        scene chap1school (25) with dissolve

        l "Ты мне должен 15 баксов, раз он не асексуал."
        pe "Эй, то, что он хочет разговаривать с девчонками, не значит, что он хочет с ними спать. Есть разница, знаешь ли."
        l "Ты просто так говоришь, потому что знаешь, что проспорил."

        scene chap1school (26) with dissolve

        mc "Господи, ребят, я вообще-то тут стою. Можем сосредоточиться на реальной проблеме на секунду?"
        mc "Погодите...."

        scene chap1school (26) with hpunch

        mc "ВЫ ЧТО, СПОРИЛИ НА МОЮ СЕКСУАЛЬНОСТЬ!?"

        scene chap1school (24) with dissolve

        pe "эмм ты прав [mcname], давай сосредоточимся на реальной проблеме"
        mc "(Я серьёзно пересматриваю свои варианты насчёт помощи.)"

        scene chap1school (28) with dissolve

        mc "Так вы мне поможете или нет?"
        pe "Конечно поможем, чел, мы же друзья."

        scene chap1school (29) with dissolve

        pe "В смысле, я, очевидно, не в той же ситуации, что ты, но я кое-что смыслю в том, что нравится девчонкам в парнях."

        scene chap1school (30) with dissolve

        l "Не переживай, Пьер, я справлюсь."

        scene chap1school (31) with dissolve

        l "Слушай, мешки под глазами, завоевать сердце дамы очень просто."

        play sound "audio/Sound/Swoosh.mp3" volume 0.75
        scene chap1school (32) with hpunch

        l "Нужно просто показать ей свою всепоглощающую любовь к справедливости!"

        scene chap1school (33) with dissolve

        pe "В смысле, он вообще-то отчасти прав, уверенность — ключ к разговору с кем угодно."
        pe "Нам стоит потренироваться на каких-нибудь девчонках, чтобы поднять твою самооценку."

        scene chap1school (36) with dissolve

        l "Не переживай, мешки под глазами, смотри на меня, и я покажу тебе, как настоящий профи разговаривает с женщинами."

        stop music fadeout 1.0
        play ambient "audio/ambient/crowd.mp3" volume 0.75
        scene chap1school (34) with dissolve

        "Прежде чем ты успеваешь ответить, вы все замечаете громкий гомон из собирающейся за углом толпы."
        l "Эй, что там вообще происходит?"

        scene intro 0
        with fade
        play music "audio/Music/Harriet.mp3" volume 0.75

        "Все трое вы заворачиваете за угол, чтобы увидеть причину суматохи."

        scene chap1school (37) with dissolve
        "В центре толпы стоят 3 девушки. Хотя одна из них явно в центре внимания."
        "Ученики смотрят на неё со смесью страха и восхищения."
        mc "Эй, а кто эта девчонка? Почему все ею так восхищены?"
        pe "Чел!! Так нельзя говорить! Это же Харриет Беснос!"
        mc "...."
        mc "Это имя должно мне о чём-то говорить?"
        pe "Она дочь Джеффа Бесноса? Владельца Amazoff?"
        mc "......"
        mc "Всё равно не понимаю, почему это должно останавливать меня от комментариев насчёт её носа."
        pe "ЭТО ТЕБЯ КАСАЕТСЯ, ПОТОМУ ЧТО ОНА МОЖЕТ РАЗРУШИТЬ ВСЕМ НАМ ЖИЗНЬ."

        scene chap1school (47) with dissolve

        pe "Её отец — один из самых богатых людей в мире. Она, по сути, звезда в масштабах школы."
        pe "Каждый парень хочет с ней встречаться, а каждая девчонка — с ней подружиться."

        scene chap1school (37) with dissolve

        mc "Полагаю, это логично, вдобавок к тому, что она богата, она ещё и довольно симпатичная."
        pe "Ага, но есть только одна проблема с тем, чтобы пригласить её на свидание."

        scene chap1school (38) with hpunch
        stop ambient fadeout 2

        "Внезапно из толпы выскакивает ученик и начинает пресмыкаться у ног девушек."
        u "М-мисс Харриет! В-вы самая элегантная и к-красивая девушка, которую я когда-либо видел!"

        scene chap1school (38) with hpunch

        u "ПОЖАЛУЙСТА, ВСТРЕЧАЙТЕСЬ СО МНОЙ!"

        scene chap1school (48) with dissolve

        pe "О нет, бедолага."
        mc "А что не так? В смысле, он был вполне комплиментарен к ней."
        pe "Просто подожди и увидишь."

        scene chap1school (39) with vpunch

        "Тут же обе девушки рядом с Харриет начинают истерически хохотать."
        ga "ХАХАХА, ОГО, ЭТОТ ЛУЗЕР ЧТО, ПРАВДА ТОЛЬКО ЧТО ПОПЫТАЛСЯ ПРИГЛАСИТЬ ХАРРИЕТ НА СВИДАНИЕ!?"
        gb "Давно уже никто не отваживался на такое."

        scene chap1school (119) with vpunch

        h "Боже мой, ты серьёзно? Ты правда думал, что я пойду с тобой на свидание?"
        h "Ты никто. Даже не знаю, с чего ты вообще решил, что у тебя есть шанс. Ты хоть представляешь, кто мой отец? Я могу купить и продать тебя сто раз подряд."

        play sound "audio/Sound/vineboom.mp3" volume 1
        scene chap1school (43) with hpunch
        window hide
        pause 2
        scene chap1school (120)

        h "Тебе стоит просто заползти обратно в ту дыру, откуда ты вылез, и больше никогда не показываться."
        h "Никто бы по тебе не скучал, если б ты исчез. Вообще-то, миру было бы только лучше без таких неудачников, как ты."
        h "Почему бы тебе просто не сделать всем одолжение и не покончить с собой, чтобы исчезнуть навсегда?"

        play sound "audio/Sound/vineboom.mp3" volume 1
        scene chap1school (44) with hpunch
        window hide
        pause 2
        scene chap1school (121)

        h "Плюс Л плюс Рацио плюс тебе никто не даст."

        play sound "audio/Sound/vineboom.mp3" volume 1
        scene chap1school (45) with hpunch
        window hide
        pause 2
        play sound "audio/Sound/deathbell.mp3" volume 1
        scene chap1school (46)
        window hide
        pause 2
        scene chap1school (52) with dissolve

        mc "Блин, этот парень вырубился напрочь."
        pe "Ага, проблема с Харриет в том, что она безжалостна и почему-то точно знает, куда бить, чтобы было больнее всего."
        pe "Она полностью уничтожает волю любого, кто хоть косо на неё посмотрит, не говоря уже о том, чтобы позвать на свидание."
        pe "Вот почему нам нужно избегать её любой ценой."
        pe "Только идиот стал бы специально привлекать её внимание."

        scene chap1school (51) with hpunch
        stop music
        play sound "audio/Sound/bong.mp3" volume 1

        l "ЭЙ, ХАРРИЕТ! Я ТУТ!"

        scene chap1school (53)


        l "ДА, ИДИ СЮДА, К НАМ! РЕБЯТА, КОТОРЫЕ ЖУТКОВАТО ПЯЛИЛИСЬ НА ТЕБЯ ИЗ-ЗА УГЛА!"

        play music "audio/Music/Friends.mp3" volume 1.0
        scene chap1school (54) with dissolve

        pe "*Глубокий вдох*"

        scene chap1school (55) with dissolve

        pe "Что за хрень ты творишь?"

        scene chap1school (56) with dissolve

        l "Расслабься, коротышка, я разберусь."
        l "Я никогда не отступаю перед вызовом, даже если это что-то вроде разговора с девчонками."

        scene chap1school (57) with dissolve

        l "Просто смотри и учись, мешки под глазами."
        l "Я покажу тебе, как настоящий профи флиртует."

        scene chap1school (59) with dissolve

        "Три девушки уже стоят перед вами, прежде чем ты успеваешь вставить слово."
        h "Ты же парень из команды по лёгкой атлетике, да? Чего надо?"

        scene chap1school (57) with dissolve

        l "Ну, мы с друзьями тут как раз разговаривали, и хотели сказать..."

        play sound "audio/Sound/Swoosh.mp3" volume 0.75
        scene chap1school (58) with dissolve

        l "Тебя случайно не Справедливость зовут? Потому что я хочу посвятить свою жизнь служению тебе!"

        scene chap1school (61) with dissolve

        h "....."

        window hide
        pause 1

        h "....."

        scene chap1school (60) with dissolve

        h "Это должно было быть подкатом?"

        scene chap1school (68) with dissolve

        l "Эм, ага, ты не поняла?"
        l "Это вообще-то довольно умно. Знаешь, как справедливость — это что-то реально важное, и люди посвящают жизни её отстаиванию?"

        scene chap1school (69) with dissolve

        l "Фраза, по сути, говорит, что человек настолько потрясающий, что он как сама справедливость."
        l "То есть, я по сути говорю, что хочу посвятить себя-"

        scene chap1school (62) with dissolve

        h "Я поняла. Просто это было не смешно, вот и всё."

        scene chap1school (63) with dissolve

        gb "А по-моему, довольно мило."
        h "Никто не спрашивал твоего мнения, Банни."

        scene chap1school (64) with dissolve

        h "В любом случае, удивительно, что ты настолько прямолинеен, Логан."

        scene chap1school (70) with dissolve

        l "Хаха, ну, я знаю, что я завидный жених и смелее большинства других парней."

        scene chap1school (66) with dissolve

        h "О, ну конечно, и, видимо, ещё и тупее."

        stop music
        scene chap1school (71)
        window hide
        pause 1
        scene chap1school (72) with dissolve

        l "Что?"

        play music "audio/Music/Argument.mp3" volume 1.0
        scene chap1school (65) with vpunch

        h "Ой, прости, Логан, ты ещё и глухой в придачу к тому, что тупой? Позволь сказать максимально просто."
        h "Ты — ходячая шутка. Ты просто мышцы без мозгов, и ты сам это знаешь."
        h "Годишься только чтобы кидать мяч или быстро бегать."

        scene chap1school (73) with dissolve

        l "Э-эй, это как-то не очень—."

        scene chap1school (65) with vpunch

        h "Что? Не мило? Правда обычно и не бывает милой."
        h "Если честно, Логан, тебе стоит просто сдаться. Никто не воспринимает тебя всерьёз, и никогда не будет."

        scene chap1school (66) with vpunch

        h "Ты просто ходячее клише, отчаянно пытающееся доказать, что в тебе есть что-то больше, чем просто мышцы."

        scene chap1school (65) with vpunch

        h "Ты поэтому и тусуешься с этими двумя? Потому что они дают тебе какой-то комплекс превосходства?"
        h "Когда на самом деле ты втайне знаешь, что под этой блаженно-невежественной оболочкой у тебя ничего нет?"

        scene chap1school (74) with dissolve

        l "Ладно, ты доказала свою точку зрения, господи."

        scene chap1school (66) with vpunch

        h "Нет, я докажу свою точку зрения, когда закончу говорить."
        h "Новость дня: ты никто. Ты пустое место, и никто бы по тебе не скучал, если б ты исчез."

        scene chap1school (67) with vpunch

        h "Так почему бы тебе просто не заползти обратно под тот камень, откуда ты вылез, и там и остаться?"
        h "Именно там тебе самое место, если уж говорить откровенно."

        stop music
        play sound "audio/Sound/deathbell.mp3" volume 1
        scene chap1school (75)
        window hide
        pause 2
        $ renpy.pause(4, hard=True)
        scene chap1school (76)
        window hide
        pause 3

        "Логан выглядит таким же коматозным, как и предыдущий парень."

        scene chap1school (77) with dissolve

        pe "Что ж, от него толку не было, да?"

        scene chap1school (80) with dissolve

        pe "Видимо, теперь мне придётся спасать нас из этого бардака."
        pe "Не говори потом, что я для тебя ничего не делаю."

        scene chap1school (81) with dissolve

        pe "*Глубокий вдох*"

        play music "audio/Music/Romance.mp3" volume 1 
        scene chap1school (78) with flash

        pe "Привет, дамы."
        pe "Слушайте, это всё было просто большим недоразумением, так что мы пойдём своей дорогой."
        pe "Почему бы вам троим просто не вернуться к своим делам?"
        pe "Не могли бы вы сделать это ради меня?"

        scene chap1school (82)

        h "Почему ты так одет?"

        stop music
        play sound "audio/Sound/Shatter.wav" volume 1
        scene chap1school (79)

        pe "А?"

        scene chap1school (82)

        h "Почему у тебя под формой худи с галстуком в комплекте?"

        play sound "audio/Sound/boom.mp3" volume 1
        scene chap1school (83)

        h "И эта уродливая серьга тоже не помогает."

        play sound "audio/Sound/boom.mp3" volume 1
        scene chap1school (84)

        h "Выглядит безвкусно."

        play sound "audio/Sound/boom.mp3" volume 1
        scene chap1school (85)

        h "Ты сам выглядишь безвкусно."

        play sound "audio/Sound/deathbell.mp3" volume 1
        scene chap1school (86)
        window hide
        pause 2
        scene chap1school (87) with dissolve

        mc "...."
        mc "Так, это как-то само собой произошло. В смысле, я вообще в этом не участвовал."

        scene chap1school (88) with dissolve

        h "Что ж, странный мальчик с белыми волосами, готов к своей очереди?"

        scene chap1school (89) with dissolve

        mc "У меня же особо нет выбора, да?"

        scene chap1school (90) with dissolve

        h "О, может, ты не такой тупой, как твои друзья."

        h "Определённо уродливее, впрочем, выглядишь как дешёвый статист из фильма про зомби."

        scene chap1school (88) with dissolve

        h "Не говоря уже о том, что у тебя такие впалые глаза, что кажется, будто ты не спал уже несколько дней."
        h "Что? Не спишь всю ночь, размышляя, насколько ненавидишь свою жизнь?"
        h "Или плачешь, потому что знаешь, что ни одна женщина не захочет спать с таким ходячим трупом, как ты."

        scene chap1school (90) with dissolve

        h "Или просто засиживаешься допоздна, репетируя реплики для нового фильма Тима Бёртона?"
        h "Полагаю, называться будет «Жалкий, уродливый кретин, у которого не было ни друзей, ни жизни, и который в итоге сдался и покончил с собой»."

        scene chap1school (91) with dissolve

        mc "...."
        "Будь на твоём месте любой другой парень. То, что только что сказала Харриет, наверное, довольно сильно ранило бы."
        "Однако после стольких лет, когда голоса в твоей голове говорили о тебе вещи и похуже, единственное, чем ты мог ответить, было…"

        scene chap1school (92) with dissolve

        mc "Хех, неплохо."

        scene chap1school (95) with dissolve

        h "...."

        play music "audio/Music/embarrased.mp3"
        scene chap1school (96) with hpunch

        h "ЧТО?????????????????????????"
        "Ты видишь, как вся манера Харриет начинает меняться, будто она смущается."

        scene chap1school (101) with dissolve

        h "Т-ты тупой? Я над тобой издеваюсь, идиот!"

        scene chap1school (100) with dissolve

        h "Ч-что? Отбеливатель из твоей краски для волос уже мозги тебе выжигает, или что?"

        scene chap1school (93) with dissolve

        mc "Хахахаха!"
        "Ты не можешь остановиться от смеха, будто это самая смешная шутка, что ты слышал за годы."

        scene chap1school (94) with dissolve

        mc "Блин, ты уморительна! Тебе никогда не говорили, что тебе бы стендапом заняться?"

        scene chap1school (98) with dissolve

        h "Что?"
        h "Нет!"
        "Ты видишь, как царственное поведение Харриет начинает быстро сдавать позиции, пока она слегка не начинает дрожать."
        "Похоже, она попалась в собственные слова."

        scene chap1school (97) with dissolve

        h "Это не—"

        scene chap1school (99) with dissolve

        h "Т-ты не должен-"

        scene chap1school (102) with dissolve

        h "Уфффф, да забудь!"
        "Харриет уходит прочь в ярости, остальные девушки следуют за ней."

        scene chap1school (103) with dissolve

        h "Запомни мои слова, странный белоголовый мальчишка."

        scene chap1school (104) with dissolve

        h "Никто меня не смущает и не остаётся безнаказанным."

        scene chap1school (105) with dissolve

        "Ты остаёшься скорее озадаченным, чем каким-либо ещё."

        scene chap1school (106) with dissolve
        stop music fadeout 1.
        mc "Хм, она не показалась такой уж плохой."
        mc "И мне показалось, или она правда покраснела?"

        scene chap1school (107) with dissolve
        play music "audio/Music/School.mp3" fadein 1

        l "Только тебе показалось, чел."

        scene chap1school (108) with dissolve

        mc "Правда? Мне казалось, она выглядела довольно-"
        l "Не, извини, чувак, если моё обаяние на неё не подействовало, ничьё не подействует."

        scene chap1school (107) with dissolve

        l "У неё, наверное, просто аллергия на пыльцу была или типа того, бро."

        scene chap1school (109) with dissolve

        l "......"
        mc "......"

        scene chap1school (110) with dissolve

        mc "Блин."
        l "Ой, да не грусти, чел! Ты хотя бы с ней поговорил!"
        l "Пошли на урок, и начнём тренироваться на других девчонках!"

        scene chap1school (111) with dissolve

        l "Да, Пьер?"

        scene chap1school (112) with dissolve
        $ renpy.music.set_volume(0.1)

        l "....."

        scene chap1school (113) with dissolve


        l "Пьер?"
        play sound "audio/Sound/Bong.mp3"

        scene chap1school (114)

        pe "Она назвала меня безвкусным...."
        l "Ой, да ладно, Пьер, ты не можешь принимать её слова близко к сердцу."

        scene chap1school (116) with dissolve

        pe "Идите уже без меня..."
        pe "Тебе не нужна помощь от безвкусного человека…"
        mc "...."

        scene chap1school (117) with dissolve

        mc "О, да блин."
        mc "Если поможешь мне, я как-нибудь свожу тебя за одеждой."

        scene chap1school (118) with hpunch

        pe "ЛАДНО, ДАВАЙ НАЙДЁМ ТЕБЕ ЦЫПОЧЕК!"
        $ renpy.music.set_volume(1.0)
        scene intro 0 with fade
        play sound "audio/Sound/bell.wav" volume 1.0

        scene chap1class (7) with dissolve

        pe "Ладно, [mcname]. У нас есть немного времени до начала урока, и кое-кто уже здесь."

        scene chap1class (3) with dissolve
        pe "Мы с Логаном неплохо знаем большинство местных, так что укажи на каких-нибудь девчонок, и мы тебе всё расскажем."
        mc "Эм, ладно, наверное..."

        pe "Так? О ком хочешь узнать?"

        scene chap1class (6) with dissolve
        menu GirlsClassroom:

            "Девушка с гитарой" if option1 == False:
                scene chap1classbrook with dissolve

                "Что ты знаешь о той девушке вон там?"
                "Бруклин? Немного. Хотя она была у меня в классе пару лет назад."
                "Она всегда будто в своём мире, но я никогда не видел её без гитары."
                "Уверен, с ней будет относительно легко разговориться."
                "Я часто вижу её в школьных коридорах, скорее всего, найдёшь её там большинство дней после уроков."
                $ Brooklyn.quest = "Поговорить с Бруклин на уроке утром."
                $ option1 = True
                jump GirlsClassroom

            "Готка" if option2 == False:
                scene chap1classjune with dissolve

                mc "А что за девушка облокотилась о стену?"
                pe "Её зовут Джун. Насколько я знаю, ей особо никто не нравится."
                l "Она меня как-то пугает!"
                pe "Ага, меня тоже. От неё исходит какая-то тревожная энергия."
                mc "Кто-нибудь из вас пробовал с ней реально поговорить?"
                pe "....."
                l "....."
                mc "Ну да, так и думал. Может, стоит перестать судить книгу по обложке."
                "Блин, если бы никто со мной не разговаривал, судя по энергии, что я излучаю, у меня бы вообще никого в жизни не было."
                pe "Может, ты и прав. Ей бы, наверное, понравилось, если бы кто-то к ней потянулся."
                l "Просто... она всегда выглядит такой неприступной."
                mc "Ну, может, я рискну. Иногда людям, к которым сложнее всего достучаться, друг нужнее всего."
                pe "Удачи тебе с этим. Ты можешь её удивить, а можешь она — тебя."
                l "Эй, мешки под глазами, может, вы с Джун станете страшными готическими корешами!"
                mc "Ты прав, Логан! Можем вместе тренировать страшные лица! Будешь нашим первым подопытным."
                l "Хахаха!"
                l "....."
                l "....."
                l "Ты же шутишь, да?"
                mc "Господи Иисусе...."
                pe "В любом случае, она обычно тусуется за школой, курит, скорее всего, найдёшь её там."
                $ June.quest = "Поговорить с Джун в классе утром."
                $ option2 = True
                jump GirlsClassroom


            "Девушка с телефоном" if option3 == False:
                scene chap1classnorah with dissolve

                mc "А что насчёт девушки, что вечно в телефоне?"
                pe "Это Нора. Она модель, и у неё абсолютно потрясающие глаза. Это её отличительная черта."
                l "Ага, она реально красивая, но вечно сидит в телефоне."
                mc "Думаешь, она будет открыта к разговору?"
                pe "Если честно, если Нора заинтересуется, она сама подойдёт. Она не стесняется делать первый шаг."
                l "Ага, у неё этот гяру-стиль, и она не боится высказывать своё мнение. Она даст знать, если захочет поговорить."
                mc "Звучит пугающе. А если я ей не понравлюсь?"
                pe "Просто будь собой. Она обожает моду, так что если она заметит что-то в твоём стиле, может сама подойти."
                l "Люди часто нервничают, потому что она такая красивая и популярная, но на самом деле она вполне доступна для общения, если заинтересована."
                mc "Ладно, буду иметь в виду. Наверное, просто подожду и посмотрю."
                pe "Именно. Если она захочет поговорить, она даст это понять. Просто будь готов к её прямоте."
                $ Nora.quest = "Представиться Норе в классе утром."

                $ option3 = True
                jump GirlsClassroom



            "Девушка со скетчбуком." if option4 == False:
                scene chap1classmei with dissolve

                mc "А кто та девушка, что рисует вон там?"
                pe "Это Мэй. У неё очень жизнерадостный характер, но она много через что прошла."
                l "Слышал, её брат умер в прошлом году. Довольно ужасная ситуация."
                pe "Ага, она невероятно талантлива, но держится особняком."
                mc "Понимаю, искусство может быть отличным побегом от реальности. Может, найду способ сблизиться с ней через это."
                pe "У неё всегда с собой скетчбук. Я видел некоторые её работы, это потрясающе."
                l "Думаю, она использует искусство, чтобы справляться со всем этим. Ей, наверное, тяжело."
                mc "Может, я спрошу её про рисунки. Может стать неплохим способом начать разговор."
                pe "Просто будь помягче. Она кажется довольно чувствительной насчёт личных вещей."
                mc "Понял. Подойду аккуратно."
                l "Ей, наверное, будет приятно, если кто-то оценит её искусство. Это может много для неё значить."

                $ Mei.quest = "Поговорить с Мэй в классе утром."
                $ option4 = True
                jump GirlsClassroom


            "Футболистка." if option5 == False:
                scene chap1classjordan with dissolve

                pe "Эй, Логан, разве ты не знаешь ту девушку из женской футбольной команды?"
                l "Ага, это Джордин. Она одна из лучших игроков в стране в своём возрасте."
                mc "Спортсменка, значит. Думаешь, стоит поздороваться?"
                l "Конечно! Она супердружелюбная и обожает говорить о спорте."
                l "Но будь готов, она очень напористая и соревновательная."
                mc "Я вообще-то не особо разбираюсь в спорте. Что если ей будет со мной скучно?"
                pe "Просто будь честным. Судя по тому, что я слышал, Джордин классная и ценит людей такими, какие они есть."
                l "Она всегда на тренировках, так что найти её по школе будет несложно, но она любит поговорить обо всём, не только о футболе."
                mc "Спасибо, постараюсь не отставать от её энергии."
                pe "Просто будь собой. У неё энергии хватит на вас обоих."
                mc "Понял."
                $ Jordyn.quest = "Поговорить с Джордин в классе утром."
                $ option5 = True
                jump GirlsClassroom

            "Книжная девушка." if option6 == False:
                scene chap1classella with dissolve

                mc "А кто та девушка, что читает в углу?"
                pe "Это Юки. Настоящий книжный червь и довольно тревожная в общении."
                l "С ней сложно разговаривать, но если постараться, она кажется довольно милой."
                mc "Похоже, ей просто нужно немного поддержки."
                pe "Она может открыться, если увидит, что у вас общие интересы."
                mc "Спасибо, постараюсь быть терпеливым с ней."
                l "По-моему, она в основном сидит в библиотеке, так что попробуй поискать её там после уроков."
                $ Yuki.quest = "Поговорить с Юки в классе утром."

                $ option6 = True
                jump GirlsClassroom

            "Две девушки в центре" if option7 == False:
                scene chap1classriley with dissolve

                mc "А кто те девушки, что разговаривают друг с другом?"
                l "Хм... я их не знаю. А ты, Пьер?"
                pe "Та, с розовыми прядями — Райли. Реально странная, я бы с ней не связывался."
                pe "А вторую девушку... без понятия, кто это, наверное, новенькая."
                pe "Если она разговаривает с Райли, может, уже слишком поздно её спасать."
                mc "Блин, ты говоришь про эту Райли так, будто она прям супер-Гитлер какой-то."
                pe "Она просто странная, чел, она сидит на этих форумах 4chan и вечно говорит какую-то дичь не по делу."
                pe "Не знаю, по-моему, хронически сидеть в интернете — это тревожный звоночек, но решать тебе."
                l "Похоже, тебе всё же придётся поговорить с ней, если хочешь пообщаться со второй девушкой."
                "Несмотря на предупреждения Пьера, обе девушки выглядят весьма симпатично. К тому же, Райли не может быть настолько плохой, да?"
                $ Tamara.quest = "Поговорить с Тамарой и Райли на уроке утром."
                $ Tamara.quest = "Поговорить с Тамарой и Райли на уроке утром."
                $ Riley.quest = "Поговорить с Тамарой и Райли на уроке утром."
                $ option7 = True
                jump GirlsClassroom
            "Трио" if option8 == False:
                scene chap1class (4) with dissolve

                pe "А? Почему тебя интересуют эти трое?"
                mc "Эм... просто любопытно, насколько хорошо вы разбираетесь в теме."
                l "Оооу, ты нас проверяешь? Принимаю этот вызов!"

                scene chap1classtrio with dissolve

                pe "Так... ну, Лили только переехала сюда, так что ты, наверное, знаешь о ней больше, чем мы."
                mc "Да, справедливо. Лили милая, но ещё и очень беззаботная, наверное, поэтому она так хорошо ладит с двумя другими."
                l "То же самое с Отэм, ты явно знаешь о ней больше, раз она твоя сводная сестра."
                l "Но если хочешь понять её в двух словах — она дерзкая пацанка, обожает скейтборд, да?"
                mc "В смысле, это в целом суть. А что насчёт Изры?"

                scene chap1class (8) with dissolve

                pe "...."
                mc "...."

                scene chap1class (9) with dissolve

                mc "Что?"

                scene chap1class (14) with dissolve

                pe "В какую игру ты тут играешь, [mcname]?"
                mc "Я же сказал, мне просто любопытно."
                pe "То есть ты хочешь сказать, что не втюрился в мою сестру?"

                scene chap1class (15) with dissolve

                mc "Что, нет...{w} конечно нет..."

                scene chap1classtrio with dissolve

                pe "*вздох* Ладно, ну, Изра — огненная, прямолинейная и зрелая не по годам."
                pe "Так что лучший способ с ней сблизиться..."
                mc "....ага?"
                pe "Вообще с ней не сближаться."
                pe "Отвали от моей сестры."
                mc "Принято к сведению."

                scene chap1class (1) with dissolve

                "Логан начинает шептать тебе на ухо."
                l "У Пьера есть резон, несмотря на его очевидную предвзятость. У Изры сильный характер, и она не ищет никого, кто сметёт её с ног."
                l "Если ты и правда хочешь с ней сблизиться, просто относись к ней с уважением и не будь своим обычным неловким собой."
                mc "Спасибо, Логан, я твой должник."
                $ Izra.quest = "Поговорить с трио в классе утром."
                $ Lily.quest = "Поговорить с трио в классе утром."
                $ Autumn.quest = "Поговорить с трио в классе утром."

                scene chap1class (2) with dissolve

                l "Ага, ты отдашь мне свои ответы на контрольных до конца года."

                $ option8 = True
                jump GirlsClassroom

            "Девушка в очках." if option9 == False:


                scene chap1classyejin with dissolve

                mc "Эй, а кто та девушка у окна?"
                pe "О, это Йеджин Пак. Она типа вечно первая в потоке. Первое место на каждом пробном экзамене."
                l "Ага… она меня как-то пугает."
                mc "А? Почему?"
                l "Не знаю, чувак. Просто странная атмосфера. Типа, она слишком идеальная. Это неестественно."
                pe "Ты про буквально любого, кто умнее тебя, так говоришь."
                l "Нет! Я серьёзно! В её глазах что-то есть. Будто она что-то скрывает."
                mc "Или она просто... умная?"
                pe "Именно. Она сосредоточенная. Всегда вежливая. Немного холодная, но не грубая или типа того."
                l "Можете смеяться, но говорю вам, в ней есть {i}что-то{/i} не то."
                mc "Может, тебя просто пугают умные девчонки."
                l "Нет! Ладно, может. Но ещё, да ладно, ты хоть раз видел, чтобы она улыбалась? Ни разу. Кто вообще не улыбается?"
                pe "Может, она просто не находит тебя смешным, Логан."
                mc "Так где она обычно тусуется?"
                pe "Я видел, она остаётся здесь после уроков. Может, стоит попробовать там."
                l "Или, знаешь, {i}не надо{/i}, если хочешь остаться в живых."
                mc "Ладно, расслабься. Рискну."
                $ Yejin.quest = "Поговорить с Йеджин на уроке утром"
                $ option9 = True

                jump GirlsClassroom

        $ Utami.quest = "Достичь 5 симпатии у Норы и Зары и подождать до среды."
        $ Parker.quest = "Подождать две недели, затем подождать до понедельника после уроков."
        $ Zara.quest = "Поговорить с Зарой в спортзале после уроков."
        $ Kyra.quest = "Подойти к банде Кайры перед школой."
        $ Grace.quest = "Пойти в левый коридор второго этажа."


        scene chap1class (13) with dissolve

        a "Эй, вы вообще сядете, или так и будете жутко пялиться на всех?"
        mc "(Похоже, это наш сигнал. К счастью, я хотя бы успел выучить имена всех девчонок в классе.)"

        scene chap1class (17) with dissolve

        "Остаток учебного дня прошёл довольно спокойно."

        label Chap1nightroom:

        scene intro 0
        with fade
        stop music fadeout 1.
        play music "audio/Music/Kitsune.mp3" volume 1.0 fadein 1
        "Позже той ночью ты пошёл к себе в комнату поговорить с Кицунэ."

        scene chap1room (51) with dissolve

        k "Так... ты наконец закончил обустраивать комнату..."
        k "Твои постеры примерно такие, как я и ожидала: клише и напускная мрачность."

        scene chap1room (49) with dissolve

        mc "Эй, да пошла ты, я ношу свои увлечения на рукаве...на постерах в комнате, куда никому нельзя входить без моего разрешения."

        scene chap1room (50) with dissolve

        mc "Неважно, хватит об этом. Раз уж ты дала мне этот прикольный символ, ты же теперь начнёшь меня тренировать, да?"

        scene chap1room (53) with dissolve

        k "Такой план, мой болезненный маленький твинк."
        mc "Не называй меня так."

        scene chap1room (5) with dissolve

        k "Сначала нам нужно разобраться с твоей аурой, а потом уже решим, какие тренировки тебе нужны."
        mc "Отлично, полагаю, сейчас будет та часть, где ты объяснишь, что такое аура?"

        scene chap1room (4) with dissolve

        k "Ещё бы!"

        scene chap1room (4) with dissolve

        k "Так, ты уже слышала монолог про сияющих. Люди с силами, бла-бла-бла, судьба, ня-ня-ня, вываливание лора, и так далее."

        scene chap1room (5) with dissolve

        k "Но настоящая суть? Всё дело в твоей ауре, детка."
        k "Цвет говорит всё, что нужно знать о том, каким крутым засранцем ты станешь."
        mc "Ладно, и какой у меня цвет? Полагаю, ты уже знаешь мой цвет из прошлой временной линии."

        scene chap1room (4) with dissolve

        k "Притормози, дружок. Я как раз к этому веду. Сначала давай поговорим о теории."
        k "Смотри, у каждого Сияющего есть аура, связанная с травмирующим событием — как шрам, но, знаешь, куда круче. Это источник твоей силы."
        k "Она может меняться каждый раз, когда ты её пробуждаешь в течение жизни, так что твоя нынешняя аура может отличаться от той, что была у твоей будущей версии."
        mc "О, так вот почему ты решила отправиться к более ранней версии меня?"

        scene chap1room (53) with dissolve

        k "В точку! Ну, это была одна из причин, во всяком случае."
        mc "(О, отлично, это прозвучало вообще не зловеще!)"
        k "Возвращаясь к теме, есть три основных цвета, и каждый много говорит о тебе."
        mc "Три типа? Ладно, выкладывай. Какие они?"

        scene chap1room (1) with dissolve

        k "Смотри сюда."
        play sound "audio/Sound/Flash.wav" volume 0.75
        scene auralore (4) with flash

        "Кицунэ начинает формировать изображение крошечного жёлтого человечка с мечом."
        k "Жёлтый — это Усилители. У них есть хватка... буквально. Всё, к чему они прикоснутся, они могут сделать сильнее. Оружие, броню, что угодно."
        k "Они — качки мира Сияющих."
        mc "(Звучит полезно в бою. И, наверное, превращение в танк — не худший вариант.)"
        mc "Ладно, а остальные?."

        play sound "audio/Sound/Flash.wav" volume 0.75
        scene auralore (8) with flash

        "Затем Кицунэ начинает формировать красного человечка, превращающегося в пламя."
        k "Красный — это Трансмуторы. Они непредсказуемые — могут превращаться в стихии, вроде огня и воды, всё в таком духе."
        k "Правда, ограничены только одной стихией. Может быть что угодно, от огня до крови."
        mc "Я почти уверен, что кровь — это не стихия. Я почти уверен, что это просто...кровь."

        scene chap1room (52) with dissolve

        k "Ага, ну... да пошёл ты, это круто."
        "Примечание автора: да пошёл ты, это круто."
        "Эм чёрт, ладно, теперь снова мысли [mcname]."
        mc "(В любом случае... умение менять форму, похоже, отлично подошло бы для быстрого побега, в зависимости от стихии.)"

        play sound "audio/Sound/Flash.wav" volume 0.75

        scene auralore (6) with flash
        "Последний человечек Кицунэ появляется синим, окружённым сгустками энергии."
        k "Наконец, у нас Синие — они же Заклинатели. Они кукловоды, дёргающие за ниточки стихий."
        k "Призыв бурь, подчинение земли своей воле, всё в таком духе. У них всё дело в контроле, удержании хаоса в узде."
        mc "(Контроль? Зная мою удачу, я в итоге сделаю что-то нелепое, типа подожгу дом.)"
        mc "И… это все типы, да? Или ты что-то от меня скрываешь?"

        scene auralore (7) with dissolve

        k "Не совсем, малыш. Это основные цвета, но иногда вселенной нравится пофантазировать и немного всё перемешать."
        k "Вот тут-то и появляются гибриды. Есть фиолетовые, зелёные, оранжевые — это уже совсем другой уровень."

        scene auralore (6) with flash

        k "Подумай вот о чём: скажем, у тебя есть способность создавать обсидиан. Это один из самых острых материалов в мире, так что ты пытаешься сделать меч."
        k "Знаешь, в чём проблема с этим размышлением?"
        mc "Ты не смогла бы сделать меч, который бы не сломался?"
        k "Динь-динь-динь! Десять баллов Гриффиндвери!"
        k "Хотя обсидиан безумно острый, потому что он, по сути, закалённое стекло, он крайне хрупкий и сломается от первого же удара."
        mc "Ладно, я это уже знал... Как бы я ни ценил факты про камни, к чему ты вообще клонишь?"

        scene auralore (10) with flash

        k "Ну, скажем, у тебя есть ещё и способности усилителя..."
        k "Теперь ты можешь усилить прочность этого обсидианового меча так, чтобы он был крепким, как титан!"
        mc "То есть у тебя было бы одно из самых острых и самых прочных оружий в истории!"
        k "Именно, [mcname]. Я бы дала тебе золотую звёздочку, если бы они у меня были."
        k "Видишь ли, эти силы сами по себе пугающе мощные."

        scene auralore (12) with flash
        play sound "audio/Sound/Flash.wav" volume 0.75

        k "Но вместе они способны сделать тебя неудержимым!"
        mc "(Комбинация? В этом есть потенциал… но звучит и слегка перебором.)"
        mc "Насколько редки гибриды? Кажется, с ними было бы сложно иметь дело."

        scene chap1room (5) with flash

        k "Достаточно редки, чтобы я могла пересчитать тех, кого встречала, по пальцам одной руки. Но если такого встретишь? Ты, выражаясь по-человечески, пропал."
        k "Они мощные, конечно, но ещё и... непредсказуемые."
        k "Вся эта сила, окутывающая тебя — представь, будто пытаешься стрелять из двух пистолетов одновременно."

        scene chap1room (6) with dissolve

        k "Конечно, это намного сложнее, и ты можешь сам себе навредить, но если получится — ты будешь охрененным крутышом."
        mc "(Крутышом, значит? По мне, так больше мороки, чем оно того стоит.)"
        mc "Так… а что насчёт меня? Какая у меня аура?"

        scene chap1room (4) with dissolve

        k "Вопрос на миллион долларов, да? Но вот в чём дело, [mcname] — твоя аура не появится просто так и не скажет «привет»."
        k "Тебе придётся её заслужить, копнуть глубоко и встретиться лицом к лицу с тем, что таится внутри тебя. Только тогда ты увидишь её истинный цвет."
        mc "(Встретиться с тем, что внутри меня? Уф, самокопание. Обожаю. Но если это необходимо... наверное, выбора особо нет.)"
        mc "Ладно. С чего мне начать?"
        scene chap1room (8) with dissolve


        k "С помощью старой доброй медитации. Ну, не совсем."
        k "Сначала вытяни руку вперёд и закрой глаза."

        scene chap1room (10) with dissolve

        mc "Эм, ладно? Вот так?"
        k "Ага, всё верно. Теперь попробуй представить что-то из прошлого, что-то, что вызывает у тебя сильную эмоцию."

        scene chap1room (11) with dissolve

        mc "Ладно, попробую."

        window hide dissolve
        $ renpy.pause(2, hard=True)
        scene chap1room (12) with dissolve
        window hide dissolve
        pause 1.0
        scene chap1room (13) with dissolve

        mc "Не, ничего не приходит в голову."
        k "Уф, это может быть проблемой."
        k "Попробуй связать это с каким-нибудь запахом."
        scene chap1room (15) with dissolve
        k "Закрой глаза и подумай про себя: что я чувствую? Что я слышу? Что я чувствую по запаху?"
        scene chap1room (16) with dissolve
        mc "Так, ничего необычного я не чувствую…"
        mc "И единственное, что я слышу — это твой надоедливый голос."
        k "Ха-ха, очень смешно."
        k "Отнесись к этому серьёзно, пожалуйста."
        mc "Ладно... Думай, [mcname]"
        mc "Что я чувствую по запаху?"

        scene chap1room (17) with dissolve

        mc "Я чувствую запах..."
        play sound "audio/Sound/static.mp3"
        scene scawy with ahhflash
        scene scawy with ahhflash
        scene scawy with ahhflash
        stop sound
        play music "audio/Music/Glitch2.wav" volume 0.75
        scene scawy2 with flash
        pause 2
        scene scawy3 with quickdissolve
        scene scawy4 with quickdissolve
        scene scawy2 with quickdissolve
        scene scawy3 with quickdissolve
        scene scawy4 with quickdissolve
        scene scawy2 with quickdissolve
        scene scawy3 with quickdissolve
        scene scawy4 with quickdissolve
        scene scawy2 with quickdissolve
        pause 2
        stop music
        play sound "audio/Sound/static.mp3"
        scene scawy with ahhflash
        scene scawy with ahhflash
        scene scawy with ahhflash
        scene chap1room (18) with flash
        stop sound

        mc "КРОВЬ!"

        scene chap1room (19)

        play music "audio/Music/lostfire.mp3" volume 1.0
        mc "А?"
        mc "(Где я вообще? Похоже на какую-то тюрьму.)"

        scene chap1room (21) with dissolve

        mc "(Это место... оно ощущается неправильным. Холодным. Будто я задыхаюсь.)"

        scene chap1room (22) with dissolve

        mc "(Погоди...)"

        scene chap1room (23) with dissolve

        mc "(Это похоже на... меня? Но... я этого не помню... И с кем я разговариваю?)"

        scene chap1room (25) with dissolve

        "Молодая версия тебя нарушает тишину, голос сорванный и напряжённый."
        young_mc "Меня заставили обрить голову, но... это не так уж плохо. Это просто волосы. Они отрастут."
        "Он делает паузу, будто ожидая ответа, который так и не приходит."
        young_mc "Ты же... тебе всегда нравились мои волосы подлиннее, да? Говорила, что я похож на одного из тех героев из историй."
        "Тишина. Девочка не двигается, всё ещё повернувшись к нему спиной."
        young_mc "Они отрастут. Твои тоже. Может... может, мы просто притворимся, что это новое начало. Как новая глава."
        mc "Ты, наверное, закатываешь глаза на меня сейчас, да? Знаю, знаю... вечно пытаюсь найти хорошее в ужасной ситуации."

        scene chap1room (26) with dissolve

        mc "Уверен, ты будешь такой же красивой, когда сделают это и с тобой тоже."
        "Тишина заполняет комнату. На мгновение кажется, что кто-то слушает."
        young_mc "Я знаю, что это больно. Всё больно. Но мы не можем сдаться, ладно? Мы просто... должны продолжать идти."
        "Девочка остаётся неподвижной, её маленькое тело дрожит."
        young_mc "Хотел бы я... хотел бы я забрать всю эту боль. Заставить её прекратиться. Но всё, что я могу — это остаться здесь, с тобой."
        "Он придвигается ближе, его голос смягчается."
        young_mc "Ты не одна. Я здесь, рядом. Я всегда буду рядом."
        "В комнате становится холоднее, и у тебя перехватывает дыхание, пока ты наблюдаешь, как разворачивается эта сцена."
        young_mc "Мы сильные, помнишь? Нам просто нужно потерпеть сейчас, и однажды... однажды мы выберемся отсюда. Вместе."
        "Это воспоминание ощущается как острый осколок в его сознании, разрезающий любое чувство утешения."

        scene chap1room (29) with dissolve

        young_mc "Они думают, что смогут нас сломать, но они ошибаются. Мы сильнее, чем они когда-либо узнают."
        "Его голос дрожит, выдавая собственный страх."
        young_mc "Однажды... однажды мы выберемся отсюда. Мы снова увидим солнце. Обещаю."
        young_mc "Я буду тебя защищать. Несмотря ни на что. Никто больше тебя не тронет. Клянусь."
        young_mc "Всё будет хорошо. Я не позволю, чтобы с тобой снова что-то случилось. Обещаю. Я буду защищать свою сестру, несмотря ни на что."
        mc "(Мою... сестру? Почему я не могу вспомнить её лицо?)"

        scene chap1room (30) with dissolve

        mc "(Это... это не может быть реальным. Я не помню свою сестру... и уж точно не помню ничего из этого.)"
        mc "(Так... почему это ощущается настолько реальным? Настолько... знакомым?)"

        scene chap1room (31) with dissolve

        u "Воспоминания, погребённые в тени, но эхо остаётся, не так ли, [mcname]?"

        scene chap1room (32) with dissolve
        window hide dissolve
        pause 1.0
        scene chap1room (33) with dissolve

        "(Говорящая сова? Что вообще происходит? Что это такое?)"
        u "Прошлое — это головоломка с осколками, разбросанными повсюду. Одни потеряны, другие спрятаны..."
        u "А некоторые, [mcname], заперты в самых глубоких уголках твоего разума."
        play ambient "audio/ambient/feathers.mp3" volume 0.3

        scene chap1room (34) with dissolve


        mc "О чём ты вообще? Кто ты?"
        u "Имена, как и воспоминания, текучи... меняются со временем."
        u "Но я — хранитель тайн, страж забытых истин."
        u "И ты, [mcname], на грани того, чтобы вспомнить нечто давно утраченное."

        scene chap1room (35) with dissolve

        mc "Вспомнить? Но я даже не знаю, что именно должен вспомнить. Что всё это такое?"
        u "Со временем ты найдёшь свои ответы. Но пока знай одно: прошлое никогда по-настоящему не уходит."
        play sound "audio/Sound/feathers.mp3" volume 0.3

        scene chap1room (36) with dissolve

        u "Оно живёт в тебе, в шёпоте снов и тенях твоей души."
        mc "Я не понимаю... что это значит? Что мне делать?"
        play sound "audio/Sound/feathers.mp3" volume 0.3


        scene chap1room (37) with dissolve

        u " Если продолжишь искать, ты это найдёшь. Но берегись..."
        u "Не все истины нежны, твой разум сломан, а травма твоя глубока."
        mc "(Что эта сова пытается мне сказать? Это так туманно, но я чувствую, что здесь есть что-то важное, что-то, что мне нужно понять.)"
        play sound "audio/Sound/feathers.mp3" volume 0.3

        scene chap1room (38) with dissolve
        u "Когда мы встретимся снова, кусочки могут начать складываться воедино. А пока... помни, истина внутри тебя. Найди её."
        stop sound
        stop ambient
        stop music
        play sound "audio/Sound/Flash.wav" volume 0.3
        scene chap1room (41) with flash
        window hide dissolve
        pause 1.0
        scene chap1room (40) with dissolve

        "(А???)"

        scene chap1room (42) with dissolve
        "(Это всё был сон? Но я же не засыпал?)"
        "(Да что вообще, чёрт возьми, происходит!?)"

        scene chap1room (44) with dissolve

        "Что за хрень это вообще было!?"
        "Ты уж лучше дай мне какой-нибудь внятный ответ на то, что я там видел!"
        k "[mcname]..."
        mc "Кто была эта сова? Что это было за место? Почему я не могу вспомнить, что это вообще происходило?!"

        scene chap1room (48) with dissolve

        k "[mcname], смотри."

        scene chap1room (45) with dissolve

        mc "А?"

        scene chap1room (46) with dissolve
        window hide dissolve
        pause 1.0
        scene chap1room (47) with dissolve
        window hide dissolve
        pause 1.0
        $ renpy.pause(2, hard=True)
        scene chap1room (48) with dissolve

        k "Твоя аура..."
        scene intro 0
        k "Белая...."

        pause 4
        jump World


    label skiptoworld:
        $ Utami.quest = "Достичь 5 симпатии у Норы и Зары и подождать до среды."
        $ Parker.quest = "Подождать две недели, затем подождать до понедельника после уроков."
        $ Zara.quest = "Поговорить с Зарой в спортзале после уроков."
        $ Kyra.quest = "Подойти к банде Кайры перед школой."
        $ Grace.quest = "Пойти в левый коридор второго этажа."
        $ June.quest = "Поговорить с Джун в классе утром."
        $ Brooklyn.quest = "Поговорить с Бруклин на уроке утром."
        $ Nora.quest = "Представиться Норе в классе утром."
        $ Mei.quest = "Поговорить с Мэй в классе утром."
        $ Jordyn.quest = "Поговорить с Джордин в классе утром."
        $ Yuki.quest = "Поговорить с Юки в классе утром."
        $ Tamara.quest = "Поговорить с Тамарой и Райли на уроке утром."
        $ Riley.quest = "Поговорить с Тамарой и Райли на уроке утром."
        $ Izra.quest = "Поговорить с трио в классе утром."
        $ Lily.quest = "Поговорить с трио в классе утром."
        $ Autumn.quest = "Поговорить с трио в классе утром."
        $ Yejin.quest = "Поговорить с Йеджин на уроке утром"
        $ main.quest = "Поговорить с Кицунэ ночью."












    label World:
        play music "audio/Music/Nights.mp3" volume 1.0 fadein 1
        scene bedroomnight_bg with fade
        mc "(Что ж, насыщенный вышел денёк.)"
        mc "(Кицунэ, похоже, тоже не особо поняла, что с этим делать. Не очень-то обнадёживает. Никогда не видел её настолько растерянной.)"
        mc "(Белая... это же вроде не должно так работать? Кицунэ упоминала стандартные цвета, но белый?)"
        mc "(Такое чувство, будто я исключение... будто я вообще сюда не вписываюсь.)"
        mc "(Не уверен, хорошо это или плохо.)"
        mc "(Она сказала, что разберётся, выяснит, что это значит. Но пока что мне что делать?)"
        mc "(Не могу же я просто сидеть и ждать, пока ответы появятся сами по себе, будто по волшебству. Нужно двигаться дальше, попытаться разобраться самому.)"
        mc "Наверное, завтра стоит начать разговаривать с девчонками."
        mc "...."
        mc "Что вообще происходит с моей жизнью…"


    $ main.quest = "Поговорить с Кицунэ ночью."

    "{i}С этого момента ты сможешь принимать решения, которые повлияют на твои отношения с девушками в игре.{/i}"
    "{i}Выходные будут делиться на утро, день, вечер и ночь.{/i}"
    "{i}Каждая фаза даёт тебе время провести с одной девушкой. Но каждая девушка доступна только в определённое время в определённых местах каждый день.{/i}"
    "{i}В учебные дни у тебя будет время поговорить с девушками до урока, после урока и вечером.{/i}"
    "{i}События и знакомства персонажей открываются в зависимости от того, сколько ты с ними общаешься.{/i}"
    "{i}Ты не можешь получить доступ к событию знакомства персонажа после школы, не представившись ему сначала.{/i}"
    "{i}Ты также не можешь получить доступ к выходному событию персонажа, пока не поговоришь с ним после школы.{/i}"
    "{i}Далее ты сможешь получить доступ к особым событиям персонажа, зарабатывая симпатию.{/i}"
    "{i}У Изры сейчас больше всего контента, так что я бы начал с неё.{/i}"
    "{i}Ну вот, в общем-то, и всё!{/i}"
    "{i}Ты наверняка будешь часто теряться, но ничего не поделаешь! Разберёшься, я в тебя верю.{/i}"
    "{i}Наслаждайся!{/i}"

    hide freeroam with dissolve




label day_cycle:

    if rileyarcadeintro >= 1 and rileyroom == 0:


        $ Riley.quest = "Достичь 5 симпатии, затем поговорить с Райли на выходных."

    if rileyroom >= 1 and rileyconfront == 0:

        $ rileyroom = 1
        $ Riley.quest = "Подождать до конца урока."
    if yukibook2event == 1 and firstfight == 1 and yukikitsunebook == 0:
        $ Yuki.quest = "Поговорить с Кицунэ вечером о книгах Юки."
    if yukibook2event == 1 and firstfight == 0 and yukikitsunebook == 0:
        $ Yuki.quest = "Продолжить историю."


    if june15event2 >= 1 and junehallway1 == 0:
        $ june15event2 = 1
        $ June.quest = "Подождать до конца урока завтра."

    if zaraskateintro == 1 and zaraskateeventone == 0:
        $ Zara.quest = "Достичь 5 симпатии и поговорить с Зарой на выходных."

    if tamarabarintro == 1 and tamaradrinkoff == 0:
        $ Tamara.quest = "Достичь 5 симпатии с Тамарой, затем посетить бар ночью."
    if tamaradrinkoff == 1 and tamara_liquor_walk == 0:
        $ Tamara.quest = "Снова посетить бар ночью."

    if utamihairintro == 1 and utamisurf == 0:
        $ Utami.quest = "Посетить Утами в салоне"


    if june15event2 == 1 and junehallway1 == 0:
        $ june15event2 == 1
        $ June.quest = "Подождать до конца урока завтра."

    if junehelp == 1 and junepanick == 0:
        $ June.quest = "Подождать до ночи."

    if izraclimaxevent >= 1 and izrabj == 0:
        $ Izra.quest = "Пойти встретиться с Изрой в танцевальном зале."

    if autumnskateintro == 1 and autumnmovie == 0:
        $ Autumn.quest = "Поговорить с Отэм в гостиной вечером."

    if brooklyncafeintro == 1 and brooklyntalent1 == 0:

        $ Brooklyn.quest = "Поговорить с Бруклин после урока."
    if brooklyntalent2 == 1 and brooklyntalent_signup == 0:
        $ Brooklyn.quest = "Достичь 5 симпатии с Бруклин, затем подождать до полудня в школе."

    if gracemallintro == 1 and graceinvest == 0:

        $ Grace.quest = "Достичь 5 симпатии с Грейс и подождать до школьного утра."

    if graceinvest == 1 and graceinterrogate == 0:
        $ Grace.quest = "Поднять симпатию до 7 и найти Грейс в школьном коридоре"

    if rileyroom >= 1 and rileyconfront == 0:

        $ rileyroom = 1
        $ Riley.quest = "Подождать до конца урока."

    if rileyroom == 1 and rileyconfront == 0:
        $ Riley.quest = "Подождать до конца урока."

    if yejinbully == 1 and yejinblackmail == 0:
        $ Yejin.quest = "Найти Йеджин в классе после урока."
    if yejinblackmail == 1 and yejinpatrol == 0:
        $ Yejin.quest = "Пойти к шкафчикам после урока."

    if mei5event == 1 and meisketch == 0:
        $ Mei.quest = "Поднять симпатию, затем подождать несколько дней до урока."

    if firstfight == 1 and kyraalleyevent == 0:
        $ main.quest = "Поговорить с Кайрой в школе."

    if kyraalleyevent >= 1 and firstdream == 0:
        $ firstfight = 1
        $ kyraalleyevent = 1
        $ main.quest = "Поговорить с Кицунэ о карте ночью."
    if kyraalleyevent >= 1 and kyra_recruitment == 0:
        $ Kyra.quest = "Поговорить с Кайрой в школе."

    if kyraalleyevent == 1 and firstdream == 0:
        $ main.quest = "Поговорить с Кицунэ о карте ночью."

    if lilyzoointro == 1 and lilyflowerroof == 0:
        $ Lily.quest = "Достичь 5 симпатии и подняться на крышу школы."
    if lilyflowerroof == 1 and lilyzooshed == 0:
        $ Lily.quest = "Посетить Лили в зоопарке."

    if storydream2 == 1 and pillowtrain == 0:

        $ main.quest =  "Поговорить с Кицунэ о тренировках вечером."


    if autumnskateintro == 1:
        $ unlock_event(Autumn, "Назови моё имя", "autumn_tv_intro")
        $ unlock_event(Autumn, "Мистер Безопасность Прежде Всего", "autumn_skate_intro")
    if brooklyncafeintro == 1:
        $ unlock_event(Brooklyn, "Застенчивая гитаристка", "brooklyn_intro")
        $ unlock_event(Brooklyn, "Тайная симпатия", "brooklyn_hallway_intro")
        $ unlock_event(Brooklyn, "Кафе «Коала»", "brooklyn_cafe_intro")
    if gracemallintro == 1:
        $ unlock_event(Grace, "Новости не ждут никого", "grace_intro")
        $ unlock_event(Grace, "Развешивание газет", "grace_poster_intro")
    if izraclimaxevent == 1:
        $ unlock_event(Izra, "Лёгкость на ногах", "izra_ballet_intro")
        $ unlock_event(Izra, "Стабилизатор на скейте", "izra_skate_intro")
        $ unlock_event(Izra, "Короткий путь", "izra_5_event")
        $ unlock_event(Izra, "Претенциозное кафе", "izra_10_event")
        $ unlock_event(Izra, "Разделённые обеды", "izra_15_event")
        $ unlock_event(Izra, "Скрытые мотивы", "izra_20_event")
        $ unlock_event(Izra, "Разрядка обстановки", "izra_25_event")
        $ unlock_event(Izra, "Монтаж свиданий!", "izra_inbetween_event")
        $ unlock_event(Izra, "La Belle Époque", "izra_30_event")
        $ unlock_event(Izra, "Тост за багетом", "izraclimaxevent")
    if jordyndogevent == 1:
        $ unlock_event(Jordyn, "Скучающая нападающая", "jordyn_intro")
        $ unlock_event(Jordyn, "Дриблинг у фонтана", "jordyn_park_intro")
        $ unlock_event(Jordyn, "20 вопросов", "jordyn_dog_event")
    if june15event2 == 1:
        $ unlock_event(June, "В основном скука", "june_intro")
        $ unlock_event(June, "Знакомство в переулке", "june_alley_intro")
        $ unlock_event(June, "Перекур", "june_smoke_intro")
        $ unlock_event(June, "Знакомство в переулке", "june_alley_intro")
        $ unlock_event(June, "Скрытые тайны", "june_5_event")
        $ unlock_event(June, "Тихие высоты", "june_10_event")
        $ unlock_event(June, "Передача записок", "june_15_event_1")
        $ unlock_event(June, "Великий побег свиньи", "june_15_event_2")
    if kyraalleyevent == 1:
        $ unlock_event(Kyra, "Любопытная зараза", "kyra_intro")
        $ unlock_event(Kyra, "В переулке", "kyra_alley_event")
    if lilyzoointro == 1:
        $ unlock_event(Lily, "Убежище на крыше", "lily_roof_intro")
        $ unlock_event(Lily, "Заклинательница хорьков", "lily_zoo_intro")
    if mei5event == 1:
        $ unlock_event(Mei, "Маленькие наброски", "mei_intro")
        $ unlock_event(Mei, "Кола-магия", "mei_paint_intro")
        $ unlock_event(Mei, "Естественная среда обитания", "mei_hill_intro")
        $ unlock_event(Mei, "Переполненный холст", "mei_5_event")
    if nora5event == 1:
        $ unlock_event(Nora, "Так шикарно", "nora_intro")
        $ unlock_event(Nora, "Прими позу", "nora_gym_intro")
        $ unlock_event(Nora, "Тяжела блестящая голова", "nora_mall_intro")
        $ unlock_event(Nora, "Идём за покупками!", "nora_5_event")
    if nora5event == 1:
        $ unlock_event(Nora, "Так шикарно", "nora_intro")
        $ unlock_event(Nora, "Прими позу", "nora_gym_intro")
        $ unlock_event(Nora, "Тяжела блестящая голова", "nora_mall_intro")
        $ unlock_event(Nora, "Идём за покупками!", "nora_5_event")
    if parkercityintro == 1:
        $ unlock_event(Parker, "Отдай мой кошелёк!", "parker_intro")
        $ unlock_event(Parker, "Хардкорный паркур", "parkercityintro")
    if rileyroom == 1:

        $ unlock_event(Riley, "Профессиональная тупица", "riley_library_intro")
        $ unlock_event(Riley, "Сделана иначе", "riley_arcade_intro")
        $ unlock_event(Riley, "Ты вот так живёшь!?", "riley_room_event")
    if tamarabarintro == 1:
        $ unlock_event(Tamara, "Добро пожаловать в Cabanas!", "tamara_bar_intro")

    if utamihairintro == 1:
        $ unlock_event(Utami, "Радужные волосы", "utami_intro")
        $ unlock_event(Utami, "Фруктовый аромат", "utami_hair_intro")

    if yejinbully == 1:
        $ unlock_event(Yejin, "Президент класса", "yejin_intro")
        $ unlock_event(Yejin, "Методичный список дел", "yejin_afterclass_intro")
        $ unlock_event(Yejin, "Белый пояс", "yejin_dojo_intro")
        $ unlock_event(Yejin, "Императрица", "Yejin_in_school")

    if yukibook2event == 1:
        $ unlock_event(Yuki, "Я-я нервничаю...", "yuki_intro")
        $ unlock_event(Yuki, "Лёгкое чтение", "yuki_library_intro")
        $ unlock_event(Yuki, "Политика магазина", "yuki_con_intro")
        $ unlock_event(Yuki, "Держись от неё подальше", "yuki_5_event")
        $ unlock_event(Yuki, "Бросая камешки", "yuki_10_event")
        $ unlock_event(Yuki, "Сигналы спящим", "yuki_book2_event")

    if zaraskateintro == 1:
        $ unlock_event(Zara, "Конструктивная критика", "zara_intro")
        $ unlock_event(Zara, "Идеальные кадры", "zara_skate_intro")

    scene bedroommorning_bg with fade

    $ totaldays += 1
    $ day += 1

    if day == 1:
        hide sunday onlayer date
        show monday onlayer date

    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date

    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date

    if day == 5:
        hide thursday onlayer date
        show friday onlayer date

    if day == 6:
        hide friday onlayer date
        show saturday onlayer date

    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date




    if day == 6 or day == 7:
        jump weekend_morning
    elif day > 7:

        $ day = 1
        jump weekday_morning
    else:
        jump weekday_morning



label weekday_morning:






    show screen day_tracker

    if day == 1:
        hide sunday onlayer date
        show monday onlayer date

    stop ambient fadeout 1
    stop music fadeout 1

    "Утро, и пора идти на урок."
    if storydream1 == 1 and storydream2 == 0:
        jump class_scene
    if junebrotherintro == 1 and junehelp == 0:
        jump junehelp
    elif Izra.affection >= 5 and totaldays >= 10 and izraballetintro == 1 and izraskateintro == 1 and izra5event == 0:
        jump izra_5_event
    elif izra30event == 1 and izraclimaxevent == 0:
        jump izraclimaxevent

    elif juneskatepark == 1 and junetalkto == 1 and junebrotherintro == 0:
        jump june_alley_confrontation

    elif June.affection >= 5 and junealleyintro == 1 and june5event == 0:
        jump june_5_event



    elif Grace.affection >= 5 and gracemallintro == 1 and graceinvest == 0:
        play music "audio/Music/School.mp3" volume 1.0
        play ambient "audio/ambient/crowd.mp3" volume 0.3
        jump Grace_confronts
    else:
        jump class_scene


    label class_scene:

    scene schoolentrance with fade

    "Ты торопливо идёшь на урок."
    play music "audio/Music/School.mp3" volume 1.0
    play ambient "audio/ambient/crowd.mp3" volume 0.3
    scene classroom with fade
    if Mei.affection >= 5 and totaldays >= 10 and meihillintro == 1 and meievent5prelude == 0:
        jump mei_5_prelude
    if Mei.affection >= 8 and totaldays >= 14 and mei5event == 1 and meisketch == 0:
        stop ambient fadeout 1.0
        jump mei_ducks
    else:
        jump in_class


    label in_class:
    mc "Привет, Пьер."
    l "Как оно, мешки под глазами!"
    pe "С кем сегодня будешь болтать?"
    jump class_example

    menu:
        "Поговорить с Норой":
            stop ambient fadeout 1.0
            if not intro_nora:
                jump nora_intro
            else:
                jump nora_class
        "Поговорить с Джун":
            stop ambient fadeout 1.0
            if intro_june == 0:
                jump june_intro
            else:
                jump june_class
        "Поговорить с Бруклин":
            stop ambient fadeout 1.0
            if intro_brooklyn == 0:
                jump brooklyn_intro
            else:
                jump brooklyn_class
        "Поговорить с Юки":
            stop ambient fadeout 1.0
            if intro_yuki == 0:
                jump yuki_intro
            else:
                jump ella_class
        "Поговорить с Мэй":

            stop ambient fadeout 1.0
            if intro_mei == 0:
                jump mei_intro
            else:
                jump mei_class
        "Поговорить с Джордин":
            stop ambient fadeout 1.0
            if intro_jordyn == 0:
                jump jordyn_intro
            else:
                jump jordyn_class
        "Поговорить с Тамарой и Райли":
            stop ambient fadeout 1.0
            if intro_2 == 0:
                jump tamara_riley_intro
            else:
                jump tamara_riley_class
        "Поговорить с Трио":
            stop ambient fadeout 1.0
            if intro3 == 0:
                jump trio_intro
            else:
                jump trio_class




label nora_class:
    scene noraw with dissolve
    "Ты подходишь к Норе и немного болтаешь о домашке."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Норы возросла.{/i}"
    $ Nora.affection += 1

    jump weekday_afternoon

label june_class:
    scene juneclassintro (9) with dissolve
    "Ты прислоняешься к стене и немного болтаешь с Джун."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Джун возросла.{/i}"
    $ June.affection += 1

    jump weekday_afternoon

label brooklyn_class:
    scene brooklynw with dissolve
    "Ты слушаешь, как Бруклин играет на гитаре."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Бруклин возросла.{/i}"
    $ Brooklyn.affection += 1
    jump weekday_afternoon

label ella_class:
    scene yukiintro (2) with dissolve
    "Ты смотришь, как Юки читает книгу."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Юки возросла.{/i}"
    $ Yuki.affection += 1

    jump weekday_afternoon

label mei_class:
    scene meiw with dissolve
    "Ты смотришь, как Мэй рисует."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Мэй возросла.{/i}"
    $ Mei.affection += 1

    jump weekday_afternoon

label jordyn_class:
    scene jordynw with dissolve
    "Ты проводишь немного времени, болтая с Джордин о спорте."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Джордин возросла.{/i}"
    $ Jordyn.affection += 1

    jump weekday_afternoon

label tamara_riley_class:
    scene tamarileyw with dissolve
    "У тебя непринуждённый разговор с Тамарой и Райли."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Тамары возросла.{/i}"
    "{i}Симпатия Райли возросла.{/i}"
    $ Tamara.affection += 1
    $ Riley.affection += 1


    jump weekday_afternoon

label yejin_class:
    scene yejinw with dissolve
    "Ты пытаешься завести разговор с Йеджин, но она просто игнорирует тебя."
    $ Yejin.affection += 1
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Йеджин возросла.{/i}"
    jump weekday_afternoon

label trio_class:
    scene datriow with dissolve
    "Лили, Отэм и Изра рассказывают тебе о своих планах после школы."
    $ Autumn.affection += 1
    $ Izra.affection += 1
    $ Lily.affection += 1
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Отэм возросла.{/i}"
    "{i}Симпатия Изры возросла.{/i}"
    "{i}Симпатия Лили возросла.{/i}"

    jump weekday_afternoon

label weekday_afternoon:
    if storydream1 == 1 and storydream2 == 0:
        jump after_class

    if Yuki.affection >= 5 and yukiconintro == 1 and yuki5event == 0:
        jump yuki_5_event
    elif izra25event == 1 and izrainbetweenevent == 0:
        jump izra_inbetween_event
    elif June.affection >= 15 and june10event == 1 and june15event1 == 0:
        jump june_15_event_1

    elif day == 3 and Zara.affection >= 5 and Nora.affection >= 5 and intro_utami == 0:
        jump utami_intro

    elif day == 1 and totaldays>= 14 and intro_parker == 0:
        jump parker_intro
    else:
        jump after_class


label after_class:

    if pushupintro == 1 and main.strength >= 5 and intro_2 == 1 and intro3 == 1 and intro_jordyn == 1 and intro_brooklyn == 1 and intro_june == 1 and intro_mei == 1 and intro_nora == 1 and intro_yuki == 1 and intro_yejin == 1 and firstfight ==0:
        $ main.quest =  "Поговорить с Кицунэ ночью."

    play sound "audio/Sound/bell.wav" volume 1.0
    stop ambient fadeout 2

    image stupid1 = "images/Stupid/stupid1.webp"
    image stupid2 = "images/Stupid/stupid2.webp"
    image stupid3 = "images/Stupid/stupid3.webp"
    image stupid4 = "images/Stupid/stupid4.webp"
    image stupid5 = "images/Stupid/stupid5.webp"
    image stupid6 = "images/Stupid/stupid6.webp"
    image stupid7 = "images/Stupid/stupid7.webp"
    image stupid8 = "images/Stupid/stupid8.webp"
    image stupid9 = "images/Stupid/stupid9.webp"
    image stupid10 = "images/Stupid/stupid10.webp"
    image stupid11 = "images/Stupid/stupid11.webp"
    image stupid12 = "images/Stupid/stupid12.webp"
    image stupid13 = "images/Stupid/stupid13.webp"
    image stupid14 = "images/Stupid/stupid14.webp"
    image stupid15 = "images/Stupid/stupid15.webp"
    image stupid16 = "images/Stupid/stupid16.webp"
    image stupid17 = "images/Stupid/stupid17.webp"
    image stupid18 = "images/Stupid/stupid18.webp"
    image stupid19 = "images/Stupid/stupid19.webp"
    image stupid20 = "images/Stupid/stupid20.webp"
    image stupid21 = "images/Stupid/stupid21.webp"
    image stupid22 = "images/Stupid/stupid22.webp"
    image stupid23 = "images/Stupid/stupid23.webp"
    image stupid24 = "images/Stupid/stupid24.webp"
    image stupid25 = "images/Stupid/stupid25.webp"
    image stupid26 = "images/Stupid/stupid26.webp"
    image stupid27 = "images/Stupid/stupid27.webp"
    image stupid28 = "images/Stupid/stupid28.webp"
    image stupid29 = "images/Stupid/stupid29.webp"
    image stupid30 = "images/Stupid/stupid30.webp"
    image stupid31 = "images/Stupid/stupid31.webp"
    image stupid32 = "images/Stupid/stupid32.webp"
    image stupid33 = "images/Stupid/stupid33.webp"
    image stupid34 = "images/Stupid/stupid34.webp"
    image stupid35 = "images/Stupid/stupid35.webp"
    image stupid36 = "images/Stupid/stupid36.webp"
    image stupid37 = "images/Stupid/stupid37.webp"
    $ random_number = random.randint(1, 37)
    $ random_image = "stupid" + str(random_number)
    scene expression random_image with fade

    "Урок был скучным, как всегда."
    if storydream1 == 1 and storydream2 == 0:
        scene classnoon with dissolve


        "Урок закончился. Куда хочешь пойти?"

        jump avoclass_example

    if rileyroom == 1 and rileyconfront == 0:

        jump riley_afterclass_confront
    elif june15event2 == 1 and junehallway1 == 0:
        jump june_hallway_banter
    else:
        scene classnoon with dissolve


        "Урок закончился. Куда хочешь пойти?"

        jump avoclass_example

    menu:
        "Библиотека":
            jump library
        "Спортивное поле"(color="pink"):
            jump sports_field
        "Коридор":
            jump hallway
        "Вход":
            jump entrance
        "Крыша":
            jump rooftop
        "Классы":
            jump classrooms

    jump weekday_evening

label weekday_evening:
    if storydream1 == 1 and storydream2 == 0:
        jump stillindream
    if Izra.affection >= 20 and totaldays >= 20  and  izra15event == 1 and izra20event == 0:
        jump izra_20_event
    elif Izra.affection >= 25 and totaldays >= 25  and  izra20event == 1 and izra25event == 0:
        jump izra_25_event
    stop sound
    stop music fadeout 1
    play music "audio/Music/evening.mp3" volume 1.0 fadein 1
    scene schoolentrance with fade
    "Вы с Отэм решаете пойти домой на сегодня."
    scene weekdaybedroomevening_bg with fade
    "Вечер. Можешь отдохнуть или провести время с кем-то."
    jump weekdaybedroomevening_example

    menu:
        "Пойти в бар":
            if intro_2 == 1:
                jump tamarabarevents
            else:
                mc "А? Зачем мне идти в бар? Я ещё не в том возрасте, чтобы пить."
                mc "Если только я не знаю кого-то, кто владеет баром, в этом нет смысла."
                jump weekday_night
        "Посмотреть телек с Отэм":
            if intro3 ==1:
                jump autumntvevents
            else:
                mc "Эх, она, наверное, разозлится, что я там торчу."
                "Ты решаешь вместо этого посмотреть телек у себя в комнате."
                jump weekday_night

    jump weekday_night

label weekday_night:
    stop sound
    stop music fadeout 1
    play music "audio/Music/nights.mp3" volume 0.75
    play ambient "audio/ambient/night.mp3" volume 0.5
    scene bedroomnight_bg with fade
    "Ночь. Чем хочешь заняться?"

    menu:
        "Отдохнуть":
            jump rest
        "Тренироваться":
            jump train


    if day == 5:
        jump day_cycle
    else:
        jump weekday_morning


label weekend_morning:


    if storydream1 == 1 and storydream2 == 0:
        if day == 6:
            hide saturday onlayer date
            show friday onlayer date
        if day == 7:
            hide sunday onlayer date
            show friday onlayer date
        "Утро, и пора идти на урок."
        jump class_scene
    else:
        scene bedroommorning_bg
        stop ambient fadeout 1.0
        stop music fadeout 1.0
        play music "audio/Music/Acting.mp3" volume 1.0
        stop sound
        "Выходные! Куда хочешь пойти?"
        if izrainbetweenevent == 1 and izra30event == 0:
            jump izra_30_event
        elif junelilyzoo == 1 and june15event2== 0:
            jump june_15_event_2
        else:
            jump bedroommorning_example


label weekend_morningmap:
    scene mapweekendmorning_bg
    jump mapweekendmorning_example


    menu:
        "Парк":
            if meipaintintro == 1:
                jump meihillevents
            else:
                play ambient "audio/ambient/Park.mp3" volume 0.5
                scene park with fade
                "Парк сегодня тихий. Ты решаешь прогуляться"
                "Щебет птиц приятно слушать. Хотя, если честно, ты бы предпочёл быть дома."
                jump parkcrossroadsmorning_example
        "Торговый центр":


            if brooklynhallintro == 1:

                jump brooklyncafeevents
            else:

                play ambient "audio/ambient/Mall.mp3" volume 0.5
                scene mall with fade
                "Ты прибываешь в торговый центр"
                jump mall1morning_example
        "Город":
            if rileylibraryintro == 1:
                jump rileyarcadeevents
            else:
                play ambient "audio/ambient/City.mp3" volume 0.5
                scene city with fade
                "Ты отправляешься в город."
                "В это время дня ничего не открыто, чтобы развеять скуку."
                "Придётся сближаться с людьми, если хочешь чем-то заняться."
                jump weekend_morning
        "Скейтпарк":

            if izraballetintro == 1 and izra20event == 0:
                jump izracityevents
            elif izra20event == 1 and izra25event == 0 and izra30event == 0:
                play ambient "audio/ambient/skatepark.mp3" volume 0.5
                scene skatepark with fade
                "Ты пытаешься найти Изру в скейтпарке."
                "Похоже, она тебя избегает."
                jump skateparknoon_example
            elif izra30event == 1 and izraclimaxevent == 0:
                play ambient "audio/ambient/skatepark.mp3" volume 0.5
                scene skatepark with fade
                mc "...."
                mc "Не хочу тут находиться."
                mc "Не могу смотреть ей в глаза после того, что случилось."
                jump skateparknoon_example
            else:
                play ambient "audio/ambient/skatepark.mp3" volume 0.5
                scene skatepark with fade
                jump skateparkmorning_example


label park_morning:
    stop music fadeout 1.0
    play ambient "audio/ambient/Park.mp3" volume 0.5
    scene park with fade
    "Ты прибываешь в парк."
    scene meipaint1 with fade
    "Ты поднимаешься на холм, чтобы полюбоваться видом парка."

    play music "audio/Music/Mei.mp3" volume 1.0 fadein 1.0
    scene MeiWeekend with dissolve
    "Ты находишь Мэй на холме — она расставила мольберт и рисует умиротворяющий пейзаж парка."
label mei_menu:
    scene MeiWeekend with dissolve
    "Ты находишь Мэй на холме — она расставила мольберт и рисует умиротворяющий пейзаж парка."
label mei_menu2:
    call screen Meiaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump mei_menu2
label park_morninghang:
    "Мэй замечает тебя и улыбается, приглашая взглянуть на её работу."
    scene meipaint with fade
    m "Что думаешь? Неплохо продвигается, да?"
    "Картина прекрасно передаёт утренний свет. Ты киваешь с восхищением."
    "Вы немного болтаете о её творческом процессе, и Мэй делится с тобой парой советов по живописи."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Мэй возросла.{/i}"
    $ Mei.affection += 1
    stop music fadeout 1.0
    jump hillnoon_example
label park_morningwait:
    "Ты просто стоишь рядом, особо не разговаривая с Мэй."
    jump hillnoon_example

label mall_morning:
    stop music fadeout 1.0
    play ambient "audio/ambient/Mall.mp3" volume 0.4
    scene mall with fade
    scene mall with fade
    "Ты прибываешь в торговый центр"

    play music "audio/Music/Cafe.mp3" volume 0.75 fadein 1.0
    scene cafe with fade
    "Бруклин работает в кафе, занята заказами. Заметив тебя, она машет тебе подойти."
label brooklyn_menu:
    scene BrooklynWeekend with dissolve
    call screen  Brooklynaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump brooklyn_menu
label mall_morninghang:
    b "Рада, что ты здесь! Мне бы не помешала компания, если хочешь задержаться ненадолго?."
    scene brooklyncafe with fade
    "Вы немного дурачитесь с Бруклин, делая её утро чуть менее унылым"
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Бруклин возросла.{/i}"
    $ Brooklyn.affection += 1
    jump cafenoon_example
label mall_morningwait:
    "Ты просто ждёшь в кафе."
    jump cafenoon_example

label city_morning:
    stop music fadeout 1.0
    play ambient "audio/ambient/City.mp3" volume 0.5

    scene city with fade
    "Ты отправляешься в город."
    scene arcade with fade
    "Ты идёшь в игровые автоматы, где звуки и огни завораживают."
    stop ambient
    play music "audio/Music/Arcade.mp3" volume 1 fadein 1.0
    scene rileyarcade1 with fade
    "Ты заходишь в зал автоматов и находишь Райли, погружённую в игру, сосредоточенную и напряжённую."
    play music "audio/Music/Riley.mp3"
label riley_menu:
    scene RileyWeekend with dissolve
    call screen  Rileyaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump riley_menu
label arcade_morninghang:

    r "О, привет! Отличное время. Готов снова получить разгром?"
    mc "Это мы ещё посмотрим!"
    r "Ты и в прошлый раз так говорил."

    scene rileyarcade with fade

    "Ты подходишь к другому автомату и начинаешь играть вместе с Райли, азартно долбя по кнопкам"

    "К концу она полностью надрала тебе задницу. Но вы оба смеётесь."
    play sound "audio/Sound/affection.mp3" volume 0.4
    "{i}Симпатия Райли возросла.{/i}"
    $ Riley.affection += 1
    stop music fadeout 1.0
    jump mapweekendnoon_example
label arcade_morningwait:
    "Ты просто ждёшь в зале автоматов."
    stop music fadeout 1.0
    jump mapweekendnoon_example

label skatepark_morning:
    stop music fadeout 1.0
    play ambient "audio/ambient/Skatepark.mp3" volume 0.5
    scene skatepark with fade
    "Ты оказываешься в скейтпарке."
    play music "audio/Music/Izra.wav" volume 1.0 fadein 1.0
label izra_menu:

    scene IzraWeekend with dissolve
    "Ты видишь, как Изра пытается кататься на роликах, но явно испытывает с этим трудности."
    call screen Izraaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump izra_menu
label skatepark_morninghang:

    I "Эмм... хочешь снова помочь."
    scene izraskate with fade
    "В течение следующих нескольких минут ты остаёшься рядом, подавая руку каждый раз, когда она шатается. В итоге у неё начинает получаться лучше, она даже смеётся каждый раз, когда поскальзывается."

    I "Похоже, мне нужно ещё много практики, да?"
    "Вы оба смеётесь, и она благодарит тебя за то, что остался рядом и помог ей."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Изры возросла.{/i}"
    $ Izra.affection += 1
    jump skateparknoon_example
label skatepark_morningwait:
    "Ты немного ждёшь вместе с Изрой"
    jump skateparknoon_example

label weekend_noon:
    stop sound
    stop music fadeout 1.0
    scene afternoon with fade
    "Ты пытаешься убить немного времени, но быстро снова скучаешь."
    "Полдень. Куда хочешь пойти дальше?"
label weekend_noonmap:
    scene mapweekendnoon_bg
    jump mapweekendnoon_example
    menu:
        "Парк":
            if jordyntrackintro == 1:
                jump jordynparkevents
            else:
                play ambient "audio/ambient/Park.mp3" volume 0.5
                scene park with fade
                "Парк сегодня тихий. Ты решаешь прогуляться"
                jump fountainmorning_example
        "Торговый центр":
            if noragymintro == 1:
                jump noramallevents
            else:
                play ambient "audio/ambient/Mall.mp3" volume 0.5
                scene mall with fade
                "Ты бесцельно бродишь по торговому центру, не находя ничего интересного"
                jump mallnoon_example
        "Город":

            if junesmokeintro == 1:
                jump junealleyevents
            else:
                play ambient "audio/ambient/City.mp3" volume 0.5
                scene city with fade
                "Ты начинаешь исследовать город"
                "Ты бродишь без цели. Хотя без компании довольно скучно."
                jump weekend_noon
        "Додзё":

            if yejinclassintro == 1:
                jump yejindojoevents
            else:
                play ambient "audio/ambient/City.mp3" volume 0.5
                scene city with fade
                "Ты отправляешься в додзё"
                "У тебя нет причин здесь находиться."
                jump weekend_noon
        "Скейтпарк":
            if autumntvintro == 1:
                jump autumnskateevents
            else:
                play ambient "audio/ambient/Skatepark.mp3" volume 0.5
                scene skatepark with fade
                jump skateparkevening_example


label park_noon:
    play ambient "audio/ambient/Park.mp3" volume 0.5
    scene park with fade
    "У фонтана ты видишь Джордин, отрабатывающую футбольные упражнения, её сосредоточенность заметна, пока она работает над техникой ног."
    play music "audio/Music/Jordyn.mp3" volume 1.0 fadein 1.0
label jordyn_menu:
    scene JordynWeekend with dissolve
    call screen Jordynaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump jordyn_menu
    "Джордин замечает тебя и жестом приглашает подойти."

label park_noonhang:

    J "Эй! Хочешь попробовать? Спорим, не угонишься за мной!"
    scene jordynpark with fade
    "Ты смеёшься и присоединяешься к ней, пытаясь не отставать от её упражнений."

    "После нескольких раундов вы оба запыхались и смеётесь, впечатлённые её мастерством."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Джордин возросла.{/i}"
    $ Jordyn.affection += 1
    jump fountainevening_example
label park_noonwait:
    "Ты ждёшь в парке вместе с Джордин."
    jump fountainevening_example

label mall_noon:
    play ambient "audio/ambient/Mall.mp3" volume 0.5
    scene mall with fade
    "Ты бродишь по торговому центру, заглядывая в магазины и покупая пару вещей."
    play music "audio/Music/Nora.mp3" volume 1.0 fadein 1.0
label nora_menu:
    scene NoraWeekend with dissolve
    call screen  Noraaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump nora_menu

label mall_noonhang:
    n "Привееет, а можешь, типа, сделать мне огромное одолжение? Эти пакеты такие, типа, тяяжеленные!"
    "Она надувает губки и вручает тебе свои пакеты, прежде чем ты успеваешь ответить."
    scene norahmall with fade
    "Ты берёшь пакеты, следуя за ней, пока она ныряет в каждый магазин, болтая о моде."
    n "Ты сейчас, типа, мой герой! Я бы совсем потерялась без тебя!"
    "После ещё нескольких магазинов Нора благодарит тебя яркой улыбкой и обещает как-нибудь отплатить тем же."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Норы возросла.{/i}"
    $ Nora.affection  += 1
    jump mall1evening_example
label mall_noonwait:
    "Ты ждёшь с Норой до вечера."
    jump mall1evening_example

label city_noon:
    play ambient "audio/ambient/City.mp3" volume 0.5
    scene city with fade
    "Ты начинаешь исследовать город"
    scene alleyway with fade
    "Ты исследуешь переулок, замечая интересное стрит-арт."
    play music "audio/Music/June.mp3" volume 1.0 fadein 1.0
label june_menu:
    scene JuneWeekend with dissolve
    "В переулке ты замечаешь Джун, облокотившуюся на стену, непринуждённо крутую в своём тёмном наряде."
    call screen  Juneaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump june_menu
label alley_noonhang:

    j "О, привет. Не ожидала, что кто-то заглянет. Не то чтобы я против... или мне вообще не всё равно."
    "Она пожимает плечами, медленно затягиваясь сигаретой, её слова звучат резко, хотя ты видишь, что она не хотела грубить."
    j "Можешь тусоваться, если хочешь. Просто... не жди, что я буду тебя развлекать или типа того."
    scene junealley with dissolve
    "Ты садишься рядом с ней, беря сигарету и разделяя тихий момент. Несмотря на её слова, между вами уютная тишина."
    "Она бросает на тебя короткий взгляд, затем отворачивается, лёгкий намёк на признательность мелькает в её выражении, хотя она бы никогда не сказала этого прямо."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Джун возросла.{/i}"
    $ June.affection += 1
    stop music fadeout 1.0
    jump mapweekendnight_example

label alley_noonwait:
    "Ты ждёшь в переулке вместе с Джун."
    stop music fadeout 1.0
    jump mapweekendnight_example

label skatepark_noon:
    play ambient "audio/ambient/Skatepark.mp3" volume 0.5
    scene skatepark with fade
    "Ты смотришь на скейтбордистские трюки и подбадриваешь райдеров."
    play music "audio/Music/Autumn.mp3" volume 1.0 fadein 1.0
label autumn_menu:
    scene AutumnWeekend with dissolve
    "Ты замечаешь Отэм в скейтпарке, она непринуждённо лавирует между рампами и перилами с уверенной ухмылкой."
    call screen  Autumnaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump autumn_menu
label skatepark_noonhang:
    a "В чём дело? Слишком боишься присоединиться? Я же не кусаюсь, знаешь ли."
    a "В чём дело? Слишком боишься присоединиться? Я же не кусаюсь, знаешь ли."
    "Она приподнимает бровь, поддразнивая тебя этим знакомым, вызывающим взглядом, но ты со смехом качаешь головой."
    a "Ладно, ладно. Тогда просто сядь и наслаждайся зрелищем!"
    "Она закатывает глаза, но, похоже, довольна вниманием, пока скользит обратно к рампам, выполняя лишний трюк-другой напоказ."
    scene autumnskate with fade
    "Наблюдая за её катанием, ты не можешь не восхититься её природным талантом и уверенностью, с которой она делает трюк за трюком."
    a "Говорила же, я хороша. Может, в следующий раз у тебя хватит духу встать на доску!"
    mc "Что-то сомневаюсь."
    "Она машет тебе рукой, заканчивая свой заезд, её пацанская улыбка полна гордости и удовлетворения."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Отэм возросла.{/i}"
    $ Autumn.affection += 1
    stop music fadeout 1.0
    jump skateparkevening_example

label skatepark_noonwait:
    "Ты немного ждёшь вместе с Отэм."
    stop music fadeout 1.0
    jump skateparkevening_example


label weekend_evening:
    stop music fadeout 1.0
    stop sound
    scene evening with fade
    "Ты пытаешься убить немного времени, но быстро начинаешь скучать."
    "Уже вечер. Куда хочешь пойти?"
label weekend_eveningmap:
    scene mapweekendevening_bg
    jump mapweekendevening_example


label park_evening:
    play ambient "audio/ambient/Park.mp3" volume 0.5
    scene park with fade

    "Ты осматриваешься по парку, пытаясь найти, чем заняться в такой поздний час."
    play music "audio/Music/LilyTheme.mp3" volume 1.0 fadein 1.0
    scene zoo with fade
    "Ты направляешься к приюту для животных, где Лили занята кормлением зверей."
label lily_menu:
    scene LilyWeekend with dissolve
    "Она машет тебе рукой, когда ты подходишь."
    call screen  Lilyaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump lily_menu
label park_eveninghang:
    L "Хочешь помочь? Животные обожают внимание!"

    scene lilyzoo with fade
    "Ты проводишь время с Лили, кормя животных и убирая клетки."

    "К тому моменту, как вы уходите, и ты, и Лили довольны, что вместе помогли животным."
    "{i}Симпатия Лили возросла.{/i}"
    $ Lily.affection += 1
    stop music fadeout 1.0
    jump zoonight_example
label park_eveningwait:
    "Ты немного ждёшь вместе с Лили."
    stop music fadeout 1.0
    jump zoonight_example

label mall_evening:
    play ambient "audio/ambient/Mall.mp3" volume 0.5
    scene mallevening with fade
    "Ты заходишь в торговый центр, до закрытия которого осталось несколько часов."
    play music "audio/Music/Grace.mp3" volume 1.0 fadein 1.0
    scene gracemall1 with fade
    "Ты видишь, как Грейс с трудом вешает газету, на лице — решимость."
label grace_menu:
    scene GraceWeekend with dissolve
    "Вопреки здравому смыслу, ты решаешь подойти к ней."
    call screen  Graceaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump grace_menu
label mall_eveninghang:
    g "Эй! Тебе заняться нечем, или ты просто пялишься? Помоги-ка мне с этим, а?"
    "Не дожидаясь ответа, она суёт тебе в руки стопку газет."
    scene gracemall3 with dissolve
    g "Не отставай, дружище! Это тебе не прогулка в парке! Это прогулка по торговому центру, вот!"
    "Ты стараешься изо всех сил поспевать за её темпом и не оглохнуть, помогая раздавать газеты как можно быстрее."
    g "Отличная работа! Не припомню, чтобы у меня был помощник, который бы меня не тормозил."
    "Она хлопает тебя по плечу с довольной ухмылкой."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Грейс возросла.{/i}"
    $ Grace.affection += 1
    jump mall2night_example
label mall_eveningwait:
    "Ты немного ждёшь вместе с Грейс."
    jump mall2night_example

label city_evening:
    play ambient "audio/ambient/City.mp3" volume 0.5
    scene city2 with fade
    "Ты исследуешь город, прежде чем отправиться домой."
    scene constore with fade
    "Ты заходишь на заправку, покупая сигарет на вечер."
    play music "audio/Music/Yuki.mp3"
    stop ambient
label yuki_menu:
    scene YukiWeekend with dissolve
    "Ты находишь Юки за прилавком, явно умирающую от скуки."
    call screen  Yukiaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump yuki_menu
label con_eveninghang:
    y "Э-эй! Хочешь снова постоять на стрёме?"
    mc "Мне всё ещё нельзя тут курить?"
    y "Н-нет, извини."
    mc "Тогда пойду возьму что-нибудь попить."

    scene yukicon2 with dissolve
    "Ты стоишь у прилавка, пока Юки читает."
    "Вместе вы заставляете время идти быстрее."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Юки возросла.{/i}"
    $ Yuki.affection += 1
    stop music fadeout 1.0
    jump mapweekendnight_example
label con_eveningwait:
    "Ты немного ждёшь вместе с Юки"
    stop music fadeout 1.0
    jump mapweekendnight_example

label skatepark_evening:
    play ambient "audio/ambient/Skatepark.mp3" volume 0.5
    scene skatepark1 with fade
    "Ты осматриваешься по скейтпарку."
    play music "audio/Music/Zara.mp3" volume 1.0 fadein 1.0
label zara_menu:

    scene ZaraWeekend with dissolve
    call screen  Zaraaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump zara_menu
label skatepark_eveninghang:
    "Ты находишь Зару, как обычно делающую фотографии."
    z "О, привет. Отличное время. Сходи принеси мне кофе, ладно?"
    "Она едва поднимает взгляд, уже уверенная, что ты это сделаешь."

    "Ты вздыхаешь, но соглашаешься, направляясь за кофе для неё в ближайшее кафе."
    scene zarapark with fade

    z "Наконец-то! Долго же ты."
    "Она делает глоток, кивая тебе."

    z "Неплохо. Наверное, теперь я твоя должница. Может быть."
    "Она слегка усмехается, прежде чем вернуться к фотографиям."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Зары возросла.{/i}"
    $ Zara.affection += 1

    jump skateparknight_example
label skatepark_eveningwait:
    "Ты немного ждёшь вместе с Зарой."
    jump skateparknight_example

label weekend_night:
    stop sound
    stop music fadeout 1
    play music "audio/Music/nights.mp3" volume 0.75
    play ambient "audio/ambient/night.mp3" volume 0.5
    scene bedroomnight_bg with fade
    "Ночь. Чем хочешь заняться?"
label weekend_nightmap:
    scene mapweekendnight_bg
    jump mapweekendnight_example
    scene black

label weekday_nightmap:
    scene mapweekdaynight_bg
    jump mapweekdaynight_example
    scene black

    menu:
        "Пойти домой":
            jump bedroomnight_example
        "Пойти в бар":

            if intro_2 == 1:
                jump tamarabarevents
            else:
                mc "А? Зачем мне идти в бар? Я ещё не в том возрасте, чтобы пить."
                mc "Если только я не знаю кого-то, кто владеет баром, в этом нет смысла."
                jump bedroomnight_example



label library:
    scene library with fade
    "Ты заходишь в тихую библиотеку. Полки, полные книг, тянутся, насколько хватает взгляда."

    menu:
        "Сесть рядом с Юки":
            if intro_yuki == 1:
                jump yukilibraryevents
            else:
                "Ты ещё недостаточно хорошо знаешь Юки, чтобы с ней говорить."
                jump weekday_evening
        "Посмотреть, чем занята Райли":

            if intro_2 == 1:
                jump Rileylibraryevents
            else:
                "Ты ещё недостаточно хорошо знаешь Райли, чтобы с ней говорить."
                jump weekday_evening


    return

label library_yuki:
    scene black
    play music "audio/Music/Yuki.mp3" volume 1.0 fadein 1.0
    scene yukilibrary1 with dissolve
    "Ты садишься рядом с Юки, которая продолжает читать тебе свою историю."

    "Вы наслаждаетесь спокойным моментом вместе, прежде чем уйти."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Юки возросла.{/i}"
    $ Yuki.affection += 1
    jump weekday_evening

label library_riley:
    scene black
    play music "audio/Music/Riley.mp3" volume 1.0 fadein 1.0
    scene rileylibrary1 with dissolve
    "Ты подходишь к Райли, которая полностью сосредоточена на своей игре."

    scene rileylibrary2 with dissolve
    "Ты немного смотришь, как она играет, прежде чем пойти дальше."
    scene rileylibrary3 with dissolve
    "Ладно, может, ты немного слишком увлёкся."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Райли возросла.{/i}"
    $ Riley.affection += 1
    jump weekday_evening



    jump weekday_evening

label sports_field:

    scene sportsground with fade

    "Ты прибываешь на спортивное поле. Здесь тренируются несколько учеников."


    menu:
        "Пойти на дорожку бегать с Джордин":
            if intro_jordyn == 1:
                jump jordyntrackevents
            else:
                "Ты ещё недостаточно хорошо знаешь Джордин, чтобы с ней говорить."
                jump weekday_evening
            jump track_with_jordyn
        "Пойти в спортзал":
            jump gym_options


    return

label track_with_jordyn:
    scene black
    play music "audio/Music/Jordyn.mp3" volume 1.0 fadein 1.0
    scene jordyntrack1 with dissolve
    "Ты направляешься к беговой дорожке и находишь Джордин, разминающуюся перед забегом."
    "Она бросает на тебя вызывающий взгляд и приглашает пробежаться вместе."


    scene jordyntrack2 with dissolve
    "После напряжённой пробежки с Джордин ты чувствуешь прилив энергии."
    scene jordyntrack3 with dissolve
    "Оказывается, это просто твоя душа покидала тело."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Джордин возросла.{/i}"
    $ Jordyn.affection += 1

    jump weekday_evening

label clipboard_with_yejin:
    scene black
    play music "audio/Music/Yejin.mp3" fadein 1.0
    scene yejinafterclassintro (1) with dissolve
    "Ты снова видишь Йеджин, работающую со своим планшетом с зажимом."
    scene yejinafterclassintro (2) with dissolve
    mc "Нужна компания?"
    ye "Мм"
    "Она не отвечает. Но и не отказывает."
    if storydream1 == 1 and storydream2 == 0:
        scene yejinafterclassintro (7) with dissolve
        "Ты стоишь рядом с Йеджин, пока она разбирает темы, в которых ты либо ничего не понимаешь, либо тебе на них плевать."
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i}Симпатия Йеджин возросла.{/i}"
        $ Yejin.affection += 1
        jump weekday_evening
    elif yejinbully == 1 and yejinblackmail == 0:
        jump blackmail_scene
    else:
        scene yejinafterclassintro (7) with dissolve
        "Ты стоишь рядом с Йеджин, пока она разбирает темы, в которых ты либо ничего не понимаешь, либо тебе на них плевать."
        play sound "audio/Sound/affection.mp3" volume 0.5
        "{i}Симпатия Йеджин возросла.{/i}"
        $ Yejin.affection += 1



    jump weekday_evening

label gym_options:

    scene gym with fade
    "Ты заходишь в спортзал, где Зара и Нора проводят фотосессию."

    menu:
        "Зара":
            if intro_zara == 0:
                jump zara_intro
            else:
                jump gym_coffee_for_zara
        "Нора":

            if intro_nora == 1:
                jump noragymevents
            else:
                "Ты ещё недостаточно хорошо знаешь Нору, чтобы к ней присоединиться."

            jump weekday_evening

label gym_coffee_for_zara:
    scene black
    play music "audio/Music/Zara.mp3" volume 1.0 fadein 1.0
    "Ты предлагаешь принести Заре кофе, и она благодарно улыбается."
    scene zaragym1 with dissolve
    "Ты приносишь ей свежий кофе, и она на мгновение наслаждается им."
    scene zaragym2 with hpunch
    "Ну да, конечно... она выхватывает его у тебя из рук раньше, чем ты успеваешь заметить."

    "После недолгой болтовни ты рад, что смог помочь."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Зары возросла.{/i}"
    $ Zara.affection += 1

    jump weekday_evening

label gym_photos_for_nora:
    scene black
    play music "audio/Music/Nora.mp3" volume 1.0 fadein 1.0
    scene noragym1 with dissolve
    "Нора замечает тебя и спрашивает, не мог бы ты сделать пару фото для её поста о тренировке."
    "Ты делаешь несколько снимков, пока она принимает разные позы."

    "Сделав фото, она удовлетворённо кивает и благодарит тебя."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Норы возросла.{/i}"
    $ Zara.affection += 1
    jump weekday_evening

label hallway:

    scene hallway
    "Коридор кишит учениками, переходящими между уроками."
    "Пока ты идёшь по коридору, ты слышишь слабый звук гитары."
    menu:
        "Послушать, как Бруклин играет на гитаре":

            if intro_brooklyn == 1:
                jump brooklynhallevents
            else:
                "Хм, похоже, ты не можешь найти, откуда доносится музыка…"
                mc "Эти коридоры СЛИШКОМ запутанные."
                jump weekday_evening


            jump listen_to_brooklyn
        "Идти дальше":

            if intro_grace == 0:
                jump grace_intro
            else:
                jump bump_into_grace





label listen_to_brooklyn:
    scene black
    play music "audio/Music/Brooklyn.mp3" volume 1.0 fadein 1.0
    scene brooklynhall1 with dissolve
    "Ты идёшь на звук гитары и находишь Бруклин, перебирающую струны."
    "Похоже, она погружена в музыку, и ты решаешь просто тихо послушать."


    "Спустя какое-то время она замечает тебя и слегка улыбается, продолжая играть."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Бруклин возросла.{/i}"
    $ Brooklyn.affection += 1
    jump weekday_evening

label bump_into_grace:
    scene black
    play music "audio/Music/Grace.mp3" volume 1.0 fadein 1.0
    "Ты продолжаешь идти по коридору, особо не обращая внимания."
    scene gracehall1 with dissolve
    "Внезапно ты натыкаешься на Грейс, которая с трудом несёт кипу газет."

    scene gracehall2 with dissolve


    "Ты предлагаешь помочь ей разнести газеты, и вместе вы успеваете раздать их все."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Грейс возросла.{/i}"
    $ Grace.affection += 1
    jump weekday_evening

    jump weekday_evening

label entrance:
    scene schoolentrance with fade
    "Ты оказываешься у входа в школу. Популярное место, где тусуются ученики."
    menu:
        "Пойти потусоваться с Джун":
            if intro_june == 1:
                jump junesmokeevents
            else:
                "Ты не знаешь Джун и немного боишься её потревожить без нормального знакомства."
                jump weekday_evening
        "Осторожно подойти к банде":
            if intro_kyra == 0:
                jump kyra_intro
            else:
                jump approach_kyra_gang



    return

label smoke_with_june:
    scene black
    play music "audio/Music/June.mp3" volume 1.0 fadein 1.0
    scene juneschool1 with dissolve
    "Ты подходишь к Джун, сидящей на лестнице с сигаретой в руке."
    scene juneschool2 with dissolve
    "Она предлагает тебе сигарету и кивает, когда ты присоединяешься."


    "Вы проводите тихий момент вместе с Джун, прежде чем вернуться."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Джун возросла.{/i}"
    $ June.affection += 1
    jump weekday_evening

label approach_kyra_gang:
    scene black
    play music "audio/Music/Kyra.mp3" volume 1.0 fadein 1.0
    scene kyragang with dissolve
    "Ты осторожно подходишь к группе, собравшейся вокруг Кайры, которая явно тут главная."
    "Атмосфера напряжённая, и Кайра одаривает тебя взглядом «шевельнёшься — убью», пока ты подходишь ближе."


    "Ты решаешь, что оно того не стоит, по крайней мере сегодня."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Кайра не попыталась тебя убить, так что, думаю, её симпатия возросла?{/i}"
    $ Kyra.affection += 1
    jump weekday_evening

label rooftop:
    scene schoolroof
    "Ты выходишь на крышу, наслаждаясь спокойным видом на окрестности."
    menu:
        "Помочь Лили с садоводством":
            if intro3 == 1:
                jump lilyroofevent
            else:
                "Тебе нужно узнать Лили получше, может, попробуй поговорить с ней до урока."
                jump weekday_evening


label rooftop_garden_with_Lily:
    scene black
    play music "audio/Music/LilyTheme.mp3" volume 1.0 fadein 1.0
    scene lilyroof1 with dissolve
    "Ты подходишь туда, где Лили ухаживает за растениями. Она поднимает взгляд и тепло тебе улыбается."
    scene lilyroof2 with dissolve
    "Вместе вы начинаете работать над садом на крыше, наслаждаясь умиротворяющей атмосферой."
    scene lilyroof3 with dissolve

    "Проведя некоторое время за садоводством, ты чувствуешь, как тебя окутывает приятное спокойствие."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия Лили возросла.{/i}"
    $ Lily.affection += 1
    jump weekday_evening

label rooftop_mysterious_woman:
    play music "audio/Music/Strange.mp3" volume 1.0 fadein 1.0
    "Ты замечаешь женщину, тихо сидящую на краю крыши и смотрящую на город."
    scene mysterywoman with dissolve
    scene mysterywoman with dissolve
    "В её присутствии есть что-то интригующее, и ты решаешь к ней присоединиться."


    "Вы сидите в тишине некоторое время, мирный вид простирается перед вами."
    play sound "audio/Sound/affection.mp3" volume 0.5
    "{i}Симпатия ??? возросла.{/i}"
    jump weekday_evening

label classrooms:
    scene classes with fade
    "Ты бродишь по пустым классам, думая о сегодняшних уроках."

    menu:
        "Зайти в кабинет рисования":

            if intro_mei == 1:
                jump meipaintevents
            else:
                "У меня нет причин идти в кабинет рисования. Я не знаю никого, кто рисует."
                jump weekday_evening
        "Зайти в пустой класс":
            if intro3 == 1 and izra20event == 0:
                jump izraballetevents
            elif izra20event == 1 and izra25event == 0 and izra30event == 0:
                "Ты пытаешься найти Изру в классе."
                "Там никого нет."
                "Похоже, она тебя избегает."
                jump weekday_evening
            elif intro3 == 1 and izra25event == 1 and izra30event ==0:
                jump izraballetevents
            elif izra30event == 1:
                mc "...."
                mc "Не хочу тут находиться."
                mc "Не могу смотреть ей в глаза после того, что случилось."
                jump weekday_evening
            else:

                "Класс заперт изнутри."
                "Ты слышишь классическую музыку и движение из-за двери класса."
                jump weekday_evening


label paint_room_mei:
    scene black
    scene meiroom1 with dissolve
    play music "audio/Music/Mei.mp3" volume 1.0 fadein 1.0
    "Ты заходишь в кабинет рисования и видишь, как Мэй работает над прекрасным холстом."
    "Запах графита наполняет комнату, пока Мэй сосредоточена на своём искусстве."


    scene meiroom2 with dissolve

    "Ты проводишь немного времени, болтая с Мэй, пока она рисует, наслаждаясь её компанией."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Мэй возросла.{/i}"
    $ Mei.affection += 1
    jump weekday_evening

label ballet_with_izra:
    scene black
    scene izraballet1 with dissolve
    "Ты заходишь в один из пустых классов, а Изра уже разминается."
    scene izraballet2 with dissolve
    "Вы оба начинаете практиковать балет, Изра грациозно двигается по комнате."
    "Ты... не так уж грациозно."


    scene izraballet3 with hpunch
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Несмотря на твоё позорное отсутствие равновесия, симпатия Изры возросла{/i}."
    $ Izra.affection += 1
    jump weekday_evening


label bar:
    scene black
    stop ambient
    play music "audio/Music/Cabanas.mp3" volume 1.0
    "Ты решаешь заглянуть в бар выпить и, может, немного пообщаться."
    scene cabanas1 with fade
    "Ты заходишь в бар, знакомый звон бокалов и гул разговоров наполняют комнату. Кабана стоит за стойкой, протирая стаканы с дружелюбной улыбкой."

    c "А, вот и мой любимый помощник! Рад тебя видеть, малец."
    "Он тепло тебе ухмыляется и кивает в сторону Тамары, которая занята обслуживанием столиков."
label tamara_menu:

    scene TamaraWeekend with dissolve
    t "Hola, [mcname]!"
    call screen Tamaraaction_menu
    if _return == "gift_unavailable":
        "Подарки пока недоступны."
        jump tamara_menu
label bar_hang:
    scene cabanas2 with dissolve
    "Ты садишься и помогаешь ей практиковаться, поправляя произношение и грамматику."
    scene cabanas3 with dissolve
    "Спустя какое-то время она благодарит тебя, явно почувствовав себя увереннее в английском."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Тамары возросла.{/i}"
    $ Tamara.affection += 1
    jump day_cycle
label bar_wait:
    "Ты решаешь подождать в баре."
    jump day_cycle
label watch_tv_with_autumn:
    scene kitchennight with fade
    "Ты находишь Отэм на диване, её взгляд прикован к экрану, пока идёт «Во все тяжкие»."
    "Она жестом приглашает тебя сесть, не отрывая взгляда от сериала."
    scene autumntv with fade
    "Ты смотришь вместе с ней, тихо обмениваясь реакциями, пока идут часы."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Отэм возросла.{/i}"
    $ Autumn.affection += 1
    if junepolice == 1:
        jump weekdaylivingroomnightjune_example
    else:
        jump weekdaylivingroomnight_example


label rest:
    scene rest with fade
    "Ты решаешь переждать ночь с Кицунэ."
    jump day_cycle

label train:
    scene train1 with fade
    "Ты проводишь немного времени, тренируясь с Кицунэ, к её большому веселью."
    scene train2 with dissolve
    "Твой уровень силы возрос."
    $ main.strength += 1
    jump day_cycle


label weekendbar:
    stop ambient
    "На выходных Cabanas открыт допоздна, так что стоит этим воспользоваться."
    scene cabanas1 with fade
    play music "audio/Music/Cabanas.mp3" volume 1.0
    "Ты заходишь в бар, знакомый звон бокалов и гул разговоров наполняют комнату. Кабана стоит за стойкой, протирая стаканы с дружелюбной улыбкой."

    c "А, вот и мой любимый помощник! Рад тебя видеть, малец."
    "Он тепло тебе ухмыляется и кивает в сторону Тамары, которая занята обслуживанием столиков."
    scene cabanas2 with dissolve
    "Ты садишься и помогаешь ей практиковаться, поправляя произношение и грамматику."
    scene cabanas3 with dissolve
    "Спустя какое-то время она благодарит тебя, явно почувствовав себя увереннее в английском."
    play sound "audio/Sound/affection.mp3" volume 1.0
    "{i}Симпатия Тамары возросла.{/i}"
    $ Tamara.affection += 1

    jump day_cycle










label demo_menus:
    scene black
    if day == 1 and intro_parker == 1:
        jump demomap_Parker
    elif day == 3 and intro_utami == 1:
        jump demomap_Utami
    else:
        jump demo_map


label demo_map:
    scene mapweekdaynoon_bg
    jump mapweekdaynoon_example


label demo_mapeve:
    scene mapweekdayevening_bg
    jump mapweekdayevening_example




    menu:
        "Пойти домой":
            jump weekdaybedroomnoon_example
        "Школа":
            jump firsthallway1_example


label demomap_Parker:

    scene mapweekdayparker_bg
    jump mapweekdayparker_example
    menu:
        "Паркер":
            if parkercityintro == 0:
                jump parkercityintro
            else:
                jump mondaycity_eveningparker
        "Пойти домой":

            jump weekdaybedroomnoon_example
        "Школа":

            jump firsthallway1_example


label demomap_Utami:

    scene mapweekdayutami_bg
    jump mapweekdayutami_example
    menu:
        "Утами":
            if utamihairintro == 0:
                jump utami_hair_intro
            jump city_noonutami
        "Пойти домой":
            jump weekdaybedroomnoon_example
        "Школа":

            jump firsthallway1_example

label stoplooking:
    play ambient "audio/ambient/tv.mp3"
    $ renpy.pause (2, hard= True)
    play sound "audio/sound/chromark.mp3"
    scene chromark
    $ renpy.pause (16, hard= True)
    stop sound
    scene weird (1)
    $ renpy.pause (5, hard= True)
    scene weird (5)
    $ renpy.pause (4, hard= True)
    scene weird (6)
    $ renpy.pause (5, hard= True)
    scene weird (7)
    $ renpy.pause (5, hard= True)
    scene weird (8)
    $ renpy.pause (5, hard= True)
    scene weird (1)
    $ renpy.pause (5, hard= True)
    scene weird (9)
    $ renpy.pause (5, hard= True)
    scene weird (10)
    $ renpy.pause (5, hard= True)
    scene weird (11)
    $ renpy.pause (5, hard= True)
    play sound "audio/sound/mm.mp3"
    scene red
    scene red
    $ renpy.pause (1, hard= True)
    stop sound
    scene weird (17)
    $ renpy.pause (2, hard= True)
    scene weird (12)
    $ renpy.pause (2, hard= True)
    scene weird (13)
    $ renpy.pause (2, hard= True)
    scene weird (14)
    $ renpy.pause (2, hard= True)
    scene weird (15)
    $ renpy.pause (2, hard= True)
    scene weird (16)
    $ renpy.pause (2, hard= True)
    scene weird (17)
    $ renpy.pause (5, hard= True)

    play sound "audio/sound/gy.mp3"
    scene weird (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weird (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    $ persistent.damian_triggered = False
    $ renpy.quit()
    return





label first_fight:

    scene black with fade
    "В комнате тихо, единственный свет исходит из окна."

    play music "audio/music/Kitsune.mp3"
    scene storyevent1 (7) with dissolve
    "Кицунэ парит посреди твоей комнаты, её хвост лениво подрагивает, пока золотистые глаза наблюдают за тобой."
    k "У тебя, знаешь ли, неплохо получается."
    mc "…Неплохо получается?"
    scene storyevent1 (6) with dissolve
    k "Ага. Твоя сила наконец начала формироваться, и ты и правда разговариваешь с девчонками из класса, а не дуешься в углу."
    scene storyevent1 (7) with dissolve
    k " Я бы назвала это прогрессом."
    mc "Спасибо, наверное…"
    k "Так, скажи мне — что ты думаешь о каждой из них на данный момент?"

    "Ты моргаешь, захваченный врасплох внезапным вопросом."

    mc "Эм, ну, полагаю—"
    scene storyevent1 (2) with hpunch
    k "Хотя, погоди, неважно. Мне на самом деле не так уж интересно."
    mc "Ого. Спасибо, что впустую потратила мои силы."
    scene storyevent1 (5) with dissolve
    k "Важно то, что ты строишь связи. Отношения. Вот что имеет значение."

    "Кицунэ выпрямляется, её выражение обостряется, голос наполняется волнением."
    scene storyevent1 (7) with dissolve
    k "А значит… ты наконец готов пройти проверку."
    mc "Звучит зловеще. Что именно ты имеешь в виду?"
    scene storyevent1 (9) with dissolve
    k "Просто. Ты идёшь в патруль. Пора найти кого-нибудь, кого можно поколотить."
    mc "…Прости, что?"
    scene storyevent1 (3) with dissolve
    k "Не смотри так встревоженно. Лучший способ научиться пользоваться силой — использовать её на практике. Считай это… полевой тренировкой."
    mc "Полевая тренировка звучит очень похоже на «нападение»."
    scene storyevent1 (7) with dissolve
    k "Семантика. К тому же ты будешь избивать только плохих парней."
    mc "Не думаю, что это сработает в суде."
    scene storyevent1 (1) with dissolve
    k "Что такое суд?"
    mc "..."
    scene storyevent1 (14) with dissolve
    mc "Ладно. Так что дальше? Мне полагается плащ? Маска? Может, трико?"
    scene storyevent1 (12) with dissolve
    k "Не совсем. Но тебе понадобится новая форма."
    scene storyevent1 (11) with dissolve
    mc "О боже, серьёзно?"
    scene storyevent1 (12) with dissolve
    k "Ты правда хочешь, чтобы твою личность рассекретили, пока ты используешь свои силы?"
    mc "Полагаю, в этом есть смысл."
    scene storyevent1 (7) with dissolve
    stop music fadeout 1.0
    k "Теперь сядь поудобнее и дай мне поколдовать."

    play music "audio/Music/reveal.mp3" volume 1.0
    play sound "audio/Sound/beam.mp3"
    scene storyevent1 (19) with flash
    "Кицунэ поднимает палец к потолку. Над головой расцветает сияющий свет, тёплый и ослепляющий."
    scene storyevent1 (18) with dissolve
    mc "Эм, что именно ты дела-"

    play sound "audio/sound/powerup.mp3" volume 1.0
    scene storyevent1 (20) with dissolve
    "Прежде чем ты успеваешь среагировать, твоя одежда начинает мерцать — нити распускаются в чистый свет."

    play sound "audio/sound/flash.wav" volume 1.0
    scene storyevent1 (21) with flash
    "В мгновение ока сияние гаснет… оставляя тебя облачённым в полный комплект доспехов."
    "Блестящий, пластинчатый и до нелепости вычурный."
    mc "…Ты, должно быть, шутишь."
    k "Узри! Это не просто доспехи. Это костюм поколений — который носили пользователи Сияния с древних времён. Каждая пластина выкована с—"
    scene storyevent1 (22) with dissolve
    stop music 
    mc "Я это не надену."
    play sound "audio/Sound/bop2.mp3"
    k "Чт-"
    play sound "audio/Sound/deathbell.mp3"
    scene storyevent1 (22) with hpunch
    k "Ты о чём вообще?!"
    scene storyevent1 (23) with dissolve
    mc "Это отстой. И даже лицо не закрывает."
    mc "Как-то не выполняет свою функцию, не находишь?"
    scene storyevent1 (22) with dissolve
    k "Это священная реликвия! Нельзя просто назвать её отстойной!"
    scene storyevent1 (23) with dissolve
    mc "А вот и назову. Отказываюсь ходить, будто я на ролевой по D&D."
    k "Ты невыносим…"
    scene storyevent1 (24) with dissolve
    mc "Извини, но верни меня обратно. Сейчас же."
    "Кицунэ что-то бормочет себе под нос."
    play sound "audio/sound/flash.wav" volume 1.0
    scene storyevent1 (25) with flash
    "Она щёлкает пальцами. Доспехи растворяются в искрах света, исчезая в никуда."
    scene storyevent1 (26) with hpunch
    play sound "audio/sound/bong.mp3" volume 1.0
    mc "..."
    mc "Я сейчас голый, да?"
    k "...{w}Возможно."
    scene storyevent1 (27) with dissolve
    mc "Ты специально это сделала."
    "Кицунэ невинно улыбается."
    k "Ты о чём вообще?"
    scene storyevent1 (25) with dissolve
    mc "(Уф, видимо, придётся справляться самому..)"

    mc "(Посмотрим, что я смогу придумать.)"
    scene black with fade
    "Ты роешься в своём шкафу, ищя хоть что-то, из чего можно собрать более-менее приличный костюм."

    mc "Наверное, сойдёт."
    play music "audio/music/mysterious.mp3" volume 1.0
    scene storyevent1 (28) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/pants.mp3"
    scene storyevent1 (29) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/belt.mp3"
    scene storyevent1 (30) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/gloves.mp3"
    scene storyevent1 (31) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/jacket.mp3"
    scene storyevent1 (32) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/hood.mp3"
    scene storyevent1 (33) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    scene storyevent1 (34) with fade
    $ renpy.pause(1, hard=True)
    pause 1
    play sound "audio/Sound/mask.mp3"
    scene storyevent1 (35) with dissolve
    $ renpy.pause(1, hard=True)
    pause 1
    scene storyevent1 (36) with dissolve
    $ renpy.pause(1, hard=True)
    pause 1
    scene storyevent1 (37) with dissolve

    mc "Хм, неплохо. Учитывая, что у меня было немного материала."

    scene storyevent1 (38) with dissolve

    mc "Ну, что думаешь?"
    scene storyevent1 (39) with dissolve

    k "Ты выглядишь как школьный стрелок."
    scene storyevent1 (40) with dissolve

    mc "И зачем я вообще тебя спросил?"

    scene storyevent1 (41) with dissolve

    mc "Слушай, ты мне не особо много дала для работы."

    mc "Что мне вообще делать там снаружи?"
    scene storyevent1 (42) with dissolve

    k "Узнаешь, когда перестанешь ныть и реально выйдешь из комнаты."

    scene storyevent1 (43) with dissolve

    mc "Господи...иногда я тебя ненавижу."

    k "Знаю!"

    scene black with fade
    play ambient "audio/ambient/raincity.mp3"
    "Ты выбираешься через окно на край крыши многоквартирного дома."

    scene storyevent1 (47) with dissolve
    "Город гудит внизу, неоновые огни мерцают сквозь дождь. Ты приседаешь на карнизе здания, холодный ветер треплет твою куртку."
    scene storyevent1 (45) with dissolve
    "Капли стекают по твоей маске, искажая свечение улиц далеко под ногами. Ты крепче сжимаешь край, мысли тяжелеют, закручиваясь по спирали."
    mc "(Что я вообще, чёрт возьми, тут делаю?)"
    "Вопрос повисает в голове, как лезвие, острый и неумолимый."
    scene storyevent1 (46) with dissolve
    "Хорошего ответа нет — ни героической речи, ни благородной причины, которая бы всё объяснила."
    mc "(Кроме того, что, наверное, выгляжу до чёртиков круто.)"

    mc "(Это правда должен быть первый шаг? Мне просто нужно ждать, пока что-то произойдёт?)"
    scene storyevent1 (47) with dissolve

    "Ты вглядываешься в огни города, будто пустота зовёт тебя к себе."
    scene storyevent1 (48) with dissolve
    mc "..."

    mc "Ого. Я выше, чем думал."
    play sound "audio/Sound/flash.wav"
    scene storyevent1 (49) with flash

    "Внезапно на твоих плечах вспыхивает свет, который тебе уже до боли знаком."
    scene storyevent1 (50) with flash

    k "Вуху! Ебать да! Пойдём кого-нибудь бить!"
    scene storyevent1 (51) with dissolve

    k "Мы так надерём задниц!"
    scene storyevent1 (53) with dissolve

    k "Ху! Ха! Хия!"

    "Кицунэ неумело изображает какие-то каратэ-движения."

    mc "..."

    mc "Ты закончила?"

    k "Нет...но ради тебя я возьму себя в руки."

    mc "Можешь просто сказать мне, с кем я дерусь и почему я так высоко?"
    scene storyevent1 (55) with dissolve

    mc "Господи, ты, наверное, худший духовный наставник на свете."

    k "Эй! Мне обидно это слышать!"

    scene storyevent1 (56) with dissolve

    k "И если хочешь знать, ты сейчас в очень удобной точке обзора, чтобы видеть, что происходит в городе."

    k "Так что пора начинать мою супер-специальную программу тренировок!"
    scene storyevent1 (58) with dissolve

    k "Так что слушай внимательно, новичок!"
    scene storyevent1 (57) with dissolve

    k "Первый урок ночи: выбери лёгкую цель."

    mc "Лёгкую цель?"
    scene storyevent1 (59) with dissolve

    k "Ага! Кого-то, с кем ты реально сможешь справиться."
    scene storyevent1 (60) with dissolve

    k "Типа подростка, пытающегося стащить кошелёк у бедной женщины..."
    scene storyevent1 (57) with hpunch
    k "Или буйного наркомана на кокаине!"
    mc "...{w}Ты хочешь, чтобы я ходил и избивал наркоманов?"
    scene storyevent1 (58) with dissolve
    k "Я тут почитывала книжки, пока ты в школе. Они могут выдержать избиение и даже не почувствовать его!"

    mc "Я почти уверен, что это просто их болевые рецепторы отказали, это не делает это нормальным!"
    mc "К тому же, как-то паршиво драться с кем-то из-за такой мелочи."
    scene storyevent1 (57) with dissolve
    k "Пффф, персонажи в твоих книжках с рисунками постоянно так делают!"

    mc "Погоди, так вот что ты за книжки читаешь!?"
    scene storyevent1 (59) with dissolve

    k "Довольно умно с моей стороны провести исследование, да? Теперь я знаю все тонкости борьбы с преступностью!"

    "В этот момент тебе пришло в голову, что Кицунэ, возможно, не понимает концепцию комикса."

    scene storyevent1 (61) with dissolve

    k "Слушай, суть в том, что тебе нужно с чего-то начать."

    k "Не выходишь же ты в свою первую ночь сразу против другого Сияющего."

    mc "Наверное, тогда буду высматривать мелкие преступления."
    scene storyevent1 (58) with dissolve

    k "Молодец!"
    scene storyevent1 (62) with dissolve

    "Ты осматриваешь город, высматривая движение."

    k "Эй, кажется, я вижу там мужика, переходящего дорогу в неположенном месте. Мы могли бы его взять."

    k "Или вон тот парень, похоже, он тут просто слоняется!"

    scene storyevent1 (63) with dissolve

    "Ты пропускаешь болтовню Кицунэ мимо ушей и пытаешься найти настоящее преступление, происходящее в городе."

    mc "..."

    u "Помогите!!"

    scene storyevent1 (64) with dissolve

    "Что-то щёлкает в твоей голове, и тебя тут же тянет к определённому месту"

    mc "Там."

    "Ты замечаешь движение внизу — переулок, разрезающий пространство между двумя зданиями."

    scene storyevent1 (65) with dissolve

    "Трое парней прижимают девушку к стене, их голоса твёрдые и злые."

    "Девушка выглядит всего на пару лет старше тебя, она огрызается в ответ, но явно напугана."
    scene storyevent1 (68) with dissolve

    mc "Внимание. В переулке что-то похожее на домогательство."

    mc "Похоже, всё может обернуться плохо."

    k "Хм...как жаль..."

    k "В любом случае, тебе стоит продолжить поиски-"
    scene storyevent1 (69) with dissolve

    mc "Ты вообще о чём?! Она явно в беде!"

    scene storyevent1 (71) with dissolve

    k "Ага, и их там явно трое, к тому же похожи на бандитов."
    scene storyevent1 (70) with dissolve

    k "Это слишком опасно для первой миссии. Мы найдём кого-то попроще—"

    scene storyevent1 (72) with hpunch

    "Девушка издаёт отчаянный сдавленный крик."

    u "П-помогите! Кто-нибудь!"

    mc "Нет времени!"
    play sound "audio/Sound/hood.mp3"

    scene storyevent1 (73) with dissolve

    mc "Я не собираюсь сидеть и ждать, пока кто-то зовёт меня на помощь, Кицунэ."

    k "Может, ты меня всё-таки послушаешь?!"

    k "Ты сейчас ринешься прямиком в конфликт, о котором вообще ничего не знаешь, против трёх взрослых мужчин!"

    k "У тебя есть хоть подобие плана?!"

    k "Ты ещё не выучил ни одного приёма!"

    scene storyevent1 (74) with dissolve

    "Ты отводишь взгляд, немного смущённый, но всё ещё упрямый."

    mc "Я-я разберусь по ходу дела."

    mc "Сейчас главный приоритет — спасти эту женщину."

    k "Просто подожди секу-"
    scene storyevent1 (75) with dissolve
    play sound "audio/Sound/jump.mp3"

    "Ты спрыгиваешь с балкона, прежде чем Кицунэ успевает возразить дальше."
    stop music fadeout 1.0
    scene black with fade
    "Слабый ветер бросает дождь тебе в лицо, пока ты падаешь. Но ты остаёшься собранным."
    play music "audio/music/tense.mp3"
    play sound "audio/Sound/hoodie.wav"
    scene storyevent1 (76) with hpunch
    "Один из бандитов хватает девушку и зажимает в удушающий захват."

    thg1 "Чёрт тебя дери, сука!"

    thg1 "Просто скажи нам, кто он такой!"

    u "Отвали от меня на хрен!"
    play sound "audio/Sound/puddle.mp3"
    scene storyevent1 (77) with vpunch

    "Ты сильно ударяешься о землю, но умудряешься приземлиться, не покалечившись."
    "Вода расплёскивается у твоих ног, отражая яркие неоновые огни вокруг."
    scene storyevent1 (78) with dissolve

    thg1 "Эй! Ты кто вообще такой?"

    mc "..."
    scene storyevent1 (79) with dissolve

    thg1 "Эй! Пацан! Я с тобой разговариваю!"
    $ renpy.music.set_volume(0.01)
    mc "Если тебе дорога твоя жизнь..."
    scene storyevent1 (80) with dissolve

    mc "То я тебя умоляю..."
    play sound "audio/Sound/flash2.mp3"
    scene storyevent1 (81) with flash

    mc "Отпустить её."

    scene storyevent1 (82) with dissolve
    tg2 "Это что за хрень—?!"
    tg3 "Он откуда вообще взялся?!"
    $ renpy.music.set_volume(1.0)
    thg1 "С крыши, похоже…"
    "Напряжение бандитов немного спадает. Понимая, что он, вероятно, легко справится с этой ситуацией."
    thg1 "У тебя есть яйца, пацан. Или тяга к смерти."
    scene storyevent1 (95) with dissolve
    thg1 "Эта девчонка знает кое-какую очень важную инфу, которая нам нужна."

    thg1 "А ты, похоже, слегка не по зубам себе кусок откусил."

    scene storyevent1 (99) with dissolve

    mc "(Ну, тут он не ошибся. Как бы это всё ни закончилось, я вижу только плохой исход для нас.)"

    mc "(Но да пофиг, Кицунэ хотела, чтобы я был героем. Значит, получит именно это.)"

    scene storyevent1 (104) with dissolve

    mc "Неважно, вы явно собираетесь причинить ей вред."
    scene storyevent1 (90) with dissolve
    mc "А я не могу просто сидеть и позволить этому случиться."
    "Лицо бандита искажается в оскале, явно раздражённый твоей настойчивостью."
    scene storyevent1 (82) with dissolve
    thg1 "Пффф. Скажи мне — кем ты вообще себя возомнил?"

    mc "Имя не важно."

    thg1 "Смелые слова для того, кто только что свалился в мой переулок."
    scene storyevent1 (83) with dissolve
    thg1 "Вы двое его раньше видели?"
    tg2 "Не-а. Не из наших районов."
    tg3 "Но одет слишком чисто для уличного отребья."
    scene storyevent1 (82) with dissolve
    thg1 "Хмф."
    thg1 "Тогда ответь мне вот на что: ты из {i}Цербера{/i}?"



    scene storyevent1 (87) with dissolve
    mc "Цербер? Кто вообще такой этот Цербер?"

    scene storyevent1 (85) with dissolve
    mc "Йо, Кицунэ, это ведь ты у нас с ответами. У тебя есть идеи?"
    scene storyevent1 (91) with dissolve
    k "Не смотри на меня. Я вообще никогда не слышала этого имени."
    mc "Отлично. Реально полезно."
    scene storyevent1 (108) with hpunch
    k "Это ты идиот, который спрыгнул сюда без всякого плана!"
    scene storyevent1 (86) with dissolve
    mc "И что мне было делать, дать им напасть на неё?"
    scene storyevent1 (104) with dissolve
    thg1 "Эй! Я задал тебе вопрос. Ты из Цербера или нет?"
    thg1 "Не строй из себя дурака. Только они стали бы совать нос на нашу территорию."
    scene storyevent1 (83) with dissolve
    tg2 "Босс, если он из Цербера, это плохие новости."
    tg3 "Ага, никто не хочет проблем с ними."
    thg1 "Вот почему я хочу, чтобы он сказал это мне в лицо."
    scene storyevent1 (103) with dissolve


    menu:
        "Как ответить насчёт Цербера?"
        "Сказать, что ты из Цербера":
            scene storyevent1 (104) with dissolve
            mc "Да… Я из Цербера. Так что отвалите."
            thg1 "Тц… Значит, правда. Цербер присылает какого-то щенка, чтобы что-то доказать?"
            scene storyevent1 (83) with dissolve
            tg2 "Босс, может, лучше нам просто уйти—"
            tg3 "Или, может, лучше выпотрошить его и передать им сообщение."
            mc "(Чёрт...{w} наверное, это была плохая идея.)"
            scene storyevent1 (76) with dissolve
            thg1 "Это ты за этим стоишь, сука?"
            thg1 "Богом клянусь, если ты передала им сообщение, живой отсюда не выйдешь."
            u "Понятия не имею, кто этот парень! Клянусь!"
            scene storyevent1 (82) with dissolve
            mc "(Погоди, значит, она как-то связана с этим их Цербером?)"
            mc "(Чёрт, я реально влип по самые уши.)"
        "Сказать, что ты не из Цербера":


            scene storyevent1 (87) with dissolve
            mc "Нет. Я даже не знаю, что такое Цербер."
            scene storyevent1 (102) with dissolve
            k "Наконец-то. Честность."
            scene storyevent1 (104) with dissolve
            thg1 "Не ври мне, пацан. Никто не встаёт у нас на пути, если за ним нет подкрепления."
            scene storyevent1 (100) with dissolve
            mc "Значит, я никто, получается."
            scene storyevent1 (83) with dissolve
            tg2 "Босс, он блефует. Давайте просто свернём и уйдём."
            tg3 "Или, может, он говорит правду и просто достаточно туп, чтобы влезть."
            scene storyevent1 (85) with dissolve
            k "Вот это было бы точнее."
            scene storyevent1 (102) with dissolve
            mc "Заткнись."
    scene storyevent1 (84) with dissolve
    thg1 "Слушай, пацан, скажу это ещё раз."
    thg1 "Либо ты отступаешь..."
    scene storyevent1 (96) with dissolve
    "Бандит тянется за спину. У тебя ёкает сердце, когда ты понимаешь, что он собирается достать."
    play sound "audio/Sound/gunclick.wav"
    scene storyevent1 (97) with dissolve
    thg1 "Либо в тебе будет больше дырок, чем в соте."
    scene storyevent1 (98) with dissolve
    thg1 "Так что выбираешь, крутыш?"
    scene storyevent1 (88) with dissolve
    mc "(Чёрт! У него, блядь, пистолет.)"
    mc "(Что мне, нахрен, делать?! Всё пошло по пизде!)"
    scene storyevent1 (89) with dissolve
    k "Вот что я имела в виду под {i}не лезь без плана{/i}. "
    mc "Заткнись, нахрен! Что мне делать!?"
    k "Уходишь. Как он сказал. Доживёшь до следующего раза, чтобы снова сглупить."
    scene storyevent1 (103) with dissolve
    "Ты обдумываешь это. Это правда единственный оставшийся вариант?"
    scene storyevent1 (86) with dissolve
    mc "Ты же знаешь, я не могу просто уйти, Кицунэ. Это было бы неправильно."
    scene storyevent1 (108) with dissolve
    k "Да похер на правильность! Если ты здесь умрёшь, ты не сможешь спасти будущее!"
    k "И я не могу снова вернуться назад во времени!"
    scene storyevent1 (88) with dissolve
    mc "(Чёрт...Я правда сейчас здесь умру?)"
    mc "Пожалуйста. Помоги мне найти другой способ."
    scene storyevent1 (91) with dissolve
    k "Из всех моментов ты выбрал именно этот, чтобы перестать быть тряпкой."
    k "Ладно, есть один способ выбраться отсюда."
    scene storyevent1 (92) with dissolve
    k "Но сначала я хочу это услышать."
    mc "Услышать что?!"
    scene storyevent1 (107) with dissolve
    k "Что я была права! Не стоило тебе лезть в это без плана!"
    scene storyevent1 (89) with hpunch
    mc "Твою мать, сейчас правда время для этого!?"
    scene storyevent1 (105) with dissolve
    k "Если ты здесь умрёшь, я этого не услышу."
    scene storyevent1 (94) with dissolve
    k "Так что я просто хочу подстраховаться."
    mc "Охренеть, не поверить."
    scene storyevent1 (107) with dissolve
    mc "Ладно! Ты была права! Если будет следующий раз, я тебя послушаю!"
    scene storyevent1 (92) with dissolve
    k "Единственный способ выбраться без бега — это {i}обезоружить{/i} его."
    scene storyevent1 (93) with dissolve
    k "У тебя есть хоть что-нибудь — и я имею в виду {i}хоть что-нибудь{/i} — в карманах?"
    scene storyevent1 (85) with dissolve
    mc "Эм—"
    play sound "audio/Sound/coins.mp3"
    scene storyevent1 (110) with dissolve
    "Ты шаришь по карманам, пальцы нащупывают хоть что-то полезное."
    scene storyevent1 (85) with dissolve
    mc "Эм—монеты. Это всё, что у меня есть."
    k "Сойдёт."
    scene storyevent1 (92) with dissolve
    k "Слушай, это отнимет у меня много энергии. Так что я выйду из строя на остаток боя."
    scene storyevent1 (91) with dissolve
    k "Ты останешься сам по себе, так что будь {i}абсолютно{/i} уверен, что справишься."
    mc "Ладно...{w}я уверен..."
    scene storyevent1 (106) with dissolve
    k "Лучше бы тебе быть чертовски уверенным."
    scene black with fade
    "..."
    scene storyevent1 (111) with dissolve
    "Кицунэ хватает одну из монет, крепко сжимая её в руках."
    k "У тебя всего один выстрел с этим, так что не облажайся."
    k "Ну, была не была..."
    play sound "audio/Sound/powerup.mp3"
    scene storyevent1 (112) with dissolve
    "Её лицо искажается от усилия, крошечные руки дрожат, пока она вливает сияние в монеты."
    scene storyevent1 (115) with dissolve
    "Одну за другой она роняет монеты тебе в руку, их тепло обжигает кожу."
    "Последняя оставляет её дрожащей, её свечение слабо мерцает."
    mc "(Один шанс... нужно не облажаться.)"
    stop sound fadeout 1.0
    scene storyevent1 (116) with dissolve
    mc "Эй, дамочка, как тебя звали?"
    scene storyevent1 (122) with dissolve
    u "М-моё имя?"
    mc "Да, хотел бы узнать твоё имя."
    scene storyevent1 (123) with dissolve
    "Женщина замирает на секунду."
    scene storyevent1 (122) with dissolve
    u "Э-это Джианна..."
    scene storyevent1 (121) with dissolve
    G "Пожалуйста...просто беги...спасайся."
    scene storyevent1 (119) with dissolve
    G "Он не блефует. Я не хочу, чтобы тебя убили!"
    scene storyevent1 (125) with dissolve
    mc "Джианна, значит?"
    mc "Теперь это не просто незнакомка в беде… Теперь я тебя знаю."
    stop music fadeout 1.0
    mc "Это делает всё личным."
    play sound "audio/Sound/flash2.mp3"
    scene storyevent1 (126) with flash
    mc "И я не позволю этим парням тебя тронуть."
    play sound "audio/Sound/jump.mp3"
    play music "audio/Music/fightalley.mp3"
    scene storyevent1 (127) with hpunch
    "Резким взмахом запястья ты бросаешь монеты в воздух."
    play sound "audio/Sound/bang.mp3"
    scene storyevent1 (128) with flash
    "В тот же миг, как они покидают твою руку, вспыхивает свет — ослепляющий, обжигающий, будто миниатюрные солнца взрываются в переулке."
    "Бандиты вскрикивают, отшатываясь и закрывая глаза, пока сияние рикошетит от грязных стен, окрашивая всё в горящее золото."
    tg2 "Агх—! Да что за хрень?!"
    tg3 "Я ничего не вижу—!"
    G "Ч-что происходит?!"
    "Пистолет дрожит. На долю секунды прицел главного бандита сбивается от шока внезапной яркости."
label retry:
    if renpy.music.get_playing(channel="music") is None:
        play music "audio/Music/fightalley.mp3"
    play ambient "audio/ambient/running.mp3"
    scene storyevent1 (129) with hpunch
    mc "Вот он, шанс! Двигайся!"
    "Твои ноги срываются с места раньше, чем ты успеваешь подумать, ботинки бьют по асфальту."
    scene storyevent1 (130) with dissolve
    "Переулок расплывается вокруг тебя, каждый удар сердца отдаётся в ушах."
    "Бандит яростно моргает, пытаясь стабилизировать оружие, но свет всё ещё жжёт его зрение."
label qte1:
    scene storyevent1 (131) with dissolve
    play sound "audio/Sound/glitchy.mp3"

    scene qte1 (1) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (2) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (3) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (4) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (1) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (2) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (3) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte1 (4) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (131) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ result = renpy.call_screen("quicktime_button")

    if result:

        jump story1con1
    else:
        stop music
        stop ambient
        play sound "audio/Sound/gunshot.mp3"
        scene gameover1 (1) with flash
        scene gameover1 (2) with dissolve
        $ renpy.pause (2, hard= True)
        play sound "<from 1>audio/Sound/gameover.mp3"
        scene gameover1 (4) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene gameover1 (5) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene gameover1 (4) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene gameover1 (3) with quickdissolve
        $ renpy.pause (2, hard= True)
        call screen retry



label story1con1:
    stop ambient
    play sound "audio/Sound/thud.mp3"
    scene storyevent1 (132) with hpunch
    "Ты врезаешься в него, отбивая его руку в сторону, пока твоя рука тянется к пистолету."
    play sound "audio/Sound/gunshot.mp3"
    scene storyevent1 (133) with flash
    scene storyevent1 (133) with hpunch
    "Пистолет стреляет. Треск выстрела разрывает переулок, отдаваясь эхом от кирпичных стен."
    "Вспышка дула на миг ослепляет, жар обжигает твою щёку."
    "Хватка бандита ослабевает, и в этот отчаянный момент Джианна вырывается из его рук."
    "Она мчится по переулку так быстро, как только могут нести её ноги."
    scene storyevent1 (135) with dissolve
    thg1 "Нет—! Чёрт!"
    thg1 "Она сбежала!"
    scene storyevent1 (134) with dissolve
    thg1 "Ах ты, ублюдок мелкий… Теперь ты точно труп!"
    scene storyevent1 (136) with hpunch
    tg3 "Получай, мразь!"
    scene storyevent1 (10) with dissolve
    play sound "audio/Sound/glitchy.mp3"
    scene qte2 (1) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (2) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (3) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (4) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (1) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (2) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (3) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene qte2 (4) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (10) with quickdissolve
    scene storyevent1 (10) with quickdissolve
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ result = renpy.call_screen("quicktime2_button")

    if result:
        play sound "audio/Sound/jump.mp3"
        scene storyevent1 (141) with dissolve
        "Ты еле-еле успеваешь пригнуться от удара бандита."
        "(Господи! Это было опасно близко.)"
        jump story1con3
    else:
        play sound "audio/Sound/punch.mp3"
        scene storyevent1 (13) with hpunch
        "Резкий хруст разрывает воздух, когда один из бандитов впечатывает кулак тебе в челюсть."
        mc "—гхх!"
        scene storyevent1 (44) with dissolve
        "Ты отшатываешься назад, ботинки скрежещут по асфальту."
        scene storyevent1 (137) with dissolve
        play sound "audio/Sound/gunclick.wav"
        "Сквозь пелену ты различаешь, как главный бандит снова поднимает пистолет."
        "Ствол находит тебя, твёрдо и безжалостно."
        scene storyevent1 (140) with dissolve
        mc "Чёрт!"
        play sound "audio/Sound/glitchy.mp3"
        scene qte3 (1) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (2) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (3) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (4) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (1) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (2) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (3) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene qte3 (4) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        scene storyevent1 (140) with quickdissolve
        $ renpy.pause (0.001, hard= True)
        stop sound
        $ result = renpy.call_screen("quicktime2_button")
        if result:
            jump story1congun
        else:
            stop music
            stop ambient
            play sound "audio/Sound/gunshot.mp3"
            scene gameover2 (1) with flash
            scene gameover2 (5) with dissolve
            $ renpy.pause (2, hard= True)
            play sound "<from 1>audio/Sound/gameover.mp3"
            scene gameover2 (4) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene gameover2 (3) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene gameover2 (4) with quickdissolve
            $ renpy.pause (0.001, hard= True)
            scene gameover2 (2) with quickdissolve
            $ renpy.pause (2, hard= True)
            call screen retry


label story1congun:
    play sound "audio/Sound/gunshot.mp3"
    scene storyevent1 (138) with flash
    scene storyevent1 (139) with hpunch
    "Пистолет разражается оглушительным грохотом, вспышка дула окрашивает переулок в неистовый оранжевый."
    "Ты инстинктивно бросаешься в сторону, пуля рассекает воздух там, где мгновение назад была твоя грудь."
    mc "(Чёрт! Это было слишком близко.)"

label story1con3:
    play sound "audio/Sound/hoodie.wav"
    scene storyevent1 (142) with hpunch
    "Бандит с рыком врезается в тебя, ты снова хватаешь его за запястье, пытаясь вырвать пистолет."
    thg1 "И зачем ты вообще припёрся, а!? Думаешь, у нас не было причины для этого?"
    scene storyevent1 (171) with dissolve
    $ renpy.pause (1, hard= True)
    scene black with hpunch
    play sound "audio/Sound/thud.mp3"
    scene storyevent1 (144) with dissolve
    "Вы оба спотыкаетесь и жёстко падаете на землю. Бандит нависает над тобой, пока остальные тебя удерживают."
    thg1 "Думаешь, ты типа герой какой-то, а?!"
    thg1 "Ты обломал нам всё сегодня! Выплату, девчонку, всё!"
    thg1 "И теперь ты за это заплатишь!"
    scene storyevent1 (150) with hpunch
    "Ты хватаешь его за запястья, пальцы отчаянно впиваются, пытаясь оттолкнуть оружие."
    scene storyevent1 (146) with dissolve
    mc "(Чёрт возьми—он слишком сильный!)"

    mc "(Что мне делать!?)"

    mc "(Блин, [mcname]! Тебе нужно думать!)"
    mc "(Давай, думай!)"
    stop music
    play sound "audio/Sound/glitch1.ogg"
    scene thinknothing (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene thinknothing (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene thinknothing (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene thinknothing (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene thinknothing (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene thinknothing (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (147) with quickflash

    mc "(Что?)"
    mc "(Что это вообще было!?)"
    mc "(Не думай ни о чём...)"
    mc "(Что это вообще){nw=2}"

    play sound "audio/Sound/abomination.mp3"
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (145) with quickflash

    mc "(Аргх! Что вообще говорит мой мозг!?)"
    play sound "<from 0.1>audio/Sound/abomination.mp3"
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (147) with quickflash
    mc "(Высвободить?! Это вообще о чём?!)"
    mc "(Что за хрень я вообще высвобождаю?!)"
    play sound "<from 1>audio/Sound/abomination.mp3"
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (5) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (146) with quickflash

    mc "(Не думать ни о чём, потом высвободить!?)"
    mc "(Я не понимаю, что это значит!)"
    scene unleash (7) with quickflash
    play sound "audio/Sound/abomination.mp3"
    $ renpy.pause (0.001, hard= True)
    scene unleash (8) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (9) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (10) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (11) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (12) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (13) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (145) with quickflash
    mc "(Чёрт! Ладно!)"
    mc "(Н-не думать ни о чём...потом высвободить...)"
    scene storyevent1 (150) with dissolve
    "Твои руки дрожат под напряжением, каждый нерв кричит, пока ствол дюйм за дюймом опускается к твоему лбу."
    scene storyevent1 (149) with dissolve
    "Но ты успокаиваешься. Ты становишься безучастным к окружающему миру."
    scene black
    "Ты...{w}не думаешь...{w}ни о чём..."
    $ renpy.pause (2, hard= True)
    scene figure (1)
    $ renpy.pause (2, hard= True)
    play sound "audio/Sound/flash2.mp3"
    scene figure (2) with dissolve
    $ renpy.pause (2, hard= True)
    play sound "<from 2>audio/Sound/abomination.mp3"
    scene unleash (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (5) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (5) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene unleash (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    scene storyevent1 (148) with hpunch
    mc "Высвободить!"
    play sound "<from 0.6>audio/Sound/burn2.mp3"
    scene storyevent1 (151) with quickflash
    play ambient "audio/ambient/raincity.mp3" fadein 1.0
    "Ты чувствуешь, как волна жара проходит через твою руку, ты чувствуешь, как волна жара проходит через твою руку."
    scene storyevent1 (152) with hpunch

    thg1 "Аргхххх!"

    "Бандит воет от боли, хватаясь за обожжённую руку, пока пистолет выскальзывает из его хватки."
    play sound "audio/Sound/gundrop.mp3"
    scene storyevent1 (153) with vpunch
    mc "Уф!"
    scene storyevent1 (154) with dissolve
    mc "Ч...Что?"
    mc "(Пистолет? Он выронил пистолет?)"
    mc "(А значит...)"

    scene storyevent1 (162) with dissolve

    thg1 "Воу, э-эй, пацан… Полегче с этой штукой!"
    tg2 "Мы же просто дурачились, ясно? Не нужно так психовать!"
    scene storyevent1 (163) with dissolve
    tg3 "Ага, успокойся! Никому не обязательно тут страдать…"
    play music "audio/music/tense.mp3"
    play sound "audio/Sound/gunclick.wav"
    scene storyevent1 (155) with hpunch
    "Почти инстинктивно ты поднимаешь оружие и целишься в группу."
    mc "Н-назад! Я предупреждаю!"
    scene storyevent1 (156) with dissolve
    "Ты дрожащими руками держишь пистолет, руки трясутся под его весом."
    $ renpy.music.set_volume(0.01)
    play sound "audio/Sound/static.mp3"
    scene ptt (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (3) with quickflash
    scene ptt (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ renpy.music.set_volume(1.0)
    scene storyevent1 (157) with quickflash
    "Твоё дыхание срывается резкими вдохами, пот стекает по лбу."
    mc "(Я правда хочу этого? Я-я не убийца!)"
    $ renpy.music.set_volume(0.01)
    play sound "audio/Sound/static.mp3"
    scene ptt (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ renpy.music.set_volume(1.0)
    scene storyevent1 (157) with quickflash
    mc "(Мой палец на курке. Если я просто… нажму… всё будет кончено.)"
    $ renpy.music.set_volume(0.01)
    play sound "audio/Sound/static.mp3"
    scene ptt (4) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (5) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (7) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ renpy.music.set_volume(1.0)
    scene storyevent1 (158) with quickflash


    mc "(Но если не нажму… что тогда? Они на меня нападут?)"

    mc "(Господи, мои руки не перестают дрожать… я даже не знаю, смог бы я нажать на курок, даже если б захотел—)"
    $ renpy.music.set_volume(0.01)
    play sound "audio/Sound/static.mp3"
    scene ptt (1) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (2) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (3) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (5) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene ptt (7) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound
    $ renpy.music.set_volume(1.0)
    scene storyevent1 (161) with quickflash

    menu:
        "Нажать на курок":
            jump itdontmatterfool
        "Не нажимать на курок":

            jump itdontmatterfool

label itdontmatterfool:

    scene storyevent1 (164) with dissolve
    "Бандит с пистолетом осторожно делает шаг вперёд, медленно поднимая руки."

    thg1 "Полегче, пацан… Ты не выстрелишь. Я вижу это по твоим глазам."
    thg1 "Просто брось его, и мы все выйдем отсюда живыми-"
    stop music
    play sound "audio/Sound/headshot.mp3"
    scene storyevent1 (165) with hpunch

    "Оглушительный выстрел разрывает переулок."
    play sound "audio/Sound/thud.mp3"
    scene storyevent1 (166) with vpunch

    "Он мгновенно падает, ударяясь об асфальт с тошнотворным стуком."
    scene storyevent1 (167) with dissolve
    tg2 "Б-блядь, он мёртв!!"
    tg3 "Бежим! БЕЖИМ!!"
    scene storyevent1 (168) with dissolve
    "Двое других мчатся в тень, их панические шаги эхом разносятся в ночи."
    "Ты сидишь неподвижно, пистолет всё ещё в твоей руке."
    scene storyevent1 (169) with dissolve
    mc "(Нет...Нет...)"
    mc "(…Я… в него выстрелил?)"
    play sound "audio/Sound/gunrattle.mp3"
    scene storyevent1 (170) with dissolve
    mc "(Нет. Нет, я—я не помню, чтобы нажимал на курок. Это я сделал? Или кто-то другой…?)"
    mc "(Здесь никого больше нет...я-)"
    play sound "audio/Sound/gundrop.mp3"
    scene storyevent1 (143) with dissolve
    "Мир кренится и вращается, пока твой разум раскалывается под тяжестью только что произошедшего."
    scene storyevent1 (172) with dissolve
    mc "(О боже… о боже, о боже, о боже… Что я наделал?)"
    mc "(Н-нет… нет нет нет нет нет—)"
    "Труп на земле искажается в твоём восприятии, глаза смотрят на тебя, обвиняюще, не моргая."
    scene storyevent1 (173) with dissolve
    "Ты опускаешь взгляд."
    stop ambient fadeout 12.0
    scene storyevent1 (174) with dissolve
    $ renpy.pause (1, hard= True)
    pause 1
    play sound "audio/Sound/earringing.mp3"
    scene storyevent1 (175) with dissolve

    "Она покрывает твои ладони."
    scene storyevent1 (176) with dissolve
    "Твои пальцы."
    scene storyevent1 (177) with dissolve
    "Просачивается в линии твоей кожи."
    scene storyevent1 (178) with dissolve

    mc "Я не стрелял...{w}Я не стрелял...{w}"

    scene storyevent1 with vpunch
    mc "Я-я...Я не..."
    play sound "audio/Sound/revolver.wav"
    scene storyevent1 (179)

    "{i}щёлк{/i}"

    u "На твоём месте я бы не двигался."
    play sound "audio/Sound/thunder.mp3"
    play ambient "audio/ambient/raincity.mp3"
    scene storyevent1 (180) with flash
    $ renpy.pause (1, hard= True)
    pause 1
    scene storyevent1 (181) with dissolve
    "Фигура возвышается над тобой — облачённая в чёрное, лицо скрыто под длинной маской чумного доктора."
    "Клюв поблёскивает в неоновой дымке переулка."
    u "Хм...так вот кем ты стал."
    scene storyevent1 (182) with dissolve
    u "Ну и хрень же ты устроил…"
    u "Кровь на руках, тело у ног…"
    scene storyevent1 (181) with dissolve
    u "Останешься здесь — и полиция будет на тебе раньше, чем пройдёт час."

    mc "..."
    scene storyevent1 (183) with dissolve
    u "Слушай, если тебе дорога твоя хрупкая жизнь…"
    u "…тебе нужно встать и исчезнуть."
    scene storyevent1 (184) with dissolve
    u "Иди через задний переулок, там нет камер."
    scene storyevent1 (185) with dissolve
    "Он уходит в тень, каждый шаг медленный и обдуманный, пока его фигура полностью не растворяется во тьме."
    u "До нашей следующей встречи, [mcname]."
    scene storyevent1 (186) with dissolve
    mc "..."
    scene storyevent1 (187) with dissolve
    mc "...{w}Мне нужно...{w}исчезнуть..."
    scene storyevent1 (188) with dissolve
    "Ты пошатываясь встаёшь на ноги, ноги дрожат под тобой."
    "Грудь сдавливает, лёгкие горят, но адреналин заставляет тебя двигаться."
    play sound "audio/ambient/running.mp3"
    scene storyevent1 (190) with dissolve
    "Не раздумывая больше, ты срываешься на бег, вырываясь из переулка на городские улицы, отчаянно желая оставить этот кошмар позади."
    scene black with fade

    stop sound fadeout 1.0
    stop ambient fadeout 1.0
    "Твои ноги не останавливаются, пока неон не остаётся позади."
    "К тому моменту, как ты добираешься до квартиры, лёгкие горят, тело тяжёлое, каждый шаг приближает тебя к обмороку."
    "Ты даже не пытаешься прятаться, вместо этого проходишь через входную дверь и по коридору."
    "К счастью, уже так поздно, что тебя никто не замечает."
    play sound "audio/Sound/dooropen.wav"
    "Ты мчишься в спальню и начинаешь яростно оттирать с себя кровь."
    play music "audio/Music/sad.mp3"
    scene storyevent1bed (1) with dissolve
    "Спустя несколько минут тебе удаётся немного успокоиться. Позади тебя появляется Кицунэ."
    scene storyevent1bed (2) with dissolve
    k "Ладно, п-признаю, могло пройти и лучше."
    scene storyevent1bed (4) with dissolve
    k "Но эй, это же просто часть пути, понимаешь?"
    k "Главное, что мы можем взять то, чему научились сегодня."
    scene storyevent1bed (3) with dissolve
    k "И...эмм..."
    scene storyevent1bed (4) with dissolve
    k "Двигаться дальше отсюда, наверное!"
    mc "..."
    scene storyevent1bed (7) with dissolve
    k "Слушай, это было тяжело. Но ты выжил. Для меня это уже победа."
    scene storyevent1bed (4) with dissolve
    k "Так что мы отдохнём, перезагрузимся, а завтра—"

    mc "Я закончил."
    scene storyevent1bed (7) with hpunch

    k "Ч-что простите!?"
    scene storyevent1bed (10) with dissolve

    mc "Я закончил, Кицунэ. Я не могу это делать."

    scene storyevent1bed (11) with dissolve

    k "Ты не можешь просто взять и бросить!? Так это не работает!"

    k "А как же спасение мир-"
    scene storyevent1bed (10) with dissolve

    mc "У меня в руках был пистолет. Человек мёртв. Я чуть не умер. Я это делать не буду."
    scene storyevent1bed (8) with dissolve
    k "Так вот и всё? Ты просто сдашься?"
    k "Ты позволишь всем своим друзьям умереть, потому что ты слишком трус."
    scene storyevent1bed (12) with dissolve
    mc "Я же говорил тебе, я не тот, кем ты меня считала."

    mc "Я слабый. Я чуть не умер на своей первой миссии."

    mc "Я не могу никого спасти. Так зачем пытаться?"
    scene storyevent1bed (5) with dissolve

    "Кицунэ выглядит отвращённой тем, что слышит."

    k "У тебя на кончиках пальцев вся сила мира."

    k "А ты всё это выбрасываешь, чтобы сдаться и снова стать тем же неудачником, каким был раньше."
    scene storyevent1bed (6) with dissolve

    k "Мне стоило понять, что ты сдающийся тип. Но я думала, конец света хотя бы остановит тебя от выбора лёгкого пути."
    scene storyevent1bed (15) with hpunch
    mc "Не корми меня этой хернёй!"

    mc "Думаешь, сдаваться для меня легко!? Это не так. Это ад!"
    scene storyevent1bed (16) with dissolve
    mc "Не смей вести себя так, будто сдаться — это какой-то лёгкий путь!"
    scene storyevent1bed (17) with hpunch
    mc "Да что ты вообще знаешь обо мне!?"

    mc "Знаешь, в чём был бы лёгкий путь? Думать, что я могу сделать то, что ты сказала!"
    play sound "audio/Sound/powerup.mp3"
    scene storyevent1bed (19) with dissolve
    mc "Думать, что я должен спасти мир, а потом сдохнуть где-нибудь в переулке!"
    mc "Умереть, веря, что я какой-то герой в твоей ебанутой фантастической истории!"
    scene storyevent1bed (20) with dissolve
    mc "Я не, блядь, герой, я не хочу быть каким-то там героем!"
    scene storyevent1bed (21) with dissolve
    mc "Так что просто вали обратно туда, откуда, чёрт возьми, пришла-"
    play ambient "audio/Sound/beam.mp3"
    scene storyevent1bed (22) with flash
    mc "И оставь меня в покое!"
    play sound "audio/Sound/floorbreak.mp3"
    scene storyevent1bed (23) with flash
    scene storyevent1bed (23) with vpunch
    stop ambient
    "Вспышка ослепляющего света вырывается из твоей руки, прожигая пол обжигающим лучом."
    scene storyevent1bed (24) with dissolve
    "Земля раскалывается, дымясь, пока в досках пробивается рваная дыра."
    "Земля раскалывается, дымясь, пока в досках пробивается рваная дыра."
    scene storyevent1bed (25) with dissolve
    mc "..."
    scene storyevent1bed (26) with dissolve
    mc "Я не тот, кем ты меня считаешь. И никогда им не буду."
    scene storyevent1bed (27) with dissolve
    mc "Так что советую и тебе с этим смириться."
    scene storyevent1bed (28) with dissolve
    stop music fadeout 1.0
    k "..."
    k "[mcname]..."

    scene storyevent1bed (29) with dissolve
    k "…Заткнись."
    play music "audio/Music/creepy.mp3"
    scene storyevent1bed (30) with fade
    k "Хватит быть жалким."

    k "Думаешь, я протащила себя через всё это, только чтобы слушать твоё нытьё о том, что ты сдаёшься?"
    k "Я не собираюсь умирать из-за тебя. Не собираюсь."
    play sound "audio/sound/glitch3.ogg"
    scene storyevent1bed (44)
    $ renpy.pause (0.1, hard= True)
    scene storyevent1bed (30)
    $ renpy.pause (0.1, hard= True)
    scene storyevent1bed (44)
    $ renpy.pause (0.1, hard= True)
    stop sound
    scene storyevent1bed (31)
    k "Если до этого дойдёт..."

    k "Я лучше буду смотреть, как ты умираешь в переулке, словно пёс, чем увижу, как ты уползаешь и сдаёшься."

    k "Так что хватит колебаться. Дыши. И двигайся вперёд."

    k "Мне плевать, насколько ты напуган. Мне плевать, насколько сильно ты меня сейчас ненавидишь."
    k "Тебе нельзя останавливаться. Не сейчас. Никогда."
    k "И не притворяйся, что боишься умереть сейчас."
    k "Если бы я не пришла к тебе той ночью…{w} мы оба знаем, куда бы ты пришёл."
    play sound "audio/Sound/beep.mp3"
    scene storyevent1bed (32)
    $ renpy.music.set_volume(0.1)
    $ renpy.pause (1.3, hard= True)
    stop sound
    $ renpy.music.set_volume(1.0)
    scene storyevent1bed (31)
    k "Теперь ты понимаешь своё положение?"

    k "У{w} тебя{w} нет{w} вы{w}бора."

    scene storyevent1bed (33) with dissolve
    "Ты смотришь на пол, дрожа. В комнате тихо, если не считать твоего прерывистого дыхания."
    scene storyevent1bed (34) with dissolve
    "Горло сжимается, руки холодные."

    mc "…Л-ладно."
    scene storyevent1bed (35) with dissolve
    mc "Л-ладно, Кицунэ...я понимаю..."
    scene storyevent1bed (36) with dissolve
    k "Молодец."
    scene storyevent1bed (37) with dissolve
    k "Теперь… как насчёт заказать пиццу или типа того? Уверена, после всего этого ты проголодался."
    mc "..."
    scene storyevent1bed (38) with dissolve
    "Кицунэ отворачивается, но затем замирает."
    k "Ещё кое-что."
    scene storyevent1bed (39) with dissolve
    k "Я правда горжусь тобой, [mcname]."
    k "Ты справился сегодня без моей помощи. Это важно."
    mc "..."
    scene storyevent1bed (40) with dissolve
    k "И тебе не нужно волноваться."
    k "Я не позволю, чтобы с тобой что-то случилось. Обещаю тебе это."

    "Её голос теперь мягкий, почти нежный, но окутан памятью об её угрозе всего мгновение назад."

    "Тепло и жестокость смешиваются, пока ты уже не можешь сказать, что из этого настоящее."
    scene storyevent1bed (41) with dissolve
    mc "(Она права.)"
    mc "(Если я сейчас сдамся, то всё это… всё… было напрасно.)"
    scene storyevent1bed (42) with dissolve
    mc "(Ненавижу это. Но она права… я не могу остановиться. Не сейчас.)"
    scene storyevent1bed (43) with dissolve
    mc "(…У меня нет выбора.)"
    scene black with fade
    stop music fadeout 1.0
    $ renpy.pause (3, hard= True)
    window hide 
    pause 1
    $ firstfight = 1
    if yukibook2event == 1:
        $ Yuki.quest = "Поговорить с Кицунэ о книгах Юки"
        $ main.quest = "Поговорить с Кайрой в школе."
        $ Kyra.quest = "Поговорить с Кайрой у школьных ворот."
    else:
        $ main.quest = "Поговорить с Кайрой в школе."
        $ Kyra.quest = "Поговорить с Кайрой у школьных ворот."

    jump day_cycle

















label thefirstdream:
    play music "audio/music/Nights.mp3"
    scene black with fade
    "Ты сидишь в своей комнате, снова слишком поздно, но какая уже разница."
    scene dreamroom (2) with dissolve
    k "Ты опять делаешь эту штуку."
    scene dreamroom (3) with dissolve
    mc "Какую штуку?"
    scene dreamroom (8) with dissolve
    k "Ту самую, «мёртвая рыба, глядящая в потолок, пока душа покидает помещение»."
    scene dreamroom (3) with dissolve

    mc "…Обхохочешься."
    scene dreamroom (55) with dissolve
    mc "Я кое-что нашёл, пока осматривал место преступления."

    "Ты лезешь в карман и достаёшь глянцевую карточку, протягивая её ей."

    mc "Тебе это кажется знакомым?"

    mc "Есть идеи, что такое «Chromark»?"
    scene dreamroom (56) with dissolve
    "Кицунэ тянется к карточке, её игривое выражение сглаживается во что-то нечитаемое, пока она берёт её."
    scene dreamroom (58) with dissolve
    "Она долго вглядывается в неё."
    scene dreamroom (57) with dissolve
    "Тишина в комнате тянется, становясь тяжёлой, пока её глаза скользят по пересекающимся линиям логотипа-глаза."

    k "..."
    scene dreamroom (59) with hpunch
    k "Понятия не имею, что это такое."

    mc "Чел, да брось."

    k "Извини, что разрушаю твои надежды, но, ну, хоть что-то уже есть."


    scene dreamroom (2) with dissolve
    mc "Что ж, если так..."
    mc "Я надеялся понять, что нам делать дальше."
    mc "Мы вообще знаем, кем был тот тип?"

    k "Мёртвый парень?"
    mc "Нет, тупица. Другой."
    scene dreamroom (5) with dissolve
    mc "Тот...{w} парень в маске чумного доктора."
    scene dreamroom (4) with dissolve
    mc "Он знал моё имя, Кицунэ..."
    scene dreamroom (15) with dissolve
    "Она на мгновение замирает, её манера слегка меняется."
    mc "Но хуже всего то...часть меня думает, что он кажется..."
    mc "Знакомым? Наверное?"
    mc "Не говоря уже про эту карточку, что вообще за хрень этот чёртов Chromark?"
    scene dreamroom (8) with dissolve
    k "В смысле, если ты хоть раз ходил на Хэллоуин выпрашивать сладости, уверена, ты бы видел кого-то, одетого как-"
    scene dreamroom (6) with dissolve
    mc "Нет, я не про его костюм... я про его…"
    scene dreamroom (7) with dissolve
    mc "Присутствие...{w} наверное..."
    mc "Но каждый раз, когда я пытаюсь об этом подумать, будто мой мозг вздрагивает, прежде чем я успеваю его вспомнить."
    scene dreamroom (13) with dissolve
    k "...."
    k "Это не есть хорошо..."
    k "Но и не плохо..."
    mc "Это вообще о чём должно говорить?"
    scene dreamroom (11) with dissolve
    k "Как ты знаешь, моя память туманна."
    k "Но я всё ещё помню важные вещи из своей временной линии."
    scene dreamroom (12) with dissolve
    k "Наш друг — чумной доктор — не из их числа."
    k "Так что либо он был неважен..."
    mc "Либо он как-то никогда не давал нам знать о своём присутствии..."
    scene dreamroom (16) with dissolve
    "Кицунэ кивает."
    k "Хорошая новость в том, что это значит, что мы реально видим изменения в будущем."
    scene dreamroom (15) with dissolve
    k "Плохая новость в том, что мы видим изменения, которые я не могу предсказать."
    mc "Блин, и какой мне тогда от тебя толк?"
    scene dreamroom (9) with dissolve
    k "Аккуратнее, неудачник. Тебе всё ещё нужны тренировки, помнишь."
    scene dreamroom (10) with dissolve
    k "И, к счастью, у меня всё ещё есть пара идей, как нам продолжить."
    mc "Тогда выкладывай, Кэ-Большая."
    scene dreamroom (19) with dissolve
    k "..."
    mc "..."
    mc "Что?"
    k "Никогда больше меня так не называй."
    mc "Предпочитаешь Кэ-Маленькая?"
    scene dreamroom (18) with dissolve
    k "Слушай, если где-то в твоей голове прячется воспоминание об этом парне, может, мы сможем его выкопать."
    mc "Ты собираешься...копаться у меня в голове?"
    scene dreamroom (11) with dissolve
    k "Пффф, нет, глупый."
    scene dreamroom (10) with dissolve
    k "Ты сам будешь там копаться!"
    scene dreamroom (4) with dissolve
    mc "Л-ладно..."
    mc "Ты имеешь в виду… что? Гипноз? Операцию на мозге? Лоботомию?"
    scene dreamroom (15) with dissolve
    k "Не совсем, я имею в виду что-то более похожее на... медитацию."

    mc "Медитацию."
    scene dreamroom (16) with dissolve
    mc "Ты вообще меня знаешь?"
    mc "Я буквально не могу спать."

    scene dreamroom (20) with dissolve
    k "Это не сон."
    k "Есть техника, которую используют некоторые Сияющие, когда их силы завязаны на памяти или травме."
    scene dreamroom (22) with dissolve
    k "Она не особо эффективна и невероятно опасна."
    k "Считай это... прогулкой по собственному разуму, как по коридору."
    scene dreamroom (1) with dissolve
    k "Открываешь двери. Проверяешь, какие из них причиняют боль. Смотришь, что прячется за теми, что ты держишь наглухо закрытыми."


    mc "…А что, если мне не понравится то, что я найду?"
    scene dreamroom (23) with dissolve
    k "Не понравится."
    k "Люди не хоронят хорошие вещи."
    scene dreamroom (20) with dissolve
    k "Вот почему я тебе говорю, что это не игра."
    k "Ты идёшь туда, зная, что тебе может не понравиться то, что ты притащишь обратно."
    scene dreamroom (1) with dissolve
    k "Ты идёшь туда, зная, что есть шанс, что выйдешь оттуда более потрясённым, чем был."
    scene dreamroom (20) with dissolve
    k "И всё же."
    scene dreamroom (22) with dissolve
    k "Ты всё равно идёшь туда… потому что альтернатива — ждать, пока этот тип в маске, или кто бы там на него ни работал, сделает следующий шаг."
    k "Ты всё равно идёшь туда… потому что альтернатива — ждать, пока этот тип в маске, или кто бы там на него ни работал, сделает следующий шаг."
    k "Я не собираюсь заставлять тебя нырять в собственный разум, особенно учитывая все риски."

    mc "С каких пор тебя вообще волнует, чтобы меня не заставлять?"

    scene dreamroom (21) with dissolve
    k "С тех пор, как это место, куда я не могу за тобой последовать."
    k "Там, снаружи, я могу тренировать тебя, жульничать и протянуть руку помощи."
    scene dreamroom (1) with dissolve
    k "Там, внутри..."
    k "Ты сам по себе."

    mc "…"

    scene dreamroom (14) with dissolve
    "Ты издаёшь резкий, горький смешок."

    mc "Ты правда умеешь продавать идеи."
    stop music fadeout 1.0
    scene dreamroom (16) with dissolve
    k "Слушай меня, [mcname]."
    k "Это твоё последнее предупреждение. Ты точно хочешь это сделать?"
    $ yes_clicked = 0
    window hide

    label yes_no_loop:

        $ no_clicked = 0

    window hide

    label yes_no_prompt:

        menu:
            "Да.":
                jump yes_accept
            "Нет.":

                jump no_refuse


    label no_refuse:

        play sound "audio/sound/s_kill_glitch1.ogg"
        $ renpy.pause(0.15)


        $ no_clicked += 1


        show layer master:
            truecenter
            zoom 1.0 + no_clicked * no_clicked * 0.07
            yalign 0.35

        show layer screens:
            truecenter
            zoom 1.0 + no_clicked * no_clicked * 0.07
            yalign 0.35


        if no_clicked < 6:
            jump yes_no_prompt
        else:
            jump yes_no_prompt


    label yes_accept:
    show layer master:
        zoom 1.0 yalign 0.5
    show layer screens:
        zoom 1.0 yalign 0.5


    scene dreamroom (28) with dissolve
    "Тишина повисает между вами. На этот раз Кицунэ её не заполняет."
    "Она просто смотрит на тебя, взгляд твёрдый, хвост неподвижен."
    scene dreamroom (29) with dissolve
    mc "…Ладно."
    scene dreamroom (30) with dissolve
    mc "Давай сделаем это. Я уже зашёл так далеко."
    "Кицунэ вздыхает. Будто знала, что ты выберешь именно это решение."

    k "Ладно. Давай сделаем это."
    play music "audio/music/reveal.mp3"
    play sound "audio/sound/flash.wav"
    scene dreamroom (31) with flash
    k "Узри, ответ на твои молитвы!"
    play sound "audio/sound/coins.mp3"
    scene dreamroom (32) with hpunch
    k "Реликвия, что приведёт тебя к тому, что ты ищешь!"
    stop music
    play sound "audio/sound/flash.wav"
    scene dreamroom (34) with flash
    "Свет вырывается из её рук, закручиваясь в тугую, вращающуюся спираль над твоей кроватью."
    play sound "audio/sound/pants.mp3"
    scene dreamroom (35) with hpunch
    "Он падает тебе на колени с тихим, антикульминационным стуком."
    scene dreamroom (36) with dissolve
    mc "..."
    scene dreamroom (37) with dissolve
    mc "Это же просто Бенадрил..."
    scene dreamroom (42) with dissolve
    "Кицунэ выглядит самодовольной, будто только что подарила тебе лучшее изобретение со времён нарезанного хлеба."
    k "Хмф."
    scene dreamroom (41) with dissolve
    k "Не обманывайся, это ключ к пробуждению твоего разума."
    mc "Я буквально принимал это сотни раз, меня от него в сон не клонит."
    scene dreamroom (40) with dissolve
    k "Ну, естественно, твоя биология Сияющего метаболизирует его иначе."
    k "Он не вырубит тебя — он смягчит грани. Ослабит замки. Облегчит скольжение внутрь себя, а не наружу."
    scene dreamroom (43) with dissolve
    mc "Звучит смутно сексуально."
    k "Уф, вытащи свои мысли из канавы."
    play music "audio/music/mysterious.mp3"
    scene dreamroom (38) with dissolve
    mc "Ты же не серьёзно сейчас предлагаешь мне передознуться Бенадрилом, чтобы я лучше медитировал."
    k "..."
    k "{i}«Передознуться»{/i} — это человеческое слово."
    scene dreamroom (48) with dissolve
    mc "Заткнись."
    mc "Я слышал про людей, которые умирали от такой хрени."
    scene dreamroom (37) with dissolve
    k "Ой, расслабься, ты не выпиваешь всю пачку."
    k "Просто больше, чем ты привык."
    scene dreamroom (49) with dissolve
    mc "Всё это звучит невероятно опасно."
    k "Ну да, для обычного человека так и есть."
    k "Но для тебя это ослабит шестерёнки, которые не крутились последние 10 лет."
    scene dreamroom (45) with dissolve
    mc "..."
    scene dreamroom (46) with dissolve
    mc "Да и хрен с ним, наверное."
    scene black with dissolve
    "Ты глотаешь таблетки, горло сжимается, в груди гудит коктейль из страха и смирения."
    k "Молодец."
    k "Теперь садись."
    play sound "audio/sound/hoodie.wav"
    scene dreamroom (50) with dissolve
    "Ты ложишься на кровать, пытаясь сесть прямо."
    stop music fadeout 1.0
    scene dreamroom (51) with dissolve
    "Кицунэ кладёт руку тебе на плечо, пытаясь тебя удержать."
    k "Ладно, помни, ты не пытаешься заснуть, ты просто пытаешься очистить разум."

    k "Закрой глаза. Сосредоточься на звуке."

    mc "На каком звуке? Тут гробовая тишина."
    scene dreamroom (52) with dissolve
    k "Именно. Сосредоточься на гуле тишины."
    k "Дай ему стать громче."
    scene dreamroom (53) with dissolve
    "Ты делаешь, как велено. Закрываешь глаза."
    scene dreamroom (54) with dissolve
    "Сначала это просто темнота твоих собственных век."
    scene black with dissolve
    "Затем накатывает ощущение."
    "Это не волна сонливости. Это физическое падение."
    "Будто пропустил ступеньку на лестнице в темноте."

    play sound "audio/sound/heartbeat.mp3"

    "Твоё сердце тяжело, одиноко стучит о рёбра."
    "Воздух в комнате внезапно становится густым, давит на кожу, как тёплая вода."

    mc "Кицунэ...?"

    k "Не разговаривай. Не закрепляйся здесь."
    k "Отпусти."
    k "Увидимся на той стороне, ладно?"

    "Её голос звучит неправильно. Отдалённо. Будто она говорит с тобой с другого конца длинной металлической трубы."
    "Химикаты попадают в кровоток, реагируя со спящей энергией внутри тебя."
    "Жжёт. Холодный, электрический зуд бежит по затылку."

    scene black with fade
    stop music fadeout 2.0

    "Кровать под тобой растворяется."
    "Гравитация выкручивается, хватает тебя за лодыжки и тянет вниз."
    "Вниз сквозь матрас."
    "Вниз сквозь половицы."
    play music "audio/music/drown.mp3" volume 0.4 fadein 1.0
    scene black with fade
    play ambient "audio/ambient/Underwater.mp3"

    scene dreamocean (1) with dissolve
    "Воздух превращается в жидкость."
    "Холодную. Тяжёлую. Обволакивающую."
    "Ты готовишься к удушью — жгущим лёгким, панике утопающего."
    "Но этого не происходит."

    scene dreamocean (2) with dissolve


    "Ты открываешь глаза."
    "Ты плывёшь в бескрайнем пространстве глубокой, тихой синевы."
    "Столбы солнечного света пронзают поверхность далеко наверху, танцуя, как ленты, в течении."
    scene dreamocean (4) with dissolve
    mc "Я... под водой?"


    "Ты дрыгаешь ногами, дрейфуя в невесомости. Спокойно."
    "Тише, чем в комнате. Тише, чем голос Кицунэ."
    "На мгновение ты забываешь, зачем ты здесь."
    scene dreamocean (6) with dissolve
    mc "Не так уж и плохо."
    mc "Если это мой разум... может, я более спокоен, чем думал."

    "Вода прохладная на коже. Она давит на тебя мягким, постоянным весом."
    "Ощущается как объятие от кого-то, кого ты не можешь толком вспомнить."
    scene dreamocean (8) with dissolve
    mc "Так тихо..."

    "Твои мысли, обычно спутанный клубок тревоги, страха и ответственности, начинают распутываться."
    "Они уплывают от тебя, как чернила в течении."
    "Человек в маске. Кицунэ. Тренировки. Страх быть слабым."
    "Здесь ничего из этого не имеет значения."
    "Здесь ты просто тело, парящее в синеве."
    scene dreamocean (9) with dissolve
    mc "Я мог бы просто... остаться здесь."
    mc "Совсем ненадолго."
    mc "Пусть мир крутится без меня пять минут."
    scene dreamocean (10) with dissolve
    "Ты снова закрываешь глаза, позволяя течению медленно тебя вращать."
    "Это опьяняет. Отсутствие ожиданий. Отсутствие боли."
    "Ты чувствуешь порыв открыть рот. Вдохнуть воду. Позволить ей заполнить тебя, пока ты не станешь просто частью океана."

    mc "Ага..."
    mc "Ещё пять минут..."
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with dissolve
    "..."
    "......"
    "Уют мгновенно портится."
    "Мягкое давление на коже внезапно ощущается тугим. Сжимающим."
    "Ты снова открываешь глаза..."
    play music "audio/music/drown2.mp3"
    play ambient "audio/ambient/darkocean.mp3"
    scene dreamocean (11) with hpunch
    play sound "audio/sound/heartbeat.wav" fadein 2.0

    "Синевы больше нет."
    "Вода не просто изменила цвет. Она изменила текстуру."
    "Она густая. Вязкая. Тёплая."
    "Она липнет к твоим пальцам, как сироп."
    "Вкус соли сменяется подавляющим, металлическим привкусом железа."
    scene dreamocean (13) with hpunch
    mc "Нет..."
    mc "Слезь с меня!"
    mc "Слезь с меня!"

    "Ты барахтаешься, пытаясь плыть вверх, но жидкость сопротивляется."
    "Она тянет твою одежду. Ощущается тяжёлой, будто плывёшь в мокром бетоне."
    "Каждое движение изматывает тебя."
    "Ты открываешь рот, чтобы закричать, но красная жидкость врывается внутрь, заставляя тебя давиться."
    "На вкус — как каждая ошибка, что ты когда-либо совершал."
    scene dreamocean (12) with dissolve
    "Ты пытаешься плыть к поверхности, но твои ноги как свинец."
    "Ты не плывёшь."
    "Ты тонешь."


    scene dreamocean (14) with dissolve
    "Гравитация берёт своё."
    "Ты кувыркаешься, падая в пустоту."
    "Глубже."
    "Глубже."
    "Пока красное не исчезает, и не остаётся ничего."
    scene black with fade
    "Ты падаешь."
    "Воздуха нет, только ревущий грохот жидкости, тяжёлой от железа."
    "Водопад крови."
    stop ambient 
    stop music
    scene black with hpunch
    play sound "audio/sound/Watersplash.mp3"

    "Ты жёстко ударяешься о твёрдую землю."
    "Удар выбивает из тебя весь воздух, ты хватаешь ртом воздух на холодном, шершавом полу."
    "Ты приподнимаешься, руки скользкие от красного."


    mc "Уф..."
    mc "Что за хрень?"
    mc "Где...?"
    mc "Кицунэ? У меня получилось?"

    "Ты стираешь кровь с глаз, пытаясь сфокусироваться на тенях по углам."
    "Здесь опасно. Тихо. Слишком тихо."
    "Ты напрягаешься, ожидая нападения."

    mc "Есть кто?"

    play music "music/gameshow.mp3" 

    "Внезапно—"
    "Начинает играть громкая, радостная музыка."
    "За которой следует голос из микрофона."
    u "ЙООООООО-ШИ! Готовы создавать воспоминания!?"
    play sound "audio/sound/spotlight.mp3" volume 1.5
    scene dreamgameshow (1) with flash
    $ renpy.pause(0.5, hard=True)

    play sound "audio/sound/clapsaudience.mp3" 


    "Ты закрываешь лицо, часто моргая от атаки неоновых синих и фиолетовых тонов."
    "Ты больше не в тусклой комнате. Ты стоишь за дешёвой пластиковой трибуной."




    "Что-то похожее на картонный вырез мужчины указывает прямо на камеру, принимая драматичную позу."
    scene dreamgameshow (3) with dissolve
    u "Добро пожаловать, добро пожаловать, добро пожаловать на единственное игровое шоу, которое проходит целиком внутри разрушающегося подсознания!"
    scene dreamgameshow (2) with dissolve
    u "Я ваш ведущий! Легенда! Изобретатель Драконьего супплекса! Шестикратный тяжеловесный чемпион IWGP..."
    scene dreamgameshow (4) with hpunch
    u "ТАЦУМИ! ФУДЗИНАМИ!"

    "Из ниоткуда взрываются консервированные аплодисменты. Он сияет, впитывая их."
    scene dreamgameshow (6) with hpunch
    mc "ЧТО ЗА ХУЙНЯ ЧТО ЗА ХУЙНЯ ЧТО ЗА ХУЙНЯ ЧТО ЗА ХУЙНЯ."
    scene dreamgameshow (7) with hpunch
    mc "ЧТО ВООБЩЕ, СУКА, ПРОИСХОДИТ СО МНОЙ ПРЯМО СЕЙЧАС!?"

    scene dreamgameshow (2) with dissolve
    "Фудзинами полностью тебя игнорирует."

    host "У нас сегодня потрясающее шоу! Простая игра из вопросов, ответов и экзистенциального ужаса!"
    scene dreamgameshow (5) with dissolve
    host "Давайте познакомимся с нашими участниками!"

    host "Участник номер один! Родом откуда-то из глубин твоего разума..."
    play sound "audio/sound/spotlight.mp3" volume 1.5
    play ambient "audio/sound/clapsaudience.mp3" 

    scene dreamgameshow (8) with flash
    host "КСАХВТАГКДЖ!"

    host "Очаровательно! Просто очаровательно! Уже любимец публики!"
    stop ambient fadeout 1.0


    scene dreamgameshow (5) with dissolve


    host "Участник номер два! Он мокрый, он растерянный, и он подавляееееет всё! Встречайте..."
    play sound "audio/sound/spotlight.mp3" volume 1.5
    play ambient "audio/sound/clapsaudience.mp3" 
    scene dreamgameshow (9) with flash
    host "[mcname]!"

    "Звучат редкие, неуверенные, вежливые аплодисменты."
    stop ambient fadeout 1.0
    "Твой разум снова начинает работать."
    mc "Погодите, стоп. Почему японский рестлер ведёт игровое шоу у меня в мозгу?"
    mc "Я даже рестлинг не смотрю."
    scene dreamgameshow (11) with dissolve

    host "Отличный вопрос!"
    scene dreamgameshow (12) with hpunch
    play sound "audio/sound/clapsaudience.mp3" 
    host "Это будет стоить тебе -50 очков!"
    scene dreamgameshow (5) with dissolve
    host "И, наконец, участник номер три!"
    host "Он буквально просто кот!"
    play sound "audio/sound/spotlight.mp3" volume 1.5
    play ambient "audio/sound/clapsaudience.mp3" 
    scene dreamgameshow (10) with dissolve

    "Прожектор перемещается направо от тебя."
    host "Это ПОПО!"
    mc "(Ну, он не соврал, это буквально просто, блин, кот.)"
    host "Посмотрите на эту сосредоточенность! Вот оно, лицо чемпиона!"
    scene dreamgameshow (13) with dissolve
    stop ambient fadeout 1.0
    "Фудзинами хлопает в ладоши, звук странно отдаётся эхом в студии."

    host "Теперь, я знаю, о чём вы спрашиваете!"
    host "Тацуми, за что играют эти счастливчики сегодня?"
    scene dreamgameshow (13) with dissolve
    mc "Я точно не собираюсь это спрашивать."
    $ renpy.music.set_volume(0.01)
    scene dreamgameshow (15) with dissolve
    play sound "audio/sound/drumroll.mp3" 
    host "Что ж, без лишних слов..."
    host "Главный приз сегодня..."
    play sound "audio/sound/tada.mp3" 
    play ambient "audio/sound/oooh.mp3" 
    scene dreamgameshow (38) with flash
    host "...Путёвка в один конец, все расходы оплачены..."
    stop ambient fadeout 0.5
    host "...Вниз по Коридору ТВОЕГО разума!"

    "Огромный прожектор освещает дверь наверху лестничного пролёта."
    "Тени двери, кажется, сочатся из-под неё."

    scene dreamgameshow (16) with dissolve
    mc "Хм. Кицунэ упоминала что-то про коридор, но я не думал, что она говорила буквально."


    $ renpy.music.set_volume(1.0)
    scene dreamgameshow (17) with hpunch
    "Свет снова становится ярким и жизнерадостным."

    host "Ладно, зрители! Не трогайте пульт! Потому что сегодня вас ждёт угощение!"

    host "Участники! Начинаем! Руки на кнопках!"
    scene dreamgameshow (2) with dissolve
    host "Вопрос номер один!"
    host "Это раунд на скорость! Кто первый нажмёт, получает очки!"


    scene dreamgameshow (3) with dissolve
    host "За 100 очков:"
    host "В нейроанатомии, какая миндалевидная структура в височной доле в первую очередь отвечает за обработку памяти, принятие решений и эмоциональные реакции, такие как страх?"

    host "Это А: «Гиппокамп»?"
    host "Или Б: «Миндалевидное тело»?"

    "В студии повисает тишина."


    play ambient "audio/sound/clock.mp3" volume 1.2
    scene dreamgameshow (27) with dissolve
    mc "..."
    mc "(Ну, я уж точно понятия не имею.)"
    "Ты ждёшь, что кто-то ответит."
    scene dreamgameshow (29) with dissolve
    mc "Погодите-ка..."
    scene dreamgameshow (28) with dissolve
    mc "У той штуки слева от меня нет рук."
    scene dreamgameshow (27) with dissolve
    mc "А кот... это кот."
    scene dreamgameshow (29) with dissolve
    mc "Играю только я один."

    host "Не томите, ребята!"

    mc "Эмм ладно тогда."
    stop ambient
    play sound "audio/sound/buzzer.wav" 
    scene dreamgameshow (20) with hpunch

    "Ты со всей силы бьёшь по красной кнопке."

    host "ДА! Участник номер два! Дай мне ответ!"

    menu:
        "Гиппокамп.":
            scene dreamgameshow (23) with hpunch
            play sound "audio/sound/wrong_5.mp3" 
            host "Близко, но нет! Это за навигацию! Мы ищем СТРАХ!"
            mc "Что ж. Это была лучшая догадка, на какую я был способен."
            $ quiz_score = 0
        "Миндалевидное тело.":

            scene dreamgameshow (24) with hpunch
            play sound "audio/sound/correct.mp3" 
            host "ПРАВИЛЬНО! Миндалевидное тело! Та самая штучка в твоём мозгу, что прямо сейчас кричит от ужаса! Молодец!"
            mc "Было 50 на 50, тут я мало что мог сделать."
            $ quiz_score = 1
        "Иди в жопу.":

            scene dreamgameshow (25) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "НЕПРАВИЛЬНО! И ещё и грубо!"
            mc "Пффф, вся эта затея тупая! Не буду я играть в твою игру!"
            host "Если хочешь хоть какой-то шанс выбраться, придётся!"
            $ quiz_score = 0
    scene dreamgameshow (3) with dissolve
    host "Не будем сбавлять темп! Кот сияет от восторга!"

    "Попо зевает."
    scene dreamgameshow (2) with dissolve
    play ambient "audio/sound/clock.mp3" volume 1.2
    host "Вопрос номер два! Тема: Древняя история!"
    host "За 200 очков!"
    scene minagame (1) with dissolve
    host "Как зовут девушку, которую ты героически спас от хулиганов, получив избиение похуже того, что я устраиваю своим соперникам!?"
    stop ambient
    play sound "audio/sound/buzzer.wav" 
    scene dreamgameshow (21) with hpunch
    "На этот раз ты даже не колеблешься. Бьёшь по кнопке."


    menu:
        "Юки.":
            scene dreamgameshow (24) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно! Её ты встретил позже! Сверься со своей временной линией!"
            host "У тебя что, все девушки сливаются в одну?"
        "Мина.":

            scene dreamgameshow (25) with hpunch
            play sound "audio/sound/correct.mp3" 
            host "БИНГО! Мина! Классическая девица в беде!"
            $ quiz_score += 1
            scene minagame (2) with dissolve
            scene minagame (2) with dissolve
            host "Хотя, эм... сверяясь со сценарием тут..."
            host "Мы ведь её больше не видели с той заправки, да?"
            host "Интересно, что случилось с той девчонкой?"
        "Отэм.":

            scene dreamgameshow (23) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно! Если бы ты попытался её спасти, она бы, наверное, сама избила хулиганов!"
            host "Тебе бы уже пора это знать! Она же твоя лучшая подруга! Или так ты говоришь!"
    scene dreamgameshow (3) with dissolve
    host "Ты жжёшь, пацан! Просто огонь! В отличие от моих коленей в 1989-м!"
    host "Ладно, добавляем бонусный раунд! Этот для истинных ценителей!"
    scene dreamgameshow (4) with dissolve
    play ambient "audio/sound/clock.mp3" volume 1.2
    host "Тема: Наследие Дракона!"
    host "За 500 очков!"
    scene dreamgameshow (2) with dissolve
    host "В 1978-м, в Мэдисон-Сквер-Гарден, я победил Хосе Гонсалеса, чтобы завоевать особый титул, привёз его обратно в Японию и положил начало революции пуроресу."

    host "Какой это был чемпионский титул?"
    play sound "audio/sound/buzzer.wav" 
    stop ambient
    scene dreamgameshow (20) with hpunch
    play sound "sfx/buzzer_press.ogg"
    "Ты жмёшь на кнопку раньше, чем он успевает закончить вопрос."

    menu:
        "Тяжеловесный титул IWGP.":
            scene dreamgameshow (25) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно! Я держал его шесть раз позже, конечно, но не с него всё началось!"
            "Серьёзно, откуда мне было вообще это знать."
            $ quiz_score += 0
        "Мировой тяжеловесный титул NWA.":

            scene dreamgameshow (24) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Вот бы! У нас с Риком Флэром были свои войны, но это не тот ответ на сегодня!"
            "Серьёзно, откуда мне было вообще это знать?"
            $ quiz_score += 0
        "Юниорский тяжеловесный титул WWF.":

            scene dreamgameshow (23) with hpunch
            play sound "audio/sound/correct.mp3" 
            host "ДРАКОНЬЯ РАКЕТА! Угадал! Именно он поставил New Japan на карту!"
            mc "Серьёзно, откуда мне было вообще это знать."
            mc "Да откуда ты вообще это знаешь? Ты буквально у меня в голове!"
            $ quiz_score += 1
    stop music fadeout 1.0
    scene dreamgameshow (3) with dissolve
    host "Последний вопрос раунда! Этот на всё!"
    scene dreamgameshow (2) with dissolve
    play ambient "audio/sound/clock.mp3" volume 1.2
    host "Тема: Текущие события."
    host "Мы все видели человека в маске. Мы все видели клюв. Мы все видели шляпу."
    host "Вопрос прост..."
    play sound "audio/sound/static.mp3" volume 1.2
    scene storyevent1 (180) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (181) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (182) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (183) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene storyevent1 (184) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene black with quickflash
    $ renpy.pause (0.001, hard= True)
    scene dreamgameshow (2) with quickflash
    stop sound 
    host "Чего он хотел?"

    scene dreamgameshow (31) with dissolve
    mc "Что...?"
    scene dreamgameshow (30) with dissolve
    host "Чумной Доктор! Чего он хотел?"
    mc "Это не... я не знаю ответа на это."

    host "Жми на кнопку, участник два. Время идёт."

    menu:
        "Он хотел меня убить.":
            scene dreamgameshow (34) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно!"
            scene dreamgameshow (35) with dissolve
            mc "Так каким тогда был правильный ответ!?"
            scene dreamgameshow (36) with dissolve
            host "Не знаю! Поэтому и спросил!"
        "Он хотел меня предупредить.":

            scene dreamgameshow (34) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно!"
            scene dreamgameshow (35) with dissolve
            mc "Так каким тогда был правильный ответ!?"
            scene dreamgameshow (36) with dissolve
            host "Не знаю! Поэтому и спросил!"
        "Он хотел, чтобы я его запомнил.":

            scene dreamgameshow (37) with hpunch
            play sound "audio/sound/wrong_5.mp3"
            host "Неправильно!"
            scene dreamgameshow (35) with dissolve
            mc "Так каким тогда был правильный ответ!?"
            scene dreamgameshow (36) with dissolve
            host "Не знаю! Поэтому и спросил!"
    stop ambient
    scene dreamgameshow (4) with hpunch
    host "И ЭТО КОНЕЦ РАУНДА!"

    scene dreamgameshow (2) with dissolve
    host "Со счётом [quiz_score] из 4..."
    play sound "audio/sound/winner.mp3"
    scene dreamgameshow (42) with hpunch
    host "Участник номер два — наш ПОБЕДИТЕЛЬ!"
    scene dreamgameshow (43) with dissolve
    mc "Я бы выиграл, что бы я ни выбрал, да?"
    scene dreamgameshow (43) with hpunch
    host "Верно! Ты получаешь эти 50 очков обратно!"
    mc "Эмм, спасибо, наверное."
    host "Поздравляю, пацан! Знаешь, что это значит!"
    play music "audio/music/scawr.mp3"
    scene dreamgameshow (39) with dissolve

    "Он с размахом указывает на гигантскую дверь..."

    host "Пора забрать свою награду!"
    host "Выметайся отсюда! И не возвращайся, пока не получишь ответы!"

    scene dreamgameshow (40) with dissolve
    "Зрители студии ликуют — зацикленный, лихорадочный звук, который уже не особо похож на человеческий."
    "Ты поднимаешься по лестнице. Дверь становится всё больше."
    scene dreamgameshow (41) with dissolve
    "Ты тянешься, чтобы коснуться дверной ручки.{nw}"
    stop music
    play ambient "audio/ambient/vcr1.mp3" volume 0.5
    play sound "audio/sound/static.mp3"
    scene tvstatic with quickflash
    $ renpy.pause (0.01, hard= True)
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene tvstatic with quickflash
    $ renpy.pause (0.01, hard= True)
    $ renpy.pause (0.01, hard= True)
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene tvstatic with quickflash
    $ renpy.pause (0.1, hard= True)
    stop sound
    play music "audio/music/sitcom1.mp3"
    scene citysit with quickflash
    $ renpy.pause (7, hard= True)
    scene sitcom (1) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (3) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (2) with dissolve
    $ renpy.pause (1, hard= True)

    scene sitcom (5) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (6) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (4) with dissolve
    $ renpy.pause (1, hard= True)

    scene sitcom (7) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (8) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (9) with dissolve
    $ renpy.pause (1, hard= True)

    scene sitcom (10) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (11) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (12) with dissolve
    $ renpy.pause (1, hard= True)

    scene sitcom (13) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (14) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (15) with dissolve
    $ renpy.pause (1, hard= True)

    scene sitcom (16) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (17) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (18) with dissolve
    $ renpy.pause (2, hard= True)
    scene black with fade
    $ renpy.pause (2, hard= True)

    stop music fadeout 1.0
    play sound "audio/sound/sitcomtransition.mp3"
    scene citysit with dissolve
    $ renpy.pause (5, hard= True)



    play sound "audio/sound/sitcomcheer.mp3"
    scene sitcom (19) with dissolve
    play music "audio/music/Dontpass.mp3" volume 0.4
    "Ты сидишь за кухонным столом. Освещение неестественно плоское и яркое."
    mc "Что!?"
    scene sitcom (20) with dissolve
    mc "Что за хрень это такое?"
    scene sitcom (21) with dissolve
    mc "Я же только что был на том диване!?"
    mc "Почему я...?"






    scene sitcom (22) with hpunch
    I "Доброе утро! Кто готов к питательному завтраку?"
    scene sitcom (23) with dissolve
    mc "Изра? Почему ты одета как домохозяйка из 1950-х?"
    scene sitcom (24) with dissolve
    I "Ой, ты глупый гусь! Ты же знаешь, «Изра» — это просто моё имя."
    scene sitcom (25) with dissolve
    I "Зови меня Мамочка."
    scene sitcom (26) with dissolve
    play sound "audio/sound/sitcomlaugh.mp3"
    mc "Вот уж точно не буду."
    scene sitcom (27) with dissolve
    play sound "audio/sound/knock.wav"
    "Стук в дверь привлекает внимание вас обоих."
    I "О? Должно быть, это твой отец!"


    play sound "sfx/audience_cheer_huge.ogg"
    scene sitcom (28) with dissolve
    "Заходит Лили. На ней комично большой пиджак и накладные усы."

    L "Дорогая, я домаааа!"
    "Она делает голос ниже, но звучит просто как Лили, пытающаяся звучать как мужчина."
    L "Работа на Бизнес-Фабрике сегодня была безумной!"
    scene sitcom (30) with dissolve
    I "О, дорогой! Ты так усердно работаешь!"
    play sound "audio/sound/kiss.mp3" volume 1.3
    scene sitcom (29) with dissolve
    "Изра целует Лили в щёку."
    "Изра целует Лили в щёку."
    L "Хех, есть ещё, откуда это взялось?"
    mc "Лили? Ты типа мой... папа?"
    mc "Ты ниже Изры и даже причёску не поменяла."
    scene sitcom (31) with dissolve
    L "Не умничай с отцом, спортсмен!"
    scene sitcom (32) with dissolve
    L "А то я из тебя всю душу выбью.{nw}"
    $ renpy.music.set_volume(0.01)
    play sound "audio/sound/error.mp3"
    scene sitcom
    $ renpy.pause (1, hard= True)
    $ renpy.music.set_volume(1.0)
    scene sitcom (33)
    L "Или никаких тебе карманных денег!"


    play sound "audio/sound/sitcomlaugh.mp3"

    "Внезапно кто-то съезжает по перилам лестницы."

    scene sitcom (34) with hpunch
    play sound "audio/sound/disneycheer.mp3"
    a "Здарова, неудачники."
    "Отэм вплывает в комнату с дикой уверенностью."
    "На ней, похоже, какой-то хиппи-наряд."
    scene sitcom (35) with dissolve
    "Ты рад видеть хоть кого-то, кто, кажется, играет самого себя."
    mc "Отэм? Ты, типа... знаешь..."
    mc "Нормальная?"
    scene sitcom (36) with dissolve
    "Отэм медленно подходит к тебе."
    play sound "audio/sound/punch.mp3" volume 1.5

    scene sitcom (37) with hpunch
    "А затем резко бьёт тебя по руке."
    a "Единственный тут ненормальный — это ты, ЗАНУДА!"

    play sound "audio/sound/sitcomlaugh.mp3"
    scene sitcom (38) with dissolve
    mc "Да что вообще со всеми вами не так!?"
    scene sitcom (39) with dissolve
    mc "Это не-"
    scene sitcom (40) with dissolve
    mc "В-вы не-"
    play sound "audio/sound/s_kill_glitch1.ogg"
    scene sitcom (41) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (42) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (41) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (42) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (41) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (42) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (43) with quickdissolve
    "Твой мозг просто как бы сдаётся."

    mc "На самом деле... забудьте."

    mc "Я допустил ошибку."
    scene sitcom (44) with dissolve
    mc "Наверное, эта ошибка — я сам."

    "Напряжение покидает твои плечи. Зачем ты вообще сопротивлялся?"
    "Это нормально. Это семья. Это сценарий."
    scene sitcom (45) with dissolve
    L "Так, детки, как дела в школе?"

    mc "Лучше и не придумаешь! Мы изучаем Франца Кафку!"
    scene sitcom (46) with dissolve
    L "Кто это?"
    scene sitcom (47) with dissolve
    L "Лучше бы он не был коммунистом или чем там вас в этой школе пичкают!"
    scene sitcom (48) with dissolve
    mc "Он знаменито сказал: {i}«Бывают моменты, когда я убеждён, что не гожусь ни для каких человеческих отношений»{/i}"
    scene sitcom (49) with dissolve
    mc "{i}«Я не могу избавиться от чувства, что был создан для какой-то цели, но не могу её найти.»{/i}"
    scene sitcom (50) with hpunch
    a "СКУУУУЧНОООО!"
    play sound "audio/sound/sitcomlaugh.mp3"
    scene sitcom (51) with dissolve
    I "Ой, милый, не используй такие умные слова за столом! У отца от них мигрень случится."
    L "Именно! В этом доме мы не занимаемся «экзистенциальным ужасом»!"
    scene sitcom (52) with dissolve
    L "А теперь ешь свои блинчики, по сценарию ты обожаешь блинчики."
    scene sitcom (53) with dissolve
    play sound "audio/sound/doorbell1.mp3"
    "Внезапно звонит дверной звонок."

    I "Кто бы это мог быть?"

    scene sitcom (54) with hpunch
    play sound "audio/sound/disneycheer.mp3"

    "Входная дверь не просто открывается — её распахивают с той самой уверенностью, на которую способна только высокобюджетная приглашённая звезда."

    scene sitcom (55) with dissolve
    pe "Воу, эй-эй..."

    pe "Мы не не вовремя зашли?"

    scene sitcom (56) with dissolve

    play sound "audio/sound/sitcomlaugh.mp3"
    I "Ой! Пьер и... тот, другой!"
    scene sitcom (57) with dissolve
    pe "Именно, Сестрёнка! Мы слышали, тут кто-то говорил про «цель» и «человеческие отношения»."
    scene sitcom (58) with dissolve
    "Пьер скользит по полу. Он наклоняется, его ухмылка настолько широка, что выглядит болезненно."

    pe "Слушай меня, пацан. Забудь Кафку! Единственная «метаморфоза», о которой тебе стоит волноваться — это когда твои карманные деньги превращаются в деньги на пиццу!"
    scene sitcom (59) with dissolve
    mc "Ты прав, дядя Пьер! Зачем думать, когда можно просто... потреблять?"

    a "Наконец-то! Зануда исцелился и говорит разумные вещи!"
    play sound "audio/sound/sitcomlaugh.mp3"
    play ambient "audio/sound/sitcomlaugh2.mp3"
    scene sitcom (60) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (61) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (62) with dissolve
    $ renpy.pause (1, hard= True)
    scene sitcom (63) with dissolve
    mc "Хахаха."
    mc "Хахаха..."
    mc "Ха..."
    play sound "audio/sound/sitcomlaugh.mp3"
    stop music fadeout 1.0
    scene sitcom (64) with dissolve
    mc "Ох, блин... это... это смешно."
    "Ты смотришь, как реагирует твоя семья."
    scene sitcom (65) with dissolve
    "Они всё ещё смеются."
    "Но из их ртов не выходит ни звука."

    stop sound fadeout 2.0

    mc "Эм, народ?"
    scene sitcom (66) with dissolve
    "Студийные огни гудят. Тишина внезапна и абсолютна."
    mc "Ч-что происходит?"

    scene sitcom (67) with dissolve
    "Их лица по-прежнему ничего не выражают, тебе становится тревожно."
    mc "Ладно... ладно, шутка окончена."
    mc "Можем вернуть всё, как было?"

    scene sitcom (68) with dissolve
    mc "П-пожалуйста-"
    stop ambient
    play sound "audio/sound/s_kill_glitch1.ogg"
    scene sitcom (69) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (70) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (69) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (70) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (69) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (70) with quickdissolve
    $ renpy.pause (0.1, hard= True)
    scene sitcom (71) with quickdissolve

    "Ты медленно приходишь в себя."
    play ambient "audio/ambient/vcr1.mp3" volume 0.5
    scene sitcom (72) with dissolve
    play sound "audio/sound/lowhum.wav"
    play music "audio/music/dark.mp3"
    "Лица всё ещё не двигаются. Они просто стоят там, пустые и полые."
    "Яркая гостиная начинает казаться очень маленькой. Очень фальшивой."
    "Стены выглядят как картон. Еда выглядит как воск."
    play sound "audio/sound/dooropen.wav"
    scene sitcom (76) with dissolve
    "Ты пятишься назад, врезаясь в кухонный остров."
    "Ты смотришь в сторону входной двери, отчаянно желая уйти."
    "Но двери больше нет."



    scene sitcom (75) with dissolve
    "То место, где раньше была входная дверь, изменилось."
    "На её месте — зияющая, прямоугольная пасть тьмы."
    "Коридор."
    "Он дышит. Холодный, влажный сквозняк задувает в тёплую студийную декорацию."

    scene sitcom (77) with dissolve
    mc "..."
    mc "Ясно."

    scene sitcom (78) with dissolve
    mc "Видимо, шоу закрыли уже какое-то время назад."



    scene sitcom (79) with dissolve
    "Ты поворачиваешься спиной к теплу."
    "Ты шагаешь во тьму."

    scene hallway (1) with dissolve

    "Обои отслаиваются длинными, выгоревшими на солнце полосами."
    "Половицы искорёжены, торчат вверх, как рваные зубы."


    "Ты делаешь шаг вперёд, дерево скрипит под твоим весом."

    mc "..."

    mc "Знаешь, когда в коридоре всего две двери, это как-то антикульминационно."

    mc "Может, я более поверхностный, чем сам думал."

    mc "Наверное, это ещё значит, что не стоит слишком об этом раздумывать."
    scene hallway (7) with dissolve
    "Ты поворачиваешься к двери прямо справа от тебя."
    "Это обычная белая деревянная дверь. Краска рядом с ручкой облупилась."
    "Она выглядит тревожно обычной. Выглядит как дверь в спальню твоего детства."
    "На ней краской нарисована цифра один."
    mc "(Наверное, стоит начать по порядку.)"
    play sound "audio/sound/dooropen.wav"
    scene hallway (2) with dissolve

    mc "Ну, была не была."

    "Ты поворачиваешь ручку."

    "По ту сторону нет никакой комнаты."
    "Просто стена абсолютной, удушающей тьмы."
    "Ни лучика света. Ни звука."
    "Просто пустота, ожидающая быть заполненной."

    mc "..."

    "Ты делаешь вдох, который дребезжит у тебя в груди."
    "И шагаешь внутрь."

    scene black with fade
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient 
    "Тьма мгновенно поглощает тебя."
    "Дверь захлопывается за твоей спиной."

    "Ты стоишь в абсолютной тьме."
    "Воздух затхлый. Пахнет озоном и... черникой?"

    play sound "audio/sound/lightswitch.mp3" volume 1.4

    scene dunkle (1)


    "Одинокий прожектор вспыхивает в центре пустоты."
    "Там стоит... нечто."
    "Оно маленькое. Оно синее. Выглядит как плюшевая игрушка, повидавшая слишком много ужасов."

    scene dunkle (2) with dissolve

    mc "Что... это вообще за хрень?"

    "Существо смотрит на тебя немигающими глазами размером с блюдца."
    "Его рот не двигается, но голос вырывается из него, как из перегруженного динамика."
    scene dunkle (3) with dissolve
    play sound "audio/sound/dunkle/dunkle_14.mp3"
    $ renpy.pause (1, hard= True)
    scene dunkle (2) with dissolve
    "Почему...он так разговаривает?"
    play music "audio/music/dunkle.mp3" volume 0.2
    mc "Я? Я [mcname]."
    mc "М-мне больше любопытно, кто вообще ты такой?"
    scene dunkle (4) with dissolve
    scene dunkle (5) with dissolve
    play sound "audio/sound/dunkle/dunkle_02.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (4) with dissolve
    "Ты смотришь на него. Имя скачет по твоему черепу, не имея абсолютно никакого смысла."
    "Твой мозг коротит. Ты открываешь рот, чтобы задать вопрос, но вместо этого выпадает что-то другое."
    scene dunkle (6) with dissolve
    scene dunkle (7) with dissolve
    play sound "audio/sound/dunkle/dunkle_new_01.mp3" 
    $ renpy.pause (3, hard= True)
    scene dunkle (4) with dissolve
    mc "Л-ладно?"
    scene dunkle (7) with dissolve
    play sound "audio/sound/dunkle/dunkle_01.mp3"
    $ renpy.pause (2, hard= True)

    scene dunkle (4) with hpunch
    mc "Что за хрень!? Зачем ты вообще это сказал!"
    mc "И какого чёрта ты вообще тут делаешь? Какую часть моего разума ты должен представлять?"
    mc "Я пытаюсь найти парня в маске Чумного Доктора, как это мне вообще поможет!?"


    "..."
    "Тишина тянется. Ты понятия не имеешь, зачем это сказал."
    scene dunkle (15) with dissolve
    "Данкл Фанкл подходит к тебе ближе, его тело вибрирует."
    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_25.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (10) with dissolve
    mc "Бесцельный?"
    mc "Эй, слушай сюда, ты... кем бы ты там ни был."

    mc "Пока что я чуть не утонул в океанах, поучаствовал в игровом шоу, в котором не было ни капли смысла, и застрял в очень травмирующем ситкоме."
    mc "Не думаю, что мне нужно, чтобы ты говорил мне, что я бесцельный!"
    scene dunkle (10) with dissolve
    $ renpy.pause (1, hard= True)

    scene dunkle (11) with hpunch
    play sound "audio/sound/dunkle/dunkle_08.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (10) with dissolve

    mc "Какие у тебя вообще проблемы?!"
    mc "Мне не нужны оскорбления от галлюцинации!"
    $ renpy.pause (0.5, hard= True)
    scene dunkle (12) with dissolve
    play sound "audio/sound/boowomp.mp3"
    $ renpy.pause (0.5, hard= True)
    "Странное существо хмурится от твоих слов. Тебе становится немного стыдно."
    mc "Я...извини за-"

    scene dunkle (13) with hpunch

    play sound "audio/sound/dunkle/dunkle_00.mp3"
    $ renpy.pause (4, hard= True)
    scene dunkle (14) with dissolve
    mc "Ладно! Господи! Понял!"
    mc "Ты невероятно враждебный!"
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_03.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (10) with dissolve
    mc "Ой...эм, я вообще-то не знаю?"
    mc "Наверное, я тут по какой-то причине, да?"
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_04.mp3"
    $ renpy.pause (1.5, hard= True)
    scene dunkle (10) with dissolve
    mc "Прошу прощения?"
    mc "Я не..."
    mc "Не думаю, что ты можешь такое говорить."
    scene dunkle (13) with dissolve
    play sound "audio/sound/dunkle/dunkle_05.mp3"
    $ renpy.pause (5.5, hard= True)
    scene dunkle (10) with dissolve
    mc "Я..."

    mc "(Стоит ли мне волноваться, что нечто в моей голове разговаривает вот так?)"

    mc "В любом случае... наверное, я..."

    mc "..."
    stop music fadeout 1.0
    mc "Мне страшно, что всё это ничего не значит."
    mc "Я хожу по коридорам собственной травмы, надо мной издеваются ведущие игровых шоу и безликие версии моей семьи."
    mc "А там снаружи? В реальном мире? Есть парень в маске чумного доктора, который знает моё имя, и я не понимаю почему."

    "Ты делаешь дрожащий вдох, слова начинают вырываться быстрее."

    mc "Я чувствую, будто тону. Каждый раз, когда мне кажется, что я плыву наверх, вода превращается в кровь и тащит меня обратно вниз."
    mc "У меня нет плана. У меня нет судьбы. Я просто жду, когда случится следующая плохая вещь."
    mc "Я в ужасе от того, что когда время выйдет, я так и не успею по-настоящему {i}пожить{/i}."
    mc "Это то, что ты хотел услышать?"
    scene dunkle (15) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_06.mp3"
    $ renpy.pause (3, hard= True)
    play music "audio/music/calmguitar.mp3" fadein 1.0 volume 0.3
    scene dunkle (10) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_07.mp3"
    $ renpy.pause (8, hard= True)
    scene dunkle (10) with dissolve
    mc "..."
    mc "Погоди, что?"
    scene dunkle (15) with dissolve
    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_042.mp3"
    $ renpy.pause (5, hard= True)
    scene dunkle (15) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_052.mp3"
    $ renpy.pause (4, hard= True)
    scene dunkle (10) with dissolve

    $ renpy.pause (0.5, hard= True)
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_062.mp3"
    $ renpy.pause (5, hard= True)
    scene dunkle (10) with dissolve
    mc "..."
    "Ты замолкаешь."
    "Резкая смена настроения сбивает с толку."

    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_072.mp3"
    $ renpy.pause (4.5, hard= True)
    scene dunkle (10) with dissolve
    mc "Что ж, это было тяжеловато...."
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_19.mp3"
    $ renpy.pause (3, hard= True)
    scene dunkle (10) with dissolve
    mc "Наверное, в этом есть смысл..."
    scene dunkle (15) with dissolve
    $ renpy.pause (0.5, hard= True)

    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_10.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (10) with dissolve
    "Он замирает, его глаза чуть сужаются."
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_11.mp3"
    $ renpy.pause (3, hard= True)
    scene dunkle (14) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (13) with dissolve
    play sound "audio/sound/dunkle/dunkle_20.mp3"
    $ renpy.pause (5, hard= True)
    scene dunkle (14) with dissolve
    mc "Ты про карму? Типа, я делаю добро, получаю добро?"
    scene dunkle (15) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (16) with dissolve
    play sound "audio/sound/dunkle/dunkle_21.mp3"
    $ renpy.pause (3, hard= True)
    scene dunkle (10) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_22.mp3"
    $ renpy.pause (4, hard= True)
    scene dunkle (10) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (11) with dissolve
    play sound "audio/sound/dunkle/dunkle_23.mp3"
    $ renpy.pause (4, hard= True)
    scene dunkle (10) with dissolve

    "Ты чувствуешь, как что-то щёлкает у тебя в груди."
    "Комната начинает яростно трястись."

    mc "Кажется... кажется, я начинаю понимать."
    mc "Дело не в пункте назначения. Дело в--"


    stop music

    play sound "audio/sound/sparkle.wav"
    play ambient "audio/ambient/park.mp3" volume 0.5
    scene dunkle (17) with quickflash

    "Тёмная комната мгновенно исчезает."
    "Запах черники сменяется свежей травой и солнечным светом."
    "Ты стоишь на вершине холмистого зелёного холма посреди нигде. Небо идеально синее."

    scene dunkle (19) with dissolve
    $ renpy.pause (0.5, hard= True)
    play sound "audio/sound/bop.mp3"
    scene dunkle (20) with hpunch
    play sound "audio/sound/dunkle/dunkle_12.mp3"
    $ renpy.pause (2, hard= True)

    mc "Я не знаю! Это же тебя я слушаю!"
    scene dunkle (17) with dissolve
    "Данкл поворачивается обратно к тебе."
    "Он выглядит искренне обеспокоенным."
    scene dunkle (18) with dissolve
    play sound "audio/sound/dunkle/dunkle_13.mp3"
    $ renpy.pause (3, hard= True)
    scene dunkle (17) with dissolve
    mc "Я-я не знаю как!?"
    scene dunkle (23) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (24) with dissolve
    play sound "audio/sound/dunkle/dunkle_new_02.mp3"
    $ renpy.pause (4.5, hard= True)
    scene dunkle (17) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (18) with dissolve
    play sound "audio/sound/dunkle/dunkle_26.mp3"
    $ renpy.pause (2, hard= True)
    scene dunkle (17) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene dunkle (18) with dissolve
    play sound "audio/sound/dunkle/dunkle_27.mp3"
    $ renpy.pause (5, hard= True)
    "Он смотрит прямо тебе в душу, отчаянно желая, чтобы ты понял."
    scene dunkle (21) with dissolve
    $ renpy.pause (0.5, hard= True)
    $ renpy.pause (0.5, hard= True)
    scene dunkle (22) with dissolve
    play sound "audio/sound/dunkle/dunkle_16.mp3"
    $ renpy.pause (5.5, hard= True)
    scene dunkle (17) with dissolve
    mc "Эм... не знаю."
    mc "Наверное... почистил бы зубы?"
    mc "Проверил телефон? Отлил бы?"
    mc "Всякое такое, что я обычно делаю, наверное?"
    scene dunkle (18) with dissolve

    play sound "audio/sound/dunkle/dunkle_17.mp3"
    $ renpy.pause (1, hard= True)
    scene dunkle (17) with dissolve
    mc "Эм..."
    mc "Это вопрос с подвохом? Потому что-"
    stop ambient
    scene black
    play sound "audio/sound/dunkle/dunkle_18.mp3"
    $ renpy.pause (1, hard= True)


    scene hallway (4) with dissolve
    $ renpy.pause (0.5, hard= True)
    scene hallway (5) with hpunch
    play ambient "audio/ambient/vcr1.mp3" volume 0.5
    play music "audio/music/dark.mp3"

    "Ты резко дёргаешься вперёд, лёгкие тяжело дышат."
    "Ты не на холме. Ты не в тёмной комнате."

    scene hallway (6) with dissolve
    "Ты снова в Коридоре."


    mc "Что... за чёрт... это было?"

    scene hallway (1) with dissolve

    "Ты стоишь в коридоре, грудь тяжело вздымается, ждёшь, что синий инопланетянин снова выскочит."
    "Но он не выскакивает."

    mc "Ладно..."
    mc "Ладно, успокойся."
    mc "Не так уж и плохо было."
    scene hallway (8) with dissolve
    "Ты смотришь на оставшуюся дверь."
    mc "Попробуем эту, наверное..."
    mc "(Пожалуйста, пусть это будет не снова он...)"
    scene hallway (3) with dissolve

    play sound "audio/sound/dooropen.wav"

    "Ты толкаешь дверь с цифрой 2. Она открывается внутрь с торжественной тяжестью."
    stop ambient
    stop music
    scene black with dissolve
    $ renpy.pause (0.5, hard= True)
    play music "music/library.mp3" fadein 2.0

    scene weirdshit (1) with dissolve
    "Ты входишь в собор тишины."
    "Это библиотека. Но не обычная."
    "Полки тянутся вверх в бесконечную тьму, а проходы уходят в бесконечность."
    "Миллионы книг. Миллиарды страниц."
    "Воздух прохладный и неподвижный, наполненный запахом стареющей бумаги и забытых слов."

    mc "Есть кто?"

    "Твой голос не отдаётся эхом. Книги мгновенно поглощают звук."
    scene weirdshit (2) with dissolve
    "Ты идёшь по центральному проходу. Половицы отполированы до зеркального блеска."
    scene library (3) with dissolve
    "Ты проходишь мимо секций, помеченных датами. {i}5 лет назад{/i}. {i}10 лет назад{/i}. {i}Прошлый вторник{/i}."

    mc "Это... воспоминания?"
    mc "Нет. Не воспоминания."
    scene weirdshit (2) with dissolve
    mc "Это не истории."
    mc "Это журнал. Всё, что уже случилось."
    scene library (1) with dissolve
    mc "..."
    scene library (2) with dissolve
    mc "Хм?"
    "Одна из книг на полках привлекает твой взгляд."

    mc "Что это?"
    scene weirdshit (2) with dissolve
    play sound "audio/Sound/grab.mp3" volume 1.5
    "Ты тянешься и касаешься обложки."
    "В момент, когда твоя кожа соприкасается с ней, тебя окатывает волна холода."

    scene weirdshit (3) with dissolve

    "Название выбито серебряными буквами:"
    "{b}Книга «Что, Если»{/b}"
    play sound "audio/Sound/paper.wav"
    mc "Что, если...?"
    play sound "audio/Sound/paper.wav"
    scene weirdshit (4) with dissolve

    "Ты не хочешь открывать её. Ты знаешь, что не следует."
    "Но вопросы начинают наводнять тебя ещё до того, как ты переворачиваешь страницу."
    "Они просачиваются в твой разум, как ядовитый газ."

    "{i}Что, если бы ты остался со своей настоящей семьёй?{/i}"
    "{i}Что, если бы у тебя были оценки получше?{/i}"
    "{i}Что, если бы ты был быстрее? Сильнее?{/i}"
    "{i}Что, если бы ты завёл больше друзей вместо того, чтобы всех отталкивать?{/i}"
    scene weirdshit (5) with dissolve

    "Не нужно быть гением, чтобы понять, что означает эта книга."
    mc "Я всё испортил."
    "Ты один в бесконечной библиотеке собственных провалов."

    "..."
    "......"
    scene weirdshit (6) with dissolve
    host "Я никогда особо не любил такие книги..."





    "Внезапно рядом с тобой возникает легендарное присутствие."

    scene weirdshit (7) with dissolve
    "На нём нет того безвкусного костюма из игрового шоу."
    "На нём простой рестлинг-халат, он выглядит величественно. Достойно."

    mc "Ты...?"
    mc "Я думал, ты ведущий?"
    mc "(Серьёзно, почему этот тип так часто у меня в голове?)"
    mc "(Отэм что, оставила телек включённым, когда я вырубился, или как?)"
    scene weirdshit (8) with dissolve
    host "Я многое из себя представляю. Сегодня я просто старик, который прочитал слишком много книг."
    host "Я понимаю, тяжело отпустить то, что могло бы быть..."
    "Он смотрит на тебя не с жалостью. Он смотрит на тебя с уважением."



    host "...но принимая то, что произошло, мы наконец можем двигаться дальше."

    scene weirdshit (9) with dissolve

    host "Прошлое — это решённый матч, пацан. Ты не можешь изменить итог."
    host "Но следующий матч? Карточка турнира ещё открыта."

    host "Почему бы тебе снова не взглянуть на эту книгу?"



    scene weirdshit (10) with dissolve
    mc "Ты о чём..."
    play sound "audio/Sound/bookclose.mp3"

    scene weirdshit (11) with dissolve
    "Ты снова смотришь на обложку книги в своих руках."

    scene weirdshit (12) with dissolve

    "Название изменилось."
    "Серая кожа превратилась в обнадёживающее, яркое золото."

    "{b}Что Теперь?{/b}"
    "{i}Что случилось на самом деле, и как нам из этого извлечь урок.{/i}"
    scene weirdshit (13) with dissolve
    stop music fadeout 1.0
    mc "..."
    mc "Слушай, я ценю твою помощь, но..."
    mc "Всё не так просто."
    scene weirdshit (14) with dissolve
    mc "Пытаться продолжать двигаться вперёд, когда у меня столько вопросов о прошлом, это-"
    play sound "audio/Sound/punch.mp3"

    scene weirdshit (15) with hpunch
    "Боль взрывается в твоей челюсти."

    scene weirdshit (16) with dissolve
    "Сила удара отбрасывает тебя назад, впечатывая в книжную полку."
    "Книги обрушиваются вокруг тебя, как мёртвые птицы."
    scene weirdshit (17) with dissolve
    mc "Гах! Да что за хрень с—?!"



    scene weirdshit (18) with dissolve

    mc "Ты...?"
    play music "audio/music/ugh.mp3"

    scene weirdshit (19) with dissolve
    "Это ты."
    "По крайней мере... тебе так кажется..."
    "Чем бы оно ни было, другом оно точно не выглядит."
    scene weirdshit (20) with dissolve
    mc "Что за хрень происхо-"
    play sound "audio/Sound/punch.mp3"
    scene weirdshit (21) with hpunch
    "Другой Ты не ждёт."
    "Он вбивает кулак тебе в живот."
    scene weirdshit (22) with dissolve
    "Ты складываешься пополам, хватая ртом воздух."
    scene weirdshit (23) with dissolve
    mc "Ты забываешь всю чёртову суть!"

    play sound "audio/Sound/thud.mp3"

    scene weirdshit (24) with hpunch

    "Он впечатывает тебя обратно в полки. Его голос — рычание, раздирающее твоё горло."
    scene weirdshit (25) with dissolve
    mc "Ты теперь сравниваешь себя с другими людьми."
    mc "Ты, блядь, неуверен в себе, и всегда хочешь пойти по лёгкому пути."

    play sound "audio/Sound/punch.mp3"
    scene weirdshit (26) with hpunch
    "Он снова бьёт тебя. Сильно."
    mc "Ты совсем, блядь, тупой!?"
    scene weirdshit (27) with dissolve
    mc "Я понимаю, что сейчас тяжело, но ты знал об этом ещё до того, как вошёл!"
    mc "Почему ты останавливаешься от малейшего сопротивления!?"
    "Ты пытаешься поднять руки, чтобы защититься, но он отбивает их в сторону."
    play sound "audio/Sound/strangling.wav"
    scene weirdshit (30) with dissolve
    "Он хватает тебя за горло, крепко сжимая."

    mc "Так что пора начать задавать себе вопрос..."
    mc "Ты правда этого хочешь?!"
    mc "Или тебе просто нравилось говорить себе, как сильно ты этого хочешь?!"
    scene weirdshit (31) with dissolve
    "Он смотрит тебе в глаза, бросая вызов ответить."
    "Ты не можешь дышать. Не можешь отвести взгляд."

    mc "Я..."

    "Он ухмыляется."

    mc "Жалок."
    play sound "audio/Sound/hoodie.wav"
    scene weirdshit (32) with vpunch

    "Он отталкивает тебя назад со всей силы."
    "Ты падаешь назад, готовясь к удару о деревянный пол."
    play sound "audio/Sound/hitgrass.mp3"
    play ambient "audio/ambient/wind.mp3" fadein 1.0
    scene weirdshit (33) with hpunch

    "Но ты ударяешься не о дерево."
    "Ты приземляешься мягко."
    "Запах старой бумаги исчез."
    "Запах старой бумаги исчез."
    "Его сменил запах земли. Полевых цветов. Дождя."
    scene weirdshit (34) with dissolve
    "Его руки всё ещё на твоём горле."
    "Твои руки всё ещё на твоём горле."
    "Ты пытаешься вырваться и кричать, но он слишком силён."
    scene weirdshit (35) with hpunch
    mc "Я ТЕБЯ, БЛЯДЬ, НЕНАВИЖУ!"
    mc "СЛЫШИШЬ МЕНЯ!?"
    mc "Я ТЕБЯ, БЛЯДЬ, НЕНАВИЖУ!"
    scene weirdshit (36) with dissolve
    "Ты сжимаешь. Сжимаешь изо всех сил."
    "Ты хочешь раздавить сомнение. Хочешь заглушить голос, который говорит, что ты недостаточно хорош."
    "Твоё лицо краснеет. Глаза выпучиваются."
    "Но ты не сопротивляешься."
    scene weirdshit (37) with dissolve
    "Вместо этого... ты улыбаешься."
    "Спокойной, кровавой, тревожащей улыбкой."
    scene weirdshit (38) with dissolve
    mc "Гнев не лучшая эмоция, знаешь ли."
    mc "ЗАТКНИСЬ!"
    scene weirdshit (39) with dissolve
    mc "Что, если бы ты в итоге..."

    play sound "audio/Sound/glitch1.ogg"
    scene weirdshit (39) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (40) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (39) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (40) with quickflash
    $ renpy.pause (0.01, hard= True)
    stop sound

    mc "Причинил боль тому, о ком заботился??"
    "Шея под твоими руками начинает меняться."
    "Она становится меньше. Мягче."
    "Линия челюсти смягчается. Волосы рассыпаются, превращаясь из твоей растрёпанной стрижки в длинные, тёмные волны."


    scene weirdshit (41) with dissolve
    "Ты больше не душишь самого себя."
    "Ты душишь Отэм."

    a "Тебе нравится причинять боль другим, [mcname]?"
    scene weirdshit (42) with dissolve
    mc "От... Отэм?"

    mc "Ч-что? Что происходит?"
    scene weirdshit (41) with dissolve
    "Ты пытаешься убрать руки, но они словно заблокированы. Твои мышцы застыли в спазме насилия."
    "Она смотрит на тебя снизу вверх не со страхом, а с разочарованием."

    scene weirdshit (40) with dissolve
    a "Тебе нравится причинять людям боль, [mcname]?"
    mc "Что!?{w} Нет, я-"
    a "Тогда почему ты постоянно это делаешь?"
    mc "Ты о чём-{w} Я не-"
    a "Ты в постоянном цикле причинения боли другим-"
    a "Можно только предположить, что тебе это нравится."
    scene weirdshit (59) with dissolve
    mc "Это неправда! Я-"
    a "Тебе нужно быть осторожнее."
    a "Если позволишь злости взять верх..."

    play sound "audio/Sound/glitch1.ogg"
    scene weirdshit (40) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (43) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (40) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (43) with quickflash
    $ renpy.pause (0.01, hard= True)
    stop sound
    scene weirdshit (43) with dissolve
    thg1 "...Ты кончишь тем, что сделаешь больше, чем просто причинишь боль."
    mc "Нет! Я не хотел—"


    scene weirdshit (44) with dissolve


    "Это не Отэм."
    "Это тот бандит из переулка."
    "Тот, что умер."
    "Тот, кого ты..."

    mc "Гах!"
    scene weirdshit (45) with hpunch
    "Ты отшатываешься назад, отпуская горло."
    "Ты смотришь на свои руки."
    "Они неконтролируемо дрожат. Они ощущаются испачканными, хотя крови нет."
    scene weirdshit (46) with dissolve

    mc "Нет... Нет..."

    play sound "audio/Sound/glitch1.ogg"
    scene storyevent1 (175) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (46) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene storyevent1 (175) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (46) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene storyevent1 (175) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (46) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene storyevent1 (175) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (46) with quickflash
    $ renpy.pause (0.01, hard= True)
    stop sound

    mc "Нетнетнетнет..."
    scene weirdshit (69) with dissolve
    mc "Хватит... Хватит..."
    scene weirdshit (58) with hpunch
    stop music 
    mc "ХВАТИТ!"
    "Ты оглядываешься назад, туда, где было тело."

    play music "audio/music/feild.mp3"
    scene weirdshit (47) with dissolve
    "Там никого нет."
    "Ни Двойника. Ни Отэм. Ни Бандита."
    "Только примятая трава там, где ты боролся с призраком."

    scene weirdshit (48) with dissolve

    "Ты один."
    "По-настоящему один."
    "Ветер шелестит в высокой траве — одинокий, гулкий звук, который будто имитирует вздох."
    "Стебли клонятся в унисон, шепча секреты, которые тебе не полагается слышать."
    "Затем резко выпрямляются, будто вовсе и не двигались."
    "Ты следишь взглядом за путём ветра, рябью движения по полю, ища форму, которой там нет."


    "Адреналин спадает, оставляя тебя холодным и опустошённым."
    scene grass1
    mc "..."
    mc "Я не уверен, где мне полагается быть..."
    mc "Я не уверен, кем мне полагается быть."
    mc "Но... я не особо знаю, как самому в этом разобраться..."
    mc "Всю мою жизнь...всё как-то просто происходило вокруг меня."
    mc "Не знаю, хорошо это или плохо."
    mc "Но...теперь ощущение, будто меня закинуло в совершенно противоположном направлении."
    scene grass2
    mc "Если я не сделаю то, что необходимо, миру, блядь, придёт конец."
    mc "Но в то же время...что вообще будет считаться необходимым?"
    mc "..."
    mc "Знаю, что вероятность того, что всё в итоге будет хорошо, невелика, но..."
    scene weirdshit (49) with dissolve
    mc "Я же могу помечтать, да?"
    mc "Это разрешено...{w} да?"
    mc "..."
    mc "Прямо сейчас я ничего не могу с этим поделать..."
    mc "Единственный человек, у которого есть хоть малейшее понимание чего-либо — это Кицунэ."
    mc "Такое чувство, будто я тут бегаю кругами."
    mc "Но хотя бы здесь спокойно."


    scene black with fade
    "Ты сидишь там, глядя на невозможные цвета неба."
    stop music fadeout 1.0
    "Тишина тяжёлая. Она давит тебе на грудь, как камень."

    "Затем небо раскалывается."
    play sound "audio/sound/heaven.mp3" 
    play ambient "audio/sound/scarybell.mp3"

    scene weirdshit (50) with hpunch
    "Луч чистого, ослепляющего белого света пронзает облака, обжигая траву вокруг тебя."
    mc "АРГХХ ГОСПОДИ ИИСУСЕ!!"

    "Ты закрываешь глаза от бликов."
    play music "audio/music/cathedral.mp3"
    scene weirdshit (51) with dissolve
    mc "Погоди... Иисусе Христе!?"

    "Свет затвердевает. Фигура медленно спускается, паря в нескольких дюймах над землёй."
    "Она стоит над тобой, руки раскинуты в позе абсолютной, божественной благосклонности."
    "Солнце обрамляет её голову, как нимб."

    scene weirdshit (53) with dissolve


    mc "Отэм...?"

    "На секунду твоё сердце подпрыгивает. Похоже на неё. У неё её лицо, её волосы."
    "Однако в глубине души... ты знаешь."
    scene weirdshit (54) with dissolve
    u "Здравствуй, [mcname]"
    "Это не Отэм."


    mc "Что ты такое? Ты... ты тоже часть моего разума?"
    mc "Это тебя я только что душил? Или ты ещё одна часть меня самого!?"

    "Фигура улыбается — блаженной, гипсово-святой улыбкой."

    u "Лица — это просто занавесы, [mcname]. Я просто ношу тот, которого ты боишься больше всего."
    u "Возможно, тебе нужно напомнить, кто я-"
    play sound "audio/sound/heavenglitch.mp3" 
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (1) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (57) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (1) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (57) with quickflash
    $ renpy.pause (0.01, hard= True)

    "Отэм исчезла. Теперь над тобой стоит Мина, сияя тем же неземным светом."
    "Она смотрит на тебя сверху с бесконечной жалостью."
    mc "Погоди... это ты была той, кто-"
    u "Высвободил свои сексуальные желания на?"
    scene weirdshit (56) with dissolve
    u "Именно так."
    scene weirdshit (55) with dissolve
    u "Посмотри на себя."
    u "Свернулся в грязи собственного разума. Прячешься от той самой силы, для владения которой ты был рождён."
    u "Ты говоришь себе, что защищаешь их. Говоришь себе, что благороден."
    play sound "audio/sound/heavenglitch.mp3" 
    scene weirdshit (57) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (1) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (57) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (1) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)

    u "Но ты просто тянешь время."
    u "Ты ребёнок, отказывающийся покидать утробу, потому что воздух снаружи холодный."

    mc "Я не тяну время! И хватит носить её лицо!"
    "Сущность склоняет голову набок."

    u "Предпочитаешь другую форму? Кого-то... более подходящего твоей слабости?"
    u "Предпочитаешь другую форму? Кого-то... более подходящего твоей слабости?"
    u "Может, одну из множества девушек, чьи сердца ты сейчас коллекционируешь, как трофеи?"

    u "Ты заявляешь, что кого-то «защищаешь», а сам плетёшь паутину полуправды и задержавшихся взглядов, удерживая их всех на своей орбите."

    u "Сколько чувств ты готов раздавить, лишь бы продолжать ощущать себя желанным?"

    u "У тебя в голове тесновато от людей. Скажи мне... кто из них по-настоящему особенный, а кто просто заполнитель для твоего эго?"

    mc "Это не... Я не делаю этого!"

    mc "У-у меня нет выбора!"

    mc "Ты же знаешь, мы пытаемся спасти-"

    u "Грязь в твоём разуме становится ещё грязнее от всех этих слёз, мальчик. Ты не герой..."

    u "Ты просто жонглёр, ждущий, когда упадёт первое стеклянное сердце."


    play sound "audio/sound/heavenglitch.mp3" 
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (2) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_izra with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (2) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_izra with quickflash
    $ renpy.pause (0.01, hard= True)

    u "Тебе нужен кто-то элегантный и твёрдый?"
    u "Кто-то, кто закутает тебя в вату и пообещает, что плохие люди больше тебя не тронут?"
    u "Это то, чего ты хочешь? Быть маленьким?"

    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_izra with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (2) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_lily with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_izra with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (2) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_lily with quickflash
    $ renpy.pause (0.01, hard= True)



    u "Или, может, тебе нужен кто-то напористый."
    u "Кто-то милый, но с характером и рвением?"
    u "Легче быть солдатом, чем генералом, не так ли?"
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_lily with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (3) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_brooklyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_lily with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (3) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_brooklyn with quickflash
    $ renpy.pause (0.01, hard= True)

    u "Может, кого-то {i}Застенчивого{/i}?"
    u "Кого-то невинного. Кого-то, рядом с кем ты чувствуешь себя большим."
    u "Её застенчивость заставляет тебя чувствовать себя сильным, [mcname]? Питает это изголодавшееся эго?"
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_brooklyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (3) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_mei with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_brooklyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (3) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_mei with quickflash
    $ renpy.pause (0.01, hard= True)



    u "Или кого-то {i}Выразительного{/i}?"
    u "Громкая энергия, чтобы заглушить тихие мысли."
    u "Хаос в тишине под стать твоему собственному. Огонь, чтобы сжечь дом, лишь бы не пришлось его убирать."
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_mei with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (4) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_riley with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_mei with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (4) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_riley with quickflash
    $ renpy.pause (0.01, hard= True)


    u "Нет... может, тебе нужна {i}Циничная{/i}."
    u "Кто-то, кто ненавидит мир так же сильно, как и ты."
    u "Кто-то, с кем можно сидеть в темноте и насмехаться над людьми, которые реально стараются."


    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_riley with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (4) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_tamara with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_riley with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (4) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_tamara with quickflash
    $ renpy.pause (0.01, hard= True)


    u "Или {i}Трудолюбивую{/i}."
    u "Работа. Фокус. Дисциплина."
    u "Ты ей восхищаешься, не так ли? Потому что она делает то, что не можешь ты. Она продолжает двигаться."
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_tamara with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (5) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_yuki with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_tamara with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (5) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_yuki with quickflash
    $ renpy.pause (0.01, hard= True)

    u "Возможно, {i}Интровертку{/i}."
    u "Тишина. Общий взгляд. Слова не нужны."
    u "Ты думаешь, она тебя понимает. Но, может, она боится тебя так же, как ты боишься её."
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_yuki with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (5) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_jordyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_yuki with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (5) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_jordyn with quickflash
    $ renpy.pause (0.01, hard= True)


    u "{i}Целеустремлённую{/i}?"
    u "Амбиции. Победа. Успех."
    u "Она бежит навстречу будущему, пока ты бежишь от прошлого. Хочешь, чтобы она несла тебя?"
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_jordyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (6) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_jordyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (6) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)


    u "Или тебе нужна кто-то {i}Холодный{/i}?"
    u "Лёд, чтобы притупить боль. Отстранённость. Безразличие."
    u "Если ты прячешь своё настоящее «я»..."
    u "Если ничего не чувствуешь, то ничего не теряешь. Это тот покой, что ты ищешь?"
    play sound "audio/sound/heavenglitch.mp3" 
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (6) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_nora with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (6) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_nora with quickflash
    $ renpy.pause (0.01, hard= True)



    u "Или, может... может быть..."
    u "Тебе нужен {i}Гламур{/i}."
    u "Красота. Блеск. Отвлечение настолько яркое, что забываешь, что стоишь на кладбище."



    "Свет усиливается. Фигура снова меняется, на этот раз быстрее."
    "Цвета сливаются воедино."

    u "Или, может быть..."
    u "Тебе нужно..."
    play sound "audio/sound/heavenglitch2.mp3" 
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)
    scene weirdshit (54) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_nora with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_lily with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_brooklyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_mei with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_riley with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_tamara with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_yuki with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_jordyn with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_june with quickflash
    $ renpy.pause (0.01, hard= True)
    scene wakeup (7) with quickflash
    $ renpy.pause (0.01, hard= True)
    scene christ_nora with quickflash
    $ renpy.pause (0.01, hard= True)
    stop music
    stop ambient
    scene weirdshit (68) with quickflash
    $ renpy.pause (1, hard= True)
    scene weirdshit (68) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene wakeup (7) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene weirdshit (68) with quickflash
    $ renpy.pause (0.001, hard= True)
    scene wakeup (7) with quickflash
    $ renpy.pause (0.001, hard= True)
    stop sound

    scene hallway (9)
    $ renpy.pause (0.5, hard= True)
    scene hallway (10) with hpunch
    mc "ГАСПППП!"
    scene hallway (11) with dissolve
    mc "Ч-что?"
    scene hallway (12) with dissolve
    mc "..."
    mc "Ой, да ладно!"
    play ambient "audio/ambient/vcr1.mp3" volume 0.2 fadein 1.0
    play music "audio/music/dark.mp3" fadein 1.0

    scene hallway (13) with dissolve
    "Ты снова в Коридоре."
    "Но он другой."
    scene hallway (1) with dissolve
    mc "И что теперь...?"
    mc "Это конец?"

    mc "Погоди, это ещё что за хрень?"
    scene black with fade
    "Ты смотришь на стену прямо рядом с собой."
    scene hallway (14) with dissolve
    "Кто-то написал последовательность цифр на куске скотча. Выглядит свежо."

    "{b}2 1 2 2{/b}"

    "Под цифрами — небольшая, заржавевшая клавиатура, закреплённая на стене."

    mc "Этого тут раньше не было..."

    "Ты подходишь ближе и нажимаешь на кнопки."
    mc "Хмм, интересно, а вдруг..."
    scene hallway (15) with dissolve
    "2... 1... 2... 2..."
    play sound "audio/sound/wrong.mp3"
    scene hallway (16) with hpunch
    "БЗЗЗТ."

    "Ничего не происходит. Огонёк на клавиатуре насмешливо мигает."

    mc "Ну конечно. Это было бы слишком просто."
    mc "Это не для клавиатуры..."
    mc "Тогда для чего вообще это?"


    $ puzzle_sequence = 0

    label hallway_puzzle_loop:
    scene hallway (1) with dissolve
    menu:
        "Проверить код на стене.":
            scene hallway (14) with dissolve
            "Ты смотришь на царапины на штукатурке."
            "{b}2 1 2 2{/b}"
            mc "Хмм..."
            jump hallway_puzzle_loop
        "Открыть ЛЕВУЮ дверь.":

            if puzzle_sequence == 0:
                scene hallway (8) with dissolve
                "Ты снова смотришь на дверь перед собой."

                play sound "audio/sound/dooropen.wav"
                scene hallway (3) with dissolve
                "Ты открываешь Левую дверь."
                "Она открывается в короткий коридор, который сразу же зацикливается обратно в этот же коридор."
                $ puzzle_sequence = 1
                jump hallway_puzzle_loop

            elif puzzle_sequence == 2:
                scene hallway (8) with dissolve
                "Ты снова смотришь на дверь перед собой."

                scene hallway (3) with dissolve
                play sound "audio/sound/dooropen.wav"
                "Ты открываешь Левую дверь."
                "Она открывается в короткий коридор, который сразу же зацикливается обратно в этот же коридор."
                "Ты приближаешься."
                $ puzzle_sequence = 3
                jump hallway_puzzle_loop

            elif puzzle_sequence == 3:
                scene hallway (8) with dissolve
                "Ты снова смотришь на дверь перед собой."

                scene hallway (3) with dissolve
                "Ты открываешь Левую дверь."
                play sound "audio/sound/dooropen.wav"
                jump hallway_puzzle_success
            else:

                scene hallway (8) with dissolve
                "Ты снова смотришь на дверь перед собой."
                scene hallway (3) with dissolve
                "Ты проходишь через дверь."
                jump hallway_puzzle_fail
        "Открыть ПРАВУЮ дверь.":

            if puzzle_sequence == 1:
                scene hallway (7) with dissolve
                "Ты снова смотришь на дверь перед собой."
                scene hallway (2) with dissolve
                play sound "audio/sound/dooropen.wav"
                "Ты открываешь Правую дверь."
                "Ты проходишь через неё и оказываешься там же, где был раньше..."
                $ puzzle_sequence = 2
                jump hallway_puzzle_loop
            else:


                scene hallway (7) with dissolve
                "Ты снова смотришь на дверь перед собой."
                play sound "audio/sound/dooropen.wav"
                scene hallway (2) with dissolve
                "Ты проходишь через дверь."
                jump hallway_puzzle_fail


    label hallway_puzzle_fail:

        scene black with dissolve
        "Пола нет. Коридора нет."
        "Просто абсолютная, ледяная тьма."

        scene hallway (1) with dissolve
        "Ты моргаешь."
        "Ты снова в начале коридора."
        mc "Чёрт...я всё испортил?"
        $ puzzle_sequence = 0
        jump hallway_puzzle_loop


    label hallway_puzzle_success:
        stop music
        scene buttons (1)
        $ renpy.pause (2, hard= True)


        "Оно не двигается."
        "Оно просто ждёт."

        scene buttons (2) with dissolve
        mc "..."

        mc "Мне так много хочется тебе сказать..."
        scene buttons (3) with dissolve

        mc "Но..."

        mc "Единственное, что сейчас приходит мне на ум, это..."
        scene question2
        $ renpy.pause (2, hard= True)
        scene buttons (5)
        $ renpy.pause (1, hard= True)
        scene buttons (6) with dissolve
        $ renpy.pause (1, hard= True)
        play music "audio/music/mother.mp3"
        play sound "audio/sound/hoodie.wav"
        scene buttons (7) with dissolve

        "Медленно ты опускаешься на пол."
        "Фигура холодна на ощупь, но ты почти этого не чувствуешь."
        "На самом деле тебе тепло."
        "Так тепло..."
        mc "..."
        scene buttons (9) with dissolve
        mc "Это нечестно."
        mc "Это никогда не будет честно."

        mc "..."
        mc "Чёрт."
        mc "Даже в собственном разуме я не могу найти слов, чтобы сказать тебе."

        scene buttons (8) with dissolve
        mc "Почему..."
        mc "Почему всё сложилось именно так?"

        mc "Я ничего не чувствую. Будто дыра в груди, которую кто-то должен был заполнить."

        mc "Я даже не знаю, чего хотел... Но в то же время знаю, что части меня не хватает."

        "Ты крепче сжимаешь фигуру."

        scene buttons (12) with dissolve
        mc "У меня должен был быть кто-то в жизни..."

        mc "Кто-то, к кому я мог бы прийти, когда становилось слишком тяжело."

        mc "Теперь у меня есть только я сам..."
        scene buttons (11) with dissolve
        mc "И я даже не могу вспомнить твоё лицо."

        mc "Как мне вообще делать это в одиночку..."

        mc "Почему никто не может просто разбудить меня от этого дурацкого сна, что длится уже десять лет."
        scene buttons (10) with dissolve
        mc "..."

        mc "Я просто хочу маму..."

        "На мгновение воцаряется пугающая неподвижность."
        scene buttons (13) with dissolve
        "Фигура возвышается над тобой, пустота там, где должно быть лицо, не предлагая ни утешения, ни выхода."

        play sound "audio/sound/catchfire.mp3"
        scene buttons (14) with flash
        "Затем тебя окутывает запах дыма — густой, едкий и до жути знакомый."
        "Искры начинают танцевать в воздухе, как умирающие светлячки."


        mc "Н-нет! ХВАТИТ!"

        "Силуэт не кричит."
        "Он просто вспыхивает, серый свет коридора поглощается яростным, голодным оранжевым."
        play sound "audio/sound/smallfire.mp3"
        scene buttons (15) with dissolve

        "Это заканчивается так же быстро, как и началось, пламя мгновенно уносит фигуру."
        "Исчезла в один миг, остаются лишь несколько угольков и случайные языки пламени."
        scene buttons (16) with hpunch
        mc "Ты не можешь так со мной поступать!"

        mc "Только не снова! Пожалуйста!"

        "Нет смысла кричать, коридор лишь эхом повторяет твои же слова."

        "В конце концов, ты снова один."
        scene black with fade
        stop music
        stop sound
        stop ambient
        "Один."
        scene alone2
        $ renpy.pause (2, hard= True)

    scene aftermath (2)
    $ renpy.pause (1, hard= True)
    scene aftermath (3) with hpunch
    mc "ГАСППП!"
    play sound "audio/sound/pants.mp3"
    scene aftermath (1) with hpunch
    "Твои глаза резко распахиваются. Ты рывком подаёшься вперёд, хватаясь за грудь, хватая ртом воздух, который больше не состоит из пепла."
    "Твои глаза резко распахиваются. Ты рывком подаёшься вперёд, хватаясь за грудь, хватая ртом воздух, который больше не состоит из пепла."
    "Спальня выглядит точно так же, как ты её оставил. Тусклый свет. Мятые простыни."
    "Твоя рубашка насквозь пропитана холодным потом."
    play music "audio/music/nights.mp3"
    scene aftermath (4) with dissolve

    k "Эй. Эй, посмотри на меня."

    "Кицунэ хватает тебя за плечо, её золотистые глаза встречаются с твоими, заставляя сосредоточиться на настоящем."
    scene aftermath (5) with dissolve
    k "Ты снова в своей комнате. Ты в безопасности. Просто дыши."

    mc "Но там был этот инопланетянин — Данкл Фанкл — и он на меня орал!"

    mc "А потом какой-то профи-рестлер вёл игровое шоу, а потом девушки... они были ангелами, а потом коридор загорелся и—"
    scene aftermath (6) with dissolve
    k "Воу, воу, помедленнее."

    "Она стирает каплю холодного пота с твоего лба, её выражение смягчается во что-то похожее на настоящее сочувствие."
    scene aftermath (7) with dissolve
    k "Твой мозг только что прошёл через блендер на максимальной скорости. Если попытаешься разобрать всё это прямо сейчас, заработаешь себе аневризму."

    mc "Но мне нужно рассказать тебе, что я видел—"
    scene aftermath (8) with dissolve
    k "И ты расскажешь."
    k "Но сейчас поздно, и ты выглядишь так, будто вот-вот реально вырубишься."
    k "Мы обсудим синих инопланетян и игровые шоу завтра. После школы."

    "Ты делаешь глубокий, дрожащий вдох. Призрачный запах дыма наконец начинает исчезать, сменяясь знакомым, пыльным ароматом твоей собственной комнаты."
    "Твой пульс начинает замедляться до нормального ритма."

    mc "Ладно... ладно. После школы."


    scene aftermath (11) with dissolve
    k "Так... я должна спросить."
    k "За всем этим..."
    scene aftermath (12) with dissolve
    k "Ты нашёл хоть какую-то зацепку насчёт Чумного Доктора?"

    "Вопрос бьёт тебя, как камень."
    "Ты вспоминаешь тёмный коридор, головоломку и силуэт, вспыхнувший пламенем."
    "Доктора там не было. Ничего из этого не было связано с ним."

    "Ты обмякаешь, откидываясь на изголовье, на тебя накатывает тяжёлая волна поражения."

    mc "Нет."
    mc "Ничего. Ни единого его следа."

    "Ты трёшь глаза, эмоциональное и физическое истощение оседает глубоко в костях."
    scene aftermath (7) with dissolve
    mc "Я прошёл через всё это... открыл все эти двери... и всё зря."
    mc "Прости, Кицунэ. Это был полный тупик."

    "Ты ожидаешь, что она разозлится. Ждёшь саркастичного замечания о твоей бесполезности."
    "Вместо этого она просто качает головой и одаривает тебя маленькой, успокаивающей улыбкой."
    scene aftermath (9) with dissolve
    k "Не извиняйся, [mcname]."
    k "Разум — это огромное, запутанное место. Мы выстрелили в темноту и попали в стену. Так бывает."
    scene aftermath (10) with dissolve
    k "Мы рано или поздно что-нибудь узнаем. У этого типа гигантский птичий клюв, вечно прятаться он не сможет."

    mc "Да... наверное."

    "Ты проводишь остаток ночи, пытаясь привести мысли в порядок."

    "Тебе не особо хочется вспоминать всё, что ты видел..."

    "Но ты понимаешь, что во всей этой странности может скрываться что-то важное."

    "И всё же...твоё тело и разум ощущаются затуманенными."
    $ storydream1 += 1

    jump day_cycle

label stillindream:
    stop sound
    stop music fadeout 1
    play music "audio/Music/evening.mp3" volume 1.0 fadein 1
    scene schoolentrance with fade
    "Вы с Отэм решаете пойти домой на сегодня."
    scene dreamreveal (1) with fade
    "Вечер. Можешь отдохнуть или провести время с кем-то.{nw}"
    play music "audio/sound/eveningglitch.mp3" 
    scene dreamreveal (2) with quickdissolve
    $ renpy.pause (4, hard= True)
    stop music
    scene black
    $ renpy.pause (3, hard= True)
    play music "audio/music/creepy.mp3" 
    scene dreamreveal (3)
    $ renpy.pause (3, hard= True)
    show uhoh (1) at center
    u "Путешествие сквозь собственный разум редко бывает отдыхом."

    mc "Ты..."
    mc "Нет. Нет, я проснулся. Кицунэ была прямо там."

    u "Удивительно, насколько реальными кажутся вещи, когда ты этого хочешь."

    u "Но...мы именно там, где нам суждено быть."

    mc "Я всё ещё сплю. Это не реально."

    mc "Да кто ты вообще такой?! Хватит прятаться и ответь мне!"

    u "Я никогда от тебя не прятался. Ты просто предпочитал беспокоиться о других дверях."

    mc "Я теперь слишком глубоко в своём разуме, мне нужны ответы."

    mc "Сними маску."

    u "Опасная просьба..."

    mc "Я сказал, сними её!"

    "Доктор замирает, будто подначивая тебя закричать снова."
    show uhoh (2) with dissolve
    u "Как пожелаешь."

    u "Только будь осторожен со своими желаниями..."
    play sound "audio/sound/jacket.mp3"
    show uhoh (4) with dissolve
    u "Тебе может не понравиться то, что ты увидишь."


    mc "..."
    mc "Нет."
    mc "Нет, это невозможно. Это не реально."
    mc "Это просто мой разум снова со мной играет. Ты просто ещё одна галлюцинация, как и остальные."


    show uhoh (5) with dissolve
    u "Всегда легче отвергнуть отражение, чем признать зеркало."
    mc "Заткнись! Ты не я!"
    mc "Тецуя сказал, что нашёл пулю от другого пистолета!"
    u "Ты когда-нибудь задумывался, почему ты такой наивный?"



    show uhoh (4) with dissolve

    u "Ты так отчаянно цепляешься за поверхность. За эстетику реальности."
    u "Сам факт, что ты хоть на минуту усомнился в себе..."

    u "Означал бы, что где-то глубоко внутри ты думаешь, что способен быть мной..."
    mc "Заткнись! Это просто очередной способ ебать мне мозги!"
    mc "Ты делал это с Отэм, с Миной и со всеми остальными девчонками!"
    mc "Я видел, как ты превращался в меня, это ничем не отличается!"

    show uhoh (3) with dissolve

    mc "Так что заткнись и скажи мне, кто ты на самом деле!"
    mc "Откуда ты!? Откуда я знаю Чумного Доктора!?"

    u "...."
    play sound "audio/sound/thud.mp3"
    show uhoh (7) with hpunch
    "Фигура роняет маску на землю."
    u "Браво! Ты можешь себя похвалить!"
    u "Может, я и не совсем тот, кого ты ищешь, но..."
    u "Ты хорошо потрудился, чтобы добраться сюда, так что я дам тебе подсказку."
    show uhoh (8) with dissolve

    u "Карточка Chromark, что ты нашёл, её символ может быть знакомее, чем ты думаешь."

    mc "Ты о чём..."
    play sound "audio/sound/static.mp3"
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene white with quickflash
    $ renpy.pause (0.01, hard= True)
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene white with quickflash
    $ renpy.pause (0.01, hard= True)
    stop sound
    scene dreamreveal (4) with quickflash
    $ renpy.pause (1, hard= True)
    scene dreamreveal (5) with dissolve
    $ renpy.pause (1, hard= True)

    play sound "audio/sound/static.mp3"
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene white with quickflash
    $ renpy.pause (0.01, hard= True)
    scene black with quickflash
    $ renpy.pause (0.01, hard= True)
    scene white with quickflash
    $ renpy.pause (0.01, hard= True)
    stop sound
    scene dreamreveal (3) with quickflash
    $ renpy.pause (0.01, hard= True)
    show uhoh (9) with hpunch
    mc "Это что вообще было!?"
    u "Не пытайся бежать от самого себя, [mcname]."
    u "Даже если доктор — не ты, ваши души могут быть похожи сильнее, чем ты думаешь..."

    show uhoh (10) with dissolve
    u "Но плоть — это лишь предположение, [mcname]. Временное одеяние."

    mc "Что ты делаешь?"
    show uhoh (11) with hpunch
    play sound "audio/sound/fleshrip.wav"
    u "Всё, что ты можешь по-настоящему знать..."

    mc "Хватит!"
    show uhoh (12) with hpunch
    u "...это то, что лежит..."
    stop music
    play sound "audio/sound/fleshrip3.mp3"
    show uhoh (13) with hpunch
    u "Под этим."
    play sound "audio/sound/evillaugh.mp3"
    show uhoh (14)
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right
    $ renpy.pause (0.001, hard= True)
    show uhoh (16) at left with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (13) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (14) at left
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (16)
    show uhoh (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (17)
    $ renpy.pause (0.001, hard= True)
    show uhoh (20) at left with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (21)
    $ renpy.pause (0.001, hard= True)
    show uhoh (18) at right with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (19)
    $ renpy.pause (0.001, hard= True)
    show uhoh (13) at right with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right
    $ renpy.pause (0.001, hard= True)
    show uhoh (16) at left with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (13)
    $ renpy.pause (0.001, hard= True)
    show uhoh (14) at left with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right
    show uhoh (15) at right
    $ renpy.pause (0.001, hard= True)
    show uhoh (16) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (13) at right
    $ renpy.pause (0.001, hard= True)
    show uhoh (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (17) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (20) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (21) at left
    $ renpy.pause (0.001, hard= True)
    show uhoh (18) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (19) at right
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (16) at left
    $ renpy.pause (0.001, hard= True)
    show uhoh (6) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (17)
    $ renpy.pause (0.001, hard= True)
    show uhoh (20) at left with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (21)
    $ renpy.pause (0.001, hard= True)
    show uhoh (18) at right with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (19)
    $ renpy.pause (0.001, hard= True)
    show uhoh (13) with quickflash
    $ renpy.pause (0.001, hard= True)
    show uhoh (14) at left
    $ renpy.pause (0.001, hard= True)
    show uhoh (15) at right
    $ renpy.pause (0.001, hard= True)

    stop music
    scene realawake (1) with hpunch
    play sound "audio/sound/thud.mp3"
    scene realawake (2) with hpunch
    mc "ААААААХ!"

    play sound "audio/sound/heartbeat.mp3" 

    "Ты дёргаешься вверх так резко, что хрустит позвоночник."
    "Твои руки мгновенно взлетают к собственному лицу, ты царапаешь себя, чтобы убедиться, что кожа всё ещё на месте. Что под ней нет черепа."
    "Комната бешено вращается. Тусклый свет твоей спальни ощущается как взгляд прямо на солнце."
    scene realawake (3)
    mc "О боже... о боже..."

    "Ты пытаешься заговорить, но твой желудок яростно бунтует."
    "Токсичный коктейль из Бенадрила, адреналина и чистого ужаса вызывает немедленное физическое отторжение."
    scene realawake (4) with hpunch
    play sound "audio/sound/splat.mp3" 

    mc "{i}БЛЕВОООТА{/i}"

    "Ты перегибаешься через край кровати, и тебя рвёт."
    "Поток розоватой жидкости и желчи выплёскивается на половицы."

    scene realawake (5) with dissolve
    "Тебя продолжает выворачивать, грудь горит, пока тело выгоняет из себя каждый след наркотика."

    mc "Уф... {i}кхе{/i}... аах..."

    "Ты падаешь обратно на матрас, неконтролируемо дрожа. Пот щиплет глаза."
    "Сквозь размытое зрение ты видишь Кицунэ."

    scene realawake (6) with dissolve
    mc "Кицунэ... это было..."

    "Ты пытаешься подобрать слова, но зубы стучат слишком сильно."

    k "..."
    play sound "audio/sound/hoodie.wav" 
    scene realawake (7) with dissolve
    k "В-всё хорошо."

    scene realawake (8) with dissolve
    "Медленно она тянется и обхватывает руками твои дрожащие плечи."

    k "Всё хорошо."

    "Она прижимает тебя к своей груди, её руки нежно прижимают затылок, укачивая тебя."
    k "Всё хорошо, [mcname]."
    scene realawake (9) with dissolve

    k "Ты вернулся. Я держу тебя. Сейчас всё будет хорошо..."
    scene black with fade
    $ renpy.pause (1, hard= True)
    "Ты позволяешь себе несколько часов, чтобы прийти в себя."
    "Ты пытаешься объяснить Кицунэ, что произошло."
    "Ну...{w}насколько это вообще возможно."
    "К тому моменту, как твой разум проясняется, уже наступает утро."

    $ firstdream += 1
    $ storydream2 += 1
    $ totaldays += 1
    $ day += 1

    if day == 1:
        hide sunday onlayer date
        show monday onlayer date

    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date

    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date

    if day == 5:
        hide thursday onlayer date
        show friday onlayer date

    if day == 6:
        hide friday onlayer date
        show saturday onlayer date

    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date


    scene chap1bed with dissolve

    play music "audio/music/sadguitar.mp3" fadein 2.0

    "Солнечный свет пробивается сквозь жалюзи, отбрасывая резкие, яркие полосы на твою кровать."
    "Голова пульсирует, тупая боль стучит за глазами."
    "Ты медленно садишься. Беспорядок, что ты устроил на полу прошлой ночью, уже убран."

    show mc_sluggish at center with dissolve
    mc "Ты...{w} ну знаешь...{w} настоящая на этот раз?"
    mc "Или я всё ещё в ловушке собственного разума?"

    show kitsune_neutral at left with dissolve
    k "..."
    play sound "audio/sound/punch.mp3" 
    hide kitsune_neutral
    show kitsune_neutral at left with hpunch
    "И сильно бьёт тебя по руке."

    hide mc_sluggish
    show mc_shocked at right
    with hpunch
    mc "Ай! Да что за хрень?!"

    hide kitsune_neutral
    show kitsune_smug at left
    k "Достаточно реально для тебя, идиот?"
    k "Ты проснулся. Больше никакого мусора со сном-внутри-сна. Ты обратно в скучном, физическом мире."

    hide mc_shocked
    show mc_sigh at right
    "Ты трёшь плечо, выпуская долгий вздох облегчения."
    "Затянувшийся ужас черепа и огня наконец начинает испаряться в утреннем свете."

    mc "Ладно. Ладно, хорошо."

    k "Ну?"
    k "Теперь, когда твой мозг не вытекает из ушей, расскажешь, что на самом деле там произошло?"
    k "Есть хоть какие-то зацепки?"

    hide mc_sigh
    show mc_armedcross at right
    mc "Вообще-то... да. Есть."
    scene sketch (1) with dissolve
    "Ты спускаешь ноги с кровати и хватаешь блокнот и ручку с тумбочки."

    mc "Там была дверь. И логотип."
    mc "Он выжжен у меня в памяти. Почти фотографически."

    play sound "audio/sound/paper.wav"
    scene sketch (2) with dissolve
    "Ты быстро зарисовываешь форму, что видел в темноте — характерные, рваные линии символа Chromark."

    mc "Чумной Доктор... или что бы там ни носило его лицо... сказал мне, что это подсказка. Что это знакомее, чем я думаю."

    scene sketch (4) with dissolve
    "Кицунэ вглядывается в набросок. Её уши дёргаются, она склоняет голову набок."

    k "Хм..."
    k "Я это узнаю... вроде как."
    mc "Правда? Что это?"

    scene sketch (5) with dissolve
    k "Не помню точно, {i}что{/i} это. Моя память всё ещё полна дыр."
    k "Но глядя на это... что-то щёлкает. Место. Кажется, я знаю, где это, или хотя бы общее направление."
    k "Извини."
    scene sketch (3) with dissolve
    mc "Ты серьёзно? Это же огромный прорыв!"
    mc "Это лучше, чем ничего. Давай, идём. Прямо сейчас."
    scene chap1bed with dissolve
    "Ты встаёшь, но Кицунэ тут же преграждает тебе путь, скрещивая руки."

    hide kitsune_dissapointed
    show kitsune_annoyed at left
    k "Нет."

    hide mc_shocked
    show mc_angry at right
    mc "Как это «нет»? У нас наконец-то есть зацепка!"

    k "Я имею в виду {i}нет{/i}, [mcname]."
    k "Ты не готов. Посмотри на себя. Ты еле стоишь прямо без гримасы боли."
    k "Тебе нужно больше тренировок. Мы не допустим повторения прошлого раза, когда ты чуть себя не угробил, влетев туда вслепую."

    mc "Я выжил, разве нет?"

    k "Еле-еле! А ставки растут."
    k "Тебе нужно лучше контролировать свои силы. Нужно выучить ещё пару приёмов."
    k "Но важнее всего..."

    "Она сильно тычет тебя пальцем в грудь."

    k "...тебе нужно стать намного, намного лучше в рукопашном бою. Если твои силы дадут сбой или их заблокируют, ты дерёшься как мокрая макаронина."

    hide mc_angry
    show mc_dissapointed at right
    mc "Эй! Я нормально бью!"

    hide kitsune_annoyed
    show kitsune_smug at left
    k "Ты бьёшь так, будто боишься сломать себе запястье."
    k "Тебе нужен учитель. Кто-то, кто реально умеет драться."



    if yejindojointro == 1 and yejinblackmail == 1:

        mc "..."
        mc "Ну... вообще-то, есть один человек."

        hide kitsune_smug
        show kitsune_neutral at left
        k "О? Кто?"

        mc "Йеджин."
        mc "Она, по сути, заправляет тем додзё в городе, и она пугающе хороша в драке."

        hide mc_dissapointed
        hide mc_dissapointed
        show mc_worried at right
        "Ты морщишься, холодный пот выступает на затылке от одной только мысли о ней."

        mc "Но мне правда, ну очень не хочется её просить."

        hide kitsune_neutral
        show kitsune_smug at left
        k "Почему нет? Звучит идеально."

        mc "Потому что она мерзкая, Кицунэ! Она меня шантажирует."
        mc "Я, по сути, её «игрушка» прямо сейчас. Если я попрошу её тренировать меня, она будет держать это надо мной и превратит мою жизнь в сущий ад."

        k "Сущий ад, в котором ты реально научишься нормально бить хуком и защищаться от захватов? По мне, так честный обмен."
        k "Иди поговори с ней."

    elif yejindojointro == 1 and yejinblackmail == 0:

        mc "..."
        mc "Есть, наверное, один человек. Йеджин."

        hide kitsune_smug
        show kitsune_neutral at left
        k "Кто это?"

        mc "Девушка из школы. Я уже бывал в додзё её семьи, и знаю, что она серьёзно подкована в боевых искусствах."

        hide kitsune_neutral
        show kitsune_happy at left
        k "Отлично. Проблема решена. Иди спроси её."

        hide mc_dissapointed
        show mc_worried at right
        mc "Не так всё просто. Мы не то чтобы близкие друзья."
        mc "Если я просто подойду ни с того ни с сего и попрошу её натренировать меня драться за свою жизнь, она подумает, что я псих."
        mc "Мне нужно будет какое-то время узнавать её получше, прежде чем вываливать на неё такую огромную просьбу."

        hide kitsune_happy
        show kitsune_smug at left
        k "Что ж, тогда тебе лучше начать включать обаяние."
        k "Иди в додзё и посмотри, сможешь ли зацепиться там хоть как-то."

    elif yejindojointro == 0 and yejinblackmail == 0:

        mc "..."
        hide mc_dissapointed
        show mc_sluggish at right
        mc "У меня никого нет."

        hide kitsune_smug
        show kitsune_neutral at left
        k "Никого? Ты не знаешь ни одного человека, который прилично бьёт кулаком?"

        hide mc_sluggish
        show mc_armedcross at right
        mc "Я играю в видеоигры и читаю комиксы, Кицунэ. Мой круг общения не особо переполнен подпольными бойцами."
        mc "Я буквально не знаю никого, кто разбирается в рукопашном бою."

        hide kitsune_neutral
        show kitsune_dissapointed at left
        k "Уф. Бесполезный."
        k "Ладно. Тогда твоя первая миссия — найти спортзал, додзё или злого мужика в переулке."
        k "Ты найдёшь того, кто тебя натренирует, иначе мы даже близко не подойдём к той двери."




    hide mc_armedcross
    hide mc_sluggish
    hide mc_worried
    show mc_sigh at right
    mc "Ладно, ладно. Я тебя услышал."
    mc "Разберусь с боевыми тренировками."

    hide kitsune_dissapointed
    show kitsune_smug at left
    k "Хорошо."
    k "А теперь иди прими душ. От тебя несёт застоявшимся потом и страхом."

    hide kitsune_smug
    show kitsune_neutral at left
    with dissolve
    k "И, [mcname]..."

    hide mc_sigh
    show mc_armedcross at right
    k "Я рада, что ты в порядке."
    play sound "audio/sound/flash.wav" 
    hide kitsune_neutral with flash
    "Кицунэ исчезает во вспышке оранжевого и белого, прежде чем ты успеваешь осознать перемену в её голосе."

    hide mc_armedcross
    show mc_sorry at center
    with dissolve
    mc "(После всего, что случилось....)"
    mc "(...не уверен, что я в это верю.)"
    mc "(Но, опять же, с ней я никогда ни в чём не уверен.)"

    scene black with fade
    $ main.quest =  "Поговорить с Кицунэ о тренировках вечером."
    "У тебя есть зацепка. У тебя есть цель."
    "Пора браться за дело."
    jump class_scene
return