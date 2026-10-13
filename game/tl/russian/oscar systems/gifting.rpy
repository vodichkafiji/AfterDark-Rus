
default ad_gift_target = "Yuki"
default ad_gift_message = ""
default ad_gift_is_error = False
default ad_gift_show_result = False
default ad_gift_history = {}
default ad_gift_quantity = "1"
default ad_gift_notification_text = ""
default ad_gift_notification_item_id = None
default ad_gift_notification_x = 0
default ad_gift_notification_y = 0

init python:

    ad_gift_targets = [
    "Yuki", "Izra", "June", "Mei", "Autumn", "Nora", "Lily", "Jordyn",
    "Kyra", "Parker", "Riley", "Brooklyn", "Tamara", "Utami", "Yejin", "Zara", "Grace",
]

    def ad_localized_character_name(name):
        return {
            "Yuki": "Юки",
            "Izra": "Изра",
            "June": "Джун",
            "Mei": "Мэй",
            "Autumn": "Отэм",
            "Nora": "Нора",
            "Lily": "Лили",
            "Jordyn": "Джордин",
            "Kyra": "Кира",
            "Parker": "Паркер",
            "Riley": "Райли",
            "Brooklyn": "Бруклин",
            "Tamara": "Тамара",
            "Utami": "Ютами",
            "Yejin": "Еджин",
            "Zara": "Зара",
            "Grace": "Грейс",
        }.get(name, name)

    def ad_gift_quantity_value():
        try:
            return max(1, int(store.ad_gift_quantity))
        except (TypeError, ValueError):
            return 1

    def ad_gift_change_quantity(change):
        store.ad_gift_quantity = str(max(1, ad_gift_quantity_value() + change))
        renpy.restart_interaction()

    def ad_toggle_gift_selection(item_id):
        if store.ad_selected_inventory_item == item_id:
            store.ad_selected_inventory_item = None
        else:
            store.ad_selected_inventory_item = item_id
        store.ad_gift_quantity = "1"
        renpy.restart_interaction()

    def ad_give_gift(amount=1):
        item_id = store.ad_selected_inventory_item
        target = store.ad_gift_target
        if item_id not in store.ad_items:
            store.ad_gift_message = "ВЫБЕРИТЕ ПРЕДМЕТ ДЛЯ ПОДАРКА."
            store.ad_gift_is_error = True
            store.ad_gift_show_result = False
            renpy.restart_interaction()
            return
        if amount < 1 or ad_item_amount(item_id) < amount:
            store.ad_gift_message = "Недостаточно {} для подарка.".format(store.ad_items[item_id]["name"])
            store.ad_gift_is_error = True
            store.ad_gift_show_result = False
            renpy.restart_interaction()
            return
        ad_remove_item(item_id, amount)
        store.ad_gift_history[target] = store.ad_gift_history.get(target, 0) + amount
        character = getattr(store, target, None)
        if character is not None and hasattr(character, "affection"):
            character.affection += amount
        store.ad_gift_message = "{} получила {} x{}.".format(ad_localized_character_name(target), store.ad_items[item_id]["name"], amount)
        store.ad_gift_is_error = False
        store.ad_gift_show_result = True
        mouse_x, mouse_y = renpy.get_mouse_pos()
        store.ad_gift_notification_x = mouse_x + 72
        store.ad_gift_notification_y = mouse_y - 82
        store.ad_gift_notification_text = "ПОДАРЕНО: {} x{} ДЛЯ {}".format(store.ad_items[item_id]["name"].upper(), amount, ad_localized_character_name(target).upper())
        store.ad_gift_notification_item_id = item_id
        if ad_item_amount(item_id) <= 0:
            store.ad_selected_inventory_item = None
        store.ad_gift_quantity = "1"
        renpy.play("audio/Sound/affection.mp3", channel="sound")
        renpy.show_screen("ad_gift_notification_screen")
        renpy.restart_interaction()
        return

    def ad_update_gift_notification_position():
        mouse_x, mouse_y = renpy.get_mouse_pos()
        store.ad_gift_notification_x = mouse_x + 72
        store.ad_gift_notification_y = mouse_y - 82


