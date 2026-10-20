init offset = -1









style custominput:
    properties gui.text_properties("custominput", accent=True)
    adjust_spacing False

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")




style image_button:
    focus_mask True

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style fanart_thumb is image_button:
    xpadding 3
    ypadding 3
    background Solid("#222222")
    hover_background Solid("#66aaff")


default ad_fullscreen_menu_open = False
default ad_hidden_weekday_tags = []

init python:
    def ad_menu_visibility(transform, st, at):
        """Keeps map HUD elements hidden while Ren'Py is in a full game menu."""
        transform.alpha = 0.0 if renpy.store._menu else 1.0
        return 0.05

    def ad_hide_weekday_indicator():
        """Temporarily hide the active weekday image while a game menu is open."""
        weekday_tags = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
        showing_tags = renpy.get_showing_tags(layer="date")
        renpy.store.ad_hidden_weekday_tags = [tag for tag in weekday_tags if tag in showing_tags]
        for tag in renpy.store.ad_hidden_weekday_tags:
            renpy.hide(tag, layer="date")

    def ad_restore_weekday_indicator():
        """Restore only the weekday image that was visible before the game menu."""
        for tag in renpy.store.ad_hidden_weekday_tags:
            renpy.show(tag, layer="date")
        renpy.store.ad_hidden_weekday_tags = []





















screen day_tracker():

    zorder -10

    if not ad_fullscreen_menu_open:
        frame:
            align (0.99, 0)
            padding (0, 10)
            text "День [totaldays]" size 100 font "NotoSansDisplay-ExtraBold.ttf" color "#FFFFFF" outlines [(3, "#000000", 1, 1)] at slide_in_delay_5


screen say(who, what, namebox_type=None):

    style_prefix "say"
    window:
        background Transform(style.window.background, alpha=persistent.say_window_alpha)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                background Transform(Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign), alpha=persistent.say_window_alpha)
                text who id "who"

        id "window"
        text what id "what" kerning persistent.say_dialogue_kerning font persistent.pref_text_font size persistent.pref_text_size




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 300
    xanchor gui.name_xalign
    xsize 1100
    ypos -75
    ysize 150

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 650
    xsize 2500
    ypos 150

    adjust_spacing False











screen input(prompt):
    style_prefix "input"

    frame:
        background Frame("gui/input_frame_bg.png", Borders(25,25,25,25))
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 100
        has vbox
        spacing 10
        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    color '#fff'
    font 'fonts/NotoSansDisplay-ExtraBold.ttf'

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    color '#fff'
    font 'fonts/NotoSansDisplay-ExtraBold.ttf'








screen custominput(prompt):
    style_prefix "custominput"

    window:


        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "custominput_prompt"
        input id "input" style "custominput_input"

style custominput_prompt is default
style custominput_prompt:
    xalign gui.dialogue_text_xalign

    properties gui.text_properties("custominput_prompt")
    font 'fonts/NotoSansDisplay-ExtraBold.ttf'

style custominput_input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    font 'fonts/NotoSansDisplay-ExtraBold.ttf'

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

screen two_col_choice(items):
    style_prefix "choice"

    hbox:

        spacing 16
        xalign 0.5




        vbox:
            xalign 0.5
            xsize 500
            for idx, it in enumerate(items):
                if idx % 2 == 0:
                    textbutton it.caption:
                        action it.action
                        xfill True


        vbox:
            xalign 0.5
            xsize 500
            for idx, it in enumerate(items):
                if idx % 2 == 1:
                    textbutton it.caption:
                        action it.action
                        xfill True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 1000
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xpadding 60


style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    font "9925.ttf"
    size 90
    color "#ffffff"
    outlines [(10, "#000000", 0, 0)]
    xmaximum 880

style choice_button_text_hover is choice_button_text:
    color "#1d1d1d"
    outlines [(10, "#ffffff", 0, 0)]





screen left_menu(choices):
    style_prefix "choice"

    vbox:
        xalign 0.01
        yalign 0.4


        for caption, action in choices:
            textbutton caption:
                action action
                text_size 150

screen right_menu(choices):
    style_prefix "choice"

    vbox:
        xalign 1.1
        yalign 0.4


        for caption, action in choices:
            textbutton caption:
                action action
                text_size 150


screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:

            yoffset -35

            xoffset -100


            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Задания") action ShowMenu('quests')
            textbutton _("Быстр.сохранение") action QuickSave()
            textbutton _("Быстр.загрузка") action QuickLoad()
            textbutton _("Настройки") action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True



style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    idle_color "#FFFFFF"
    hover_color "#FFFFFF"
    selected_idle_color "#FFFFFF"
    selected_hover_color "#FFFFFF"
    size (gui.quick_button_text_size - 4)

style quick_main_button is quick_button
style quick_main_button_text is quick_button_text:
    color "#FFFFFF"
    hover_color "#FFFFFF"
    selected_idle_color "#FFFFFF"
    selected_hover_color "#FFFFFF"
    size 38










