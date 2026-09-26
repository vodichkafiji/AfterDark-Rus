













define config.name = _("Покровы Ночи")

define config.layers = [ 'master', 'transient', 'screens', 'date', 'overlay' ]





define gui.show_name = False




define config.version = "0.26"





define gui.about = _p("""
Автор русификатора: {a=https://github.com/vodichkafiji/AfterDark-Rus}vodichkafiji{/a}

{space=30}{p}
Разработчик: {p}
{image=gui/dev_logo.webp}{p}
{space=30}Bozavest {p}
{a=https://www.patreon.com/bozavest}{image=gui/patreon.png} Patreon{/a} - {a=https://bozavest.itch.io/after-dark}{image=gui/itch.io.png} Itch.io{/a}


{space=30}Отдельная благодарность{p}
{a=}{image=gui/bootykat.png} BootyKat (контроль качества){/a} - {a=https://x.com/Gamingrecluse11}{image=gui/recluse.png} Recluse (художник){/a}



{space=30}Аниматоры{p}
{a=https://x.com/Tiaramix1527}{image=gui/Tiaramix.png} Mix (аниматор — анимации Джун){/a} 

{space=10}{a=https://rebel-tomboy-games.itch.io/project-dreadsteel}{image=gui/TheLolingPain.png} TheLolingPain (аниматор — анимации минета Изры и Утами){/a} 
""")





define build.name = "AfterDark"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "audio/Afterdark.mp3"









define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "AfterDark-1663758551"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)






    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.webp', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')