screen ad_gifting_screen():

    modal True
    zorder 200
    default ad_hovered_gift_item = None

    add ad_ui_background:
        xsize config.screen_width
        ysize config.screen_height

    add Solid("#03030762")


    add ad_ui_barbed_horizontal:
        xalign 0.5
        yalign 0.035
        xsize config.screen_width
        ysize 130


    add Transform(ad_ui_barbed_horizontal, rotate=180):
        xalign 0.5
        yalign 0.965
        xsize config.screen_width
        ysize 130

    frame:
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
        background "#05050A7C"
        padding (130, 105)
        at ad_gothic_screen_open

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 55

            frame:
                xsize 2050
                yfill True
                background "#090A1078"
                padding (52, 45)

                has vbox
                xalign 0.5
                spacing 18

                text "ВЫБЕРИТЕ ПОДАРОК":
                    xalign 0.5
                    text_align 0.5
                    size 64
                    color "#F3F3F3"
                    outlines [(2, "#000000", 1, 1)]
                    font ad_gothic_heading_font

                grid 3 1:
                    xalign 0.5
                    spacing 26

                    for item_id in ad_item_order:
                        $ item = ad_items[item_id]
                        button:
                            xsize 610
                            ysize 510
                            sensitive ad_item_amount(item_id) > 0
                            background "#1B1B25"
                            hover_background "#1B1B25"
                            selected_background "#751522"
                            action SetVariable("ad_selected_inventory_item", item_id)
                            hovered SetScreenVariable("ad_hovered_gift_item", item_id)
                            unhovered SetScreenVariable("ad_hovered_gift_item", None)

                            if ad_hovered_gift_item == item_id:
                                add Solid("#B8B8C2"):
                                    xalign 0.5
                                    yalign 0.4
                                    xsize 275
                                    ysize 275
                                add Solid("#15151C"):
                                    xalign 0.5
                                    yalign 0.4
                                    xsize 265
                                    ysize 265

                            add item["icon"]:
                                xalign 0.5
                                yalign 0.4
                                xsize 250
                                ysize 250
                                at (ad_item_hover if ad_hovered_gift_item == item_id else ad_item_idle)

                            text item["name"]:
                                xalign 0.5
                                yalign 0.72
                                text_align 0.5
                                size 34
                                color ("#FFFFFF" if ad_hovered_gift_item == item_id else "#F0F0F0")
                                outlines ([(2, "#B8B8C2", 0, 0)] if ad_hovered_gift_item == item_id else [(1, "#000000", 1, 1)])
                                font ad_gothic_body_font

                            text "x[ad_item_amount(item_id)]":
                                xalign 0.5
                                yalign 0.88
                                text_align 0.5
                                size 32
                                color "#CFCFCF"
                                font ad_gothic_body_font

                if ad_selected_inventory_item in ad_items:
                    text "Выбрано: [ad_items[ad_selected_inventory_item]['name']]":
                        xalign 0.5
                        text_align 0.5
                        size 34
                        color "#DADADA"
                        font ad_gothic_body_font
                else:
                    text "Выберите предмет в инвентаре.":
                        xalign 0.5
                        text_align 0.5
                        size 34
                        color "#A7A7A7"
                        font ad_gothic_body_font

            frame:
                xfill True
                yfill True
                background "#0C0C146E"
                padding (60, 58)

                has vbox
                xalign 0.5
                spacing 12

                text "КОМУ ПОДАРИТЬ":
                    xalign 0.5
                    text_align 0.5
                    size 52
                    color "#F2F2F2"
                    outlines [(2, "#000000", 1, 1)]
                    font ad_gothic_heading_font

                viewport:
                    xsize 900
                    ysize 720
                    mousewheel True
                    scrollbars "vertical"
                    has vbox
                    xalign 0.5
                    spacing 7
                    for target in ad_gift_targets:
                        textbutton ad_localized_character_name(target):
                            xsize 820
                            background ("#751522" if ad_gift_target == target else "#25252D")
                            hover_background "#4A101A"
                            padding (26, 15)
                            action SetVariable("ad_gift_target", target)
                            text_xalign 0.5
                            text_color "#F2F2F2"
                            text_hover_color "#FFFFFF"
                            text_size 34
                            text_font ad_gothic_body_font

                textbutton "ПОДАРИТЬ":
                    xalign 0.5
                    background "#5B111C"
                    hover_background "#9A1D2D"
                    padding (42, 22)
                    action Function(ad_give_gift)
                    text_color "#F2F2F2"
                    text_size 34
                    text_font ad_gothic_body_font

                if ad_gift_message:
                    text ad_gift_message:
                        xalign 0.5
                        xmaximum 820
                        text_align 0.5
                        size 30
                        color "#D4D4D4"
                        outlines [(1, "#000000", 1, 1)]
                        font ad_gothic_body_font

        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -22
            yoffset 12
            idle Transform(ad_ui_close, size=(112, 112), alpha=0.82)
            hover Transform(ad_ui_close, size=(130, 130), alpha=1.0)
            action [SetVariable("ad_gift_message", ""), Hide("ad_gifting_screen")]

        text "ЗАКРЫТЬ":
            xalign 1.0
            yalign 0.0
            xoffset -38
            yoffset 118
            size 24
            color "#D8D8D8"
            outlines [(2, "#200408", 1, 1)]
            font ad_gothic_body_font
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
