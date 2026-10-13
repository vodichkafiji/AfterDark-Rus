
default ad_selected_store_item = None
default ad_store_message = ""
default ad_store_show_result = False
default ad_store_quantity = "1"

init python:

    ad_general_store_items = ["flowers", "plush_toy", "chocolates"]
    ad_general_store_prices = {"flowers": 3, "plush_toy": 5, "chocolates": 2}

    def ad_store_quantity_value():
        try:
            return max(1, int(store.ad_store_quantity))
        except (TypeError, ValueError):
            return 1

    def ad_store_change_quantity(change):
        store.ad_store_quantity = str(max(1, ad_store_quantity_value() + change))
        renpy.restart_interaction()

    def ad_buy_from_store(item_id, price_table, amount=1):
        if item_id not in store.ad_items or item_id not in price_table or amount < 1:
            return
        price = price_table[item_id] * amount
        if not ad_spend_money(price):
            store.ad_store_message = "Недостаточно денег."
            store.ad_store_show_result = True
            renpy.hide_screen("ad_store_purchase_result_screen")
            renpy.show_screen("ad_store_purchase_result_screen")
            renpy.restart_interaction()
            return
        ad_add_item(item_id, amount)
        store.ad_store_message = "Куплено: {}.".format(store.ad_items[item_id]["name"])
        store.ad_store_show_result = True
        mouse_x, mouse_y = renpy.get_mouse_pos()
        store.ad_gift_notification_x = mouse_x + 72
        store.ad_gift_notification_y = mouse_y - 82
        store.ad_gift_notification_text = "КУПЛЕНО: {} x{}".format(store.ad_items[item_id]["name"].upper(), amount)
        store.ad_gift_notification_item_id = item_id
        renpy.show_screen("ad_gift_notification_screen")
        renpy.hide_screen("ad_store_purchase_result_screen")
        renpy.show_screen("ad_store_purchase_result_screen")
        renpy.restart_interaction()
        return






transform ad_store_buy_idle:
    alpha 0.90
    zoom 1.0
    yoffset 0

transform ad_store_buy_hover:
    alpha 0.0
    zoom 0.94
    yoffset 5
    parallel:
        easeout 0.16 alpha 1.0
    parallel:
        easeout 0.16 zoom 1.075
    parallel:
        easeout 0.16 yoffset -5

screen ad_store_purchase_result_screen():
    zorder 250
    timer 2.0 action Hide("ad_store_purchase_result_screen")
    text ad_store_message:
        xcenter int(config.screen_width * 0.7725)
        ypos int(config.screen_height * 0.8822) + 10
        yanchor 0.955
        text_align 0.5
        size int(config.screen_height * 0.019)
        color "#E6E6E6"
        outlines [(1, "#000000", 0, 0)]
        font ad_gothic_body_font
        at ad_gift_notification_pop


