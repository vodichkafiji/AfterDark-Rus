






define oscar_replay_events = (
    ("Первый бой", "first_fight", ad_replay_first_fight, "firstfight"),
    ("Первый сон", "thefirstdream", ad_replay_first_dream, "firstdream"),
    ("Разговор о Ярких", "brighttalk", ad_replay_bright_talk, "pillowtrain"),
    ("Расследование на складе", "warehouse_investigation", ad_replay_warehouse_investigation, "chromarkwarehouse"),
)




init python:
    def oscar_replay_is_unlocked(progress_variable):
        return getattr(store, progress_variable, 0) >= 1

screen oscar_replay_test_button():
    textbutton "Повторить события":
        style "oscar_replay_button"
        xpos 70
        yalign 1.0
        yoffset -80
        xsize 590
        action ShowMenu("oscar_replay_gallery")

screen oscar_replay_gallery():
    tag menu
    default oscar_page = 0
    $ oscar_page_count = max(1, (len(oscar_replay_events) + 5) // 6)
    add "#0B0B10"
    add Transform(ad_ui_background, xysize=(config.screen_width, config.screen_height))
    add "#08080BB8"

    key "game_menu" action ShowMenu("main_menu")
    key "K_LEFT" action SetScreenVariable("oscar_page", max(0, oscar_page - 1))
    key "K_RIGHT" action SetScreenVariable("oscar_page", min(oscar_page_count - 1, oscar_page + 1))

    vbox:
        align (0.5, 0.5)
        spacing 65
        text "ПОВТОР СОБЫТИЙ":
            xalign 0.5
            font "oscar assets/fonts/oscar_CinzelDecorative.ttf"
            size 100
            color "#F3E9E9"
        grid 3 2:
            spacing 40
            for oscar_slot in range(6):
                $ oscar_index = oscar_page * 6 + oscar_slot
                if oscar_index < len(oscar_replay_events):
                    $ oscar_title, oscar_label, oscar_image, oscar_progress = oscar_replay_events[oscar_index]
                    if oscar_replay_is_unlocked(oscar_progress):
                        button:
                            style "oscar_replay_card"
                            action Replay(oscar_label, scope={"mcname": getattr(store, "mcname", None) or "Miles"}, locked=False)
                            alt oscar_title
                            add Transform(oscar_image, xysize=(860, 440))
                    else:
                        button:
                            style "oscar_replay_card"
                            sensitive False
                            add Transform(oscar_image, xysize=(860, 440))
                            add Transform(ad_replay_locked, xysize=(860, 440))
                else:
                    frame:
                        xysize (860, 440)
                        background "#141219BB"
                        text "СКОРО" align (0.5, 0.5) font "oscar assets/fonts/oscar_CinzelDecorative.ttf" size 34 color "#796B74"

        hbox:
            xalign 0.5
            spacing 14
            textbutton "‹":
                style "oscar_replay_nav_arrow"
                sensitive oscar_page > 0
                action SetScreenVariable("oscar_page", oscar_page - 1)
            for oscar_page_number in range(oscar_page_count):
                textbutton str(oscar_page_number + 1):
                    style "oscar_replay_nav_page"
                    selected oscar_page == oscar_page_number
                    action SetScreenVariable("oscar_page", oscar_page_number)
            textbutton "›":
                style "oscar_replay_nav_arrow"
                sensitive oscar_page < oscar_page_count - 1
                action SetScreenVariable("oscar_page", oscar_page + 1)

        textbutton "НАЗАД":
            style "oscar_replay_nav_back"
            xalign 0.5
            action ShowMenu("main_quest")

style oscar_replay_button is button:
    background "#281C27"
    hover_background "#683346"
    selected_background "#683346"
    insensitive_background "#17131B"
    padding (40, 24)

style oscar_replay_button_text is button_text:
    font "oscar assets/fonts/oscar_CinzelDecorative.ttf"
    size 40
    color "#F3E9E9"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    insensitive_color "#665C65"
    xalign 0.5

style oscar_replay_nav_arrow is button:
    xsize 82
    ysize 76
    background "#17141B"
    hover_background "#4E2638"
    insensitive_background "#101015"
    padding (0, 0)

style oscar_replay_nav_arrow_text is button_text:
    font "oscar assets/fonts/oscar_CinzelDecorative.ttf"
    size 58
    color "#D4C8CD"
    hover_color "#FFFFFF"
    insensitive_color "#4C464C"
    xalign 0.5
    yalign 0.5

style oscar_replay_nav_page is button:
    xsize 92
    ysize 76
    background "#251923"
    hover_background "#60314A"
    selected_background "#84506A"
    padding (0, 0)

style oscar_replay_nav_page_text is button_text:
    font "oscar assets/fonts/oscar_CinzelDecorative.ttf"
    size 34
    color "#D4C8CD"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style oscar_replay_nav_back is button:
    xsize 300
    ysize 72
    background "#17141B"
    hover_background "#4E2638"
    padding (0, 0)

style oscar_replay_nav_back_text is button_text:
    font "oscar assets/fonts/oscar_CinzelDecorative.ttf"
    size 32
    color "#D4C8CD"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5




style oscar_replay_card is button:
    xysize (860, 440)
    background "#281C27EE"
    hover_background "#683346EE"
    padding (0, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
