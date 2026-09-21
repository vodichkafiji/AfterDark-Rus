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

    def _compute_main_quest(state):
        """
    Update the main quest text and its requirement based on current Strength.
    Tweak thresholds/text to match your story beats.
    """
        s = state.strength
        if s < 5:
            state.quest = "Сходи в спортзал. Достигни - Сила 5."
            state.req_strength = 5
        elif s < 10:
            state.quest = "Потренируйся с Паркером за спортивным залом. Достигни - Сила 10."
            state.req_strength = 10
        elif s < 15:
            state.quest = "В сумерках проникни через южную стену школы. Достигни - Сила 15."
            state.req_strength = 15
        else:
            
            state.quest = "Отправляйтесь на крышу ночью, чтобы продолжить сюжет."
            state.req_strength = 15

    def refresh_main():
        _compute_main_quest(main)


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
    font "NotoSansDisplay-ExtraBold.ttf"
    outlines [(16, "#000000", 0, 0)]




screen main_quest():
    tag menu


    use game_menu(_("Главный квест"), scroll=None):
        on "show" action Function(refresh_main)
        add "mainquest_art" at mq_art_br
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
                bar value FieldValue(main, "strength", max(main.req_strength, 1)) xmaximum 1000


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