screen ad_store_layout(store_title, store_items, store_prices):





    modal True
    zorder 200
    default ad_store_quantity_input = VariableInputValue("ad_store_quantity", default=False)
    $ ad_store_panel_height = int(config.screen_height * 0.84)
    $ ad_store_left_width = int(config.screen_width * 0.52)
    $ ad_store_right_width = int(config.screen_width * 0.36)
    $ ad_store_gap = int(config.screen_width * 0.025)
    $ ad_store_grid_width = int(ad_store_left_width * 0.88)


    $ ad_store_grid_height = int(ad_store_panel_height * 0.66)
    $ ad_store_grid_gap = max(4, int(config.screen_height * 0.008))
    $ ad_store_horizontal_gap = ad_store_grid_gap + 75
    $ ad_store_slot_size = int(min((ad_store_grid_width - 48 - (ad_store_horizontal_gap * 3)) / 4, (ad_store_grid_height - 48 - (ad_store_grid_gap * 3)) / 4))
    $ ad_store_slot_border = max(8, int(ad_store_slot_size * 0.12))

    add Solid("#0101034D")

    fixed:
        xalign 0.5
        yalign 0.5
        xsize config.screen_width
        ysize config.screen_height
        at ad_gothic_screen_open

        add ad_ui_background:
            xsize config.screen_width
            ysize config.screen_height
            alpha 0.66
        add Solid("#05050A82"):
            xsize config.screen_width
            ysize config.screen_height
        use ad_barbed_border(config.screen_width, config.screen_height, 64, 74)


        button:
            xsize config.screen_width
            ysize config.screen_height
            background None
            focus_mask None
            action ad_store_quantity_input.Disable()

        hbox:
            xalign 0.5
            yalign 0.5
            spacing ad_store_gap


            fixed:
                xsize ad_store_left_width
                ysize ad_store_panel_height
                add Solid("#090A108C"):
                    xpos 26
                    ypos 26
                    xsize ad_store_left_width - 52
                    ysize ad_store_panel_height - 52
                use ad_barbed_border(ad_store_left_width, ad_store_panel_height, int(config.screen_height * 0.035), int(config.screen_height * 0.045))

                text store_title:
                    xalign 0.5
                    ypos int(ad_store_panel_height * 0.045)
                    text_align 0.5
                    size int(config.screen_height * 0.052)
                    color "#F0F0F2"
                    outlines [(2, "#24070B", 1, 1), (1, "#000000", 0, 0)]
                    font ad_inventory_title_font
                text "КУПИТЬ ПРЕДМЕТЫ":
                    xalign 0.5
                    ypos int(ad_store_panel_height * 0.115)
                    text_align 0.5
                    size int(config.screen_height * 0.024)
                    color "#BDBDC7"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_gothic_body_font

                fixed:
                    xalign 0.5
                    ypos int(ad_store_panel_height * 0.17)
                    xsize int(ad_store_left_width * 0.52)
                    ysize int(ad_store_panel_height * 0.11)
                    add Solid("#101017A8"):
                        xpos 8
                        ypos 6
                        xsize int(ad_store_left_width * 0.52) - 16
                        ysize int(ad_store_panel_height * 0.11) - 12
                    use ad_barbed_border(int(ad_store_left_width * 0.52), int(ad_store_panel_height * 0.11), int(config.screen_height * 0.022), int(config.screen_height * 0.030))
                    text "ДЕНЬГИ  [ad_format_money(ad_money)]":
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        size int(config.screen_height * 0.034)
                        color "#D4D4DB"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_inventory_money_font


                fixed:
                    xalign 0.5
                    ypos int(ad_store_panel_height * 0.30)
                    xsize ad_store_grid_width
                    ysize ad_store_grid_height
                    add Solid("#08080E9B"):
                        xpos 12
                        ypos 12
                        xsize ad_store_grid_width - 24
                        ysize ad_store_grid_height - 24
                    use ad_barbed_border(ad_store_grid_width, ad_store_grid_height, int(config.screen_height * 0.025), int(config.screen_height * 0.034))

                    grid 4 4:
                        xalign 0.5
                        yalign 0.5
                        xspacing ad_store_horizontal_gap
                        yspacing ad_store_grid_gap
                        for item_id in store_items:
                            $ item = ad_items[item_id]


                            button:
                                xsize ad_store_slot_size
                                ysize ad_store_slot_size
                                background None
                                hover_background None
                                selected_background None
                                focus_mask None
                                selected False
                                action [SetVariable("ad_selected_store_item", item_id), SetVariable("ad_store_quantity", "1"), ad_store_quantity_input.Disable()]
                                add Solid("#0909109B" if ad_selected_store_item == item_id else "#0D0D157C"):
                                    xpos ad_store_slot_border
                                    ypos ad_store_slot_border
                                    xsize ad_store_slot_size - (ad_store_slot_border * 2)
                                    ysize ad_store_slot_size - (ad_store_slot_border * 2)
                                use ad_barbed_border(ad_store_slot_size, ad_store_slot_size, ad_store_slot_border, int(ad_store_slot_size * 0.14))
                                add item["icon"]:
                                    xcenter int(ad_store_slot_size * 0.5) + (-5 if item_id == "plush_toy" else 5)
                                    yalign 0.40
                                    yoffset 10
                                    xsize int(ad_store_slot_size * 0.63)
                                    ysize int(ad_store_slot_size * 0.63)
                                    at ad_item_hover
                                text "[ad_format_money(store_prices[item_id])]":
                                    xalign 0.5
                                    yalign 0.84
                                    xoffset 5
                                    text_align 0.5
                                    size int(config.screen_height * 0.020)
                                    color "#D4D4DB"
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font
                        for empty_slot in range(16 - len(store_items)):
                            button:
                                xsize ad_store_slot_size
                                ysize ad_store_slot_size
                                background None
                                hover_background None
                                selected_background None
                                sensitive False
                                add Solid("#0D0D157C"):
                                    xpos ad_store_slot_border
                                    ypos ad_store_slot_border
                                    xsize ad_store_slot_size - (ad_store_slot_border * 2)
                                    ysize ad_store_slot_size - (ad_store_slot_border * 2)
                                use ad_barbed_border(ad_store_slot_size, ad_store_slot_size, ad_store_slot_border, int(ad_store_slot_size * 0.14))
                                text "X":
                                    xcenter int(ad_store_slot_size * 0.5)
                                    ycenter int(ad_store_slot_size * 0.5)
                                    text_align 0.5
                                    size int(config.screen_height * 0.055)
                                    color "#777782"
                                    outlines [(1, "#000000", 0, 0)]
                                    font ad_gothic_body_font


            fixed:
                xsize ad_store_right_width
                ysize ad_store_panel_height
                add Solid("#090A108C"):
                    xpos 26
                    ypos 26
                    xsize ad_store_right_width - 52
                    ysize ad_store_panel_height - 52
                use ad_barbed_border(ad_store_right_width, ad_store_panel_height, int(config.screen_height * 0.035), int(config.screen_height * 0.045))
                text "ВЫБРАННЫЙ ПРЕДМЕТ":
                    xalign 0.5
                    ypos int(ad_store_panel_height * 0.055)
                    text_align 0.5
                    size int(config.screen_height * 0.037)
                    color "#F0F0F2"
                    outlines [(1, "#000000", 0, 0)]
                    font ad_inventory_title_font

                if ad_selected_store_item in store_items:
                    $ selected = ad_items[ad_selected_store_item]
                    fixed:
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.14)
                        xsize int(ad_store_right_width * 0.68)
                        ysize int(ad_store_panel_height * 0.29)
                        add Solid("#0D0D157C"):
                            xpos 14
                            ypos 14
                            xsize int(ad_store_right_width * 0.68) - 28
                            ysize int(ad_store_panel_height * 0.29) - 28
                        use ad_barbed_border(int(ad_store_right_width * 0.68), int(ad_store_panel_height * 0.29), int(config.screen_height * 0.028), int(config.screen_height * 0.036))
                        add selected["icon"]:
                            xalign 0.5
                            yalign 0.5
                            xsize int(ad_store_panel_height * 0.22)
                            ysize int(ad_store_panel_height * 0.22)
                    text selected["name"]:
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.48)
                        text_align 0.5
                        size int(config.screen_height * 0.042)
                        color "#F0F0F2"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_gothic_body_font
                    text selected["description"]:
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.56)
                        xmaximum int(ad_store_right_width * 0.82)
                        text_align 0.5
                        size int(config.screen_height * 0.022)
                        color "#CFCFD6"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_gothic_body_font
                    text "ЦЕНА  [ad_format_money(store_prices[ad_selected_store_item])]":
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.66)
                        text_align 0.5
                        size int(config.screen_height * 0.029)
                        color "#D4D4DB"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_gothic_body_font
                    fixed:
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.73)
                        xsize int(ad_store_right_width * 0.52)
                        ysize int(ad_store_panel_height * 0.11)
                        add Solid("#101017A8"):
                            xpos 6
                            ypos 6
                            xsize int(ad_store_right_width * 0.52) - 12
                            ysize int(ad_store_panel_height * 0.11) - 12
                        use ad_barbed_border(int(ad_store_right_width * 0.52), int(ad_store_panel_height * 0.11), int(config.screen_height * 0.020), int(config.screen_height * 0.028))
                        button:
                            xalign 0.5
                            yalign 0.5
                            xsize int(ad_store_right_width * 0.52)
                            ysize int(ad_store_panel_height * 0.11)
                            background None
                            hover_background None
                            focus_mask None
                            key_events True
                            action ad_store_quantity_input.Enable()
                            input:
                                xalign 0.5
                                yalign 0.5
                                value ad_store_quantity_input
                                prefix "x"
                                allow "0123456789"
                                length 9
                                text_align 0.5
                                size int(config.screen_height * 0.037)
                                color "#F0F0F2"
                                outlines [(1, "#000000", 0, 0)]
                                font ad_inventory_money_font
                    imagebutton:
                        xpos max(0, int(ad_store_right_width * 0.32) - 216)
                        ypos int(ad_store_panel_height * 0.785)
                        yanchor 0.5
                        idle Transform("arrowleft_idle.png", size=(161, 161))
                        hover Transform("arrowleft_hover.png", size=(171, 171))
                        action [ad_store_quantity_input.Disable(), Function(ad_store_change_quantity, -1)]
                    imagebutton:
                        xpos int(ad_store_right_width * 0.68) + 60
                        ypos int(ad_store_panel_height * 0.785)
                        yanchor 0.5
                        idle Transform("arrowleft_idle.png", xzoom=-1, size=(161, 161))
                        hover Transform("arrowleft_hover.png", xzoom=-1, size=(171, 171))
                        action [ad_store_quantity_input.Disable(), Function(ad_store_change_quantity, 1)]
                    button:
                        xalign 0.5
                        ypos int(ad_store_panel_height * 0.88) - 10
                        xsize int(ad_store_right_width * 0.72)
                        ysize int(ad_store_panel_height * 0.075)
                        background None
                        action [ad_store_quantity_input.Disable(), Function(ad_buy_from_store, ad_selected_store_item, store_prices, ad_store_quantity_value())]
                        focus_mask True
                        text "КУПИТЬ  [ad_format_money(store_prices[ad_selected_store_item] * ad_store_quantity_value())]":
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            color "#F1EEF0"
                            outlines [(1, "#000000", 0, 0)]
                            font ad_gothic_body_font
                            size int(config.screen_height * 0.028)
                            at ad_item_hover
                else:
                    text "Выберите товар в магазине.":
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
                        size int(config.screen_height * 0.030)
                        color "#B6B6BF"
                        outlines [(1, "#000000", 0, 0)]
                        font ad_gothic_body_font

        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -31
            yoffset 27
            idle Transform(ad_ui_close, size=(112, 112), alpha=0.88)
            hover Transform(ad_ui_close, size=(130, 130), alpha=1.0)



            action [ad_store_quantity_input.Disable(), SetVariable("ad_store_message", ""), SetVariable("ad_store_show_result", False), Hide("ad_gift_notification_screen"), Hide("ad_store_purchase_result_screen"), Hide("ad_general_store_screen"), Return("close")]

        text "ЗАКРЫТЬ":
            xalign 1.0
            yalign 0.0
            xoffset -49
            yoffset 131
            size 25
            color "#E0E0E4"
            outlines [(1, "#000000", 0, 0)]
            font ad_gothic_body_font


screen ad_general_store_screen():
    use ad_store_layout("МАГАЗИН", ad_general_store_items, ad_general_store_prices)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