screen Autumnaction_menu():
    tag action_menu

    vbox:
        xpos 1500
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("skatepark_noonhang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("skatepark_noonwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Autumn"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5
screen Brooklynaction_menu():
    tag action_menu

    vbox:
        xpos 1500
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("mall_morninghang")
                at slide_in_delay_3

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("mall_morningwait")
                at slide_in_delay_4

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Brooklyn"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_5
            xalign 0.5


screen Graceaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("mall_eveninghang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("mall_eveningwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Grace"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Izraaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("skatepark_morninghang")
                at slide_in_delay_3

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("skatepark_morningwait")
                at slide_in_delay_4

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Izra"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_5
            xalign 0.5

screen Juneaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("alley_noonhang")
                at slide_in_delay_3

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("alley_noonwait")
                at slide_in_delay_4

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "June"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_5
            xalign 0.5


screen Jordynaction_menu():
    tag action_menu

    vbox:
        xpos 1500
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("park_noonhang")
                at slide_in_delay_3

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("park_noonwait")
                at slide_in_delay_4

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Jordyn"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_5
            xalign 0.5


screen Lilyaction_menu():
    tag action_menu

    vbox:
        xpos 40
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("park_eveninghang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("park_eveningwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Lily"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Meiaction_menu():
    tag action_menu

    vbox:
        xpos 40
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("park_morninghang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("park_morningwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Mei"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5


screen Noraaction_menu():
    tag action_menu

    vbox:
        xpos 40
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("mall_noonhang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("mall_noonwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Nora"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Parkeraction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("city_eveninghangparker")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("city_eveningwaitparker")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Parker"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Rileyaction_menu():
    tag action_menu

    vbox:
        xpos 1500
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("arcade_morninghang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("arcade_morningwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"



            action [SetVariable("ad_gift_target", "Riley"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Tamaraaction_menu():
    tag action_menu

    vbox:
        xpos 40
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("bar_hang")
                at slide_in_delay_0

            imagebutton:
                idle Transform("wait_idle.png", crop=(8, 444, 649, 573), size=(642, 566))
                hover Transform("wait_hover.png", crop=(8, 444, 649, 573), size=(642, 566))
                xoffset 8
                yoffset 444
                action Jump("bar_wait")
                at slide_in_delay_1

        hbox:
            spacing 20

            imagebutton:
                idle "gift_idle.png"
                hover "gift_hover.png"
                focus_mask True
                xoffset 188
                action [SetVariable("ad_gift_target", "Tamara"), SetVariable("ad_gift_message", ""), SetVariable("ad_gift_is_error", False), SetVariable("ad_gift_show_result", False), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
                at slide_in_delay_2

            imagebutton:
                idle ad_tamara_work_button_idle
                hover ad_tamara_work_button_hover
                focus_mask True
                xoffset -180
                action Jump("tamara_work")
                at slide_in_delay_2

screen Utamiaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("mall_eveninghangutami")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("mall_eveningwaitutami")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Utami"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Yejinaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("city_eveninghangyejin")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("city_eveningwaityejin")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Yejin"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

screen Yukiaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 200
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                focus_mask True
                action Jump("con_eveninghang")
                at slide_in_delay_3

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                focus_mask True
                action Jump("con_eveningwait")
                at slide_in_delay_4




        hbox:
            spacing 20

            imagebutton:
                idle "gift_idle.png"
                hover "gift_hover.png"
                focus_mask True
                xoffset 188
                action [SetVariable("ad_gift_target", "Yuki"), SetVariable("ad_gift_message", ""), SetVariable("ad_gift_is_error", False), SetVariable("ad_gift_show_result", False), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
                at slide_in_delay_5

            imagebutton:
                idle ad_yuki_store_button_idle
                hover ad_yuki_store_button_hover
                focus_mask True
                action Return("store")
                at slide_in_delay_5

screen Zaraaction_menu():
    tag action_menu

    vbox:
        xpos 1600
        ypos 100
        spacing 20

        hbox:
            spacing 20
            imagebutton:
                idle "hangout_idle.png"
                hover "hangout_hover.png"
                action Jump("skatepark_eveninghang")
                at slide_in_delay_0

            imagebutton:
                idle "wait_idle.png"
                hover "wait_hover.png"
                action Jump("skatepark_eveningwait")
                at slide_in_delay_1

        null height 10

        imagebutton:
            idle "gift_idle.png"
            hover "gift_hover.png"
            action [SetVariable("ad_gift_target", "Zara"), SetVariable("ad_gift_message", ""), Show("ad_gifting_input_blocker"), Show("ad_character_gifting_screen")]
            at slide_in_delay_2
            xalign 0.5

transform slide_in_delay_0:
    alpha 0
    xoffset -400
    easein 0.4 xoffset 0 alpha 1

transform slide_in_delay_1:
    alpha 0
    xoffset -400
    pause 0.15
    easein 0.4 xoffset 0 alpha 1

transform slide_in_delay_2:
    alpha 0
    xoffset -400
    pause 0.3
    easein 0.4 xoffset 0 alpha 1

transform slide_in_delay_3:
    alpha 0
    xoffset 400
    easein 0.4 xoffset 0 alpha 1

transform slide_in_delay_4:
    alpha 0
    xoffset 400
    pause 0.15
    easein 0.4 xoffset 0 alpha 1

transform slide_in_delay_5:
    alpha 0
    xoffset 400
    pause 0.3
    easein 0.4 xoffset 0 alpha 1
    function ad_menu_visibility

screen start_choice():
    modal True
    zorder 100
    add Solid("#0008")

    vbox:
        xalign 0.5
        yalign 0.6
        spacing 30

        imagebutton:
            idle "gui/beginning_idle.png"
            hover "gui/beginning_hover.png"
            action Jump("actualintro")

        imagebutton:
            idle "gui/world_idle.png"
            hover "gui/world_hover.png"
            action Jump("skiptoworld")

transform startbutton:

    on idle:
        easein 0.05 rotate 0 zoom 1.0
    on hover:
        rotate 0
        easein 0.05 rotate 10 zoom 1.05
        easein 0.05 rotate -8 zoom 1.05
        easein 0.05 rotate 6 zoom 1.05
        easein 0.05 rotate -4 zoom 1.05
        easein 0.05 rotate 0 zoom 1.05

transform loadbutton:

    on idle:
        easein 0.05 rotate 0 zoom 1.0
    on hover:
        rotate 0
        easein 0.05 rotate 10 zoom 1.05
        easein 0.05 rotate -8 zoom 1.05
        easein 0.05 rotate 6 zoom 1.05
        easein 0.05 rotate -4 zoom 1.05
        easein 0.05 rotate 0 zoom 1.05

transform settingsbutton:

    on idle:
        easein 0.05 rotate 0 zoom 1.0
    on hover:
        rotate 0
        easein 0.05 rotate 10 zoom 1.05
        easein 0.05 rotate -8 zoom 1.05
        easein 0.05 rotate 6 zoom 1.05
        easein 0.05 rotate -4 zoom 1.05
        easein 0.05 rotate 0 zoom 1.05

transform biosbutton:

    on idle:
        easein 0.05 rotate 0 zoom 1.0
    on hover:
        rotate 0
        easein 0.05 rotate 10 zoom 1.05
        easein 0.05 rotate -8 zoom 1.05
        easein 0.05 rotate 6 zoom 1.05
        easein 0.05 rotate -4 zoom 1.05
        easein 0.05 rotate 0 zoom 1.05


screen navigation():

    fixed:
        style_prefix "navigation"
        spacing 40

        if main_menu:

            imagebutton auto "gui/start_%s.png" action Start() at startbutton xpos 70 ypos 725 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/load_%s.png" action ShowMenu("load") at loadbutton xpos 70 ypos 900 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/settings_%s.png" action ShowMenu("preferences") at settingsbutton xpos 80 ypos 1030 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/about_%s.png" action ShowMenu("about") at biosbutton xpos 70 ypos 1220 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"




        else:

            imagebutton auto "gui/history_%s.png" action ShowMenu("history") at loadbutton xpos 60 ypos 100 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/save_%s.png" action ShowMenu("save") at loadbutton xpos 70 ypos 300 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"

            imagebutton auto "gui/load_%s.png" action ShowMenu("load") at loadbutton xpos 70 ypos 450 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"

            imagebutton auto "gui/settings_%s.png" action ShowMenu("preferences") at settingsbutton xpos 80 ypos 550 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"

            imagebutton auto "gui/about_%s.png" action ShowMenu("about") at biosbutton xpos 70 ypos 1000 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"







        if _in_replay:

            textbutton _("Закончить повтор") action EndReplay(confirm=True)

        elif not main_menu:
            imagebutton auto "gui/story_%s.png" action ShowMenu("main_quest") at biosbutton xpos 70 ypos 710 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/quest_%s.png" action ShowMenu("quests") at biosbutton xpos 70 ypos 840 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
            imagebutton auto "gui/mainmenu_%s.png" action MainMenu() at biosbutton xpos 60 ypos 1050 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"

        if renpy.variant("pc") and main_menu:



            imagebutton auto "gui/quit_%s.png" action Quit(confirm=not main_menu) at biosbutton xpos 70 ypos 1370 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"
        elif renpy.variant("pc"):
            imagebutton auto "gui/quit_%s.png" action Quit(confirm=not main_menu) at biosbutton xpos 70 ypos 1290 hovered Play("sound", "audio/sound/hover.mp3") activate_sound "audio/sound/select.mp3"

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")







transform wiggle_on_hover:
    on idle:
        easein 0.05 rotate 0
    on hover:
        rotate 0
        easein 0.05 rotate 10
        easein 0.05 rotate -8
        easein 0.05 rotate 6
        easein 0.05 rotate -4
        easein 0.05 rotate 0

transform patreonbutton:
    xalign 0.99
    yalign 1.0
    on idle:
        easein 0.05 rotate 0
    on hover:
        rotate 0
        easein 0.05 rotate 10
        easein 0.05 rotate -8
        easein 0.05 rotate 6
        easein 0.05 rotate -4
        easein 0.05 rotate 0
transform discordbutton:
    xalign 0.9
    yalign 1.0
    on idle:
        easein 0.05 rotate 0
    on hover:
        rotate 0
        easein 0.05 rotate 10
        easein 0.05 rotate -8
        easein 0.05 rotate 6
        easein 0.05 rotate -4
        easein 0.05 rotate 0
transform itchbutton:
    xalign 0.82
    yalign 1.0
    on idle:
        easein 0.05 rotate 0
    on hover:
        rotate 0
        easein 0.05 rotate 10
        easein 0.05 rotate -8
        easein 0.05 rotate 6
        easein 0.05 rotate -4
        easein 0.05 rotate 0





screen main_menu():
    tag menu



    add gui.main_menu_background
    imagebutton auto "gui/patreon_%s.png":
        action OpenURL("https://patreon.com/Bozavest?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink")
        at patreonbutton
        focus_mask True
        hover_sound "audio/Sound/hover.mp3"
        activate_sound "audio/Sound/select.mp3"

    imagebutton auto "gui/discord_%s.png":
        action OpenURL("https://discord.gg/jWBcjvwkjM")
        at discordbutton
        focus_mask True
        hover_sound "audio/Sound/hover.mp3"
        activate_sound "audio/Sound/select.mp3"

    imagebutton auto "gui/itch_%s.png":
        action OpenURL("https://bozavest.itch.io")
        at itchbutton
        focus_mask True
        hover_sound "audio/Sound/hover.mp3"
        activate_sound "audio/Sound/select.mp3"







    frame:
        style "main_menu_frame"



    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 840
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -60
    xmaximum 2400
    yalign 1.0
    yoffset -60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    on "show" action [SetVariable("ad_fullscreen_menu_open", True), Hide("day_tracker"), Function(ad_hide_weekday_indicator)]
    on "hide" action [SetVariable("ad_fullscreen_menu_open", False), Show("day_tracker"), Function(ad_restore_weekday_indicator)]

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Назад"):
        style "return_button"

        action Return()


    label title:
        style "quick_menu_title_label"
        xcenter int((config.screen_width + 840) / 2)

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 90
    top_padding 360

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 840
    yfill True

style game_menu_content_frame:
    left_margin 120
    right_margin 60
    top_margin 30

style game_menu_viewport:
    xsize 2760

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 30

style game_menu_label:
    xpos 150
    ysize 350

style game_menu_label_text:
    size gui.title_text_size
    color gui.choice_button_text_hover_color
    yalign 0.4

style quick_menu_title_label is game_menu_label:
    xanchor 0.5

style quick_menu_title_label_text is game_menu_label_text:
    color "#FFFFFF"

style about_game_menu_label is game_menu_label

style about_game_menu_label_text is game_menu_label_text:
    color "#FFFFFF"

style settings_game_menu_label is about_game_menu_label:
    xpos 100

style settings_game_menu_label_text is about_game_menu_label_text

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -90


transform about_link_hover:
    subpixel True
    xoffset 0
    yoffset 0
    zoom 1.0
    alpha 0.92
    on idle:
        easeout 0.20 xoffset 0 yoffset 0 zoom 1.0 alpha 0.92
    on hover:
        easein 0.07 xoffset 1 yoffset 2 zoom 0.985 alpha 0.88
        easeout 0.13 xoffset 0 yoffset -7 zoom 1.075 alpha 1.0
        easein 0.11 yoffset -4 zoom 1.04

transform about_group_link_hover:
    subpixel True
    xoffset 0
    yoffset 0
    alpha 0.94
    on idle:
        easeout 0.20 xoffset 0 yoffset 0 alpha 0.94
    on hover:
        easein 0.07 xoffset 2 yoffset 2 alpha 0.88
        easeout 0.13 xoffset 0 yoffset -7 alpha 1.0
        easein 0.11 yoffset -4


transform about_oscar_glow_idle:
    alpha 0.0

transform about_oscar_glow_active:
    alpha 0.0
    easein 0.18 alpha 0.82
    blur 9





init -2 python:
    class OscarAboutCard(renpy.Displayable):
        """A responsive layered card background used only by the About screen."""
        
        def __init__(self, variant="panel", **properties):
            super(OscarAboutCard, self).__init__(**properties)
            self.variant = variant
        
        def render(self, width, height, st, at):
            width = max(1, int(width))
            height = max(1, int(height))
            rv = renpy.Render(width, height)
            
            def layer(color, x, y, layer_width, layer_height):
                if layer_width <= 0 or layer_height <= 0:
                    return
                
                displayable = renpy.display.imagelike.Solid(color)
                rendered = renpy.render(displayable, layer_width, layer_height, st, at)
                rv.blit(rendered, (x, y))
            
            if self.variant == "feature":
                outer = "#00000078"
                steel = "#A4A6AACC"
                shadow = "#36383DCC"
            elif self.variant == "section":
                outer = "#00000070"
                steel = "#85888DCC"
                shadow = "#2B2D32CC"
            else:
                outer = "#00000066"
                steel = "#73767BCC"
                shadow = "#222429CC"
            
            border = 3
            inset = 7
            
            
            layer(outer, 0, 0, width, height)
            layer(steel, 0, 0, width, border)
            layer(steel, 0, height - border, width, border)
            layer(steel, 0, 0, border, height)
            layer(steel, width - border, 0, border, height)
            layer(shadow, inset, inset, width - (inset * 2), 2)
            layer(shadow, inset, height - inset - 2, width - (inset * 2), 2)
            layer(shadow, inset, inset, 2, height - (inset * 2))
            layer(shadow, width - inset - 2, inset, 2, height - (inset * 2))
            
            return rv


    renpy.register_textshader(
    "oscar_red_gradient",
    include_default=True,
    variables="""
    attribute vec2 a_tex_coord;
    varying vec2 v_oscar_gradient_coord;
    """,
    vertex_200="""
    v_oscar_gradient_coord = a_tex_coord;
    """,
    fragment_400="""
    vec3 l_oscar_top = vec3(0.94, 0.16, 0.16);
    vec3 l_oscar_bottom = vec3(0.16, 0.003, 0.008);
    vec3 l_oscar_color = mix(l_oscar_top, l_oscar_bottom, clamp(v_oscar_gradient_coord.y, 0.0, 1.0));
    gl_FragColor.rgb = l_oscar_color * gl_FragColor.a;
    """,
)









screen about():
    tag menu

    default about_oscar_card_hovered = False

    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            xpos 0
            xsize 2760
            spacing 18

            null height 20
            fixed:
                xpos 58
                xsize 2644
                ysize gui.label_text_size + 12
                text "{color=#FFFFFF}ОБ ИГРЕ{/color} {color=#9933FF}AFTER DARK{/color}" style "about_heading_text" xpos 0 yalign 0.5
                text _("Версия [config.version!t]") style "about_meta_text" xalign 1.0 yalign 0.5 text_align 1.0

            if gui.about:
                null height 12

                frame:
                    style "about_section_card"
                    xfill True
                    xpadding 58
                    ypadding 32

                    has vbox
                    xfill True
                    spacing 12

                    text _("Разработчик:") style "about_meta_text" xalign 0.5 xoffset -30 text_align 0.5
                    add "gui/dev_logo.webp" xalign 0.5
                    text _("Bozavest") style "about_body_text" xalign 0.5 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 20
                        frame:
                            style "about_link_card"
                            xsize 304
                            ysize 304
                            xpadding 30
                            ypadding 30
                            has button
                            background None
                            hover_background None
                            xfill True
                            yfill True
                            action OpenURL("https://www.patreon.com/bozavest")
                            at about_group_link_hover
                            fixed:
                                xfill True
                                yfill True
                                add Transform("gui/patreon_idle.png", zoom=0.8) xalign 0.5 yalign 0.5
                        frame:
                            style "about_link_card"
                            xsize 304
                            ysize 304
                            xpadding 30
                            ypadding 30
                            has button
                            background None
                            hover_background None
                            xfill True
                            yfill True
                            action OpenURL("https://bozavest.itch.io/after-dark")
                            at about_group_link_hover
                            fixed:
                                xfill True
                                yfill True
                                add Transform("gui/itch_idle.png", zoom=0.8) xalign 0.5 yalign 0.5

                frame:
                    style "about_section_card"
                    xfill True
                    xpadding 58
                    ypadding 32

                    has vbox
                    xfill True
                    spacing 14

                    text _("Отдельная благодарность:") style "about_meta_text" xalign 0.5 text_align 0.5
                    frame:
                        style "about_feature_card"
                        xsize 1305
                        ysize 304
                        xalign 0.5
                        xpadding 30
                        ypadding 24
                        has button
                        background None
                        hover_background None
                        xfill True
                        yfill True
                        action OpenURL("https://penrucci.itch.io/")
                        hovered SetScreenVariable("about_oscar_card_hovered", True)
                        unhovered SetScreenVariable("about_oscar_card_hovered", False)
                        at about_group_link_hover
                        fixed:
                            xfill True
                            yfill True
                            add Transform("gui/oscar.webp", zoom=0.342) xpos 0 yalign 0.5
                            hbox:
                                xpos 740
                                xanchor 0.5
                                ypos 31
                                spacing 14
                                fixed:
                                    fit_first True
                                    xoffset -5
                                    yoffset -8
                                    if about_oscar_card_hovered:
                                        text "oscar" style "about_oscar_glow_text" at about_oscar_glow_active
                                    else:
                                        text "oscar" style "about_oscar_glow_text" at about_oscar_glow_idle
                                    text "oscar" style "about_oscar_link_text"
                                text "(СОАВТОР)" style "about_oscar_codev_text"
                            text "Помогал исправлять баги и добавлять новые функции." style "about_card_note" xpos 755 xanchor 0.5 ypos 133 xsize 1100 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 34
                        frame:
                            style "about_link_card"
                            xsize 1305
                            ysize 304
                            xpadding 30
                            ypadding 24
                            has fixed
                            xfill True
                            yfill True
                            add "gui/bootykat.png" xpos 0 yalign 0.5
                            text " - " style "about_body_text" xpos 266 yalign 0.5
                            text "BootyKat (контроль качества)" style "about_card_text" xpos 340 yalign 0.5 text_align 0.0
                        frame:
                            style "about_link_card"
                            xsize 1305
                            ysize 304
                            xpadding 30
                            ypadding 24
                            has button
                            background None
                            hover_background None
                            xfill True
                            yfill True
                            action OpenURL("https://x.com/Gamingrecluse11")
                            at about_group_link_hover
                            fixed:
                                xfill True
                                yfill True
                                add "gui/recluse.png" xpos 0 yalign 0.5
                                text " - " style "about_body_text" xpos 266 yalign 0.5
                                text "Recluse {color=#FFFFFF}(художник){/color}" style "about_link_text" xpos 340 yalign 0.5 text_align 0.0

                frame:
                    style "about_section_card"
                    xfill True
                    xpadding 58
                    ypadding 32

                    has vbox
                    xfill True
                    spacing 16

                    text _("Аниматоры:") style "about_meta_text" xalign 0.5 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 34
                        frame:
                            style "about_link_card"
                            xsize 1305
                            ysize 304
                            xpadding 30
                            ypadding 24
                            has button
                            background None
                            hover_background None
                            xfill True
                            yfill True
                            action OpenURL("https://x.com/Tiaramix1527")
                            at about_group_link_hover
                            fixed:
                                xfill True
                                yfill True
                                add "gui/Tiaramix.png" xpos 0 yalign 0.5
                                text " - " style "about_body_text" xpos 266 yalign 0.5
                                text "Mix {color=#FFFFFF}(аниматор, анимации Джун){/color}" style "about_mix_link_text" xpos 340 yalign 0.5 text_align 0.0
                        frame:
                            style "about_link_card"
                            xsize 1305
                            ysize 304
                            xpadding 30
                            ypadding 24
                            has button
                            background None
                            hover_background None
                            xfill True
                            yfill True
                            action OpenURL("https://rebel-tomboy-games.itch.io/project-dreadsteel")
                            at about_group_link_hover
                            fixed:
                                xfill True
                                yfill True
                                add "gui/TheLolingPain.png" xpos 0 yalign 0.5
                                text " - " style "about_body_text" xpos 266 yalign 0.5
                                text "TheLolingPain\n{color=#FFFFFF}(аниматор, bj-анимации Изры и Ютами){/color}" style "about_loling_link_text" xpos 340 yalign 0.5 xsize 900

                frame:
                    style "about_section_card"
                    xfill True
                    xpadding 58
                    ypadding 32

                    has vbox
                    xfill True
                    spacing 16

                    text _("Автор перевода:") style "about_meta_text" xalign 0.5 text_align 0.5
                    textbutton "vodichkafiji":
                        style "about_link"
                        xalign 0.5
                        action OpenURL("https://github.com/vodichkafiji/AfterDark-Rus")
                        at about_link_hover

            null height 16
            text _("ДВИЖОК И ЛИЦЕНЗИЯ") style "about_meta_text" xalign 0.5 text_align 0.5
            hbox:
                xalign 0.5
                spacing 10
                text _("Сделано на ") style "about_body_text"
                textbutton "Ren'Py":
                    style "about_link"
                    xoffset -10
                    action OpenURL("https://www.renpy.org/")
                    at about_link_hover
                text "[renpy.version_only]." style "about_body_text"
            vbox:
                xalign 0.5
                xsize 1800
                spacing 0
                text _("Эта программа содержит свободное программное обеспечение под рядом лицензий, включая MIT License и GNU Lesser General Public License. Полный список программ, включая ссылки на исходный код,") style "about_legal_text" xfill True xalign 0.5 text_align 0.5
                hbox:
                    xalign 0.5
                    spacing 0
                    text _("можно найти ") style "about_legal_text"
                    textbutton "здесь":
                        style "about_inline_link"
                        action OpenURL("https://www.renpy.org/l/license")
                        at about_link_hover
                    text "." style "about_legal_text"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_section_card is frame:
    background OscarAboutCard("section")

style about_link_card is frame:
    background OscarAboutCard("link")

style about_feature_card is frame:
    background OscarAboutCard("feature")

style about_label_text:
    size gui.label_text_size

style about_meta_text is about_text:
    size gui.text_size - 18

style about_heading_text is about_label_text:
    size gui.label_text_size

style about_body_text is about_text:
    size gui.text_size - 10

style about_card_text is about_link_text:
    size gui.text_size - 20
    color "#FFFFFF"

style about_card_note is about_body_text:
    font "oscar assets/fonts/oscar_MetalMania.ttf"
    size gui.text_size - 15
    color "#FFFFFF"

style about_legal_text is about_text:
    size gui.text_size - 26

style about_link is button:
    background None
    hover_background None
    xpadding 0
    ypadding 0

style about_link_text is hyperlink_text:
    font "oscar assets/fonts/oscar_MetalMania.ttf"
    size gui.text_size - 5
    hover_color gui.hover_color
    hover_underline False

style about_oscar_link_text is about_link_text:
    size gui.text_size + 10
    textshader "oscar_red_gradient"
    color "#FFFFFFFF"

style about_oscar_glow_text is about_oscar_link_text:
    color "#3A0008D8"
    hover_color "#3A0008D8"

style about_oscar_codev_text is about_link_text:
    size gui.text_size + 5
    color "#FFFFFFFF"
    hover_color "#FFFFFFFF"

style about_inline_link_text is about_link_text:
    size gui.text_size - 26

style about_inline_link is about_link

style about_long_link is about_link

style about_long_link_text is about_link_text:
    size gui.text_size - 33

style about_mix_link is about_link

style about_mix_link_text is about_link_text:
    size gui.text_size - 15

style about_loling_link is about_link

style about_loling_link_text is about_link_text:
    size gui.text_size - 23
    text_align 0.5











screen save():
    tag menu


    use file_slots(_("Сохранить"))


screen load():
    tag menu


    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"

                        if FileNewest(slot):
                            if FileSaveName(slot):
                                text FileSaveName(slot)+"\n"+_("{b}Последнее сохранение{/b}"):
                                    style "slot_name_text"
                            else:
                                text _("{b}Последнее сохранение{/b}"):
                                    style "slot_name_text"
                        else:
                            text FileSaveName(slot):
                                style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    if persistent._file_page == "auto":
                        textbutton _("{b}{#auto_page}A{/b}") action FilePage("auto")
                    else:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    if persistent._file_page == "quick":
                        textbutton _("{b}{#quick_page}Q{/b}") action FilePage("quick")
                    else:
                        textbutton _("{#quick_page}Q") action FilePage("quick")


                if persistent._file_page.isdigit():
                    for page in range(1, 10):
                        if int(persistent._file_page) == page:
                            textbutton "{b}[page]{/b}" action FilePage(page)
                        else:
                            textbutton "[page]" action FilePage(page)
                else:
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 150
    ypadding 9

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            xsize 2680
            xalign 0.5
            spacing 18

            hbox:
                xalign 0.5
                spacing 30

# недоступно в русификаторе (смена шрифта ломает кириллицу)
#                vbox:
#                    xsize 1050
#                    spacing 0
#
#                    label _("Шрифт")
#                    for fnt in size_dict.keys():
#                        $ disp = fnt.rsplit(".", 1)[0].replace("_", " ").replace("-", " ")
#                        textbutton "{font=%s}%s" % (fnt, disp):
#                            style "settings_font_button"
#                            action [ changeFont(fnt) ]
#                            selected (persistent.pref_text_font == fnt)
#                            at settings_preferences_hover

                vbox:
                    xsize 1550
                    spacing 0

                    hbox:
                        style_prefix "settings_radio"
                        spacing 18
                        yalign 0.5
                        if renpy.variant("pc") or renpy.variant("web"):
                            label _("Экран")
                            textbutton _("Окно") action Preference("display", "window") at settings_preferences_hover
                            text "|" style "settings_toggle_separator"
                            textbutton _("Полный экран") action Preference("display", "fullscreen") at settings_preferences_hover

                    if renpy.variant("pc"):
                        hbox:
                            style_prefix "settings_radio"
                            spacing 18
                            yalign 0.5
                            label _("Быстрое меню")
                            textbutton _("Включить") action SetVariable("quick_menu", True) at settings_preferences_hover
                            text "|" style "settings_toggle_separator"
                            textbutton _("Выключить") action SetVariable("quick_menu", False) at settings_preferences_hover

                    hbox:
                        style_prefix "settings_check"
                        spacing 18
                        yalign 0.5
                        label _("Пропуск")
                        textbutton _("Непрочитанный\nтекст") action Preference("skip", "toggle") at settings_preferences_hover
                        text "|" style "settings_toggle_separator"
                        textbutton _("После\nвыборов") action Preference("after choices", "toggle") at settings_preferences_hover
                        text "|" style "settings_toggle_separator"
                        textbutton _("Переходы") action InvertSelected(Preference("transitions", "toggle")) at settings_preferences_hover

                    hbox:
                        style_prefix "settings_radio"
                        spacing 18
                        yalign 0.5
                        label _("Размер текста")
                        textbutton "Обычный":
                            action [ changeScale("regular") ]
                            selected (persistent.pref_text_scale == "regular")
                            at settings_preferences_hover
                        text "|" style "settings_toggle_separator"
                        textbutton "Крупный":
                            action [ changeScale("large") ]
                            selected (persistent.pref_text_scale == "large")
                            at settings_preferences_hover




                    hbox:
                        style_prefix "settings_check"
                        spacing 18
                        yalign 0.5
                        label _("Discord")
                        $ ad_discord_rpc_status = "ВКЛ" if persistent.ad_discord_rpc_enabled else "ВЫКЛ"
                        textbutton _("Статус в Discord: [ad_discord_rpc_status]"):
                            action Function(ad_discord_rpc_set_enabled, not persistent.ad_discord_rpc_enabled)
                            selected persistent.ad_discord_rpc_enabled
                            at settings_preferences_hover

            hbox:
                style_prefix "slider"
                xalign 0.0
                spacing 80

                vbox:
                    xsize 1300
                    spacing 0
                    label _("Прозрачность окна текста")
                    bar:
                        style "slider_slider"
                        value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.05)
                    label _("Скорость текста")
                    bar value Preference("text speed")
                    label _("Время автопрокрутки")
                    bar value Preference("auto-forward time")

                vbox:
                    xsize 1300
                    spacing 0
                    if config.has_music:
                        label _("Громкость музыки")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Громкость звуков")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound) at settings_preferences_hover
                    if config.has_voice:
                        label _("Громкость озвучки")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice) at settings_preferences_hover
                    if config.has_music or config.has_sound or config.has_voice:
                        null height (gui.pref_spacing - 20)
                        textbutton _("Выключить звук"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            xoffset -450
                            at settings_preferences_hover


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin (gui.pref_spacing - 10)
    bottom_margin 6

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 675

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")





style settings_radio_label is radio_label
style settings_radio_label_text is radio_label_text
style settings_radio_button is radio_button:
    foreground None
    left_padding 0
style settings_radio_button_text is radio_button_text:
    selected_idle_color "#D3A5FF"
    selected_hover_color "#E8D1FF"

style settings_check_label is check_label
style settings_check_label_text is check_label_text
style settings_check_button is check_button:
    foreground None
    left_padding 0
style settings_check_button_text is check_button_text:
    selected_idle_color "#D3A5FF"
    selected_hover_color "#E8D1FF"

style settings_font_button is button
style settings_font_button_text is button_text:
    hover_color gui.hover_color
    selected_hover_color gui.hover_color

style settings_toggle_separator is gui_text:
    color "#F0DFFF"
    size 68
    outlines [(2, "#3C2157", 0, 0)]
    yalign 0.5

style slider_slider:
    xsize 1050

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 30

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 1350





transform settings_preferences_hover:
    subpixel True
    on idle:
        easeout 0.14 xoffset 0 alpha 0.92
    on hover:
        easein 0.12 xoffset 7 alpha 1.0









screen biocharahub():
    tag menu

    use game_menu(_("Персонажи"), scroll="viewport"):

        style_prefix "aff"

        grid 2 1:

            spacing 20

            imagebutton:
                idle "maincharaview1.png"
                hover "maincharaview2.png"

                focus_mask True
                action ShowMenu('bio')
            imagebutton:
                idle "sidecharaview1.png"
                hover "sidecharaview2.png"

                focus_mask True
                action ShowMenu('sidebio')


screen history():
    tag menu



    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 45

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Продвигает диалог и активирует интерфейс.")

    hbox:
        label _("Пробел")
        text _("Продвигает диалог, не позволяя выбирать варианты.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Escape")
        text _("Открывает игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалог, пока зажата.")

    hbox:
        label _("Tab")
        text _("Включает/выключает пропуск диалога.")

    hbox:
        label _("Page Up")
        text _("Откатывает к предыдущему диалогу.")

    hbox:
        label _("Page Down")
        text _("Прокручивает вперёд к следующему диалогу.")

    hbox:
        label "H"
        text _("Скрывает интерфейс.")

    hbox:
        label "S"
        text _("Делает скриншот.")

    hbox:
        label "V"
        text _("Включает/выключает {a=https://www.renpy.org/l/voicing}озвучку текста{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


screen mouse_help():

    hbox:
        label _("ЛКМ")
        text _("Продвигает диалог и активирует интерфейс.")

    hbox:
        label _("СКМ")
        text _("Скрывает интерфейс.")

    hbox:
        label _("ПКМ")
        text _("Открывает игровое меню.")

    hbox:
        label _("Колесо мыши вверх\nКлик по стороне отката")
        text _("Откатывает к предыдущему диалогу.")

    hbox:
        label _("Колесо мыши вниз")
        text _("Прокручивает вперёд к следующему диалогу.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Продвигает диалог и активирует интерфейс.")

    hbox:
        label _("Левый триггер\nЛевый бампер")
        text _("Откатывает к предыдущему диалогу.")

    hbox:
        label _("Правый бампер")
        text _("Прокручивает вперёд к следующему диалогу.")


    hbox:
        label _("Крестовина, стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Start, Guide")
        text _("Открывает игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 24

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 750
    right_padding 60

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 90

        label _(message):
            style "confirm_prompt"
            xalign 0.5
            text_size 130

        hbox:
            xalign 0.5
            spacing 300

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action



    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 18

        text _("Пропуск")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 1350



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:


            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 1020

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 1200

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 1800


transform left_zara:
    xpos 0.4
    ypos 1.0
    xanchor 0.5
    yanchor 1.0

transform left_mc:
    xpos 0.2
    ypos 1.0
    xanchor 0.5
    yanchor 1.0

transform right_nora:
    xpos 0.8
    ypos 1.0
    xanchor 0.5
    yanchor 1.0















screen event_replay(g):
    tag menu


    if renpy.loadable("game_menu.png"):
        add "game_menu.png"
    else:
        add "quest"


    if renpy.has_image(g.image):
        add g.image:
            align (1.0, 1.0)
            zoom 0.95


    text "ВОСПОМИНАНИЯ: [g.name]":
        pos (120, 120)
        font "NotoSansDisplay-ExtraBold.ttf"
        size 120
        color "#ffffff"
        outlines [(16, "#000", 1, 1)]


    side "c r":
        pos (50, 240)
        xysize (1600, 1780)

        viewport id "event_vp":
            mousewheel True
            draggable True
            xfill True
            yfill True

            has vbox
            spacing 30
            xfill True

            $ events = getattr(g, 'completed_events', [])

            if not events:
                text "Пока нет общих воспоминаний..." size 50 color "#999999" italic True xpos 100
            else:
                for event_name, event_label in events:
                    textbutton "[event_name]":
                        action Replay(event_label, scope={"mcname": mcname})

                        xmaximum None
                        ymaximum None


                        xsize 10000
                        ysize 200

                        background Solid("#111111CC")
                        hover_background Solid("#7a7a7a")

                        text_idle_color "#FFFFFF"
                        text_hover_color "#FFFFFF"
                        text_size 90
                        text_font "NotoSansDisplay-ExtraBold.ttf"

                        text_xalign -0.1
                        text_xpos 60
                        text_yalign 0.5
                        text_outlines [(16, "#000", 1, 1)]


        vbar value YScrollValue("event_vp"):
            xsize 40
            ysize 2000
            base_bar Solid("#FFFFFF11")
            thumb Solid("#ffffff")
            unscrollable "hide"


    textbutton "НАЗАД":
        action Show("character_page", g=g)
        align (0.98, 0.95)
        text_size 150
        text_font "NotoSansDisplay-ExtraBold.ttf"
        text_hover_color "#797979"
        text_outlines [(16, "#000", 1, 1)]