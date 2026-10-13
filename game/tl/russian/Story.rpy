


image mainquest_art = "images/quest/kitsune_menu.webp"

transform mq_art_br:
    anchor (1.0, 1.0)
    align (0.98, 0.7)
    zoom 0.9
    alpha 0.95




init python:
    class MainState:
        def __init__(self):
            self.strength = 0         
            self.quest = ""           
            self.req_strength = 0     




    def refresh_main():
        if not hasattr(main, "strength"):
            main.strength = 0
        if not getattr(main, "quest", ""):
            main.quest = "Продолжай историю."
        
        
        
        main.req_strength = 5 if getattr(store, "pushupintro", 0) == 1 and not getattr(store, "firstfight", 0) else 0


default main = MainState()

label after_loadmain:
    $ refresh_quests()
    $ refresh_main()
    return




style mainquest_title is quest_text
style mainquest_title:
    size 300
style mainquest2_title:
    size 200
    font "Barlow-Black.ttf"
    outlines [(16, "#000000", 0, 0)]




screen main_quest():
    tag menu

    use game_menu(_("Главное задание"), scroll=None):
        on "show" action Function(refresh_main)
        add "mainquest_art" at mq_art_br


        imagebutton:
            idle "gui/eventreplay_idle.png"
            hover "gui/eventreplay_hover.png"
            action ShowMenu("oscar_replay_gallery")
            xpos 50
            ypos 1350

        frame:
            xalign 0.5
            yalign 0.00
            background None
            text "История" style "mainquest_title" size 400 xalign 0.5 yoffset -200


        frame:
            xalign 0.5
            yalign 0.4
            xsize 0.85
            background None
            top_padding 0
            has vbox
            spacing 18

            hbox:
                spacing 24
                text "Очки силы: [main.strength]" style "mainquest2_title" size 200
                if main.req_strength > 0:
                    text "(Нужно: [main.req_strength] силы)" size 200

            if main.req_strength > 0:



                bar value StaticValue(main.strength, max(main.req_strength, 1)) xmaximum 1000

            vbox:
                spacing 2
                text "Текущая цель:" style "mainquest2_title" size 200
                text "[main.quest]" style "mainquest2_title" size 150 xmaximum 2000




label main_quest_demo:
    "Открывается страница Главного квеста..."
    show screen main_quest
    "Попробуйте изменить значение main.strength в консоли или с помощью событий, чтобы понаблюдать за его обновлением."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
